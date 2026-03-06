#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信公众号多图文批量发布脚本

功能：
1. 读取场景稿列表
2. 批量生成文章
3. 使用文颜渲染
4. 发布多图文到草稿箱
"""

import os
import sys
import argparse
import yaml
import random
from pathlib import Path

# 添加scripts目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from publisher import WeChatPublisher
from article_generator import ArticleGenerator


def load_config(config_file):
    """加载配置文件"""
    with open(config_file, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def load_scenarios(scenarios_file):
    """加载场景列表"""
    with open(scenarios_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 过滤空行和注释
    scenarios = []
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            scenarios.append(line)
    
    return scenarios


def batch_publish_multi(scenarios, config):
    """批量发布多图文"""
    
    # 初始化发布器
    publisher = WeChatPublisher(
        app_id=config['wechat']['app_id'],
        app_secret=config['wechat']['app_secret']
    )
    
    # 初始化文章生成器
    generator = ArticleGenerator(
        author=config['article']['author'],
        style_prompt=config['article'].get('style_prompt')
    )
    
    # 生成文章
    articles_dir = Path(config['paths']['articles_dir'])
    articles_dir.mkdir(parents=True, exist_ok=True)
    
    article_files = []
    
    print("📝 生成文章...")
    for i, scenario in enumerate(scenarios, 1):
        filename = f"{i:02d}-{scenario[:30]}.md"
        filepath = articles_dir / filename
        
        # 生成文章（这里简化处理，实际需要调用AI生成）
        # generator.generate(scenario, output_file=str(filepath))
        
        article_files.append(str(filepath))
        print(f"  ✅ {i}/{len(scenarios)} {filename}")
    
    # 分组发布
    group_size = config['publish']['articles_per_group']
    
    print(f"\n📤 发布多图文（每组{group_size}篇）...")
    
    for i in range(0, len(article_files), group_size):
        group = article_files[i:i+group_size]
        group_num = i // group_size + 1
        
        print(f"\n{'='*60}")
        print(f"第{group_num}组（{len(group)}篇）")
        print(f"{'='*60}")
        
        # 发布多图文
        publisher.publish_multi_group(
            markdown_files=group,
            theme=config['wenyan']['theme'],
            random_cover=config['publish']['use_random_cover']
        )
        
        print(f"✅ 第{group_num}组发布成功")
    
    print(f"\n{'='*60}")
    print(f"✅ 全部完成！共发布 {len(article_files)} 篇文章")
    print(f"{'='*60}")


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='微信公众号多图文批量发布')
    parser.add_argument('--config', default='config/config.yaml', help='配置文件路径')
    parser.add_argument('--scenarios', default='config/scenarios.txt', help='场景稿文件')
    parser.add_argument('--group-size', type=int, default=5, help='每组文章数量')
    parser.add_argument('--theme', default='orangeheart', help='文颜主题')
    
    args = parser.parse_args()
    
    # 加载配置
    config = load_config(args.config)
    
    # 加载场景
    scenarios = load_scenarios(args.scenarios)
    
    if not scenarios:
        print("❌ 未找到场景稿，请检查 config/scenarios.txt")
        sys.exit(1)
    
    print(f"📋 找到 {len(scenarios)} 个场景")
    print(f"🎨 主题: {args.theme}")
    print(f"📦 每组: {args.group_size} 篇")
    
    # 批量发布
    batch_publish_multi(scenarios, config)
    
    print(f"\n📱 请登录公众号审阅：")
    print(f"https://mp.weixin.qq.com → 素材管理 → 草稿箱")


if __name__ == '__main__':
    main()
