# 微信公众号视觉排版与 HTML 合规规约 (Typesetting Core Rules)

> 本规范指导微信公众号完全内联样式的渲染与合规校验，供 `wechat-creator` Skill 与 `core/typesetter.py` 排版引擎统一遵循。

---

## 一、 移动端阅读三大核心法则

微信公众号 95% 以上发生在移动端场景，排版的核心任务是：**提升手机端视觉呼吸感、降低眼球疲劳、提高长文完读率**。

1. **短段落与呼吸留白**：
   - 严禁出现连续 4 行以上（超过 100 字）无喘息的密集黑块段落。
   - 严格执行单段 1~3 句话断行法则，段与段之间保持充裕的内联外边距（`margin: 14px 0`）。
   - 单行字符数严格适配移动端宽度，容器建议最大宽度设为 `677px` 并自动居中（`margin: 0 auto; max-width: 677px; padding: 16px 14px;`）。

2. **高级克制三色调原则**：
   - **底色**：纯白 `#ffffff` 或极浅灰白 `#fafafa`；
   - **正文字体色**：严禁使用刺眼的纯黑 `#000000`！推荐使用舒适深灰：`#2f3e3a`、`#374151` 或 `#27272a`；
   - **主强调色 (Primary Accent)**：用于章节徽章、序号胶囊、关键加粗与重点左边框，例如松烟墨绿 `#31544A`、手泽深赭 `#6B573F`、金石灰金 `#7A6A45`、科技蓝 `#1f6feb` 等；
   - **辅助淡底色 (Light Tint)**：主色的高明度淡底（如 `#f4f7f6`、`#fbf9f5`），专用于卡片和引用背景。

3. **字号与行高黄金比例**：
   - 正文字号：精细适中的 `15px`（适合快节奏阅读）或 `16px`（适合深度特稿）；
   - 行间距（line-height）：严格保持在 **`1.75 ~ 1.85`** 倍之间（过紧压抑，过松视线容易断流）；
   - 字间距（letter-spacing）：建议 `0.4px ~ 0.6px`，极大提升汉字排版的舒展度。

---

## 二、 微信公众号编辑器兼容性技术硬规（反过滤核心）

微信官方后台编辑器（mp.weixin.qq.com）底层基于定制的富文本 ProseMirror 引擎，必须严格遵守以下技术规则：

1. **文字节点必须包裹 `<span leaf="">`**：
   - **核心反过滤机制**：在直接复制粘贴进公众号后台时，裸露在 `<p>`、`<section>` 中的文字会被微信编辑器重写清洗；
   - 只要将文字节点用 `<span leaf="">正文</span>` 包裹，微信就会将其识别为**原子叶子节点**，100% 完整保留内联的 `color`、`font-size`、`letter-spacing`、`line-height` 与微下划线！

2. **必须 100% 使用内联样式 (`style="..."`)**：
   - 微信后台会直接剥离 `<style> ... </style>` 代码块；
   - 微信后台会剥离外部 CSS 类名选择器（`class="..."`）；
   - 严禁使用外部 CSS 变量 `var(--...)`（必须写死静态 Hex 色值）。

3. **标签白名单与替换原则**：
   - **禁止 `<div>`**：微信后台容易将 `<div>` 强制断行或拆碎为 `<p>`，**一律使用 `<section>` 替代容器**；
   - 允许标签：`<section>`, `<p>`, `<h1>`, `<h2>`, `<h3>`, `<span>`, `<strong>`, `<em>`, `<code>`, `<pre>`, `<blockquote>`, `<ul>`, `<ol>`, `<li>`, `<img>`, `<br>`；
   - 严禁脚本与浮动：严禁 `<script>`, `position: fixed/absolute/sticky`, `float`, `display: grid`。列表对齐与图文一律采用 `display: flex; align-items: baseline;`。

4. **中文标点全角化规范**：
   - 正文标点一律使用中文全角（`，`、`；`、`！`、`？`、`：`、`“”`、`‘’`），禁止英文直引号与半角逗号；
   - 代码块（`<code>`, `<pre>`）与 URL 链接内部严格保留英文半角符号。

5. **代码块消除 `white-space: pre`**：
   - 移动端 `white-space: pre` 会造成严重左缩进与空行崩溃；
   - 代码块每行使用紧凑 `<section style="margin: 0; line-height: 1.6;"><span leaf="">...</span></section>` 渲染，代码缩进使用全角空格 `　` 替代。

---

## 三、 标准内联组件设计规范

### 1. 二级标题（Section Heading - H2）
- 结构特征：带有双位数字序号胶囊或微下划线，标题文字严格包裹 `<span leaf="">`。
- 示范代码：
  ```html
  <section style="margin: 30px 0 14px 0; padding-bottom: 9px; border-bottom: 1px solid #d6e0dc; display: flex; align-items: center;">
    <span style="background: #31544A; color: #ffffff; font-size: 11px; font-weight: 800; padding: 2.5px 7.5px; border-radius: 6px; margin-right: 10px; display: inline-block; letter-spacing: 0.5px; flex-shrink: 0;"><span leaf="">01</span></span>
    <h2 style="margin: 0; font-size: 17px; color: #1e293b; font-weight: 700; letter-spacing: 0.4px; line-height: 1.45;"><span leaf="">章节标题文本</span></h2>
  </section>
  ```

