# HTML Spec Contract

Use this file when generating a browsable HTML design-spec artifact.

## Goal

Produce a lightweight style-guide page that a human can open locally and scan quickly. This artifact complements `DESIGN.md`; it does not replace it.

## Required Sections

1. Header
   - project name
   - category
   - style direction
   - one-sentence summary

2. Reference and pattern summary
   - pattern name
   - section order
   - CTA placement
   - key effects

3. Color palette
   - swatch for each semantic color
   - token name
   - hex value
   - short note when available

4. Typography
   - heading font
   - body font
   - mood
   - preview text

5. Token summary
   - spacing
   - radius
   - shadow or elevation

6. Components
   - primary button
   - secondary button
   - card
   - input

7. Rules
   - accessibility
   - responsiveness
   - anti-patterns

## Output Rules

- Prefer one HTML file that loads Tailwind with:
  - `<script src="https://cdn.tailwindcss.com"></script>`
- Use Tailwind utility classes for layout, spacing, typography, and most surfaces to keep markup and custom CSS small.
- Keep embedded CSS limited to theme variables, theme switching, and a small number of custom preview styles that are awkward to express purely with Tailwind.
- Keep markup deterministic and template-based.
- Use semantic color labels, not only visual swatches.
- Keep preview components simple and stable.
- External dependency exception:
  - Tailwind CDN is the default and expected dependency for this artifact.

## Default File Name

Use `design-spec.html` unless the user asks for a different output path.
