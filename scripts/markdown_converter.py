#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown转HTML转换器
将Markdown格式的文章转换为微信公众号HTML格式
"""

import markdown
from bs4 import BeautifulSoup
import re


class MarkdownConverter:
    """Markdown转HTML转换器"""
    
    def __init__(self):
        """初始化转换器"""
        # 配置markdown扩展
        self.md = markdown.Markdown(
            extensions=[
                'extra',  # 额外功能
                'codehilite',  # 代码高亮
                'toc',  # 目录
                'nl2br',  # 换行转换
                'sane_lists',  # 列表
            ]
        )
    
    def convert(self, markdown_text: str) -> str:
        """
        转换Markdown到HTML
        
        Args:
            markdown_text: Markdown文本
        
        Returns:
            HTML文本
        """
        # 转换Markdown
        html = self.md.convert(markdown_text)
        
        # 美化HTML（适配微信公众号）
        html = self._beautify_for_wechat(html)
        
        # 重置转换器（准备下次转换）
        self.md.reset()
        
        return html
    
    def _beautify_for_wechat(self, html: str) -> str:
        """
        美化HTML以适配微信公众号
        
        Args:
            html: 原始HTML
        
        Returns:
            美化后的HTML
        """
        soup = BeautifulSoup(html, 'html.parser')
        
        # 添加样式
        for tag in soup.find_all(['h1', 'h2', 'h3', 'p', 'strong', 'ul', 'ol', 'li']):
            if not tag.get('style'):
                tag['style'] = self._get_tag_style(tag.name)
        
        return str(soup)
    
    def _get_tag_style(self, tag_name: str) -> str:
        """
        获取标签样式
        
        Args:
            tag_name: 标签名称
        
        Returns:
            CSS样式字符串
        """
        styles = {
            'h1': 'font-size: 24px; font-weight: bold; color: #333; margin: 20px 0; text-align: center;',
            'h2': 'font-size: 20px; font-weight: bold; color: #333; margin: 18px 0; padding: 10px; background: #f5f5f5; border-left: 4px solid #ff6b6b;',
            'h3': 'font-size: 18px; font-weight: bold; color: #333; margin: 16px 0;',
            'p': 'font-size: 16px; line-height: 1.8; color: #666; margin: 10px 0; text-indent: 2em;',
            'strong': 'font-weight: bold; color: #ff6b6b;',
            'ul': 'margin: 10px 0; padding-left: 20px;',
            'ol': 'margin: 10px 0; padding-left: 20px;',
            'li': 'font-size: 16px; line-height: 1.8; color: #666; margin: 5px 0;',
            'code': 'background: #f5f5f5; padding: 2px 5px; border-radius: 3px; font-family: monospace;',
            'blockquote': 'margin: 10px 0; padding: 10px; background: #f9f9f9; border-left: 3px solid #ddd; color: #666;',
        }
        
        return styles.get(tag_name, '')
    
    def extract_title(self, markdown_text: str) -> str:
        """
        从Markdown文本中提取标题
        
        Args:
            markdown_text: Markdown文本
        
        Returns:
            标题字符串
        """
        # 查找第一个#标题
        match = re.search(r'^#\s+(.+)$', markdown_text, re.MULTILINE)
        if match:
            return match.group(1).strip()
        
        # 如果没有找到，返回默认标题
        return "未命名文章"
    
    def extract_summary(self, markdown_text: str, max_length: int = 100) -> str:
        """
        从Markdown文本中提取摘要
        
        Args:
            markdown_text: Markdown文本
            max_length: 最大长度
        
        Returns:
            摘要字符串
        """
        # 移除标题
        text = re.sub(r'^#\s+.+$', '', markdown_text, flags=re.MULTILINE)
        
        # 移除Markdown标记
        text = re.sub(r'[#*`\[\]()]', '', text)
        
        # 清理空白
        text = re.sub(r'\s+', ' ', text).strip()
        
        # 截断
        if len(text) > max_length:
            text = text[:max_length] + "..."
        
        return text


if __name__ == "__main__":
    # 测试代码
    converter = MarkdownConverter()
    
    # 测试Markdown
    test_md = """# 测试标题

这是一段**加粗**的文字。

## 二级标题

- 列表项1
- 列表项2
"""
    
    # 转换
    html = converter.convert(test_md)
    print("转换后的HTML:")
    print(html)
    
    # 提取标题
    title = converter.extract_title(test_md)
    print(f"\n标题: {title}")
    
    # 提取摘要
    summary = converter.extract_summary(test_md)
    print(f"摘要: {summary}")
