#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量发布脚本
自动发布所有待发布的文章到微信公众号草稿箱
"""

import os
import sys
from publisher import ArticlePublisher


def get_markdown_files(articles_dir: str) -> list:
    """
    获取所有Markdown文件
    
    Args:
        articles_dir: 文章目录
    
    Returns:
        Markdown文件列表
    """
    files = []
    
    for filename in os.listdir(articles_dir):
        if filename.endswith('.md'):
            # 跳过README和模板文件
            if not filename.startswith('README') and not filename.startswith('模板'):
                files.append(filename)
    
    # 按文件名排序
    files.sort()
    
    return files


def main():
    """主函数"""
    print("=" * 50)
    print("微信公众号自动发布系统")
    print("=" * 50)
    print()
    
    # 创建发布器
    try:
        publisher = ArticlePublisher()
    except Exception as e:
        print(f"❌ 初始化失败: {str(e)}")
        sys.exit(1)
    
    # 获取所有Markdown文件
    articles_dir = publisher.config["paths"]["articles_dir"]
    markdown_files = get_markdown_files(articles_dir)
    
    if not markdown_files:
        print("⚠️  没有找到待发布的文章")
        sys.exit(0)
    
    print(f"找到 {len(markdown_files)} 篇待发布文章:")
    for i, filename in enumerate(markdown_files[:10], 1):
        print(f"  {i}. {filename}")
    
    if len(markdown_files) > 10:
        print(f"  ... 还有 {len(markdown_files) - 10} 篇")
    
    print()
    
    # 询问是否继续
    confirm = input("是否开始发布? (y/n): ").strip().lower()
    
    if confirm != 'y':
        print("已取消发布")
        sys.exit(0)
    
    print()
    print("=" * 50)
    
    # 批量发布
    results = publisher.publish_batch(markdown_files)
    
    # 显示详细结果
    print("\n详细结果:")
    print("-" * 50)
    
    for result in results:
        status = "✅" if result["success"] else "❌"
        title = result.get("title", result.get("file", "Unknown"))
        message = "成功" if result["success"] else result.get("error", "未知错误")
        
        print(f"{status} {title}")
        if not result["success"]:
            print(f"   错误: {message}")
    
    print()
    print("=" * 50)
    print("发布完成！请登录微信公众号后台查看草稿箱")
    print("https://mp.weixin.qq.com")
    print("=" * 50)


if __name__ == "__main__":
    main()
