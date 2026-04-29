# NVIDIA 风格个人主页设计规范 (NVIDIA Personal Home)

## 1. 视觉语言 (Visual Language)

NVIDIA 的设计风格核心在于 **"技术力量" (Technical Power)**、**"高性能" (High Performance)** 以及其标志性的 **"绿色能量" (Green Energy)**。

### 核心特质:
- **高对比度**: 纯黑背景与明亮的绿色荧光效果。
- **几何感**: 硬朗的边缘、网格布局 (Bento Grid) 以及精确的间距。
- **发光效果 (Glow/Bloom)**: 模拟 GPU 硬件的灯效和计算能量的流动。
- **数据驱动**: 强调技术指标、性能参数和架构图感。

---

## 2. 色彩系统 (Color Palette)

| 角色 | 十六进制 | 用途 |
| :--- | :--- | :--- |
| **Brand Primary** | `#76B900` | NVIDIA 标志性绿色，用于核心 CTA、发光点缀、重点文字。 |
| **Brand Secondary** | `#4E7A00` | 深绿色，用于悬停状态、渐变过渡。 |
| **Background** | `#000000` | 纯黑，传达极致性能与专业感。 |
| **Surface Low** | `#1A1A1A` | 深灰色表面，用于卡片容器、侧边栏。 |
| **Surface Mid** | `#2D2D2D` | 中灰色，用于分割线、次要容器。 |
| **Text Primary** | `#FFFFFF` | 高清晰度白色文字。 |
| **Text Muted** | `#A1A1AA` | 灰色文字，用于说明性内容、脚注。 |
| **Accent Glow** | `rgba(118, 185, 0, 0.2)` | 绿色光晕，用于提升层次感。 |

---

## 3. 字体规范 (Typography)

NVIDIA 风格偏向于现代几何无衬线体，强调清晰度。

- **标题 (Headings)**: `Inter`, `Segoe UI`, `-apple-system`, `sans-serif`
  - 风格: 粗体 (Bold/Black), 紧凑字间距, 全大写 (可选)。
- **正文 (Body)**: `Inter`, `Roboto`, `sans-serif`
  - 风格: 适中的行高 (1.6), 极简主义。
- **代码/技术参数 (Monospace)**: `JetBrains Mono`, `Fira Code`, `monospace`
  - 风格: 用于展示技术栈、版本号等。

---

## 4. 布局与组件 (Layout & Components)

### 布局策略: Bento Grid (便当盒布局)
采用模块化、响应式的网格系统，将不同维度的个人信息 (技能、项目、荣誉、实时状态) 像硬件组件一样排列。

### 关键组件:
1. **Hero Section**: 
   - 动态背景 (模拟神经元网络或 GPU 核心)。
   - 巨大的标语: "ACCELERATING PERSONAL INNOVATION"。
2. **Feature Cards (Bento)**:
   - 玻璃拟态 (Glassmorphism) 或 纯黑微光边框。
   - 悬停时产生绿色呼吸灯效果。
3. **Tech Stack Specs**:
   - 类似显卡规格表的布局。
   - 进度条或图表显示技能熟练度。
4. **Project Terminal**:
   - 代码风格的项目展示区。

---

## 5. 交互与动画 (Interaction & Motion)

- **进入动画**: 扫描线效果或模块逐个亮起。
- **悬停反馈**: 边框发光 (Border Glow)、缩放、阴影扩散。
- **微交互**: 鼠标跟随的绿色微光。

---

## 6. 反模式 (Anti-patterns) - 避免使用:
- 圆润的糖果色按钮。
- 过多的留白 (应保持高密度信息感)。
- 柔和的粉彩色系。
- 复杂的装饰性插图 (应使用技术蓝图或 3D 渲染)。
