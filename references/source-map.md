# Source Map

Use this file to decide which sibling project to inspect and how to extract signal without loading unnecessary context.

## Repositories in This Workspace

### `./awesome-design-md`

Purpose:
- Supply inspiration and reference styles
- Answer "what should this feel like?"

Primary files:
- `./awesome-design-md/README.md`
- `./awesome-design-md/design-md/*/README.md`

Use for:
- brand analog matching
- mood and tone selection
- color energy and contrast direction
- typography personality
- layout density
- component and motion feel

Extract:
- brand or product category
- signature palette tendencies
- typography voice
- spatial density
- primary surface treatment
- CTA emphasis style
- notable do and do-not patterns

Avoid:
- copying long passages verbatim
- treating a reference as a complete design system for a different product

### `./ui-ux-pro-max-skill`

Purpose:
- Supply structured, searchable design rules
- Answer "how should this be designed and implemented?"

Primary files:
- `./ui-ux-pro-max-skill/SKILL.md`
- `./ui-ux-pro-max-skill/scripts/search.py`
- `./ui-ux-pro-max-skill/scripts/core.py`
- `./ui-ux-pro-max-skill/scripts/design_system.py`

Core data domains:
- `data/products.csv`: product-to-style recommendations
- `data/styles.csv`: style categories, effects, implementation hints
- `data/colors.csv`: product-aligned semantic palettes
- `data/typography.csv`: font pairings and tone
- `data/landing.csv`: landing-page structures and CTA strategy
- `data/ux-guidelines.csv`: UX rules and anti-patterns
- `data/react-performance.csv`: React and app-interface implementation guidance
- `data/stacks/*.csv`: stack-specific delivery guidance
- `data/ui-reasoning.csv`: product-level reasoning and priority rules

## Practical Retrieval Order

### For a new product brief

1. Match 1-3 brand references from `awesome-design-md`
2. Read product and style guidance from `ui-ux-pro-max-skill`
3. Pull color, typography, UX, and stack guidance
4. Synthesize the reference results and structured results into one recommended system

### For a visual-direction request

1. Start with `awesome-design-md`
2. Use `ui-ux-pro-max-skill` only to validate that the chosen direction fits the product type and platform constraints

### For a code or UI review request

1. Start with the artifact being reviewed
2. Pull `ux-guidelines`, `styles`, and relevant stack guidance
3. Use reference styles only if the user asks for better direction or stronger art direction

## Suggested Local Commands

```powershell
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --design-system -p "<Project Name>"
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain product
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain style
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain color
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain typography
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain ux
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --stack react
```

Use direct file reads only when the CLI output is insufficient for the task.
