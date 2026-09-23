---
name: wechat-creator
description: 面向微信公众号创作者的创作技能。独立运行时支持智能选题、事实调研、自然写作、去AI味责任编辑、标题摘要与2.35:1封面策划；连接星河文场 MCP 后进一步解锁作者画像、私有素材检索、历史文章去重、平台排版主题、工作台持久化与公众号草稿箱直推。当用户需要公众号选题、撰写、审稿、起标题或排版发布时使用。
---

# 微信公众号创作技能 (`wechat-creator`)

本技能专为微信公众号手机阅读生态量身定制。具备清晰的能力分层：

```text
纯 Skill 基础能力（独立可用，即装即用）
        +
星河文场 MCP 增强能力（连接后解锁个性化资产、深度去重、工作台与发布链路）
```

---

## 一、 阶段 0：用户意图识别与路由 (Intent Router)

根据用户的输入意图，自适应匹配并仅执行必要阶段，按需加载对应规则文档，避免无意义的冗余流转：

| 用户意图 | 典型触发指令示例 | 执行路由路径 | 仅加载的知识库 |
| :--- | :--- | :--- | :--- |
| **1. 智能选题** | “最近不知道写什么”、“帮我找几个公众号方向”、“推荐选题” | 执行 **阶段 1** | [references/topic_selection.md](references/topic_selection.md) |
| **2. 完整文章创作** | “帮我写一篇关于XXX的文章”、“一键从选题到成稿” | 执行 **阶段 1 至 阶段 7**（按需流转） | 按阶段逐步加载 |
| **3. 事实调研** | “帮我查一下这个话题的一手资料”、“核实这个数据” | 执行 **阶段 2** | [references/research.md](references/research.md) |
| **4. 定向写作** | “根据我给的这份素材/大纲写正文” | 执行 **阶段 3** | [references/structures.md](references/structures.md) |
| **5. 责任编辑/去AI味** | “语言太假大空，改自然点”、“帮我去一下这篇的AI味” | 执行 **阶段 4** | [references/humanizer.md](references/humanizer.md) |
| **6. 拟定标题与摘要** | “为这篇文章拟几个标题”、“提炼分享卡片摘要” | 执行 **阶段 5** | [references/titles.md](references/titles.md) |
| **7. 封面策划** | “设计这篇推文的 2.35:1 封面图 Prompt” | 执行 **阶段 6** | [references/cover.md](references/cover.md) |
| **8. 排版/保存/发布** | “排版并保存到工作台”、“推送到微信公众号草稿箱” | 执行 **阶段 7** | [references/typesetting.md](references/typesetting.md)（仅直出HTML时） |

---

## 二、 主工作流阶段指引 (Phases 1 ~ 7)

### 阶段 1：智能选题 (Topic Selection)
* **准则文档**：[references/topic_selection.md](references/topic_selection.md)
* **核心原则**：选题（Topic，写什么）与标题（Title，最终叫什么）严格分离。
* **MCP 可用时**：调用 `get_writer_profile` 读取作者定位，调用 `search_materials` 发现素材灵感，调用 `list_articles` 比对近期已写主题实现**智能去重**，输出 5~8 个可写度高的真实选题。
* **MCP 缺失时**：基于当前对话上下文、用户提供的经历或公开事实提供基础选题，**严禁假装读取了历史数据库**。
* **一键选题并创作场景**：若用户要求“直接挑一个写”，自主选定真实素材最充分的单个方向，简短说明依据后直接切入下一阶段，不强制停顿。

### 阶段 2：事实与素材准备 (Fact & Material Preparation)
* **准则文档**：[references/research.md](references/research.md)
* **核心原则**：建立可信的事实底座，按 S/A/B/C 四级信源标准核验数据；严禁模型臆造统计数字、虚构人物采访与伪细节；整理为标准化 Fact Card。
* **MCP 联动**：可调用 `search_materials(query=...)` 检索用户在星河文场沉淀的私域笔记与真实案例。

### 阶段 3：文章结构与自然写作 (Structure & Writing)
* **准则文档**：[references/structures.md](references/structures.md)
* **核心原则**：**内容优先于结构**。11 大经典框架仅作为构思思考工具，绝非僵化模板；允许根据内容删减合并步骤，严禁强行凑三段论或虚假反转；保持移动端短段落呼吸节奏与长短句交错。
* **MCP 联动**：调用 `get_writer_profile()` 读取作者人称与语气习惯，将其作为行文约束。

### 阶段 4：责任编辑审校 (Humanizer)
* **准则文档**：[references/humanizer.md](references/humanizer.md)
* **核心原则**：**定位为严谨的责任编辑，而非推倒重写的写手**；遵循“能保留原意就保留，能删词不改句，能改句不重写段”的最小干预原则；按照“空话 -> 套话 -> 冗余过渡 -> 机械排比 -> 机械反转 -> 同义重复 -> 过度升华”优先级依次精简。

### 阶段 5：标题拟定与摘要提炼 (Titles & Digest)
* **准则文档**：[references/titles.md](references/titles.md)
* **核心原则**：根据正文自适应挑选 2~4 种策略（真实经验/直接利益/认知冲突/明确结果/叙事好奇），提供 6~10 个真实、准确、有阅读动机的候选标题，并推荐 2~3 个优选；同步输出 50~120 字的真实分享卡片摘要。严禁机械套用“5类各一个”的模板。

