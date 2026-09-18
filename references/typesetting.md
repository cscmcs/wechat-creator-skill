# 微信公众号视觉排版与 HTML 合规规约 (Typesetting Core Rules)

> 本规范指导微信公众号完全内联样式的渲染与校验，供 `wechat-typesetting` Skill 与 `core/typesetter.py` 排版引擎统一遵循。

---

## 一、 移动端阅读三大核心法则

微信公众号 95% 以上发生在移动端场景，排版的核心任务是：**提升手机端视觉呼吸感、降低眼球疲劳、提高长文完读率**。

1. **短段落与呼吸留白**：
   - 严禁出现连续 4 行以上（超过 100 字）无喘息的密集黑块段落。
   - 推荐单段 1~3 句话，段与段之间保持充裕的内联外边距（`margin: 14px 0`）。
   - 单行字符数严格适配移动端宽度，容器建议最大宽度设为 `677px` 并自动居中（`margin: 0 auto; max-width: 677px; padding: 16px 14px;`）。

2. **高级克制三色调原则**：
   - **底色**：纯白 `#ffffff` 或极浅灰白 `#fafafa`；
   - **正文字体色**：严禁使用刺眼的纯黑 `#000000`！推荐使用舒适深灰：`#333333`、`#374151` 或 `#3f3f3f`；
   - **主强调色 (Primary Accent)**：仅用于章节徽章、序号胶囊、关键加粗与重点左边框，例如科技蓝 `#1f6feb`、森林墨绿 `#2d6a4f`、元气橙 `#ea580c`、黑曜金 `#18181b` 等；
   - **辅助淡底色 (Light Tint)**：主色的高明度淡底（如 `#f0f6ff`、`#f4fbf7`），专用于 Tip 卡片和引用背景。

3. **字号与行高黄金比例**：
   - 正文字号：精细适中的 `15px`（适合快节奏阅读）或 `16px`（适合深度特稿）；
   - 行间距（line-height）：严格保持在 **`1.75 ~ 1.85`** 倍之间（过紧压抑，过松视线容易断流）；
   - 字间距（letter-spacing）：建议 `0.4px ~ 0.6px`，极大提升汉字排版的舒展度。

---

## 二、 微信公众号编辑器兼容性技术硬规

微信官方后台编辑器（mp.weixin.qq.com）对外部样式有严格的过滤机制：
1. **必须完全使用内联样式 (`style="..."`)**：
   - 微信后台会直接剥离 `<style> ... </style>` 代码块；
   - 微信后台会剥离外部 CSS 类名选择器（`class="..."` 可能会被直接清洗或无法生效）；
   - 必须把所有布局、字体、颜色、边距完整写在每个标签的内联 `style` 属性中。
2. **严禁使用复杂不可控的 CSS 特性**：
   - 严禁使用 CSS Grid 布局；
   - 严禁使用复杂的 `position: fixed` 或重度负边距定位（在 Android 微信端极易错位重叠）；
   - 布局优先采用纯内联块（`display: flex; align-items: center;` 或标准块级流式布局）。
3. **标签白名单安全原则**：
   - 允许标签：`<section>`, `<div>`, `<p>`, `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<span>`, `<strong>`, `<em>`, `<code>`, `<pre>`, `<blockquote>`, `<ul>`, `<ol>`, `<li>`, `<img>`, `<br>`；
   - 严禁脚本与交互标签：严禁 `<script>`, `<iframe style="...">`, `<button>`, `onclick=...` 等任何事件监听属性。

---

## 三、 标准内联组件设计规范

### 1. 二级标题（Section Heading - H2）
- 结构特征：必须带有序号胶囊、左侧纵向强调色条或微下划线，避免单调加粗。
- 示范代码：
  ```html
  <section style="margin: 28px 0 12px 0; padding-bottom: 8px; border-bottom: 1px solid #f0f6ff; display: flex; align-items: center;">
    <span style="background-color: #1f6feb; width: 3.5px; height: 16px; border-radius: 2px; margin-right: 8px; display: inline-block; flex-shrink: 0;"></span>
    <span style="background: #f0f6ff; color: #1f6feb; font-size: 12.5px; font-weight: 700; padding: 2px 7px; border-radius: 4px; margin-right: 8px; display: inline-block; letter-spacing: 0.5px;">01</span>
    <h2 style="margin: 0; font-size: 17px; color: #1e293b; font-weight: 700; letter-spacing: 0.5px; line-height: 1.45;">章节标题文本</h2>
  </section>
  ```

