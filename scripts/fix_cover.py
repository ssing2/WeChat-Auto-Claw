#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速修复：不使用封面图片发布草稿
"""

import os
import yaml
import requests

# 加载配置
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# 获取access_token
def get_access_token():
    url = "https://api.weixin.qq.com/cgi-bin/token"
    params = {
        "grant_type": "client_credential",
        "appid": config["wechat"]["app_id"],
        "secret": config["wechat"]["app_secret"]
    }
    response = requests.get(url, params=params)
    return response.json()["access_token"]

# 不使用封面图片的发布方式
def publish_without_cover():
    access_token = get_access_token()
    url = f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={access_token}"
    
    # 读取第一篇文章
    articles_dir = config["paths"]["articles_dir"]
    with open(os.path.join(articles_dir, "01-入职一个月不签劳动合同怎么办.md"), "r", encoding="utf-8") as f:
        content = f.read()
    
    # 提取标题
    import re
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else "测试文章"
    
    # 移除标题行
    content = re.sub(r'^#\s+.+$', '', content, flags=re.MULTILINE)
    
    # 转换为简单的HTML
    html_content = content.replace("\n\n", "<br/><br/>").replace("\n", "<br/>")
    
    # 构建文章数据（不设置thumb_media_id）
    data = {
        "articles": [{
            "title": title,
            "author": "袁律",
            "digest": "这是一篇测试文章",
            "content": html_content,
            "content_source_url": ""
            # 不设置 thumb_media_id
        }]
    }
    
    # 发布
    response = requests.post(url, json=data)
    result = response.json()
    
    print("发布结果：")
    print(result)
    
    if result.get("errcode") == 0:
        print("✅ 发布成功！")
    else:
        print(f"❌ 发布失败: {result.get('errmsg')}")

if __name__ == "__main__":
    publish_without_cover()
