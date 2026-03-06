#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown转精美HTML - 使用文颜主题
"""

import subprocess
import json
import os
import tempfile

class WenyanThemeRenderer:
    """使用文颜主题渲染Markdown"""
    
    def __init__(self, theme="phycat"):
        """
        初始化渲染器
        
        Args:
            theme: 文颜主题ID（default, phycat, orangeheart等）
        """
        self.theme = theme
        
    def render_markdown(self, markdown_content: str) -> str:
        """
        使用文颜MCP渲染Markdown为HTML
        
        Args:
            markdown_content: Markdown内容
        
        Returns:
            HTML内容
        """
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as f:
            # 添加frontmatter
            f.write("---\n")
            f.write(f"title: 测试文章\n")
            f.write(f"author: 袁律\n")
            f.write("---\n\n")
            f.write(markdown_content)
            temp_path = f.name
        
        try:
            # 调用文颜MCP的render功能
            result = subprocess.run(
                ['npx', '@wenyan-md/mcp', 'render', '--file', temp_path, '--theme', self.theme],
                capture_output=True,
                text=True,
                timeout=30,
                input=markdown_content
            )
            
            # 提取HTML部分
            output = result.stdout
            if '<!DOCTYPE html>' in output:
                # 解析HTML，提取body内容
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(output, 'html.parser')
                body = soup.find('body')
                if body:
                    return str(body)
            
            # 如果没有HTML标签，可能返回的是纯文本或其他格式
            return output
            
        finally:
            # 删除临时文件
            try:
                os.unlink(temp_path)
            except:
                pass
    
    def render_and_publish_test(self, markdown_file: str):
        """
        测试渲染并发布
        
        Args:
            markdown_file: Markdown文件路径
        
        Returns:
            发布结果
        """
        result = subprocess.run(
            ['npx', '@wenyan-md/mcp', 'publish', '--file', markdown_file, '--theme', self.theme],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        return result.stdout, result.stderr, result.returncode


if __name__ == "__main__":
    # 测试
    renderer = WenyanThemeRenderer(theme="phycat")
    
    test_md = """# 测试标题

这是**加粗**文字。

## 二级标题

- 列表项1
- 列表项2
"""
    
    html = renderer.render_markdown(test_md)
    print("渲染结果：")
    print(html[:500])
