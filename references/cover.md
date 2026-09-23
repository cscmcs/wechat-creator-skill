# 微信公众号封面策划与视觉规约 (Cover Design Rules)

> 本规范指导微信公众号官方 2.35:1 头条封面视觉规划与 AI 生图 Prompt 编写，供 `wechat-creator` 技能按需引用。

---

## 一、 官方尺寸与安全视口

微信公众号在会话列表与订阅号常态流中，头条主图遵循官方标准：
* **官方推荐比例**：**2.35:1**（标准分辨率：**900 × 383** 像素）；
* **次条/小图裁剪区**：正中间通常会被特定信息流截取为正方形（1:1），因此**核心视觉主体必须居中**；
* **四周安全区域**：关键画面元素与文字距离四周边距保留至少 40px 的安全缓冲，避免因手机屏幕圆角或客户端 UI 边缘导致视觉裁切。

---

## 二、 封面视觉设计核心原则

在手机屏幕上，封面图的实际展示尺寸往往只有几厘米宽，因此必须坚持**强主体、少元素、弱干扰**：

1. **拒绝堆砌小字**：
   * 严禁将文章大纲、副标题、长篇引语塞入封面；
   * 封面标题文字**非强制项**：可以没有文字，仅靠极具质感的纯视觉主体传递氛围；若有文字，严格控制在 **2~6 个字** 的短词或胶囊标签，字号大、字重大、对比度清晰。
2. **单一核心视觉锚点**：
   * 画面必须且仅有**一个清晰的视觉主体**（如：一份工整的实操笔记、一个微光聚焦的键盘、极简的抽象几何体、深夜伏案的真实剪影等）；
   * 严禁堆砌多个分散杂乱的视觉元素，避免注意力涣散。
3. **摆脱廉价 AI 视觉刻板印象**：
   * 坚决规避：无意义的荧光透明发光线条、悬浮全息 HUD 界面、千篇一律的发光机械人脸、满屏蓝色渐变粒子；
   * 优先追求：出版物级编辑质感、摄影级自然光影、真实纸张或材质纹理、舒适克制的低饱和配色。

---

## 三、 AI 生图 Prompt 编译策略

为文生图模型（如 Midjourney、DALL-E、Imagen 等）生成英文生图 Prompt 时，须保持以下标准：

### 1. 构图与画幅修饰词
* **画幅锁定**：在 Prompt 描述中显式声明 `ultra-wide 2.35:1 editorial cover composition, horizontal banner format`；若生图工具支持参数，直接传入 `--ar 2.35:1` 或 `--ar 21:9`（**严禁使用 16:9 以免导致公众号上下裁切变形**）；
* **质感强化**：`clean composition, authentic textures, natural studio lighting, restrained color palette, ample negative space, modern editorial publication style`。

### 2. 负向过滤词 (Negative Prompts)
* `blurry, crowded elements, cluttered background, tiny unreadable text, generic cyberpunk, glowing neon particles, tacky 3d robot, watermark, low resolution`。

---

## 四、 封面与插图上传与转存规范 (Image Upload & Optimization)

为保证阅读加载体验并避免对话上下文膨胀，封面与正文插图的持久化与引用须遵循以下规约：

### 1. 尺寸规格与压缩标准
* **封面图 (Cover)**：
  - 遵循微信官方推荐 **2.35:1** 比例（标准分辨率 **900 × 383** 像素）；
  - 导出或转换为 JPEG（质量 80~85）或 WebP 格式；
  - 单图体积严格控制在 **40KB ~ 80KB**（不超过 100KB）。
* **正文插图 (Illustration)**：
  - 适应移动端屏幕阅读，宽度建议控制在 **1200 ~ 1600 像素**；
  - 压缩为 JPEG（质量 80~85）或 WebP 格式；
  - 单图体积控制在 **100KB ~ 200KB**。
* **严禁直接上传** 未经缩放与压缩的数兆高清 PNG、RAW 或全屏高分截屏。

### 2. 远程 MCP 连接与上下文保护规约
* **严禁传递本机磁盘私有路径**：在远程连接（SSE/HTTP）模式下，远程服务端无法访问客户端本地磁盘，`image_path`（如 `/Users/...`、`C:\...` 或 `file://...`）不可用。
* **严禁向对话上下文塞入超大 Base64**：未经压缩的大图 Base64 会造成成千上万 Token 消耗，导致上下文膨胀、调用延迟急剧增加甚至超出模型输入上限。
* **严禁在 Markdown 正文或 `save_article` 中直接嵌入超长 Base64 Data URL**：入库前必须先完成转存，正文中仅保留平台相对路径。

### 3. 双通道上传执行方案
* **通道一：终端脚本直传（推荐方案，完全规避对话上下文膨胀）**：
  当 Agent 具备命令行执行能力时，直接调用上传脚本（如 `scripts/mcp_call.py`）直连 MCP 服务端端点。图片二进制流直接从本地发送到服务器，**完全不经过 LLM 对话上下文**，不占用任何对话 Token。
  ```bash
  # 上传封面图（自动缩放至 900x383 并压缩）
  python3 scripts/mcp_call.py upload-image --file path/to/cover.jpg --type cover

  # 上传正文插图（限制宽度并压缩）
  python3 scripts/mcp_call.py upload-image --file path/to/illustration.png --type illustration
  ```
* **通道二：MCP 工具紧凑 Base64 上传（无终端权限时的备用通道）**：
  若 Agent 处于纯对话环境、无法执行本地命令行脚本，必须确保本地工具已完成尺寸缩放与画质压缩（体积控制在 100KB 以内），再调用 MCP 工具：
  ```text
  upload_image(
    image_data="data:image/jpeg;base64,...",
    image_type="cover",  # 封面选 cover，插图选 illustration
    filename="cover.jpg"
  )
  ```

### 4. 平台相对路径回填
* **封面图**：获取平台返回的 `/output/covers/...` 路径，回填至 `save_article(cover_url=...)`；
* **正文插图**：获取平台返回的 `/output/illustrations/...` 路径，替换 Markdown 正文中的占位链接：
  ```markdown
  ![配图说明](/output/illustrations/illustrations_1727000000_a1b2c3d4.jpg)
  ```

