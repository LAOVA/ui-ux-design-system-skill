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

2. Read reference-style input first.
   Use `./awesome-design-md` to infer visual tone, brand analogs, and transferable stylistic traits.

3. Read structured design-system output second.
   Use `./ui-ux-pro-max-skill` to infer product fit, style rules, colors, typography, UX constraints, and stack guidance.

4. Synthesize both sources into one shared design-system object.
   Extract the traits that matter: mood, palette, typography, layout density, component feel, interaction style, and anti-patterns.
   Do not paste long source passages or dump raw tables unless the user asks for them.

5. Let the LLM read the generated bundle and then render final artifacts from that shared object.
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

- `.\scripts\generate.py` is the primary generator entry point for this skill.
  It does not only search: it reads reference input, reads structured design-system output, synthesizes one shared dataset, then writes an intermediate `generation-bundle.json`.
- `.\scripts\build_design_spec.py` and `.\scripts\build_design_md.py` are exporter-level scripts.
  They are fallback exporter utilities, not the primary workflow.
- `.\scripts\finalize_manifest.py` is the run-closing utility.
  After the LLM writes final `DESIGN.md` and `design-spec.html`, use it to verify same-directory output and mark the run as complete.
- `.\scripts\search.py` remains as a compatibility wrapper, but new calls should prefer `generate.py`.

```powershell
py .\scripts\generate.py "<query>" --project-name "<Project Name>"
py .\scripts\generate.py "<query>" --format bundle
py .\scripts\generate.py "<query>" --format design-system-json
py .\scripts\finalize_manifest.py ".\artifacts\<timestamp>"
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
- `templates/design-spec.html` is the canonical design-system HTML template. Treat it as a required output contract, not a loose inspiration source.
- Prefer `scripts/generate.py` as the top-level command. It writes the intermediate bundle that the LLM must read before authoring final artifacts.
- Treat `scripts/reasoning.py` as the source-fusion layer:
  it reads `awesome-design-md`, reads `ui-ux-pro-max-skill`, then synthesizes the shared design-system object consumed by the renderers.
- Do not treat the immediate output of `scripts/generate.py` as the final deliverable. The final `DESIGN.md` and `design-spec.html` should be authored only after the LLM reads `generation-bundle.json` and `manifest.json`.
- The final `DESIGN.md` and `design-spec.html` must be written back into the same `./artifacts/<timestamp>/` directory recorded by `manifest.json`.
- Do not create a parallel final-delivery directory such as `demo/`, the repository root, or a second `artifacts/<other-timestamp>/` directory for the same run.
- After authoring the final files, run `scripts/finalize_manifest.py` on that run directory. A run is not fully complete until `manifest.json.workflow_stage` becomes `final-artifacts-authored`.
- When producing `design-spec.html`, the LLM must read `templates/design-spec.html` and author the file against that structure. Do not hand-author a different page type as a substitute for template rendering.
- Treat script execution plus template-signature verification as the success condition for `design-spec.html`. A hand-authored HTML file without the required template signature is not a valid completion.
- Do not replace `design-spec.html` with a bespoke application mockup, landing page, dashboard, editor, or prototype layout just because that feels more visually direct.
- When generating `design-spec.html`, preserve the template's document role: it is a design-system specification page, not an app screen preview.
- It is acceptable to fill the template with a brand's design language and to update token values, copy, swatches, component notes, and preview styling, but not to change the artifact into a different page type.
- If the user explicitly wants an application interface mockup or product prototype, create that as a separate artifact such as `app-preview.html`. Do not use it as a substitute for `design-spec.html`.
- If script execution is unavailable, manually mirror the existing template structure as closely as possible instead of inventing a new layout from scratch.
- `design-spec.html` should load Tailwind from `https://cdn.tailwindcss.com` and use Tailwind utilities for layout and presentation wherever practical, keeping custom CSS limited to theme variables and a small preview layer.
- Default artifact output must go under `./artifacts/<timestamp>/`. Do not write default deliverables to the project root.
- Treat `./artifacts/<timestamp>/generation-bundle.json` and `./artifacts/<timestamp>/manifest.json` as the official intermediate outputs for that generation.
- Treat the directory recorded by `manifest.json.final_output_dir` as the only valid destination for the final `DESIGN.md` and `design-spec.html`.
- If the user asks to generate a design system and does not specify a target format, produce both `design-spec.html` and `DESIGN.md` by default and summarize the result briefly.
- Keep `design-spec.html` and `DESIGN.md` aligned by rendering them from the same normalized design-system data.
- If multiple directions are plausible, narrow to one recommended direction and one fallback rather than listing many equal options.
- When reviewing UI, prioritize concrete findings and implementation impact over taste.
