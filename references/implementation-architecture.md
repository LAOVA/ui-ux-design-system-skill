# Implementation Architecture

Use this file when the user wants to build or extend the `uiux-design-system` skill itself.

## Goal

Create a skill that merges:

- curated visual references from `./awesome-design-md`
- structured UI/UX design intelligence from `./ui-ux-pro-max-skill`

The combined skill should answer both:
- what should this feel like
- how should it be designed and implemented

## MVP Capabilities

1. Reference match
   Map a brief to 1-3 relevant reference brands or products.

2. Design-system generation
   Produce a global UI system from product type, tone, and platform needs.

3. `DESIGN.md` generation
   Emit a reusable document another coding agent can follow, from the same synthesized normalized data as HTML.

4. HTML spec generation
   Emit a browsable `design-spec.html` artifact from the same synthesized design-system data.

5. Page override generation
   Define page-level deviations from the global system.

6. UI review
   Review existing UI against the chosen direction and platform rules.

## Recommended Skill Layout

```text
uiux-design-system/
|- SKILL.md
|- agents/
|  |- openai.yaml
|- references/
|  |- source-map.md
|  |- workflows.md
|  |- output-contracts.md
|  |- html-spec-contract.md
|  |- implementation-architecture.md
|- scripts/                    # add later when implementation begins
|  |- generate.py              # primary generator entry point and orchestrator
|  |- search.py                # compatibility wrapper that forwards to generate.py
|  |- reference_search.py
|  |- design_system.py
|  |- build_design_spec.py
|  |- page_override.py
|  |- review.py
|  |- build_design_md.py
|  |- core/
|     |- bm25.py
|     |- reference_parser.py
|     |- domain_search.py
|     |- reasoning.py
|     |- formatters.py
|- data/                       # add later if you localize dependencies
|  |- references/
|  |- structured/
|  |- stacks/
|- templates/                  # optional
```

## Layered Architecture

### Reference Layer

Input:
- `awesome-design-md`

Responsibility:
- identify brand analogs
- extract style traits
- prevent shallow style matching

### Knowledge Layer

Input:
- `ui-ux-pro-max-skill/data/*.csv`

Responsibility:
- map product types to styles
- provide colors, typography, UX, and stack rules
- surface anti-patterns and implementation constraints

### Retrieval Layer

Responsibility:
- run brand-reference lookup first
- run structured search second
- limit context to relevant domains only

### Reasoning Layer

Responsibility:
- combine reference results and structured results
- decide one primary direction
- resolve conflicts between taste and usability
- produce one shared final design-system object for all renderers

### Output Layer

Responsibility:
- emit `generation-bundle.json`
- emit `manifest.json` for the official intermediate run outputs
- let the LLM author `DESIGN.md`
- let the LLM author `design-spec.html`
- emit page overrides
- emit review reports

## Suggested Build Order

1. Create the skill shell and references
2. Reuse `ui-ux-pro-max-skill` search logic before rewriting anything
3. Add reference parsing for `awesome-design-md`
4. Add a small reasoning layer that merges both result sets
5. Add formatter outputs, including `DESIGN.md` and `design-spec.html`
6. Add review mode last
