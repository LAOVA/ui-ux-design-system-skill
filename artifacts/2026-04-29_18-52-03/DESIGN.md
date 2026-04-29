# DESIGN.md: Ferrari AI CMS

## Visual Theme and Atmosphere

- **Category:** Financial Dashboard
- **Style Direction:** Dark Mode (OLED)
- **Summary:** Dark Mode (OLED) direction for Financial Dashboard with minimal glow (text-shadow: 0 0 10px), dark-to-light transitions, low white emission, high readability, visible focus.
- **Key Effects:** Minimal glow (text-shadow: 0 0 10px), dark-to-light transitions, low white emission, high readability, visible focus
- **Reference Styles:** Ferrari, BMW, Minimax
- **Reference Direction:** Primary reference: Ferrari - Luxury automotive. Chiaroscuro black-white editorial, Ferrari Red with extreme sparseness

## Color Palette and Semantic Roles

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary (Rosso Corsa) | `#da291c` | `--color-primary` |
| Accent (Giallo Modena) | `#FFD700` | `--color-accent-yellow` |
| Secondary | `#b01e0a` | `--color-secondary` |
| Background | `#0A0A0A` | `--color-background` |
| Foreground | `#FFFFFF` | `--color-foreground` |
| Muted | `#888888` | `--color-muted` |
| Border | `#2A2A2A` | `--color-border` |
| Destructive | `#DC2626` | `--color-destructive` |
| Carbon Texture | `rgba(255,255,255,0.03)` | `--color-carbon` |

## Typography Rules

- **Heading Font:** "Inter", sans-serif (Simulating Ferrari's racing typography)
- **Body Font:** "Inter", sans-serif
- **Mood:** 一种奢华且高性能的品牌氛围。画布基础色为**极黑** (`#0A0A0A`)，搭配纯白显示字体。核心视觉焦点是**法拉利红 (Rosso Corsa)** (`#da291c`)，用于关键 CTA 和性能指标。**法拉利黄 (Giallo Modena)** (`#FFD700`) 作为点缀色用于辅助提示和 AI 状态。界面中融入**碳纤维 (Carbon Fiber)** 纹理和**F1 遥测 (Telemetry)** 风格的细线与网格。
- **Best For:** Fashion brands, luxury e-commerce, jewelry, high-end services
- **Google Fonts:** https://fonts.google.com/share?selection.family=Cormorant:wght@400;500;600;700|Montserrat:wght@300;400;500;600;700

## Component Styling Rules

- **Buttons:** Primary buttons should use #da291c and stay visually calm but obvious.
- **Cards:** Use soft boundaries, moderate radius, and structure-led hierarchy over decorative noise.
- **Inputs:** Inputs should remain highly legible, with clear labels and visible focus treatment.

## Layout Principles

- **Pattern Name:** Bento Grid Showcase
- **Section Order:** 1. Hero, 2. Bento Grid (Key Features), 3. Detail Cards, 4. Tech Specs, 5. CTA
- **CTA Placement:** Floating Action Button or Bottom of Grid
- **Color Strategy:** Card backgrounds: #F5F5F7 or Glass. Icons: Vibrant brand colors. Text: Dark.
- **Conversion Focus:** Scannable value props. High information density without clutter. Mobile stack.

## Depth and Elevation

- `shadow-card`: `0 10px 30px rgba(15, 23, 42, 0.10)`
- `shadow-popover`: `0 18px 48px rgba(15, 23, 42, 0.18)`
- `radius-sm`: `8px`
- `radius-md`: `12px`
- `radius-lg`: `16px`

## Do and Do-Not Rules

### Do
- Contrast ratio 4.5:1 or better for body text.
- Visible focus states on all interactive elements.
- Minimum touch target around 44 by 44 pixels.

### Do Not
- Light mode default
- Slow rendering

## Responsive Behavior

- Use mobile-first layouts and avoid horizontal scrolling.
- Adapt density and gutters at tablet and desktop widths.
- Preserve readable line length and safe tap spacing.

## Agent Prompt Guide

- Use a Dark Mode (OLED) direction with FerrariSans for headings and FerrariSans for body copy.
- Keep the pattern aligned to Bento Grid Showcase and preserve the section order: 1. Hero, 2. Bento Grid (Key Features), 3. Detail Cards, 4. Tech Specs, 5. CTA.
- Use semantic colors led by primary `#da291c`, accent `#b01e0a`, and background `#181818`.