### 2. 重点金句引用卡（Quote Card）
- 结构特征：左侧实线微彩色条，淡底色微圆角，大号半透明引号点缀。
- 示范代码：
  ```html
  <blockquote style="margin: 16px 0; padding: 10px 14px; background-color: #f8fafc; border-left: 3.5px solid #1f6feb; border-radius: 0 6px 6px 0; color: #1e293b; font-size: 14px; line-height: 1.72; position: relative;">
    <div style="font-size: 18px; font-family: Georgia, serif; color: #38bdf8; opacity: 0.7; line-height: 1; margin-bottom: 2px;">“</div>
    <div style="font-weight: 500; color: #1e293b;">核心观点与金句内容文本</div>
  </blockquote>
  ```

### 3. 高亮重点提示盒（Tip Box）
- 结构特征：虚线或实线边框浅色背景盒，用于步骤提醒或避坑指南。
- 示范代码：
  ```html
  <div style="margin: 14px 0; padding: 9px 12px; background-color: #f0f6ff; border: 1px dashed #93c5fd; border-radius: 6px; font-size: 13.5px; color: #1e293b; line-height: 1.65;">
    <strong>💡 关键提示：</strong> 说明文本内容...
  </div>
  ```

### 4. 出版级对比分析卡（Comparison / VS Card）
- 结构特征：左右或上下双列卡片，红色误区/传统做法 vs 主题色正向解法，视觉冲击极强。
- Markdown 语法支持：
  ```markdown
  > [!VS]
  > 传统做法：满屏大红大绿、花哨卡通边框、套话连篇
  > 智能破局：稳重灰调、1~3句呼吸感断行、事实查证
  ```

### 5. 杂志双语大刊头（Magazine Hero Masthead）
- 结构特征：置于正文标题上方，包含大写英文分类（如 `EDITORIAL REVIEW`、`TECH INSIGHT`）与中文刊名，附带极细灰色分隔线，出版物仪式感极强。

### 6. 关键词重点微下划线（Keyword Micro-Underline）
- 结构特征：正文加粗 `**关键概念**` 时，除保持 700 字重外，底部附带 `1.5px solid {accent}` 主题色微细线与 `padding-bottom: 1px`，避免满屏纯黑大粗体的视觉压迫感。

### 7. 代码块（Code Block）
- 结构特征：深色背景，等宽字体，开启横向滚动且带微圆角。
- 示范代码：
  ```html
  <pre style="margin: 18px 0; background-color: #1e1e1e; color: #d4d4d4; border-radius: 8px; padding: 14px 16px; overflow-x: auto; font-family: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, Courier, monospace; font-size: 13px; line-height: 1.6; -webkit-overflow-scrolling: touch;"><code>代码片段文本</code></pre>
  ```

---

## 四、 微信原生精选主题速查表 (Theme Palette)

系统全面集成出版物级与现代互联网高质感主题：
- **松烟墨绿 (`moyu_green`)**：`#31544A` 深墨绿，内刊特稿与深度测评首选（极力推荐）；
- **手泽手记 (`olive_journal`)**：`#6B573F` 熟赭色配墨黑，纸质书出版物质感，复盘特稿首选；
- **金石黑金 (`noir_gold`)**：`#18181b` 纯黑配 `#c5a059` 哑光灰金，商业财经与高管专访首选；
- **霓灰科技 (`aurora_violet`)**：`#4A4458` 低饱和灰紫，前沿 AIGC 与创新科技首选；
- **经典科技蓝 (`tech_blue`)**：`#1f6feb`，数字化开发与实战教程；
- **极简留白 (`pure_minimal`)**：素雅黑白灰，随笔与深度观点沉浸阅读；
- **清爽阅读 (`clean_read`)**：`#2563eb`，科普长文与书评；
- **典雅墨绿 (`forest_green`)**、**活力暖橙 (`warm_amber`)**、**胭脂红霞 (`crimson_editorial`)**。

---

## 五、 微信 HTML 校验门槛 (Validation Gate)

渲染完成后的 HTML 必须经过以下合规校验：
1. **无外链样式**：全文不包含 `<style>` 标签或外部 `<link rel="stylesheet">`。
2. **无违规外部脚本**：不包含 `<script>` 或任何 `on*=` 属性。
3. **样式完全内联**：所有段落、标题、列表项均显式携带 `style` 属性。
4. **图片链接合规**：图片应优先为合法 URL 或微信 CDN 链接 (`mmbiz.qpic.cn`)。