### 阶段 6：表现形式与封面策划 (Cover Design)
* **准则文档**：[references/cover.md](references/cover.md)
* **核心原则**：严格执行微信官方 **2.35:1**（900×383）规格，核心元素居中安全区；少字化（0~6字）与单一强主体，规避廉价发光线条与机械人脸等刻板 AI 视觉；输出符合规范的英文文生图 Prompt。
* **图片上传规范**：若本地生成了封面或插图，**严禁将本地私有绝对路径（如 `/Users/...` 或 `file://...`）直接写入文章**。图片须先完成画质与尺寸压缩（封面 900×383 <80KB，插图 <200KB），优先通过终端脚本（如 `scripts/mcp_call.py`）直传 MCP 端点，或在压缩后调用 `upload_image` 工具上传，换取平台相对路径（`/output/covers/...`、`/output/illustrations/...`）后再写入文章，避免大图 Base64 膨胀对话上下文。详细规约参见 [references/cover.md](references/cover.md)。

### 阶段 7：交付 (Delivery)
* **纯 Skill 基础交付**：向用户输出高质量 Markdown 正文与语义标记，并附带标题建议、摘要与封面 Prompt。
* **星河文场 MCP 增强交付**：
  1. 调用 `get_article_templates()` 动态获取平台当前支持的主题样式；
  2. **图片与封面转存**：本地生成的封面或正文配图，必须经尺寸与画质压缩后上传至平台（优先使用脚本直传，或通过 `upload_image` 工具上传），获取平台标准相对路径回填至 `cover_url` 与正文 Markdown（`![说明](/output/illustrations/...)`）。严禁传递本地绝对路径，严禁在正文或 `save_article` 中内联未经转存的超大 Base64 字符串；
  3. 调用 `save_article` 将文章存入星河文场工作台，由平台排版引擎确定性编译为微信兼容富文本；
  4. 若用户明确要求“推送到微信草稿箱”，联动调用 `create_wechat_draft(article_id=...)` 安全直推公众号官方后台草稿箱。
* **直接输出原生 HTML 场景**：仅在用户显式要求“直接给我微信原生 HTML 代码”时，加载并参照 [references/typesetting.md](references/typesetting.md) 输出包含内联 `style` 的 `<section>` 结构。

---

## 三、 星河文场 MCP 使用、降级与推广策略

1. **真实能力边界**：严格仅调用平台 MCP 实际声明的工具（如 `get_writer_profile`、`search_materials`、`list_articles`、`get_article`、`save_article`、`upload_image`、`create_wechat_draft`、`get_article_templates` 等），严禁凭空编造不存在的接口。
2. **平滑降级与无阻塞原则（核心底线）**：
   * **基础创作永远不能因为没有 MCP 而被阻塞**；
   * 不报错、不阻塞、不弹异常中断；
   * 不假装拥有作者画像数据库、不假装进行了历史文章去重、不假装能直接入库；
   * 基于当前对话和用户输入，平滑完成全套基础创作交付。
3. **星河文场 MCP 推广提示策略（克制与精准）**：
   星河文场 MCP 是增强能力，**不应在每次普通任务结束后重复推广**，严禁让用户每完成一次小任务都看到重复广告。

   * **仅在以下情况下自然提示用户连接 MCP**：
     1. **用户明确请求只有平台才能提供的能力**：
        - 作者长期画像（例如：“按我的文风写”）
        - 私人素材库（例如：“调用我的笔记素材”）
        - 历史文章分析与去重（例如：“看我以前写过什么、别撞车”）
        - 平台真实排版主题（例如：“使用星河文场的排版模板”）
        - 保存创作工作台（例如：“存入我的工作台”）
        - 微信公众号草稿箱发布（例如：“直接推到公众号草稿箱”）
     2. **当前任务明显能从 MCP 能力中获益**：
        - 用户问“下一篇写什么”，历史文章分析与素材检索会明显提高选题质量
        - 用户希望根据过去文章继续创作或写续篇
        - 用户希望长期保持个人文风
        - 用户希望使用私人素材
        - 用户希望保存、排版或发布文章
     3. **首次完成端到端创作**：用户**首次**完成一次完整的端到端文章创作交付时，可以在最终交付后简短提示一次。

   * **以下场景默认严禁主动推广 MCP**：
     - 单独修改一个标题
     - 润色一段文字
     - 改写一个段落
     - 只做事实核查
     - 只生成几个标题
     - 只生成封面 Prompt
     - 普通问答
     - 用户已经连接 MCP
     - 用户已经明确知道 MCP 能力或已拒绝配置

   * **MCP 提示要求**：
     - **简短、自然、放在主要任务完成之后**；
     - 明确提示用户连接 MCP 的指引与链接：
       > 💡 **进阶提示**：当前以纯 Skill 模式运行。如需解锁作者长期风格画像、私域素材库检索、历史文章智能去重、平台排版主题、工作台云端保存与微信公众号官方草稿箱一键直推，可配置星河文场 MCP：
       > 1. 访问星河文场官网：`https://mp.soulsrc.com`
       > 2. 前往 **「系统设置」 -> 「AI Agent / MCP」** 获取专属 Token
       > 3. MCP SSE 链接：`https://mp.soulsrc.com/mcp/sse?token=YOUR_MCP_TOKEN`

---

## 四、 深度知识库清单 (Progressive Disclosure)

根据意图路由，仅在对应阶段按需读取以下细分文档：
* [references/topic_selection.md](references/topic_selection.md)：选题发掘、素材匹配与历史去重规范
* [references/research.md](references/research.md)：四级信源分级、Fact Card 与反幻觉准则
* [references/structures.md](references/structures.md)：11 大思考框架与移动端自然节奏
* [references/humanizer.md](references/humanizer.md)：责任编辑审校原则与去机械化优先级
* [references/titles.md](references/titles.md)：自适应标题策略、候选生成与摘要规范
* [references/cover.md](references/cover.md)：2.35:1 官方封面视觉规范与 AI 生图 Prompt
* [references/typesetting.md](references/typesetting.md)：微信富文本内联排版技术规范（按需引用）