### 2. 重点金句引用卡（Quote Card）
- 结构特征：左侧实线微彩色条，淡底色微圆角，大号半透明引号点缀，全用 `<section>`。
- 示范代码：
  ```html
  <blockquote style="margin: 16px 0; padding: 10px 14px; background-color: #f4f7f6; border-left: 3.5px solid #31544A; border-radius: 0 6px 6px 0; color: #1e293b; font-size: 14px; line-height: 1.72;">
    <section style="font-size: 18px; font-family: Georgia, serif; color: #31544A; line-height: 1; margin-bottom: 2px; opacity: 0.7;">“</section>
    <section style="font-weight: 500; color: #1e293b;"><span leaf="">核心观点与金句内容文本</span></section>
  </blockquote>
  ```

### 3. 出版级对比分析卡（Comparison / VS Card）
- 结构特征：左右双列卡片，红色误区/传统做法 vs 主题色正向解法，视觉冲击极强。
- Markdown 语法支持：
  ```markdown
  > [!VS]
  > 传统做法：满屏大红大绿、花哨卡通边框、套话连篇
  > 智能破局：稳重灰调、1~3句呼吸感断行、事实查证
  ```

### 4. 杂志双语大刊头（Magazine Hero Masthead）
- 结构特征：置于正文标题上方，包含大写英文分类与中文刊名，附带极细灰色分隔线。
- 示范代码：
  ```html
  <section style="margin: 18px 0 16px 0; display: flex; align-items: center; gap: 10px; border-bottom: 1px solid #d6e0dc; padding-bottom: 10px;">
    <span style="font-size: 11.5px; font-weight: 800; color: #31544A; letter-spacing: 2px; text-transform: uppercase;"><span leaf="">EDITORIAL</span></span>
    <span style="font-size: 11px; color: #64748b; letter-spacing: 0.5px;"><span leaf="">松烟 · 深度内刊</span></span>
  </section>
  ```

### 5. 关键词重点微下划线（Keyword Micro-Underline）
- 结构特征：正文加粗 `**关键概念**` 时，除保持 700 字重外，底部附带 `border-bottom: 1.5px solid {accent}` 主题色微细线与 `padding-bottom: 1px`，避免满屏纯黑大粗体的视觉压迫感。

### 6. Mac 终端风格代码块（Terminal Code Block）
- 结构特征：深色底，红黄绿三色圆点顶栏，逐行紧凑 `<section>`，全角空格缩进，横向滚动。
- 示范代码：
  ```html
  <section style="margin: 20px 0; border-radius: 8px; overflow: hidden; background-color: #1e293b; box-shadow: 0 4px 16px -8px rgba(15,23,42,0.4);">
    <section style="display: flex; align-items: center; padding: 9px 14px; background-color: #0f172a;">
      <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background-color: #ff5f56; margin-right: 7px;"></span>
      <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background-color: #ffbd2e; margin-right: 7px;"></span>
      <span style="display: inline-block; width: 10px; height: 10px; border-radius: 50%; background-color: #27c93f;"></span>
      <span style="margin-left: 12px; font-size: 12px; color: #64748b; font-family: Consolas, monospace; letter-spacing: 1px;"><span leaf="">python</span></span>
    </section>
    <pre style="margin: 0; padding: 12px 14px; background-color: transparent; color: #e2e8f0; font-family: SFMono-Regular, Consolas, Monaco, monospace; font-size: 13px; line-height: 1.6; overflow-x: auto; border: none; white-space: normal;">
      <section style="margin: 0; line-height: 1.6;"><span leaf="">def hello_world():</span></section>
      <section style="margin: 0; line-height: 1.6;"><span leaf="">　　return "微信原生内联排版"</span></section>
    </pre>
  </section>
  ```

---

## 四、 微信原生精选主题速查表 (Theme Palette)

系统全面集成出版物级与现代互联网高质感主题：
- **松烟墨羽杂志 (`moyu_green`)**：`#31544A` 深墨绿，内刊特稿与深度测评首选（极力推荐）；
- **手泽橄榄专栏 (`olive_journal`)**：`#6B573F` 熟赭色配墨黑，纸质书出版物质感，复盘特稿首选；
- **金石黑金杂志 (`noir_gold`)**：`#18181b` 纯黑配 `#7A6A45` 哑光灰金，商业财经与高管专访首选；
- **霓灰极光紫韵 (`aurora_violet`)**：`#4A4458` 低饱和灰紫，前沿 AIGC 与创新科技首选；
- **经典科技蓝 (`tech_blue`)**：`#1f6feb`，数字化开发与实战教程；
- **极简留白 (`pure_minimal`)**：素雅黑白灰，随笔与深度观点沉浸阅读；
- **清爽阅读 (`clean_read`)**：`#2563eb`，科普长文与书评；
- **典雅墨绿 (`forest_green`)**、**活力暖橙 (`warm_amber`)**、**黑金质感 (`business_dark`)**。

---

## 五、 微信 HTML 静态合规校验器 (`core/validator.py`)

所有排版产物必须通过合规校验器验证（0 错误）：
1. **0 平台违禁标签**：无 `<style>`, `<script>`, `<div>`, `<link>`, `class`, `id`；
2. **0 不兼容样式**：无 `position: fixed/absolute/sticky`, `float`, `display: grid`, `var(--...)`；
3. **100% 文本节点保护**：所有正文、标题、徽章均包含在 `<span leaf="">` 内；
4. **全角标点合规**：正文中无混用的英文半角逗号、分号及英文直引号。
