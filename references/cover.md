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
