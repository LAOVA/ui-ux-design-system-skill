# DESIGN.md: Ferrari Personal Home

## Visual Theme and Atmosphere

- **Category:** Portfolio/Personal
- **Style Direction:** Cinematic Editorial
- **Summary:** Cinematic Editorial direction for Portfolio/Personal with smooth scroll, parallax, minimal entrance anim.
- **Key Effects:** Scroll anim (Intersection Observer), hover (300-400ms), entrance, parallax (3-5 layers), page transitions
- **Reference Styles:** Ferrari
- **Reference Direction:** Primary reference: Ferrari - Luxury automotive. Chiaroscuro black-white editorial, Ferrari Red with extreme sparseness

## Color Palette and Semantic Roles

| Role | Hex | CSS Variable |
|------|-----|--------------|
| Primary | `#da291c` | `--color-primary` |
| On Primary | `#FFFFFF` | `--color-on-primary` |
| Secondary | `#181818` | `--color-secondary` |
| Accent | `#da291c` | `--color-accent` |
| Background | `#181818` | `--color-background` |
| Foreground | `#FFFFFF` | `--color-foreground` |
| Muted | `#969696` | `--color-muted` |
| Border | `#303030` | `--color-border` |
| Destructive | `#da291c` | `--color-destructive` |

## Typography Rules

- **Heading Font:** Inter
- **Body Font:** Inter
- **Mood:** cinematic, luxurious, precise, high-performance, authoritative
- **Best For:** High-end portfolios, executive personal brands, cinematic storytelling
- **Google Fonts:** https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap

## Component Styling Rules

- **Buttons:** Primary buttons should use #da291c and stay visually calm but obvious.
- **Cards:** Use soft boundaries, moderate radius, and structure-led hierarchy over decorative noise.
- **Inputs:** Inputs should remain highly legible, with clear labels and visible focus treatment.

## Layout Principles

- **Pattern Name:** Cinematic Storytelling
- **Section Order:** Hero > Bio > Portfolio > CTA
- **CTA Placement:** Hero and Footer
- **Color Strategy:** Rosso Corsa accents
- **Conversion Focus:** High-intent CTAs

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
- Corporate templates
- Generic layouts

## Responsive Behavior

- Use mobile-first layouts and avoid horizontal scrolling.
- Adapt density and gutters at tablet and desktop widths.
- Preserve readable line length and safe tap spacing.

## Agent Prompt Guide

- Use a Cinematic Editorial direction with Inter for headings and Inter for body copy.
- Keep the pattern aligned to Cinematic Storytelling and preserve the section order: Hero > Bio > Portfolio > CTA.
- Use semantic colors led by primary `#da291c`, accent `#da291c`, and background `#181818`.
