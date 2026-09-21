# wechat-creator · 微信公众号创作技能

面向现代 AI Agent（Antigravity、Cursor、Claude Code、Workbuddy 等）定制的微信公众号创作与排版技能。

可独立完成选题、事实调研、自然写作、责任编辑审校、标题拟定与封面策划；连接**星河文场 MCP** 后，进一步解锁作者画像、私域素材检索、历史文章分析与选题去重、平台排版主题、创作工作台持久化及微信公众号官方草稿箱直推能力。

---

## ⚖️ 能力分层矩阵

本技能采用清晰的双层能力架构。无需 MCP 即可独立完成高质量长文创作，接入星河文场 MCP 则享受完整的作者资产与工程化闭环：

| 创作环节与能力 | 纯 Skill 基础能力 | 星河文场 MCP 增强 |
| :--- | :---: | :---: |
| **基础智能选题**（基于对话与公开事实） | ✅ | ✅ |
| **事实调研与四级信源核验**（Fact Card） | ✅ | ✅ |
| **11 大经典框架自然写作**（移动端短段落） | ✅ | ✅ |
| **责任编辑审校**（八级去机械化，最小干预） | ✅ | ✅ |
| **自适应标题策略与分享摘要**（6~10候选） | ✅ | ✅ |
| **2.35:1 官方头条封面视觉规划与 Prompt** | ✅ | ✅ |
| **作者长期写作风格画像**（个性化语气与习惯） | — | ✅ |
| **私域素材库检索与笔记沉淀** | — | ✅ |
| **历史文章检索与智能选题去重** | — | ✅ |
| **旧文续篇与系列文章规划** | — | ✅ |
| **平台实时排版主题与私有自定义模板** | — | ✅ |
| **平台级高兼容微信内联排版引擎** | — | ✅ |
| **创作工作台持久化与可视化二次微调** | — | ✅ |
| **微信公众号官方草稿箱安全直推** | — | ✅ |

---

## ⚡ 主工作流与阶段路由 (Workflow)

```text
阶段 0：意图识别 (Intent Router)
   │
   ├─► 阶段 1：智能选题（按需，Topic 与 Title 分离，历史去重）
   ├─► 阶段 2：事实与素材准备（按需，四级信源核验，Fact Card）
   ├─► 阶段 3：文章结构与写作（内容优先，11 大思考框架，短段落呼吸感）
   ├─► 阶段 4：责任编辑审校（去 AI 味，最小干预原则）
   ├─► 阶段 5：标题与摘要（自适应 2~4 种策略，输出 6~10 个候选）
   ├─► 阶段 6：表现形式与封面策划（2.35:1 官方比例，少字强主体）
   └─► 阶段 7：交付（默认 Markdown 正文；连接 MCP 自动入库工作台或直推草稿箱）
```

技能具备自适应路由能力，根据用户指令按需加载对应知识库，避免无意义的冗余流转。

---

## 🚀 安装与配置指引

### 方式一：仅安装 Skill（独立创作模式）

在支持 Agent Skills 的客户端（Antigravity、Cursor 等）对话框中直接发送：

```text
请帮我在当前工作区安装微信公众号创作技能，仓库地址为：https://github.com/cscmcs/wechat-creator-skill.git
请将其 clone 到 .agents/skills/wechat-creator 目录下（若本地未安装 git，请下载 zip 并解压至该目录）。
```

或在终端中手动克隆：

```bash
git clone https://github.com/cscmcs/wechat-creator-skill.git .agents/skills/wechat-creator
```

安装完成后即可独立使用选题、写作、审校、起标题与封面策划等全套基础能力。

---

### 方式二：配置星河文场 MCP（解锁全部增强能力）

连接星河文场 MCP 后，Agent 可自动读取您的专属文风、调用个人素材库并直接保存排版至工作台。

#### 1. 获取 MCP Token
登录星河文场平台官网（https://mp.soulsrc.com ），在**「系统设置」 -> 「AI Agent / MCP」**中生成专属 MCP Token。

#### 2. 客户端配置示例

##### Cursor / Workbuddy 配置 (`.cursor/mcp.json`)
```json
{
  "mcpServers": {
    "xinghe-wenchang": {
      "icon": "https://mp.soulsrc.com/assets/logo.png",
      "url": "https://mp.soulsrc.com/mcp/sse?token=YOUR_MCP_TOKEN"
    }
  }
}
```

##### Claude Desktop 配置 (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "xinghe-wenchang": {
      "command": "python3",
      "args": ["/项目绝对路径/mcp/server.py", "--token", "YOUR_MCP_TOKEN"]
    }
  }
}
```

---

## 💡 典型使用场景示例

### 场景 1：智能选题与去重
> “`@wechat-creator` 最近不知道写什么，根据我以往写过的文章和素材库，帮我推荐几个接下来值得写的公众号选题。”

### 场景 2：端到端长文创作并入库
> “`@wechat-creator` 帮我写一篇关于‘独立开发者如何验证真实需求’的公众号文章。结合我的写作风格，写完后保存到星河文场工作台。”

### 场景 3：文章责任编辑与审校（去 AI 味）
> “`@wechat-creator` 这是我写好的草稿，语言有些空泛套话，请作为责任编辑帮我审校润色，去除 AI 味并保持行文自然：[附上草稿内容]”

### 场景 4：定向拟定标题与摘要
> “`@wechat-creator` 根据这篇文章的内容与核心观点，运用不同策略拟定 8 个候选标题，并提炼一段微信分享卡片摘要：[附上正文]”

---

## 📁 目录与知识库架构

```text
wechat-creator/
├── SKILL.md                          # 技能主入口（意图路由、阶段调度与能力分层）
├── README.md                         # 规范说明与快速上手手册
├── LICENSE                           # MIT 开源协议
└── references/                       # 细分专业知识库 (Progressive Disclosure)
    ├── topic_selection.md            # 选题发掘、素材匹配与历史文章去重
    ├── research.md                   # 四级信源分级、Fact Card 与反幻觉准则
    ├── structures.md                 # 11 种思考框架与移动端自然行文节奏
    ├── humanizer.md                  # 责任编辑审校准则与八级精简顺序
    ├── titles.md                     # 自适应标题策略、候选生成与摘要规范
    ├── cover.md                      # 2.35:1 官方封面视觉规范与生图 Prompt
    └── typesetting.md                # 微信富文本内联排版技术约束（按需引用）
```

---

## 📄 开源协议

本项目基于 [MIT License](LICENSE) 协议开源。