#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号API封装
提供access_token管理和草稿箱操作
"""

import requests
import json
import time
from typing import Dict, Optional


class WeChatAPI:
    """微信公众号API封装类"""
    
    def __init__(self, app_id: str, app_secret: str):
        """
        初始化微信API
        
        Args:
            app_id: 微信公众号AppID
            app_secret: 微信公众号AppSecret
        """
        self.app_id = app_id
        self.app_secret = app_secret
        self.base_url = "https://api.weixin.qq.com"
        
        # access_token管理
        self.access_token = None
        self.token_expires_at = 0
        
    def get_access_token(self) -> str:
        """
        获取access_token
        自动处理token刷新
        
        Returns:
            access_token字符串
        """
        # 检查token是否有效
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token
        
        # 获取新token
        url = f"{self.base_url}/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": self.app_id,
            "secret": self.app_secret
        }
        
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if "access_token" in data:
                self.access_token = data["access_token"]
                # 提前5分钟刷新，避免边界情况
                self.token_expires_at = time.time() + data["expires_in"] - 300
                return self.access_token
            else:
                raise Exception(f"获取access_token失败: {data}")
                
        except Exception as e:
            raise Exception(f"请求access_token时发生错误: {str(e)}")
    
    def add_draft(self, articles: list) -> Dict:
        """
        新增草稿
        
        Args:
            articles: 文章列表，每个文章是包含title, author, content, digest等的字典
        
        Returns:
            API响应结果
        """
        access_token = self.get_access_token()
        url = f"{self.base_url}/cgi-bin/draft/add?access_token={access_token}"
        
        # 构建请求数据
        data = {
            "articles": articles
        }
        
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            result = response.json()
            
            if result.get("errcode") == 0:
                return {
                    "success": True,
                    "data": result
                }
            else:
                return {
                    "success": False,
                    "error": result.get("errmsg", "未知错误"),
                    "errcode": result.get("errcode")
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }
    
    def get_draft_list(self, offset: int = 0, count: int = 20) -> Dict:
        """
        获取草稿列表
        
        Args:
            offset: 偏移量
            count: 数量（最大20）
        
        Returns:
            草稿列表数据
        """
        access_token = self.get_access_token()
        url = f"{self.base_url}/cgi-bin/draft/batchget?access_token={access_token}"
        
        data = {
            "offset": offset,
            "count": count,
            "no_content": 0  # 返回完整内容
        }
        
        try:
            response = requests.post(url, json=data, timeout=10)
            response.raise_for_status()
            result = response.json()
            
            if result.get("errcode") == 0:
                return {
                    "success": True,
                    "data": result.get("item", [])
                }
            else:
                return {
                    "success": False,
                    "error": result.get("errmsg", "未知错误")
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }


if __name__ == "__main__":
    # 测试代码
    import yaml
    
    # 加载配置
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    # 创建API实例
    api = WeChatAPI(
        app_id=config["wechat"]["app_id"],
        app_secret=config["wechat"]["app_secret"]
    )
    
    # 测试获取access_token
    try:
        token = api.get_access_token()
        print(f"✅ access_token获取成功: {token[:20]}...")
    except Exception as e:
        print(f"❌ 获取access_token失败: {str(e)}")
