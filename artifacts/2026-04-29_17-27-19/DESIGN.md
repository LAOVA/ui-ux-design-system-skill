# BMW-M Forum Design System

## 视觉特征 (Visual Identity)
BMW-M 论坛的设计系统旨在体现“终极驾驶机器”的精神：精准、高性能、豪华且具有攻击性。

### 核心理念 (Core Concepts)
- **精准工程 (Precision Engineering)**: 每一个像素都有其目的，对齐严格，间距均匀。
- **碳纤维美学 (Carbon Fiber Aesthetic)**: 使用深色纹理和哑光表面，模拟高性能材料。
- **M 动力色彩 (M-Power Colors)**: 标志性的三色（浅蓝、深蓝、红）作为点缀。

---

## 颜色系统 (Color System)

| 角色 | 变量名 | Hex | 描述 |
| :--- | :--- | :--- | :--- |
| **Primary** | `--color-bmw-blue` | `#1c69d4` | BMW 官方蓝色，用于主要 CTA |
| **Secondary** | `--color-m-blue-light` | `#0066b1` | M 系列浅蓝色 |
| **Accent** | `--color-m-red` | `#e22718` | M 系列红色，用于强调和破坏性动作 |
| **Background** | `--color-bg-dark` | `#1a2129` | 主背景色，深灰色调 |
| **Surface** | `--color-surface` | `#262e38` | 卡片和面板背景 |
| **Foreground** | `--color-text-white` | `#ffffff` | 主要文字颜色 |
| **Muted** | `--color-text-muted` | `#bbbbbb` | 次要文字颜色 |

---

## 字体系统 (Typography)

- **Heading**: `BMW Type Next Latin` (或备选 `Inter`, `Montserrat`)
  - **Weight**: 700 (Bold)
  - **Character Spacing**: -0.02em (紧凑且有力)
- **Body**: `BMW Type Next Latin` (或备选 `Inter`, `system-ui`)
  - **Weight**: 300 (Light) / 400 (Regular)
  - **Line Height**: 1.6 (确保长文阅读体验)

---

## 组件规范 (Component Specs)

### 按钮 (Buttons)
- **Primary**: 背景 `#1c69d4`，无圆角或极小圆角 (2px)，全大写文字。
- **Secondary**: 描边 `#ffffff`，背景透明。
- **Ghost**: 仅文字，悬停时出现 `#262e38` 背景。

### 卡片 (Cards)
- **背景**: `#262e38`
- **边框**: 1px solid `#e6e6e6` (低透明度)
- **圆角**: 0px (体现工业精准感) 或 4px (微圆角)。
- **装饰**: 顶部或左侧 2px 的 M-三色线条。

---

## 布局策略 (Layout Strategy)

1. **Hero 区域**: 大图背景（高性能车型），粗体大标题。
2. **板块列表**: 紧凑的网格或列表，强调数据（帖子数、最后回复）。
3. **活动成员**: 极简头像，带在线状态指示器（M-Red 或 M-Blue）。

---

## 避免的事项 (Anti-patterns)
- ❌ 过度的圆角（如 Pill-shaped buttons）。
- ❌ 鲜艳的非品牌色（如亮绿色、紫色）。
- ❌ 复杂的阴影（优先使用边框和对比度）。
- ❌ 过于随意的排版。
