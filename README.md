# 微信公众号自动发布系统

<div align="center">
  <h3>🤖 AI生成 + 🎨 文颜排版 + 📱 多图文发布</h3>
  <p>一套完整的微信公众号内容自动化生成与发布系统</p>
</div>

---

## ✨ 核心功能

- 🤖 **AI自动生成**：基于场景稿自动生成专业文章
- 🎨 **精美排版**：文颜OrangeHeart主题，专业美观
- 📷 **随机封面**：从素材库自动选择封面图
- 📰 **多图文发布**：一次发布5篇文章（头条+次条）
- ✅ **草稿箱审核**：先发草稿箱，审阅后正式发布

---

## 🎯 适用场景

- 法律科普公众号
- 职场建议公众号  
- 专业知识科普公众号
- 需要批量生产内容的公众号

---

## 🚀 快速开始

### 第1步：安装依赖

\`\`\`bash
pip install requests beautifulsoup4 pyyaml
npm install -g @wenyan-md/cli
\`\`\`

### 第2步：配置系统

编辑 \`config/config.yaml\`：

\`\`\`yaml
wechat:
  app_id: "你的AppID"
  app_secret: "你的AppSecret"

article:
  author: "你的作者名"
\`\`\`

### 第3步：配置IP白名单

登录微信公众平台 → 设置 → 开发 → 基本配置 → IP白名单

### 第4步：运行

\`\`\`bash
python scripts/batch_publish_multi.py \\
  --config config/config.yaml \\
  --scenarios config/scenarios.txt
\`\`\`

---

## 📖 文档

- [README.md](README.md) - 系统说明
- [快速开始.md](快速开始.md) - 5分钟快速上手
- [安装部署.md](安装部署.md) - 安装和部署指南
- [文件清单.md](文件清单.md) - 文件结构说明
- [docs/主题自定义指南.md](docs/主题自定义指南.md) - 主题定制

---

## 🎨 主题系统

### 内置主题

- default - 简洁经典
- orangeheart - 暖橙色调（推荐）
- rainbow - 彩虹风格
- lapis - 靛蓝色调
- pie - 甜美风格
- maize - 玉米暖色
- purple - 紫色优雅
- phycat - 清新自然

### 自定义主题

支持3种方式：

1. **在线主题**：使用文颜主题库
2. **本地CSS**：创建自己的主题文件
3. **网络CSS**：导入CDN或GitHub主题

详见：[docs/主题自定义指南.md](docs/主题自定义指南.md)

---

## 📊 系统架构

\`\`\`
场景稿 (scenarios.txt)
  ↓
文章生成器 (article_generator.py)
  ↓
文颜渲染 (@wenyan-md/cli)
  ↓
发布器 (publisher.py)
  ↓
微信公众号API
  ↓
草稿箱 → 老板审阅 → 正式发布
\`\`\`

---

## 📝 文章格式

\`\`\`markdown
---
title: 文章标题
author: 袁律
cover: [可选]
---

# 📋 法律咨询

**问题概述**：背景

**用户法律咨询**：用户咨询内容

---

参考回答 ：袁律解答

[正文内容...]
\`\`\`

---

## ⚠️ 重要提示

### IP白名单

必须配置，否则无法发布！

\`\`\`
公众号后台 → 设置 → 开发 → 基本配置 → IP白名单
\`\`\`

### 标题限制

- 限制：64字节（UTF-8）
- 中文：约20-30个汉字
- 自动截断：系统自动处理

### 铁律

**所有文章只发草稿箱，老板审阅后正式发布！**

---

## 🛠️ 技术栈

- **Python 3.8+**：核心逻辑
- **Node.js 16+**：文颜CLI
- **文颜（Wenyan）**：精美排版引擎
- **微信公众号API**：官方发布接口

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- [文颜（Wenyan）](https://wenyan.yuzhi.tech) - 精美排版引擎
- [OpenClaw](https://openclaw.ai) - AI自动化平台
- [微信公众号](https://mp.weixin.qq.com) - 官方API支持

---

## 📞 联系方式

- 问题反馈：GitHub Issues
- 技术文档：docs/ 目录

---

<div align="center">
  <p>⭐ 如果觉得有用，请给个Star！</p>
  <p> Made with ❤️ by 袁律团队 </p>
</div>
