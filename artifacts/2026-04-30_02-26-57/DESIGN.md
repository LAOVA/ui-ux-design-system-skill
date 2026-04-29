# DESIGN.md: Ferrari CMS

## Visual Theme and Atmosphere

- **Category:** AI Photo & Avatar Generator
- **Style Direction:** AI-Native UI
- **Summary:** AI-Native UI direction for AI Photo & Avatar Generator with typing indicators (3-dot pulse), streaming text animations, pulse animations, context cards, smooth reveals.
- **Key Effects:** Typing indicators (3-dot pulse), streaming text animations, pulse animations, context cards, smooth reveals
- **Reference Styles:** Ferrari, Cohere, Composio
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
| Destructive | `#EF4444` | `--color-destructive` |

## Typography Rules

- **Heading Font:** FerrariSans
- **Body Font:** FerrariSans
- **Mood:** A luxury-automotive brand whose marketing surfaces read as cinematic editorial. The base canvas is **near-black** (`#181818`) holding pure white display type; white-canvas bands appear only inside specific editorial contexts (preowned listings, pricing tables). The single brand voltage is **Rosso Corsa** (`#da291c`) — the iconic Ferrari racing red — used scarcely on primary CTAs, the Cavallino mark, and Formula 1 race-position highlights. Type runs **FerrariSans** at modest weights (display 500, body 400) — never bombastic. Spacing follows an explicit 8px token ladder (`xxxs` 4px through `super` 128px); generous editorial pacing throughout. The brand's strongest visual signature is the **full-bleed cinematic hero photograph** that fills the viewport top with car photography, model details, or trackside livery — followed by a tighter editorial body layout below.
- **Best For:** Cross-platform apps, dashboards, system UI, onboarding, marketing pages, informational apps, icon-heavy interfaces
- **Google Fonts:** https://fonts.google.com/share?selection.family=Inter:wght@400;600;700;800

## Component Styling Rules

- **Buttons:** Primary buttons should use #da291c and stay visually calm but obvious.
- **Cards:** Use soft boundaries, moderate radius, and structure-led hierarchy over decorative noise.
- **Inputs:** Inputs should remain highly legible, with clear labels and visible focus treatment.

## Layout Principles

- **Pattern Name:** App Store Style Landing
- **Section Order:** 1. Hero with device mockup, 2. Screenshots carousel, 3. Features with icons, 4. Reviews/ratings, 5. Download CTAs
- **CTA Placement:** Download buttons prominent (App Store + Play Store) throughout
- **Color Strategy:** Dark/light matching app store feel. Star ratings in gold. Screenshots with device frames.
- **Conversion Focus:** Show real screenshots. Include ratings (4.5+ stars). QR code for mobile. Platform-specific CTAs.

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
- Inconsistent styling
- Poor contrast ratios

## Responsive Behavior

- Use mobile-first layouts and avoid horizontal scrolling.
- Adapt density and gutters at tablet and desktop widths.
- Preserve readable line length and safe tap spacing.

## Agent Prompt Guide

- Use a AI-Native UI direction with FerrariSans for headings and FerrariSans for body copy.
- Keep the pattern aligned to App Store Style Landing and preserve the section order: 1. Hero with device mockup, 2. Screenshots carousel, 3. Features with icons, 4. Reviews/ratings, 5. Download CTAs.
- Use semantic colors led by primary `#da291c`, accent `#b01e0a`, and background `#181818`.
