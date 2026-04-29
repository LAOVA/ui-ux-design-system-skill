# DESIGN.md: 极客苹果风个人主页 (Geek Apple Personal Homepage)

## 视觉主题与氛围 (Visual Theme and Atmosphere)

- **类别 (Category):** 个人主页 / 简历 (Personal Homepage / Portfolio)
- **风格导向 (Style Direction):** 极客苹果风 (Geeky Apple)
- **概述 (Summary):** 结合了苹果公司 (Apple) 的极简主义、玻璃拟态和精致间距，以及极客 (Geek) 文化中的深色模式、等宽字体细节和网格系统。打造一种“精致的复杂感”，既像高端消费电子产品的官网，又充满技术深度。
- **关键特效 (Key Effects):**
  - **玻璃拟态 (Glassmorphism):** 半透明背景配合 `backdrop-blur`，模拟磨砂玻璃质感。
  - **微光细节 (Subtle Glow):** 按钮和交互元素带有极细的边框发光特效。
  - **网格系统 (Grid System):** 采用 Apple 风格的 Bento Grid (便当盒布局)，但增加细微的网格背景纹理。
  - **动态平滑 (Smooth Motion):** 遵循苹果风格的弹性动画，配合极客感的代码打字机特效。

## 颜色面板与语义角色 (Color Palette and Semantic Roles)

| 角色 (Role)            | 十六进制 (Hex)          | CSS 变量 (Variable) | 说明 (Notes)                       |
| ---------------------- | ----------------------- | ------------------- | ---------------------------------- |
| 背景 (Background)      | `#000000`               | `--color-bg`        | 纯黑 (OLED Black)，极客感的核心    |
| 前景/文字 (Foreground) | `#F5F5F7`               | `--color-text`      | 苹果标准亮灰，降低视觉疲劳         |
| 主色 (Primary)         | `#007AFF`               | `--color-primary`   | Apple 经典的交互蓝                 |
| 强调色 (Accent)        | `#00D2FF`               | `--color-accent`    | 极客感的电光青，用于高亮代码或细节 |
| 边框 (Border)          | `#27272A`               | `--color-border`    | 深灰色边框，保持低调               |
| 玻璃面板 (Surface)     | `rgba(28, 28, 30, 0.7)` | `--color-glass`     | 带透明度的深色面板                 |

## 字体规则 (Typography Rules)

- **标题字体 (Heading Font):** `Inter`, `SF Pro Display`, `system-ui`, `sans-serif`
  - _特点:_ 苹果风格的现代感，字间距略微收紧 (`tracking-tight`)。
- **正文字体 (Body Font):** `SF Pro Text`, `Inter`, `sans-serif`
  - _特点:_ 极佳的可读性，保持专业感。
- **技术细节/代码 (Mono Font):** `JetBrains Mono`, `SF Mono`, `monospace`
  - _特点:_ 极客风的灵魂，用于展示技术栈、代码片段或终端交互。
- **氛围感:** 专业、严谨、充满技术气息。

## 组件样式规则 (Component Styling Rules)

- **按钮 (Buttons):** 采用大圆角 (`rounded-full`)，主按钮使用 `Primary Blue`，次要按钮使用毛玻璃质感。
- **卡片 (Cards):** 典型的 Bento Grid 样式，圆角控制在 `24px - 32px`，边框采用极细的 `1px` 实线。
- **终端组件 (Terminal UI):** 模拟 macOS 终端窗口，带有三色功能点，用于展示自我介绍或技术背景。
- **网格背景 (Grid Background):** 在背景层使用极淡的网格线 (`rgba(255, 255, 255, 0.05)`)。

## 布局原则 (Layout Principles)

- **布局名称:** Bento Grid Showcase (便当盒展示)
- **布局顺序:**
  1. **英雄区 (Hero):** 巨大的苹果风标题 + 极客感的技术标签云。
  2. **核心展示 (Bento Grid):** 个人技能、项目经历、贡献图 (GitHub Style) 的卡片组合。
  3. **终端交互 (Terminal):** 一个可交互或自动播放的命令行组件。
  4. **页脚 (Footer):** 极简的联系方式。

## 深度与提升 (Depth and Elevation)

- `shadow-glass`: `0 8px 32px 0 rgba(0, 0, 0, 0.37)`
- `radius-card`: `28px`
- `radius-button`: `9999px`

## 行为守则 (Do and Do-Not Rules)

### 必须做 (Do)

- 保持文字对比度，确保在深色模式下易读。
- 使用平滑的过度动画 (Ease-in-out)。
- 保持页面的留白感，即使是极客风也不要塞得太满。

### 严禁做 (Do Not)

- 严禁使用纯白色背景。
- 严禁使用过于花哨的渐变色。
- 避免使用过于尖锐的圆角（除非是模拟特定极客工具）。

## 响应式行为 (Responsive Behavior)

- **移动端优先:** 在小屏幕上 Bento Grid 应塌缩为单列布局。
- **触摸友好:** 移动端的按钮和交互区域应保持足够的尺寸。

## AI 代理提示指南 (Agent Prompt Guide)

- 这是一个“极客苹果风”的设计系统，核心是“黑底、蓝调、毛玻璃、等宽字”。
- 布局必须使用 Bento Grid，间距要宽大 (Apple-style whitespace)。
- 技术栈展示必须使用等宽字体。
- 动画要丝滑，不要有突兀的弹出。
