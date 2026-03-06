# 微信公众号友好模板集合

## 📚 目录

本目录包含多种微信公众号友好的Markdown/CSS模板，可以直接使用或自定义。

---

## 🎨 内置模板

### 1. OrangeHeart（暖橙推荐）

**特点**：暖橙色调，专业亲切，适合法律科普

**使用**：
```yaml
wenyan:
  theme: "orangeheart"
```

**预览**：
- 标题：24px，深蓝色
- 正文：16px，行高1.8
- 强调：橙红色
- 引用：蓝色边框

---

### 2. ProfessionalBlue（专业蓝）

**适合**：专业类、技术类、法律类公众号

**文件**：`themes/professional-blue.css`

```css
/* Professional Blue Theme - 专业蓝主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #2c3e50;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #1a5490;
  margin-bottom: 20px;
  border-bottom: 3px solid #3498db;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #2980b9;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #3498db;
  padding-left: 10px;
}

.weui-article h3 {
  font-size: 18px;
  font-weight: 500;
  color: #3498db;
  margin-top: 25px;
  margin-bottom: 12px;
}

/* 段落 */
.weui-article p {
  margin-bottom: 15px;
  text-align: justify;
}

/* 强调 */
.weui-article strong {
  color: #e74c3c;
  font-weight: 600;
}

.weui-article em {
  color: #3498db;
  font-style: normal;
}

/* 列表 */
.weui-article ul,
.weui-article ol {
  margin-left: 20px;
  margin-bottom: 15px;
}

.weui-article li {
  margin-bottom: 8px;
  line-height: 1.6;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #3498db;
  padding: 15px;
  margin: 20px 0;
  background: #ecf0f1;
  color: #7f8c8d;
  border-radius: 4px;
}

/* 代码 */
.weui-article code {
  background: #f4f4f4;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: "Consolas", "Monaco", monospace;
  color: #e74c3c;
}

.weui-article pre {
  background: #2c3e50;
  color: #ecf0f1;
  padding: 15px;
  border-radius: 5px;
  overflow-x: auto;
  margin: 20px 0;
}

.weui-article pre code {
  background: transparent;
  color: inherit;
  padding: 0;
}

/* 表格 */
.weui-article table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
}

.weui-article th,
.weui-article td {
  border: 1px solid #bdc3c7;
  padding: 10px;
  text-align: left;
}

.weui-article th {
  background: #3498db;
  color: white;
  font-weight: 600;
}

.weui-article tr:nth-child(even) {
  background: #ecf0f1;
}

/* 分隔线 */
.weui-article hr {
  border: none;
  border-top: 2px solid #bdc3c7;
  margin: 30px 0;
}

/* 链接 */
.weui-article a {
  color: #3498db;
  text-decoration: none;
  border-bottom: 1px dotted #3498db;
}

.weui-article a:hover {
  color: #2980b9;
  border-bottom-style: solid;
}

/* 图片 */
.weui-article img {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 20px auto;
  border-radius: 5px;
}

/* 提示框 */
.highlight-box {
  background: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 15px;
  margin: 20px 0;
  border-radius: 4px;
}

.info-box {
  background: #d1ecf1;
  border-left: 4px solid #17a2b8;
  padding: 15px;
  margin: 20px 0;
  border-radius: 4px;
}

.success-box {
  background: #d4edda;
  border-left: 4px solid #28a745;
  padding: 15px;
  margin: 20px 0;
  border-radius: 4px;
}

.warning-box {
  background: #f8d7da;
  border-left: 4px solid #dc3545;
  padding: 15px;
  margin: 20px 0;
  border-radius: 4px;
}
```

---

### 3. ElegantPurple（优雅紫）

**适合**：情感类、生活类、女性向公众号

**文件**：`themes/elegant-purple.css`

