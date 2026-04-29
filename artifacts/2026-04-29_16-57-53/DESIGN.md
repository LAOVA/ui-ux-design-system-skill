# BMW-M CMS Design System

## 1. 视觉主题与氛围 (Visual Theme & Atmosphere)

本项目采用 **BMW-M 赛车运动风格**，旨在为内容管理系统 (CMS) 提供一种高性能、精确且极具品质感的界面体验。

- **核心基调**: 德系精密工程感、豪华运动氛围、高对比度、极致效率。
- **氛围描述**: 深色高质感表面配合锐利的色彩点缀，模拟驾驶舱的专业感与掌控感。

## 2. 色彩系统 (Color Palette & Semantic Roles)

基于 BMW M 系列经典的三色标识与品牌色彩进行语义化定义。

| 角色                       | 十六进制值 | 说明                                         |
| :------------------------- | :--------- | :------------------------------------------- |
| **Primary (M-Blue)**       | `#1c69d4`  | 主品牌色，用于主要动作、导航高亮。           |
| **Secondary (Light-Blue)** | `#0066b1`  | 辅助品牌色，用于次要交互、进度指示。         |
| **Accent (M-Red)**         | `#e22718`  | 强调色，用于关键警告、核心转化、高性能状态。 |
| **Background**             | `#1a2129`  | 页面基准底色，深海军蓝，营造高级感。         |
| **Surface (Muted)**        | `#262e38`  | 容器表面色，用于卡片、侧边栏，提升层次感。   |
| **Foreground (Text)**      | `#ffffff`  | 主要文字颜色，确保在高对比度下的易读性。     |
| **Border**                 | `#3c3c3c`  | 边框与分割线，保持微妙的界限感。             |
| **Destructive**            | `#dc2626`  | 危险/删除动作。                              |

## 3. 字体规范 (Typography Rules)

- **标题字体**: `BMW Type Next Latin` (或 `Public Sans`, `Inter` 作为备选)。加粗 (700+) 以体现力量感。
- **正文字体**: `BMW Type Next Latin` (或 `Public Sans`, `System-UI`)。使用较细的字重 (300-400) 配合较大的行高 (1.6) 以提升阅读舒适度。
- **字阶**:
  - 大标题 (Display): 48px+, 紧凑字间距 (-0.05em)。
  - 页面标题: 32px。
  - 模块标题: 20px。
  - 正文: 16px。

## 4. 组件样式规则 (Component Styling Rules)

- **按钮 (Buttons)**:
  - 采用 12px-16px 的大圆角或完全直角（体现硬朗感）。
  - Primary 按钮使用深蓝渐变或纯色。
  - 悬停态增加微弱的 M-Red 底部边框或发光效果。
- **卡片 (Cards)**:
  - 深色背景 (`#262e38`)，极细边框。
  - 采用 Bento Grid (便当盒) 布局，保持高信息密度。
- **输入框 (Inputs)**:
  - 底部线条聚焦效果，聚焦时使用 Primary Blue。

## 5. 布局原则 (Layout Principles)

- **Bento Grid**: 核心功能区采用模块化方块布局，模仿仪表盘的模块感。
- **高密度**: 减少不必要的留白，通过对比度和分割线来区分区域，满足专业 CMS 的效率需求。
- **F-Pattern**: 导航置左，核心操作置于右上角，符合德系交互的逻辑性。

## 6. 深度与投影 (Depth & Elevation)

- 避免使用大面积的模糊投影，倾向于使用**内发光 (Inner Glow)** 或 **极细边框** 来体现层次。
- 层级越高，表面颜色越浅（从 `#1a2129` 到 `#262e38`）。

## 7. 执行与禁止 (Do and Do-Not)

- **Do**: 保持对齐的严谨性，使用 M-Red 进行点睛之笔。
- **Do-Not**: 禁止使用圆润、可爱或过于柔和的色彩梯度。禁止在非关键区域使用 M-Red 以免分散注意力。

## 8. 响应式行为 (Responsive Behavior)

- 移动端采用单列堆叠，但保留卡片的硬朗边缘。
- 侧边栏在平板端折叠为图标模式，保持操作空间的利用率。

## 9. AI 提示词指南 (Agent Prompt Guide)

> "Generate a dashboard interface for a high-performance CMS using BMW-M design language. Background: #1a2129. Accents: #1c69d4 and #e22718. Use sharp corners, Bento grid layout, and heavy sans-serif typography. Focus on information density and precision engineering aesthetic."
