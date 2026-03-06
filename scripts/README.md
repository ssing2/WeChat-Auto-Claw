# 微信公众号自动发布系统

基于微信官方API的文章自动发布系统，实现Markdown文章自动发布到公众号草稿箱。

## 功能特点

- ✅ 自动获取和刷新access_token
- ✅ Markdown转HTML（适配微信公众号）
- ✅ 批量发布文章到草稿箱
- ✅ 发布日志记录
- ✅ 错误处理和重试

## 安装

### 1. 安装依赖

```bash
cd /root/.openclaw/workspace/scripts/wechat-auto-publish
pip install -r requirements.txt
```

### 2. 配置文件

编辑`config.yaml`（已配置）：

```yaml
wechat:
  app_id: "wxa786d3fd78dd6bd6"
  app_secret: "81e30eec53f7f420c77bb0f16c5f965a"
  name: "亲子萌娃日常"

paths:
  articles_dir: "/root/.openclaw/workspace/articles/to-publish"
  published_log: "/root/.openclaw/workspace/logs/published-log.csv"
```

### 3. IP白名单配置

**重要！** 微信官方API需要配置服务器IP白名单。

**操作步骤**：
1. 登录公众号后台：https://mp.weixin.qq.com
2. 设置 → 开发 → 基本配置
3. IP白名单 → 添加服务器IP
4. 保存

**获取服务器IP**：
```bash
curl ifconfig.me
```

## 使用方法

### 方式1：批量发布所有文章

```bash
cd /root/.openclaw/workspace/scripts/wechat-auto-publish
python batch_publish.py
```

### 方式2：发布单篇文章

```bash
python publisher.py
```

### 方式3：作为模块导入

```python
from publisher import ArticlePublisher

publisher = ArticlePublisher()

# 发布单篇
result = publisher.publish_article("01-xxx.md")

# 批量发布
results = publisher.publish_batch([
    "01-xxx.md",
    "02-xxx.md",
    "03-xxx.md"
])
```

## 文件说明

```
wechat-auto-publish/
├── README.md                  # 本文件
├── config.yaml                # 配置文件
├── requirements.txt           # Python依赖
├── wechat_api.py             # 微信API封装
├── markdown_converter.py     # Markdown转HTML
├── publisher.py              # 发布逻辑
└── batch_publish.py          # 批量发布脚本
```

## 注意事项

### ⚠️ 铁律

- **所有文章只发布到草稿箱**
- **由老板审核后再正式发布**
- **不得直接自动发布**

### 📋 发布流程

1. 生成文章（已完成）
2. 运行批量发布脚本
3. 登录公众号后台
4. 审阅草稿箱中的文章
5. 确认无误后正式发布

### 🔍 故障排查

**问题1：获取access_token失败**

- 检查AppID和AppSecret是否正确
- 检查服务器IP是否在白名单中
- 检查网络连接

**问题2：发布失败**

- 检查文章格式是否正确
- 检查HTML内容是否合规
- 查看日志文件：`/root/.openclaw/workspace/logs/published-log.csv`

**问题3：Markdown转HTML失败**

- 检查Markdown语法是否正确
- 检查是否安装了所有依赖

## 日志文件

发布日志：`/root/.openclaw/workspace/logs/published-log.csv`

格式：
```csv
时间,文件名,标题,是否成功,消息
2026-03-06T09:00:00,01-xxx.md,标题,True,发布成功
```

## 技术支持

如有问题，联系小昕昕！

---

**开发者**: 小昕昕 (OpenClaw AI Agent)
**创建时间**: 2026-03-06
**版本**: v1.0