```css
/* Elegant Purple Theme - 优雅紫主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #4a4a4a;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #8e44ad;
  margin-bottom: 20px;
  border-bottom: 3px solid #9b59b6;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #9b59b6;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #8e44ad;
  padding-left: 10px;
}

/* 段落 */
.weui-article p {
  margin-bottom: 15px;
  text-align: justify;
}

/* 强调 */
.weui-article strong {
  color: #e91e63;
  font-weight: 600;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #9b59b6;
  padding: 15px;
  margin: 20px 0;
  background: #f3e5f5;
  color: #7b1fa2;
  border-radius: 4px;
}

/* 代码 */
.weui-article code {
  background: #f3e5f5;
  padding: 2px 6px;
  border-radius: 3px;
  font-family: "Consolas", monospace;
  color: #8e44ad;
}

/* 链接 */
.weui-article a {
  color: #9b59b6;
  text-decoration: none;
  border-bottom: 1px dotted #9b59b6;
}
```

---

### 4. FreshGreen（清新绿）

**适合**：健康类、环保类、自然类公众号

**文件**：`themes/fresh-green.css`

```css
/* Fresh Green Theme - 清新绿主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #2c3e50;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #27ae60;
  margin-bottom: 20px;
  border-bottom: 3px solid #2ecc71;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #2ecc71;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #27ae60;
  padding-left: 10px;
}

/* 强调 */
.weui-article strong {
  color: #e67e22;
  font-weight: 600;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #2ecc71;
  padding: 15px;
  margin: 20px 0;
  background: #e8f8f5;
  color: #16a085;
  border-radius: 4px;
}
```

---

### 5. MinimalistGray（极简灰）

**适合**：科技类、技术类、极简风格公众号

**文件**：`themes/minimalist-gray.css`

```css
/* Minimalist Gray Theme - 极简灰主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  line-height: 1.7;
  color: #333;
  padding: 20px;
  font-size: 15px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 22px;
  font-weight: 600;
  color: #333;
  margin-bottom: 20px;
  border-bottom: 2px solid #333;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 18px;
  font-weight: 500;
  color: #555;
  margin-top: 25px;
  margin-bottom: 12px;
}

/* 强调 */
.weui-article strong {
  color: #000;
  font-weight: 700;
}

/* 引用 */
.weui-article blockquote {
  border-left: 3px solid #333;
  padding: 12px;
  margin: 20px 0;
  background: #f8f8f8;
  color: #666;
  border-radius: 2px;
}

/* 代码 */
.weui-article code {
  background: #eee;
  padding: 2px 5px;
  border-radius: 2px;
  font-family: "Monaco", "Consolas", monospace;
  color: #333;
}
```

---

### 6. WarmOrange（温暖橙）

**适合**：美食类、生活类、温暖风格公众号

**文件**：`themes/warm-orange.css`

```css
/* Warm Orange Theme - 温暖橙主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #4a4a4a;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #e67e22;
  margin-bottom: 20px;
  border-bottom: 3px solid #f39c12;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #f39c12;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #e67e22;
  padding-left: 10px;
}

/* 强调 */
.weui-article strong {
  color: #d35400;
  font-weight: 600;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #f39c12;
  padding: 15px;
  margin: 20px 0;
  background: #fef5e7;
  color: #e67e22;
  border-radius: 4px;
}
```

---

### 7. BusinessStyle（商务风）

**适合**：商业类、财经类、企业公众号

**文件**：`themes/business-style.css`

```css
/* Business Style Theme - 商务风主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #2c3e50;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #1a5490;
  margin-bottom: 20px;
  border-bottom: 3px solid #2c3e50;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #34495e;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #2c3e50;
  padding-left: 10px;
}

/* 强调 */
.weui-article strong {
  color: #c0392b;
  font-weight: 600;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #2c3e50;
  padding: 15px;
  margin: 20px 0;
  background: #ecf0f1;
  color: #7f8c8d;
  border-radius: 4px;
}
```

---

### 8. CutePink（可爱粉）

**适合**：母婴类、美妆类、年轻化公众号

**文件**：`themes/cute-pink.css`

