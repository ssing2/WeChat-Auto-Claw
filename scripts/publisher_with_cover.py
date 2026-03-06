#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
带封面图片的文章发布器
"""

import os
import yaml
import requests
import re
from datetime import datetime

class ArticlePublisherWithCover:
    """带封面图片的文章发布器"""
    
    def __init__(self, config_path="config.yaml"):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = yaml.safe_load(f)
        
        self.cover_media_id = self.config.get('cover_media_id')
        if not self.cover_media_id:
            raise Exception("配置文件中缺少cover_media_id，请先运行upload_cover_image.py")
        
        print(f"✅ 使用封面图片media_id: {self.cover_media_id}")
    
    def get_access_token(self):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.config["wechat"]["app_id"],
            "secret": self.config["wechat"]["app_secret"]
        }
        response = requests.get(url, params=params)
        return response.json()["access_token"]
    
    def publish_article(self, markdown_file):
        articles_dir = self.config["paths"]["articles_dir"]
        file_path = os.path.join(articles_dir, markdown_file)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # 提取标题
            title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
            title = title_match.group(1) if title_match else "未命名文章"
            
            # 移除标题行
            content = re.sub(r'^#\s+.+$', '', content, flags=re.MULTILINE)
            
            # 转换为简单的HTML
            html_content = content.replace("\n\n", "<br/><br/>").replace("\n", "<br/>")
            
            # 提取摘要
            summary = content[:100].replace('*', '').replace('#', '').strip()
            
            # 获取access_token
            access_token = self.get_access_token()
            url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
            
            # 构建文章数据（包含封面图片）
            data = {
                "articles": [{
                    "title": title,
                    "author": "袁律",
                    "digest": summary,
                    "content": html_content,
                    "content_source_url": "",
                    "thumb_media_id": self.cover_media_id  # 使用封面图片
                }]
            }
            
            # 发布
            response = requests.post(url, json=data)
            result = response.json()
            
            if result.get("errcode") == 0:
                print(f"  ✅ 成功: {title}")
                return {"success": True, "title": title, "file": markdown_file}
            else:
                print(f"  ❌ 失败: {title}")
                print(f"     错误: {result.get('errmsg')}")
                return {"success": False, "title": title, "file": markdown_file, "error": result.get('errmsg')}
                
        except Exception as e:
            print(f"  ❌ 异常: {markdown_file}")
            print(f"     错误: {str(e)}")
            return {"success": False, "file": markdown_file, "error": str(e)}
    
    def publish_batch(self, markdown_files):
        print(f"\n开始批量发布 {len(markdown_files)} 篇文章...")
        
        results = []
        success_count = 0
        
        for i, markdown_file in enumerate(markdown_files, 1):
            print(f"\n[{i}/{len(markdown_files)}] 发布: {markdown_file}")
            
            result = self.publish_article(markdown_file)
            results.append(result)
            
            if result["success"]:
                success_count += 1
        
        print(f"\n发布完成！")
        print(f"  成功: {success_count} 篇")
        print(f"  失败: {len(results) - success_count} 篇")
        
        return results

if __name__ == "__main__":
    publisher = ArticlePublisherWithCover()
    
    # 测试发布第一篇
    print("=" * 50)
    print("测试发布第一篇文章")
    print("=" * 50)
    
    result = publisher.publish_article("01-入职一个月不签劳动合同怎么办.md")
    
    if result["success"]:
        print(f"\n✅ 测试成功！准备批量发布...")
    else:
        print(f"\n❌ 测试失败，请检查错误")
