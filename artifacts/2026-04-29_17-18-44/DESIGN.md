# DESIGN.md - X.AI Info Hub 设计规范

## 1. 视觉主题与氛围 (Visual Theme & Atmosphere)
X.AI Info Hub 采用极致的**单色驱动、等宽字体为主的硬核极简主义** (Monospace-driven Brutalist Minimalism)。
- **工程师视角**: 这种设计风格旨在传达“由工程师为工程师构建”的基础设施感，而非普通的消费级产品。
- **克制即是高级**: 避免任何渐变、装饰性插画或多余的色彩。通过大量的留白（负空间）和极高的对比度来传达权威感和科学可信度。
- **硬朗边缘**: 几乎不使用圆角，保持锐利的建筑感边缘。

## 2. 色彩调色板与语义角色 (Color Palette & Semantic Roles)
采用极高对比度的深色模式，不提供浅色模式以保持其独特的品牌调性。

| 角色 | 颜色值 | 说明 |
| :--- | :--- | :--- |
| **Background** | `#1f2228` | 接近纯黑的底色，减少屏幕发光感 |
| **Foreground** | `#ffffff` | 纯白文字，确保极致的可读性 |
| **Primary** | `#ffffff` | 主要操作项使用纯白色 |
| **Secondary** | `#1f2228` | 次要背景，通常与边框结合使用 |
| **Accent** | `#ffffff` | 仅在极少数需要强调的地方使用 |
| **Muted** | `#a1a1aa` | 辅助文字或非活动状态，使用灰色 |
| **Border** | `#3f3f46` | 线条感极细，通常为 1px 的灰色线条 |
| **Destructive**| `#ef4444` | 错误或危险操作，唯一的彩色点缀 |

## 3. 字体规则 (Typography Rules)
字体是该设计的灵魂。
- **标题 (Headings)**: 推荐使用 `Geist Mono` 或其他高品质等宽字体。在大尺寸（如 120px+）下使用细体 (Weight 300) 以展现科技感。
- **正文 (Body)**: 推荐使用 `Inter` 或 `Jost` 等几何无衬线字体，保持专业且易读。
- **按钮与标签**: 必须使用等宽字体，全大写字母，并增加字母间距 (`letter-spacing: 0.14em`)。

## 4. 组件样式规则 (Component Rules)
- **按钮 (Buttons)**:
  - 矩形边缘，无圆角。
  - 描边风格 (Ghost Buttons) 或 纯白填充。
  - 全大写等宽字体。
- **卡片 (Cards)**:
  - 8px 基础网格。
  - Bento Grid (便当盒网格) 布局。
  - 1px 细边框，无阴影，无圆角。
- **输入框 (Inputs)**:
  - 底部单线条描边或全边框。
  - 极简占位符，无背景填充。

## 5. 布局原则 (Layout Principles)
- **Bento Grid**: 核心功能或资讯展示采用非对称的便当盒布局，强调信息密度。
- **信息分层**: 通过对比度而非阴影来创造深度。
- **极致留白**: 在模块之间保持宽大的呼吸感，使重要信息更加突出。

## 6. 深度与高度 (Depth & Elevation)
- **零阴影**: 拒绝使用 `box-shadow`。
- **对比分层**: 使用背景色的微调（如 `#1f2228` 到 `#27272a`）来区分层级。

## 7. 准则 (Do and Do-Not)
- **Do**: 保持 100% 的对比度。
- **Do**: 使用等宽字体作为装饰或核心元素。
- **Do**: 保持边缘锐利。
- **Do Not**: 使用任何圆角超过 2px。
- **Do Not**: 使用渐变色。
- **Do Not**: 使用装饰性动效。

## 8. 响应式行为 (Responsive Behavior)
- **堆叠布局**: 移动端将 Bento Grid 转换为垂直堆叠的单列布局。
- **字体缩放**: 标题在移动端大幅度缩小，但保持其细体特征。

## 9. 提示词指南 (Agent Prompt Guide)
> "Create a high-fidelity interface for an AI information hub using the x.ai aesthetic. Use a dark background (#1f2228), pure white text (#ffffff), and Geist Mono for all headers. Implement a Bento Grid layout for news cards with 1px sharp borders. No border-radius, no shadows, no gradients. Focus on high information density and technical credibility."