```css
/* Cute Pink Theme - 可爱粉主题 */
.weui-article {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Microsoft YaHei", sans-serif;
  line-height: 1.8;
  color: #4a4a4a;
  padding: 20px;
  font-size: 16px;
}

/* 标题样式 */
.weui-article h1 {
  font-size: 24px;
  font-weight: 600;
  color: #e91e63;
  margin-bottom: 20px;
  border-bottom: 3px solid #f06292;
  padding-bottom: 10px;
}

.weui-article h2 {
  font-size: 20px;
  font-weight: 500;
  color: #f06292;
  margin-top: 30px;
  margin-bottom: 15px;
  border-left: 4px solid #e91e63;
  padding-left: 10px;
}

/* 强调 */
.weui-article strong {
  color: #c2185b;
  font-weight: 600;
}

/* 引用 */
.weui-article blockquote {
  border-left: 4px solid #f06292;
  padding: 15px;
  margin: 20px 0;
  background: #fce4ec;
  color: #e91e63;
  border-radius: 4px;
}
```

---

## 🎨 如何使用

### 方式1：直接使用内置主题

```yaml
wenyan:
  theme: "orangeheart"  # 文颜内置主题
```

### 方式2：使用本地主题文件

1. 复制上面的CSS代码到 `themes/` 目录
2. 修改配置：

```yaml
wenyan:
  theme: "custom"
  custom_theme_path: "themes/professional-blue.css"
```

### 方式3：创建自定义主题

参考上面的主题代码，修改颜色和样式即可。

---

## 📊 主题对比

| 主题 | 风格 | 适合类型 | 主色调 |
|------|------|----------|--------|
| OrangeHeart | 温暖专业 | 法律、科普 | 橙色 |
| ProfessionalBlue | 专业商务 | 技术、法律 | 蓝色 |
| ElegantPurple | 优雅情感 | 情感、生活 | 紫色 |
| FreshGreen | 清新自然 | 健康、环保 | 绿色 |
| MinimalistGray | 极简科技 | 科技、技术 | 灰色 |
| WarmOrange | 温暖生活 | 美食、生活 | 橙色 |
| BusinessStyle | 商务正式 | 商业、财经 | 深蓝 |
| CutePink | 可爱年轻 | 母婴、美妆 | 粉色 |

---

## 🎯 选择建议

### 法律科普类
- **推荐**：OrangeHeart、ProfessionalBlue
- **特点**：专业稳重，值得信赖

### 职场建议类
- **推荐**：BusinessStyle、ProfessionalBlue
- **特点**：商务正式，专业权威

### 情感生活类
- **推荐**：ElegantPurple、WarmOrange
- **特点**：温暖亲切，情感共鸣

### 健康养生类
- **推荐**：FreshGreen
- **特点**：清新自然，健康向上

### 母婴美妆类
- **推荐**：CutePink、WarmOrange
- **特点**：可爱年轻，亲和力强

### 科技技术类
- **推荐**：MinimalistGray、ProfessionalBlue
- **特点**：极简专业，技术感强

---

## ✅ 测试主题

使用以下命令测试主题：

```bash
# 方式1：使用文颜CLI
npx @wenyan-md/cli render \
  --file test.md \
  --theme custom \
  --custom-theme themes/professional-blue.css

# 方式2：直接发布测试
python scripts/publisher.py \
  --file test.md \
  --theme custom \
  --custom-theme themes/professional-blue.css
```

---

## 📝 贡献主题

欢迎贡献您的主题！

1. 创建CSS文件
2. 添加到本目录
3. 更新本文档
4. 提交Pull Request

---

## 🆘 常见问题

### Q: 如何切换主题？

修改 `config/config.yaml` 中的 `wenyan.theme` 配置。

### Q: 主题不生效？

检查CSS路径是否正确，清除缓存后重试。

### Q: 如何调整主题颜色？

编辑CSS文件，修改颜色变量即可。

---

**祝您使用愉快！** 🎨

如有问题，请查阅文档或联系技术支持。
