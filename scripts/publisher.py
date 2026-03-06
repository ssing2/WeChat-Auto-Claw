#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号发布器

支持功能：
- 单篇发布
- 多图文发布
- 随机封面图
- 文颜主题渲染
"""

import os
import requests
import json
import subprocess
import random
from pathlib import Path
from bs4 import BeautifulSoup


class WeChatPublisher:
    """微信公众号发布器"""
    
    def __init__(self, app_id, app_secret):
        """
        初始化发布器
        
        Args:
            app_id: 微信AppID
            app_secret: 微信AppSecret
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        
    def get_access_token(self):
        """获取access_token"""
        if self.access_token:
            return self.access_token
        
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_id,
            "secret": self.app_secret
        }
        
        response = requests.get(url, params=params)
        result = response.json()
        
        if 'access_token' in result:
            self.access_token = result['access_token']
            return self.access_token
        
        raise Exception(f"获取access_token失败: {result}")
    
    def get_material_images(self, count=20):
        """
        获取素材库图片列表
        
        Args:
            count: 获取数量
        
        Returns:
            图片media_id列表
        """
        access_token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/material/batchget_material?access_token={access_token}"
        
        data = {
            "type": "image",
            "offset": 0,
            "count": count
        }
        
        response = requests.post(url, json=data)
        result = response.json()
        
        if 'item' in result:
            return [item['media_id'] for item in result['item']]
        
        return []
    
    def render_with_wenyan(self, markdown_file, theme="orangeheart"):
        """
        使用文颜CLI渲染Markdown
        
        Args:
            markdown_file: Markdown文件路径
            theme: 文颜主题
        
        Returns:
            HTML内容
        """
        env = os.environ.copy()
        env['WECHAT_APP_ID'] = self.app_id
        env['WECHAT_APP_SECRET'] = self.app_secret
        
        result = subprocess.run(
            ['npx', '@wenyan-md/cli', 'render', '--file', markdown_file, '--theme', theme],
            capture_output=True,
            text=True,
            timeout=60,
            env=env
        )
        
        if result.returncode != 0:
            raise Exception(f"文颜渲染失败: {result.stderr}")
        
        # 提取HTML内容
        output = result.stdout
        soup = BeautifulSoup(output, 'html.parser')
        body = soup.find('body')
        
        if body:
            return str(body)
        
        return output
    
    def read_article_info(self, markdown_file):
        """
        读取文章信息
        
        Args:
            markdown_file: Markdown文件路径
        
        Returns:
            文章信息字典
        """
        import re
        
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取标题
        title_match = re.search(r'title: (.+)', content)
        title = title_match.group(1) if title_match else "法律科普"
        
        # 提取正文
        content = re.sub(r'^---.*?---', '', content, flags=re.DOTALL)
        
        # 生成摘要
        digest = content[:100].replace('\n', ' ')
        
        return {
            "title": title,
            "digest": digest,
            "content": content
        }
    
    def publish_single(self, markdown_file, theme="orangeheart", cover_media_id=None):
        """
        发布单篇文章
        
        Args:
            markdown_file: Markdown文件路径
            theme: 文颜主题
            cover_media_id: 封面图media_id
        """
        # 渲染文章
        html_content = self.render_with_wenyan(markdown_file, theme)
        
        # 读取文章信息
        article_info = self.read_article_info(markdown_file)
        
        # 构建文章数据
        article = {
            "title": article_info["title"],
            "author": "袁律",
            "digest": article_info["digest"],
            "content": html_content,
            "thumb_media_id": cover_media_id or "menzuMkbaFB9FiAluPMZBCEe37Krc0YMG84lkoj-WYSJWAcoyyO9wJFSXvE4JPTs",
            "show_cover_pic": 1,
            "content_source_url": ""
        }
        
        # 发布
        return self._publish_to_wechat([article])
    
    def publish_multi_group(self, markdown_files, theme="orangeheart", random_cover=True):
        """
        发布多图文
        
        Args:
            markdown_files: Markdown文件列表
            theme: 文颜主题
            random_cover: 是否使用随机封面
        """
        # 获取素材库图片
        images = []
        if random_cover:
            images = self.get_material_images(20)
        
        if not images:
            print("⚠️ 未找到素材库图片，使用默认封面")
            images = ["menzuMkbaFB9FiAluPMZBCEe37Krc0YMG84lkoj-WYSJWAcoyyO9wJFSXvE4JPTs"] * len(markdown_files)
        
        # 随机选择封面
        if random_cover and len(images) >= len(markdown_files):
            selected_images = random.sample(images, len(markdown_files))
        else:
            selected_images = images[:len(markdown_files)]
        
        # 构建文章列表
        articles = []
        for i, (markdown_file, cover_id) in enumerate(zip(markdown_files, selected_images), 1):
            # 渲染文章
            html_content = self.render_with_wenyan(markdown_file, theme)
            
            # 读取文章信息
            article_info = self.read_article_info(markdown_file)
            
            # 头条显示封面，次条不显示
            show_cover = 1 if i == 1 else 0
            
            articles.append({
                "title": article_info["title"],
                "author": "袁律",
                "digest": article_info["digest"],
                "content": html_content,
                "thumb_media_id": cover_id,
                "show_cover_pic": show_cover,
                "content_source_url": ""
            })
        
        # 发布
        return self._publish_to_wechat(articles)
    
    def _publish_to_wechat(self, articles):
        """
        发布到微信
        
        Args:
            articles: 文章列表
        
        Returns:
            Media ID
        """
        access_token = self.get_access_token()
        url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
        
        data = {"articles": articles}
        
        # 手动构建JSON，避免双重转义
        json_str = json.dumps(data, ensure_ascii=False)
        json_bytes = json_str.encode('utf-8')
        
        response = requests.post(
            url,
            data=json_bytes,
            headers={'Content-Type': 'application/json; charset=utf-8'}
        )
        
        result = response.json()
        
        if 'media_id' in result:
            return result['media_id']
        
        raise Exception(f"发布失败: {result}")


if __name__ == '__main__':
    # 示例用法
    import yaml
    
    # 加载配置
    with open('config/config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    # 初始化发布器
    publisher = WeChatPublisher(
        app_id=config['wechat']['app_id'],
        app_secret=config['wechat']['app_secret']
    )
    
    # 发布示例
    publisher.publish_multi_group(
        markdown_files=[
            'articles/to-publish/01-入职一个月不签劳动合同怎么办.md',
            'articles/to-publish/02-公司拖延签劳动合同能要双倍工资吗.md',
            'articles/to-publish/03-没签劳动合同怎么证明劳动关系.md',
            'articles/to-publish/04-劳动合同简单两页合法吗.md',
            'articles/to-publish/05-固定期限还是无固定期限合同怎么选.md'
        ],
        theme='orangeheart',
        random_cover=True
    )
    
    print("✅ 发布成功！")
