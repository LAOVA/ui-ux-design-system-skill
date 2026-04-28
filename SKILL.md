---
name: uiux-design-system
description: Combine curated DESIGN.md references with structured UI/UX design rules to turn product briefs, page requests, component requests, or existing UI code into a usable design system. Use when Codex needs to choose visual direction, map a product to reference brands, generate a global design system or DESIGN.md, create page-level overrides, or review UI for consistency, accessibility, responsiveness, and implementation guidance.
---

# UIUX Design System

Turn vague product or page requests into a concrete UI direction that another agent or engineer can implement. Blend two sources already bundled in this project:

- `./awesome-design-md`: brand and product reference styles
- `./ui-ux-pro-max-skill`: structured design rules, search scripts, and stack guidance

Keep this file lean. Read only the reference file that matches the current task:

- Read [references/source-map.md](references/source-map.md) first when you need to know where to pull information from.
- Read [references/workflows.md](references/workflows.md) when the request is about generation, review, or choosing a mode.
- Read [references/output-contracts.md](references/output-contracts.md) before producing a `DESIGN.md`, design-system spec, design-spec HTML, page override, or review report.
- Read [references/html-spec-contract.md](references/html-spec-contract.md) before generating a browsable design-spec HTML artifact.
- Read [references/implementation-architecture.md](references/implementation-architecture.md) when the user wants to build or extend the skill itself.

## Workflow

1. Classify the request.
   Use one of five modes: `reference-match`, `design-system`, `design-spec-html`, `page-override`, or `ui-review`.

2. Gather only the context you need.
   Use `./awesome-design-md` to infer visual tone and brand analogs.
   Use `./ui-ux-pro-max-skill` to infer product fit, style rules, colors, typography, UX constraints, and stack guidance.

3. Synthesize instead of copying.
   Extract the traits that matter: mood, palette, typography, layout density, component feel, interaction style, and anti-patterns.
   Do not paste long source passages or dump raw tables unless the user asks for them.

4. Produce a decision-ready output.
   Default to a concise recommendation with rationale for advisory requests.
   For generation requests, default to producing both a browsable `design-spec.html` artifact and a matching `DESIGN.md` artifact even if the user does not explicitly ask for them, unless they ask for a different output format.
   When the user wants an artifact, emit a structured `DESIGN.md`, design-system spec, design-spec HTML, page override, or review report that follows [references/output-contracts.md](references/output-contracts.md).

## Source Usage

### Reference styles

Inspect `./awesome-design-md/design-md/*/README.md` when the user references a brand, asks for a visual direction, or needs inspiration. Match by:

- product category
- mood and tone
- color energy
- typography feel
- layout density
- interaction style

### Structured rules

Prefer the existing local search tooling when you need product, style, color, typography, landing, UX, or stack guidance:

```powershell
py .\scripts\search.py "<query>" --project-name "<Project Name>"
py .\scripts\search.py "<query>" --format html --output .\artifacts\design-spec.html
py .\scripts\search.py "<query>" --format markdown --output .\artifacts\DESIGN.md
py .\scripts\search.py "<query>" --format json --output .\artifacts\design-system.json
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --design-system -p "<Project Name>"
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain style
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --domain ux
py .\ui-ux-pro-max-skill\scripts\search.py "<query>" --stack react
```

If the search output is noisy or insufficient, read the relevant CSV-backed domain description from [references/source-map.md](references/source-map.md) and inspect the source data directly.

## Mode Selection

- Use `reference-match` when the user asks what the product should look like or which brands it should resemble.
- Use `design-system` when the user wants a full visual system, `DESIGN.md`, implementation-ready UI direction, or a default generated spec artifact.
- Use `design-spec-html` when the user wants a browsable style guide, design-spec HTML, or a visual artifact that previews tokens and component rules.
- Use `page-override` when the global style already exists and the user needs rules for a specific page such as `landing`, `dashboard`, `pricing`, or `checkout`.
- Use `ui-review` when the user provides UI code, screenshots, or a page description and wants critique, fixes, or polish.

## Guardrails

- Preserve the difference between inspiration and prescription. References inform the direction; they do not replace product-specific reasoning.
- Prefer semantic tokens over raw hex values when describing systems.
- Always surface accessibility, responsiveness, and interaction constraints for implementation-facing outputs.
- For HTML outputs, prefer deterministic template rendering over ad hoc generated markup.
- If the user asks to generate a design system and does not specify a target format, produce both `design-spec.html` and `DESIGN.md` by default and summarize the result briefly.
- Keep `design-spec.html` and `DESIGN.md` aligned by rendering them from the same normalized design-system data.
- If multiple directions are plausible, narrow to one recommended direction and one fallback rather than listing many equal options.
- When reviewing UI, prioritize concrete findings and implementation impact over taste.
