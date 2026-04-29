# DESIGN.md: Apple Forum

## Visual Theme and Atmosphere

- **Category:** Sleep Tracker
- **Style Direction:** Dark Mode (OLED)
- **Summary:** Dark Mode (OLED) direction for Sleep Tracker with minimal glow (text-shadow: 0 0 10px), dark-to-light transitions, low white emission, high readability, visible focus.
- **Key Effects:** Minimal glow (text-shadow: 0 0 10px), dark-to-light transitions, low white emission, high readability, visible focus
- **Reference Styles:** Apple
- **Reference Direction:** Primary reference: Apple - Consumer electronics. Premium white space, SF Pro, cinematic imagery

## Color Palette and Semantic Roles

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary | `#0066cc` | `--color-primary` |
| On Primary | `#ffffff` | `--color-on-primary` |
| Secondary | `#92400E` | `--color-secondary` |
| Accent | `#D97706` | `--color-accent` |
| Background | `#ffffff` | `--color-background` |
| Foreground | `#1d1d1f` | `--color-foreground` |
| Muted | `#F6F6F6` | `--color-muted` |
| Border | `#e0e0e0` | `--color-border` |
| Destructive | `#DC2626` | `--color-destructive` |

## Typography Rules

- **Heading Font:** SF Pro Display
- **Body Font:** Public Sans
- **Mood:** A photography-first interface that turns marketing into a museum gallery. Edge-to-edge product tiles alternate light and dark canvases, framed by SF Pro Display headlines with negative letter-spacing and a single Action Blue (#0066cc) interactive color. UI chrome recedes so the product can speak — no decorative gradients, no shadows on chrome, only the one signature drop-shadow under product imagery resting on a surface.
- **Best For:** Magazines, online publications, editorial content, journalism
- **Google Fonts:** https://fonts.google.com/share?selection.family=Libre+Bodoni:wght@400;500;600;700|Public+Sans:wght@300;400;500;600;700

## Component Styling Rules

- **Buttons:** Primary buttons should use #0066cc and stay visually calm but obvious.
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
- Pure white backgrounds

## Responsive Behavior

- Use mobile-first layouts and avoid horizontal scrolling.
- Adapt density and gutters at tablet and desktop widths.
- Preserve readable line length and safe tap spacing.

## Agent Prompt Guide

- Use a Dark Mode (OLED) direction with SF Pro Display for headings and Public Sans for body copy.
- Keep the pattern aligned to Bento Grid Showcase and preserve the section order: 1. Hero, 2. Bento Grid (Key Features), 3. Detail Cards, 4. Tech Specs, 5. CTA.
- Use semantic colors led by primary `#0066cc`, accent `#D97706`, and background `#ffffff`.
