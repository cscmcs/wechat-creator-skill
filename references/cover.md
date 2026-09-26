# 微信公众号封面策划与视觉规约 (Cover Design Rules)

> 本规范指导微信公众号官方 2.35:1 头条封面视觉规划与 AI 生图 Prompt 编写，供 `wechat-creator` 技能按需引用。

---

## 一、 官方尺寸与双重视口安全区

微信公众号在会话列表、常态信息流与转发卡片中具有双重视口特征：
* **官方推荐比例**：**2.35:1**（标准分辨率：**900 × 383** 像素）；
* **中心 1:1 黄金安全区**：横向正中间 **383 × 383** 区域（横坐标区间 `[258px, 642px]`）。主标题与核心视觉锚点必须完整保留在安全区内，保证在订阅号常态流、消息分享卡片或次条裁切为正方形时不被破坏；
* **四周安全边距**：文字与关键视觉元素距离画面四周至少保留 40px 的缓冲边距。

---

## 二、 封面视觉设计核心原则与四大排版模板

封面设计坚持**强主体、少元素、图文分层、弱干扰**原则：

### 1. 四套出版级排版模板

| 模板代码 | 模板名称 | 适用题材 | 视觉规范 |
| :--- | :--- | :--- | :--- |
| `editorial` | **现代杂志风** (默认推荐) | 商业分析、深度报道、行业洞察 | 极简留白、分类胶囊标、加粗大标题、精美引线、副标题与底部出品微标 |
| `bold_quote` | **观点金句风** | 认知突围、职场思辨、金句观点 | 半透明双引号破格水印、居中大字号冲击力标题、暖金/深黑高对比度 |
| `tech_minimal` | **极客深色风** | AI应用、架构实践、开发实操 | 深空黑曜蓝底色、微光网格、高对比度标签、清晰层级 |
| `photo_editorial` | **光影纪实风** | 故事纪实、生活方式、人物专访 | **AI 摄影/插画底图** + 自适应暗光渐变蒙层 + 出版级白字悬浮排版 |

### 2. 图文分层原则
* **背景与主体**：由纯色渐变光晕或 AI 生成的高质感无字底图承载，负责营造氛围；
* **文本排版层**：由排版引擎精准绘制，支持大标题（40~46px 粗体）、分类胶囊（17~18px 粗体）、副标题（20~22px）与底部出品署名；
* **文字严禁交由 AI 绘制**：严禁文生图模型直接绘制中文，杜绝乱码与伪英文字符。

---

## 三、 AI 生图 Prompt 编译策略 (无字底图)

为文生图模型（如 FLUX、DALL-E、Imagen 等）生成英文底图 Prompt 时，须遵循以下规约：

### 1. 强制无字与构图约束
* **画幅锁定**：显式声明 `ultra-wide 2.35:1 horizontal banner format, panoramic composition`；支持参数的工具传入 `--ar 2.35:1` 或 `--ar 21:9`；
* **强制无字标记**：必须包含 `no text, no letters, no words, clean background`，防止模型臆造乱码；
* **质感强化**：`clean composition, authentic textures, natural studio lighting, restrained color palette, ample negative space, modern editorial publication style`。

### 2. 负向过滤词 (Negative Prompts)
`text, typography, letters, signature, watermark, blurry, crowded elements, cluttered background, generic cyberpunk, glowing neon particles, tacky 3d robot, low resolution`。

---

## 四、 本地与平台生图调用指引

### 1. 终端调用封面生成引擎
在具备命令行权限时，可直接通过 `core.cover_generator` 快速生成标准 900×383 封面：
```python
from core.cover_generator import CoverGenerator

gen = CoverGenerator()

# 1. 现代杂志风
path1 = gen.generate_cover(
    title="为什么顶级创作者都在构建专属 AI 工作流？",
    subtitle="从被动调用到构建专属 Agent 创作引擎的实操反思",
    tag="深度观察",
    theme="tech_blue",
    template="editorial",
    author="星河文场"
)

# 2. 观点金句风
path2 = gen.generate_cover(
    title="撕掉伪勤奋，用最小可行性逻辑击穿认知障碍",
    subtitle="认知突围与个人落地指南",
    tag="认知反思",
    template="bold_quote",
    theme="business_dark"
)

# 3. AI 底图图文复合
path3 = gen.generate_ai_cover(
    prompt="A minimal desk with warm lamp light, a clean notebook and fountain pen, cinematic quiet atmosphere",
    title="知识创作者的写作暗室",
    subtitle="在信息过载时代保持深度输出的实操体系",
    tag="特别企划",
    author="星河文场"
)
```

---

## 五、 封面与插图上传与转存规范 (Image Upload & Optimization)

### 1. 尺寸规格与压缩标准
* **封面图 (Cover)**：
  - 微信官方推荐 **2.35:1**（标准分辨率 **900 × 383** 像素）；
  - 格式为 PNG、JPEG（质量 85）或 WebP；
  - 单图体积控制在 **40KB ~ 100KB**。
* **正文插图 (Illustration)**：
  - 适应移动端屏幕阅读，宽度控制在 **1024 ~ 1600 像素**（推荐 16:9）；
  - 单图体积控制在 **100KB ~ 200KB**。

### 2. 上传与平台相对路径回填
* **终端脚本直传**：
  ```bash
  python3 scripts/mcp_call.py upload-image --file path/to/cover.png --type cover
  ```
* **平台相对路径回填**：
  获取平台返回的 `/output/covers/...` 路径，回填至 `save_article(cover_url=...)`，正文中严禁保留本地绝对路径或超长 Base64。
