# AI SaaS Dashboard 设计规范 (Linear + Vercel 风格)

本规范旨在为 AI SaaS 仪表盘提供一套专业、简洁、技术感强的视觉与交互指南。风格融合了 Linear 的沉浸式暗色调与 Vercel 的极简技术主义。

## 1. 视觉主题与氛围 (Visual Theme & Atmosphere)

- **核心基调**: 沉浸式暗色 (Cinematic Dark)、技术性极简 (Technical Minimalism)、高精度 (High Precision)。
- **视觉特征**: 深邃的背景、极细的边框 (Hairline Borders)、毛玻璃效果 (Glassmorphism)、微妙的渐变发光。
- **参考对象**: Linear (交互细节与色彩氛围), Vercel (排版与边框逻辑)。

## 2. 色彩系统 (Color Palette & Semantic Roles)

采用语义化色彩命名，确保暗色模式下的极致对比与舒适度。

| 角色            | 十六进制 (Hex) | 变量名                | 用途描述                                |
| :-------------- | :------------- | :-------------------- | :-------------------------------------- |
| **Primary**     | `#FFFFFF`      | `--color-primary`     | 主要文字、关键操作图标                  |
| **Secondary**   | `#8A8F98`      | `--color-secondary`   | 次要文字、说明文本                      |
| **Accent**      | `#5E6AD2`      | `--color-accent`      | Linear 经典靛蓝，用于主要按钮、激活状态 |
| **Background**  | `#000000`      | `--color-background`  | 核心背景色 (纯黑以适配 OLED)            |
| **Surface**     | `#0A0A0A`      | `--color-surface`     | 卡片、侧边栏等提升层级的背景            |
| **Muted**       | `#161616`      | `--color-muted`       | 输入框背景、禁用状态                    |
| **Border**      | `#1F1F1F`      | `--color-border`      | 极细边框，用于区分组件与区域            |
| **Success**     | `#10B981`      | `--color-success`     | 状态指示 (AI 生成成功、正常运行)        |
| **Destructive** | `#FF453A`      | `--color-destructive` | 错误、危险操作、系统警告                |

## 3. 字体系统 (Typography Rules)

选用具备极强技术感的字体族，优化阅读体验。

- **UI 字体**: `Geist Sans`, `Inter`, `-apple-system`. 重点在于几何感与清晰度。
- **代码/数据字体**: `Geist Mono`, `Fira Code`. 用于展示 AI 提示词、API 密钥、数值监控。
- **字号分级**:
  - `Display`: 32px / 1.2 (用于数据大屏标题)
  - `Title`: 20px / 1.4 (用于模块标题)
  - `Body`: 14px / 1.6 (标准正文)
  - `Small`: 12px / 1.5 (标签、辅助文字)

## 4. 组件样式规则 (Component Styling Rules)

- **卡片 (Cards)**:
  - 边框: `1px solid var(--color-border)`
  - 圆角: `12px`
  - 背景: `rgba(10, 10, 10, 0.7)`
  - 特效: `backdrop-filter: blur(12px)`
- **按钮 (Buttons)**:
  - 基础: `radius: 8px`, `padding: 8px 16px`, `transition: 200ms ease`.
  - Primary: `bg: var(--color-accent)`, `color: #FFFFFF`, `box-shadow: 0 0 20px rgba(94, 106, 210, 0.3)`.
  - Ghost: `color: var(--color-secondary)`, `hover-bg: var(--color-muted)`, `hover-color: var(--color-primary)`.
- **输入框 (Inputs)**:
  - 样式: `bg: var(--color-muted)`, `border: 1px solid var(--color-border)`.
  - 聚焦: `border-color: var(--color-accent)`, `ring: 0 0 0 2px rgba(94, 106, 210, 0.2)`.

## 5. 布局原则 (Layout Principles)

- **栅格系统**: 采用 12 列响应式栅格，仪表盘区域推荐使用 `gap: 24px`。
- **侧边栏 (Sidebar)**: 固定宽度 `240px`，使用 `border-right` 分隔，背景采用深色毛玻璃。
- **密度控制**: 保持高密度 (High Density) 但通过足够的 `padding (24px+)` 确保呼吸感。

## 6. 深度与层级 (Depth & Elevation)

- **层级 0**: `background` (#000000) - 底层容器。
- **层级 1**: `surface` (#0A0A0A) - 卡片、面板。
- **层级 2**: `popover` (#161616) - 菜单、模态框、提示浮层。
- **阴影**: 仅在 `popover` 层级使用极其微弱的弥散阴影 `0 10px 40px rgba(0,0,0,0.5)`。

## 7. 交互与动效 (Interaction & Motion)

- **进入动画**: 页面加载时，卡片采用 `y: 20 -> 0`, `opacity: 0 -> 1` 的平滑升起。
- **悬停反馈**: 边框颜色从 `border` 渐变为 `accent` 或 `primary`，持续时间 `200ms`。
- **状态切换**: AI 处理状态建议使用线性扫描光效 (Scanline effect) 或微弱的呼吸灯。

## 8. 响应式行为 (Responsive Behavior)

- **Mobile (< 768px)**: 侧边栏折叠为底部导航或汉堡菜单，卡片宽度 100%。
- **Tablet (768px - 1024px)**: 侧边栏收缩为图标模式。
- **Desktop (> 1024px)**: 全功能展示，支持多栏布局。

## 9. AI 提示词与 Agent 指引 (Agent Prompt Guide)

在生成代码时，请遵循以下原则：

- "使用 Tailwind CSS 开发，背景设为黑色，卡片使用 1px 的灰色边框和暗色透明背景。"
- "字体优先使用 Geist Sans，代码片段使用 Geist Mono。"
- "主色调使用靛蓝色 (#5E6AD2)，所有交互需添加平滑的 transition。"
- "布局保持紧凑，模块间距使用 gap-6 (24px)。"
