# DESIGN.md: Ferrari E-Commerce

## Visual Theme and Atmosphere

- **Category:** E-commerce
- **Style Direction:** Vibrant & Block-based
- **Summary:** Vibrant & Block-based direction for E-commerce with large sections (48px+ gaps), animated patterns, bold hover (color shift), scroll-snap, large type (32px+), 200-300ms.
- **Key Effects:** Large sections (48px+ gaps), animated patterns, bold hover (color shift), scroll-snap, large type (32px+), 200-300ms
- **Reference Styles:** Ferrari, ClickHouse, Framer
- **Reference Direction:** Primary reference: Ferrari - Luxury automotive. Chiaroscuro black-white editorial, Ferrari Red with extreme sparseness

## Color Palette and Semantic Roles

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary | `#da291c` | `--color-primary` |
| On Primary | `#ffffff` | `--color-on-primary` |
| Secondary | `#b01e0a` | `--color-secondary` |
| Accent | `#b01e0a` | `--color-accent` |
| Background | `#181818` | `--color-background` |
| Foreground | `#ffffff` | `--color-foreground` |
| Muted | `#666666` | `--color-muted` |
| Border | `#303030` | `--color-border` |
| Destructive | `#DC2626` | `--color-destructive` |

## Typography Rules

- **Heading Font:** FerrariSans
- **Body Font:** FerrariSans
- **Mood:** A luxury-automotive brand whose marketing surfaces read as cinematic editorial. The base canvas is **near-black** (`#181818`) holding pure white display type; white-canvas bands appear only inside specific editorial contexts (preowned listings, pricing tables). The single brand voltage is **Rosso Corsa** (`#da291c`) — the iconic Ferrari racing red — used scarcely on primary CTAs, the Cavallino mark, and Formula 1 race-position highlights. Type runs **FerrariSans** at modest weights (display 500, body 400) — never bombastic. Spacing follows an explicit 8px token ladder (`xxxs` 4px through `super` 128px); generous editorial pacing throughout. The brand's strongest visual signature is the **full-bleed cinematic hero photograph** that fills the viewport top with car photography, model details, or trackside livery — followed by a tighter editorial body layout below.
- **Best For:** Creative tools, Gen-Z marketing, e-commerce for youth culture, content portfolios, collage-style apps
- **Google Fonts:** https://fonts.google.com/share?selection.family=Space+Grotesk:wght@700

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
- Flat design without depth
- Text-heavy pages

## Responsive Behavior

- Use mobile-first layouts and avoid horizontal scrolling.
- Adapt density and gutters at tablet and desktop widths.
- Preserve readable line length and safe tap spacing.

## Agent Prompt Guide

- Use a Vibrant & Block-based direction with FerrariSans for headings and FerrariSans for body copy.
- Keep the pattern aligned to Bento Grid Showcase and preserve the section order: 1. Hero, 2. Bento Grid (Key Features), 3. Detail Cards, 4. Tech Specs, 5. CTA.
- Use semantic colors led by primary `#da291c`, accent `#b01e0a`, and background `#181818`.
