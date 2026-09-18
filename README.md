<div align="center">

# wechat-creator · 微信公众号全能创作 Skill 工具包

**把成稿排版，或按主题端到端写作，去AI味、起标题、配2.35:1封面、MCP自动直推平台工作台**

8+4 套微信 100% 原生内联主题 · 11 种自然写作结构 · 三阶去AI味责任编辑 · 2.35:1 官方封面 · MCP 全自动闭环

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![MCP Supported](https://img.shields.io/badge/MCP-Connected-blueviolet.svg)](https://modelcontextprotocol.io/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blue.svg)](https://claude.ai/code)
[![Cursor](https://img.shields.io/badge/Cursor-Skill-7c3aed.svg)](https://cursor.com)
[![Codex](https://img.shields.io/badge/OpenAI%20Codex-Skill-green.svg)](https://openai.com)
[![Themes](https://img.shields.io/badge/Themes-8%2B4%20Presets-1f6feb.svg)](references/typesetting.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/cscmcs/wechat-creator-skill/pulls)

</div>

---

面向 AI Agent（Claude Code / Cursor / Codex / Antigravity / OpenCode 等）深度定制的微信公众号全能创作与排版技能（Skill）。它可以：

- 把已有 Markdown / Word / PDF / 纯文本长文，排版成**样式 100% 内联、粘贴到微信公众平台编辑器绝不掉格式**的合规 HTML；
- 按你提供的主题与思路全流程创作：深度事实核验、11 大经典文章结构写作、三阶去 AI 味润色、5 类高吸引力真实标题打磨；
- 遵循 2.35:1 官方比例与少字化原则规划封面海报及正文视觉，并通过 MCP 自动直推保存至你的**平台创作工作台**；
- 预置 8 套精选内联主题 + 4 套杂志高定排版（松烟墨绿、手泽深赭、金石灰金、霓灰极光），支持出版级微下划线与红绿对比卡；
- 深度支持 **Model Context Protocol (MCP)**：Agent 写完自动入库平台后台，用户在网页端打开即可可视化微调排版，并由平台统一提供一键推微信或富文本复制。

---

## ✨ 这个 Skill 能做什么

- **8+4 套精选微信原生内联主题**：覆盖科技前沿、深度商业、文艺特稿、干货教程、极简随笔与杂志高定，全部打磨至拿来即用。
- **100% 原生内联 CSS · 绝不掉格式**：彻底规避 `<style>`、`class` 等微信编辑器会强行过滤剥离的语法；样式完整写在标签 `style` 属性中，跨 Mac / Windows / 微信公众号网页编辑器排版表现完全一致。
- **手机竖屏呼吸感节奏**：严格执行短段落法则（1~3 句话断行，手机屏不超过 4~5 行），正文字号 15~16px，黄金行高 1.75~1.85，字间距 0.5px，告别大段黑块文字压迫感。
- **三阶去 AI 味责任编辑**：
  - *内容层*：拒绝泛泛而谈与机械平衡，强化核心观点与真实洞察；
  - *结构层*：拒绝“首先、其次、最后”的八股模板与假大空总结尾巴；
  - *语言层*：彻底剔除“底层逻辑、抓手、赋能、闭环、维度”等 AI 翻译腔与空洞大词。
- **11 大经典文章结构自然写作**：包含清单体、对比体、故事-反转-顿悟、问题-拆解-方案、特稿叙事、时间线复盘等，防同质化行文。
- **5 类高吸引力真实标题法**：打磨直接型、经验型、冲突型、结果型、故事型标题，杜绝耸动劣质标题党。
- **2.35:1 微信官方封面海报与配图规划**：严格遵循 900×383（2.35:1）封面尺寸规范与少字化（<16字）排版原则。
- **严谨事实查证与防幻觉**：提取一手信源与数据时间戳，严禁模型臆造统计数字、虚假案例或人物对话。
- **MCP 平台双向闭环与自动直推入库**：
  - Agent 创作完成后，自动调用 `save_article` 工具同步保存至平台数据库，方便网页端二次编辑与出版级微调；
  - 创作前可调用 `get_article_templates` 动态感知平台系统主题与用户保存的专属排版模板；
  - 创作中可调用 `get_writer_profile` 注入作者专属行文风格偏好；
  - 调研中可调用 `search_materials` 检索私有素材库。

---

## 🔌 MCP 平台深度集成与自动化闭环

本 Skill 原生支持 [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)，实现与自建微信公众号创作平台的**双向无缝数据闭环**：

```
+-------------------+       1. 获取模板/画像        +-----------------------+
|                   | <---------------------------> |                       |
|     AI Agent      |                               |      MCP Server       |
| (Cursor / Claude) |       2. 创作完成自动直推      | (FastAPI + Database)  |
|                   | ----------------------------> |                       |
+-------------------+      save_article(title,...)  +-----------------------+
                                                                |
                                                                v
                                                    +-----------------------+
                                                    |    平台网页工作台      |
                                                    | (出版级排版定制器微调) |
                                                    +-----------------------+
                                                                |
                                                                v
                                                    +-----------------------+
                                                    |   微信官方公众平台     |
                                                    | (网页端一键同步草稿箱)|
                                                    +-----------------------+
```

### 核心 MCP 工具矩阵

| 工具名称 | 触发阶段 | 核心功能说明 |
| :--- | :--- | :--- |
| `get_article_templates` | Phase 5 前 | 获取系统 12 套内联排版主题及用户在网页端保存的**专属自定义排版模板** |
| `save_article` | Phase 7 | **核心交付终点**：将撰写排版完毕的文章自动存入用户个人平台文章库 |
| `get_writer_profile` | Phase 2 | 读取用户的个人写作画像（语气、人称、句式习惯、禁忌表达），实现千人千面 |
| `search_materials` | Phase 1 | 检索用户在平台上积累的私有事实素材、案例卡片与灵感备忘 |

### 客户端接入配置示例

#### 1. Cursor 配置 (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "wechat-platform": {
      "url": "http://127.0.0.1:8765/mcp/sse?token=YOUR_MCP_TOKEN"
    }
  }
}
```

#### 2. Claude Desktop 配置 (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "wechat-platform": {
      "command": "python3",
      "args": ["/绝对路径/gongzhonghao/mcp/server.py", "--token", "YOUR_MCP_TOKEN"]
    }
  }
}
```

---

## 🎨 精选微信原生内联主题速查表

| 主题名称 | 代号 | 调性定位 | 主强调色 | 适合场景 |
|---|---|---|---|---|
| **极简留白** | `pure_minimal` | 简约克制 | `#1f2937` (石墨黑灰) | 随笔、独立思考、个人成长 |
| **清爽阅读** | `clean_read` | 净白明朗 | `#2563eb` (净蓝) | 深度科普、长文阅读、书评 |
| **经典科技蓝** | `tech_blue` | 专业科技 | `#1f6feb` (科技蓝) | 技术教程、AIGC、开发者工具 |
| **松烟墨羽杂志** | `moyu_green` | 出版物高定 | `#31544A` (深墨绿) | 深度研报、长文特稿、商业复盘 |
| **手泽橄榄专栏** | `olive_journal` | 人文纸质感 | `#6B573F` (深赭棕) | 商业案例复盘、特稿随笔 |
| **金石黑金杂志** | `noir_gold` | 沉稳奢雅 | `#7A6A45` (哑光灰金) | 商业评论、财报拆解、高端访谈 |
| **霓灰极光紫韵** | `aurora_violet` | 前沿潮流 | `#4A4458` (霓灰紫) | AI 前沿、交互设计、工具评测 |
| **典雅墨绿** | `forest_green` | 人文深邃 | `#2d6a4f` (墨绿) | 人物特稿、文化思考、行业洞察 |
| **活力暖橙** | `warm_amber` | 元气高光 | `#ea580c` (暖橙) | 产品测评、干货清单、营销案例 |
| **黑金质感** | `business_dark` | 商业对称 | `#18181b` + 金光 | 商业评论、财经长文 |
| **极光紫霓** | `vibrant_orange` | 活力实用 | `#f97316` (橙灰) | 活动公告、工具榜单 |
| **用户专属模板** | `custom_<id>` | 自由调色定制 | 用户自定义配色 | 通过网页端「出版级排版定制器」保存 |

---

## 🚀 快速开始

### 方式一：让 Agent 自主一键安装（极力推荐 ⭐）

无需手动下载解压。在 **Cursor Composer、Claude Code、Codex** 或任何 AI Agent 对话框中，发送以下这句话：

```text
请帮我在当前工作区安装微信公众号创作技能，仓库地址为：https://github.com/cscmcs/wechat-creator-skill.git
请将其 clone 到 .agents/skills/wechat-creator 目录下（若本地环境未安装 git，请直接下载 zip 并解压至该目录）。
```

Agent 将自动在当前工作区完成拉取与就绪。

### 方式二：开发者手动克隆到工作区

```bash
git clone https://github.com/cscmcs/wechat-creator-skill.git .agents/skills/wechat-creator
```

---

## 📖 核心创作用法

| 对比项 | 用法 1：已有成稿，只排版润色 | 用法 2：给主题思路，AI 端到端创作 |
|---|---|---|
| **你提供** | 文章内容（Markdown / Word / 草稿正文） | 主题 + 核心观点 / 事实要点 / 约束清单 |
| **Agent 执行** | 格式归一化、可选去 AI 味、起标题、内联排版、封面、MCP 自动直推 | 事实调研、11种结构写作、三阶去AI味、5类标题、排版、封面、MCP 自动直推 |
| **去 AI 味** | 可选，默认润色口语化与节奏感 | **强制开启三阶深度去 AI 味编辑** |
| **平台同步** | 自动存入平台工作台文章库 | 自动存入平台工作台文章库 |

### 💡 提示词调用示范

#### 示范 1：已有稿件排版并自动直推工作台
> “`@wechat-creator` 请用【松烟墨羽杂志】主题把这篇稿件排版成微信内联 HTML，帮我拟 3 个冲突型标题，设计封面并自动同步到我的平台工作台：[粘贴你的文章内容]”

#### 示范 2：从零全流程创作推文
> “`@wechat-creator` 帮我写一篇关于‘普通程序员如何用 Agent 落地实际业务’的公众号文章。  
> 要求：清单体结构，短句断行，去掉所有空洞大词，使用【科技蓝】排版，完成后自动调用 save_article 保存至平台工作台。”

#### 示范 3：单独局部打磨
* **单独去 AI 味**：“`@wechat-creator` 这段内容 AI 翻译腔太重，用人话帮我重构，保留核心论点。”
* **单独起标题**：“`@wechat-creator` 根据这篇文章，按照 5 类真实标题法（经验型/冲突型/故事型等）起 5 个吸引力标题。”

---

## ⚡ 7 阶段标准创作流水线

```text
[阶段 1: 事实查证] -> [阶段 2: 结构写作] -> [阶段 3: 去AI味责任编辑]
         |                     |                       |
[阶段 7: MCP 直推工作台] <- [阶段 6: 封面设计] <- [阶段 5: 内联排版] <- [阶段 4: 5类真实标题]
```

1. **阶段 1：事实查证与防幻觉核验 (`references/research.md`)**：溯源一手信源，核对数据时间戳；支持 MCP `search_materials` 检索私有素材。
2. **阶段 2：结构化自然写作 (`references/structures.md`)**：选择 11 种结构之一，贯彻 1~3 句断行；支持 MCP `get_writer_profile` 注入作者语气风格。
3. **阶段 3：三阶去 AI 味责任编辑 (`references/humanizer.md`)**：内容层去模板、结构层去八股、语言层剔除空洞行话。
4. **阶段 4：5 类高吸引力真实标题 (`references/titles.md`)**：直接型、经验型、冲突型、结果型、故事型标题打磨。
5. **阶段 5：微信原生内联 CSS 排版 (`references/typesetting.md`)**：全属性内联化，支持微下划线与红绿对比卡；支持 MCP `get_article_templates` 获取专属模板。
6. **阶段 6：2.35:1 官方封面海报设计 (`references/cover.md`)**：900×383 黄金规格，少字化构图建议。
7. **阶段 7：MCP 自动直推平台工作台**：自动调用 `save_article` 持久化至平台数据库，向用户反馈文章 ID，便于后续在网页端进行可视化微调排版与公众号推送。

---

## 📁 目录结构

```text
wechat-creator-skill/
├── SKILL.md                # 技能主入口（包含 YAML 元数据与自适应流水线调度）
├── README.md               # 完整项目说明、MCP 接入指南与排版规范
└── references/             # 6 大细分专业知识库
    ├── research.md         # 事实调研与一手信源查证规范（含 MCP search_materials）
    ├── structures.md       # 11 种经典推文结构与竖屏短句法则（含 MCP get_writer_profile）
    ├── humanizer.md        # 内容/结构/语言三阶去 AI 味编辑指南
    ├── titles.md           # 5 类爆款真实标题打磨方法论
    ├── typesetting.md      # 12 套内联 CSS 主题、微下划线与 VS 对比卡规范
    └── cover.md            # 2.35:1 官方封面海报与视觉配图规范
```

---

## ❓ 常见问题 (FAQ)

### Q: 为什么复制到微信公众平台时不会掉格式？
**A**：微信官方编辑器会暴力剥离 `<style>` 标签和外部 CSS 类名（`class`），也会破坏部分 flex/grid 复杂布局。本技能在渲染时将所有边距、圆角、字号、边框和阴影**100% 编译为内联 `style="..."`**，标签完全符合微信安全白名单，因此无论复制还是 API 直推，样式绝不丢失。

### Q: Agent 写完文章后如何与平台网站互动？
**A**：通过 MCP 的 `save_article` 工具，Agent 会自动将排版渲染好的 Markdown 与微信 HTML 一同存入平台数据库。用户可以在平台 Web 界面上打开该文章，使用**出版级排版定制器**拖拽调色、微调字号或增减对比卡，然后再由平台网页端一键推送到微信公众平台草稿箱。

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 协议开源。欢迎 Star 与提交 PR 优化提示词及排版主题！\n