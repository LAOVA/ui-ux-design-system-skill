# DESIGN.md: NVIDIA Forum

## 视觉主题与氛围 (Visual Theme and Atmosphere)

- **类别:** 技术社区与论坛 (Technical Community & Forum)
- **风格方向:** NVIDIA 工业级科技感 (NVIDIA Industrial Tech)
- **总结:** 采用 NVIDIA 标志性的深色调与电光绿配色，强调精密工程感、高性能和技术权威性。界面整洁、锐利，带有微妙的金属质感和发光效果。
- **关键视觉特征:**
  - **NVIDIA Green:** 使用 `#76b900` 作为核心品牌触点，模拟 GPU 渲染的光效。
  - **深色背景:** 背景采用接近黑色的深灰色 (`#000000` 到 `#1a1a1a`)，营造沉浸式的高性能氛围。
  - **精密感:** 极小的圆角 (2px-4px)，细线条边框，以及清晰的层级关系，模拟专业硬件控制面板的质感。
- **参考风格:** NVIDIA GeForce Experience, NVIDIA Control Panel, High-End Gaming Hardware

## 颜色调色板与语义角色 (Color Palette and Semantic Roles)

| 角色 (Role)             | 十六进制 (Hex) | CSS 变量 (Variable)        | 用途 (Usage)             |
| ----------------------- | -------------- | -------------------------- | ------------------------ |
| 背景 (Background)       | `#000000`      | `--color-background`       | 主背景                   |
| 表面 (Surface)          | `#1a1a1a`      | `--color-surface`          | 卡片、容器、侧边栏       |
| 主色 (Primary/Accent)   | `#76b900`      | `--color-primary`          | 品牌色、高亮、按钮、图标 |
| 前景 (Foreground)       | `#ffffff`      | `--color-foreground`       | 主要文本                 |
| 次要前景 (Secondary FG) | `#999999`      | `--color-foreground-muted` | 描述文本、元数据         |
| 边框 (Border)           | `#333333`      | `--color-border`           | 分割线、容器边框         |

## 字体规则 (Typography Rules)

- **标题字体:** NVIDIA Sans (或 Inter / Segoe UI / Roboto)
- **正文字体:** Inter / Public Sans
- **氛围:** 现代、专业、工程导向、清晰易读
- **Google Fonts:** https://fonts.google.com/share?selection.family=Inter:wght@300;400;500;600;700

## 组件样式规则 (Component Styling Rules)

- **按钮 (Buttons):**
  - 采用实色填充 (#76b900) 或 细边框样式。
  - 悬停时带有微弱的发光效果 (box-shadow)。
- **卡片 (Cards):**
  - 深灰色背景 (#1a1a1a)，细边框 (#333333)。
  - 无阴影或极轻微的阴影，强调平面精密感。
- **输入框 (Inputs):**
  - 深色填充，焦点状态为 NVIDIA Green 边框。

## 布局原则 (Layout Principles)

- **结构:** 经典论坛布局。
- **核心区块:**
  1. **顶部导航 (Navbar):** 包含 Logo、搜索、用户头像。
  2. **英雄区 (Hero):** 社区欢迎语与最新公告。
  3. **分类列表 (Categories):** 按产品（GeForce, Studio, Data Center）分类。
  4. **最新动态 (Latest Posts):** 实时更新的帖子流。
  5. **侧边栏 (Sidebar):** 包含热门标签、社区统计、快速链接。

## 响应式行为 (Responsive Behavior)

- 移动端采用单列布局，隐藏次要侧边栏。
- 桌面端保持多列结构，优化宽屏阅读体验。
- 保持 44px 的最小点击区域。
