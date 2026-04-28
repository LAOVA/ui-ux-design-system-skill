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

- Prefer one self-contained HTML file with embedded CSS.
- Keep markup deterministic and template-based.
- Use semantic color labels, not only visual swatches.
- Keep preview components simple and stable.
- Avoid external dependencies for the first version.

## Default File Name

Use `design-spec.html` unless the user asks for a different output path.
