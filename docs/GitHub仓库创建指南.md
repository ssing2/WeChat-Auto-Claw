# GitHub仓库创建指南

## 📦 仓库信息

**仓库名称**: `wechat-auto-publish-system`
**仓库描述**: 微信公众号自动发布系统 - AI生成+文颜排版+多图文发布
**可见性**: Public（公开）或 Private（私有）

---

## 🚀 方式1：通过GitHub网页创建（推荐）

### 第1步：登录GitHub

访问：https://github.com

### 第2步：创建新仓库

1. 点击右上角 "+" → "New repository"
2. 填写仓库信息：
   - **Repository name**: `wechat-auto-publish-system`
   - **Description**: `微信公众号自动发布系统 - AI生成+文颜排版+多图文发布`
   - **Public/Private**: 选择 Public
   - **Initialize**: ❌ 不要勾选（我们已经有了代码）

3. 点击 "Create repository"

### 第3步：上传代码

创建仓库后，GitHub会显示上传代码的命令。在我们的服务器上执行：

```bash
cd /root/.openclaw/workspace/公众号自动发布系统

# 初始化Git（如果还没有）
git init

# 添加所有文件
git add .

# 提交
git commit -m "Initial commit: 微信公众号自动发布系统"

# 添加远程仓库
git remote add origin https://github.com/ssing2/wechat-auto-publish-system.git

# 推送到GitHub
git push -u origin main
```

**如果遇到认证问题**：

使用GitHub Token：
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token → 勾选 `repo` 权限
3. 复制token
4. 推送时输入：
   - Username: `ssing2`
   - Password: `你的token`

---

## 🚀 方式2：使用GitHub CLI（推荐开发者）

### 第1步：安装GitHub CLI

```bash
# Linux
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# 验证安装
gh --version
```

### 第2步：登录GitHub

```bash
gh auth login
```

按提示操作：
1. What account? → `GitHub.com`
2. What is your preferred protocol? → `SSH`
3. Upload your SSH public key? → `Yes`
4. Title? → `Server`
5. 获取认证代码

### 第3步：创建仓库并推送

```bash
cd /root/.openclaw/workspace/公众号自动发布系统

# 创建仓库
gh repo create wechat-auto-publish-system \
  --public \
  --description "微信公众号自动发布系统 - AI生成+文颜排版+多图文发布" \
  --source=. \
  --push
```

---

## 🚀 方式3：使用SSH密钥（推荐服务器）

### 第1步：生成SSH密钥

```bash
# 生成SSH密钥
ssh-keygen -t ed25519 -C "your_email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub
```

### 第2步：添加到GitHub

1. 复制公钥内容
2. GitHub → Settings → SSH and GPG keys → New SSH key
3. 粘贴公钥 → Add SSH key

### 第3步：测试连接

```bash
ssh -T git@github.com
```

**期望输出**：
```
Hi ssing2! You've successfully authenticated...
```

### 第4步：推送代码

```bash
cd /root/.openclaw/workspace/公众号自动发布系统

# 修改远程地址为SSH
git remote set-url origin git@github.com:ssing2/wechat-auto-publish-system.git

# 推送
git push -u origin main
```

---

## 📋 仓库配置

### 创建GitHub Token（用于API访问）

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic)
3. 设置：
   - **Note**: `WeChat Auto Publish System`
   - **Expiration**: `90 days` 或 `No expiration`
   - **Scopes**: 勾选 `repo`（所有子项）
4. Generate token
5. **重要**：复制并保存token（只显示一次）

### 仓库设置

创建仓库后，建议设置：

#### 1. 添加Topics

GitHub仓库页面 → Settings → Topics

添加：
- `wechat`
- `wechat-mp`
- `automation`
- `ai`
- `wenyan`
- `markdown`
- `python`
- `content-management`

#### 2. 设置仓库描述

Settings → General → Description

```
微信公众号自动发布系统 - AI生成+文颜排版+多图文发布

功能：
- AI自动生成专业文章
- 文颜精美排版渲染
- 随机封面图选择
- 多图文批量发布
- 草稿箱审核流程
```

#### 3. 设置仓库主页

Settings → General → Website

```
https://ssing2.github.io/wechat-auto-publish-system/
```

#### 4. 启用GitHub Pages（可选）

Settings → Pages → Build from branch → `main` → `/docs` → Save

---

## 🎯 仓库结构

推送成功后，仓库结构：

```
wechat-auto-publish-system/
├── .gitignore
├── README.md                          # 仓库主页
├── requirements.txt                   # Python依赖
├── 快速开始.md                         # 快速上手
├── 安装部署.md                         # 安装指南
├── 文件清单.md                         # 文件说明
├── 系统说明.md                         # 系统文档
├── config/
│   ├── config.yaml.example            # 配置示例
│   └── scenarios.txt                  # 场景稿
├── scripts/
│   ├── publisher.py                   # 发布器
│   ├── batch_publish_multi.py         # 批量发布
│   └── ...
└── docs/
    └── 主题自定义指南.md                # 主题指南
```

---

## 📊 仓库统计

推送后可以查看：

- **Stars**: 收藏数
- **Forks**: 复制数
- **Watchers**: 关注数
- **Issues**: 问题反馈
- **Pull Requests**: 贡献代码

---

## 🔗 分享仓库

### 仓库链接

创建成功后，仓库地址：
```
https://github.com/ssing2/wechat-auto-publish-system
```

### 克隆命令

其他用户可以克隆：

```bash
# HTTPS
git clone https://github.com/ssing2/wechat-auto-publish-system.git

# SSH
git clone git@github.com:ssing2/wechat-auto-publish-system.git
```

### 分享到社交媒体

- **微信群**: 分享链接
- **朋友圈**: 生成二维码
- **技术社区**: 发布到V2EX、掘金等

---

## 🆘 常见问题

### Q1: 推送失败？

**原因**：认证失败

**解决**：
1. 检查Token是否有效
2. 使用SSH方式
3. 检查网络连接

### Q2: 仓库已存在？

**解决**：
1. 删除GitHub上的旧仓库
2. 或使用新仓库名

### Q3: 大文件推送失败？

**解决**：
1. 使用Git LFS
2. 或移除大文件

---

## ✅ 检查清单

推送前确认：

- [ ] GitHub账号已登录
- [ ] SSH密钥已配置（或Token已创建）
- [ ] 仓库名称已确认
- [ ] 代码已提交
- [ ] .gitignore已配置

---

## 🎉 推送成功！

推送成功后，你会看到：

```
Enumerating objects: 21, done.
Counting objects: 100% (21/21), done.
Delta compression using up to 4 threads.
Compressing objects: 100% (21/21), done.
Writing objects: 100% (21/21), 35.45 KiB | 2.36 MiB/s, done.
Total 21 (delta 0), reused 0 (delta 0)
To github.com:ssing2/wechat-auto-publish-system.git
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

**访问仓库**：
```
https://github.com/ssing2/wechat-auto-publish-system
```

---

**祝您发布成功！** 🎉

如有问题，请查阅GitHub文档或联系技术支持。
