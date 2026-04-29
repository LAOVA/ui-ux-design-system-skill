# Workflows

Choose the workflow that matches the user's request. Keep the answer proportional to the request.

## 1. Reference Match

Use when the user says things like:
- "What should this look like?"
- "Give me a visual direction."
- "Make it feel like Linear, Vercel, or Apple."

Process:
1. Identify product type, audience, and tone.
2. Match 1-3 relevant references from `awesome-design-md`.
3. Explain the recommended primary reference and one fallback.
4. Summarize the transferable traits:
   - mood
   - palette direction
   - typography feel
   - layout density
   - component character
   - motion character

## 2. Design System

Use when the user wants a full system, `DESIGN.md`, or implementation-ready direction.

Process:
1. Parse the brief into:
   - product type
   - audience
   - platform
   - page type
   - tone
   - density
2. Read reference-style input from `awesome-design-md`.
3. Read structured design-system output from `ui-ux-pro-max-skill`.
4. Synthesize those two result sets into one shared design-system object.
5. Decide one primary direction.
6. Produce:
   - style direction
   - semantic palette
   - typography system
   - spacing and surface rules
   - component rules
   - motion and interaction rules
   - accessibility and responsive constraints
   - anti-patterns

Execution note:
- Prefer `scripts/generate.py` as the top-level command for this workflow.
- `scripts/reasoning.py` should do the source fusion: reference input first, structured output second, synthesis third.
- `scripts/generate.py` should then write `generation-bundle.json` and `manifest.json`, not the final deliverables.
- After that, the LLM should read the bundle and author the final `DESIGN.md` and `design-spec.html`.
- Those final files must be written into the exact same run directory recorded by `manifest.json.final_output_dir`.
- Treat writing to `demo/`, the repository root, or a second run directory as a workflow failure for that generation.
- After authoring the final files, run `scripts/finalize_manifest.py <run_dir>` so the manifest moves from `bundle-generated` to `final-artifacts-authored`.

Default output rule:
- If the user asks to generate or create a design system and does not specify a format, first generate the intermediate bundle, then author both `design-spec.html` and `DESIGN.md` from that bundle.
- If the user explicitly asks for `DESIGN.md`, Markdown, JSON, or another format, honor that instead after bundle generation.
- Unless the user explicitly overrides the path, store generated artifacts under `./artifacts/<timestamp>/`.
- Treat `./artifacts/<timestamp>/manifest.json` as the official record of the run.
- The final artifacts for that run must stay in the same directory as `generation-bundle.json` and `manifest.json`.

## 3. Design-Spec HTML

Use when the user wants a browsable design spec, lightweight style guide page, or HTML artifact that previews the system visually.

Process:
1. Prefer `scripts/generate.py` as the top-level generator so the run starts from one shared bundle.
2. Generate or load the synthesized design-system data first.
3. Normalize it into a consistent structure for export.
4. Read `templates/design-spec.html` and treat it as the required structural contract.
5. Author the HTML from that template instead of freehand markup for a different page type.
   Default to Tailwind CDN plus utility classes for layout and spacing, with only a small custom CSS theme layer.
6. Include the sections required by [html-spec-contract.md](html-spec-contract.md).
7. Save the artifact to a user-visible path when the user asks for a file output.
8. Verify the generated file contains the required template signature. If signature verification fails, treat the run as failed rather than silently accepting the HTML.

Important distinction:
- `design-spec.html` is a spec page.
- A dashboard, editor, landing page, CMS, or app screen preview is a separate artifact type.
- If the user asks for both, generate `design-spec.html` from the template and create the app preview separately.

Script role reminder:
- `scripts/generate.py` is the orchestrator and recommended entry point for intermediate data.
- `scripts/build_design_spec.py` is the dedicated HTML exporter.
- `scripts/build_design_md.py` is the dedicated Markdown exporter.

## 4. Page Override

Use when the product already has a global system and the user needs a specific page defined.

Process:
1. Read the global system or infer it from context.
2. Identify the page archetype.
3. Pull relevant landing, UX, and style rules.
4. Output only page-level differences:
   - layout
   - section order
   - density
   - CTA emphasis
   - component emphasis
   - page-specific risks

## 5. UI Review

Use when the user wants critique, polish, or design fixes.

Process:
1. Inspect the code, image, or description first.
2. Evaluate:
   - visual hierarchy
   - consistency
   - accessibility
   - responsiveness
   - touch and interaction
   - motion and state feedback
   - stack-specific risks
3. Lead with concrete findings.
4. If useful, suggest one upgraded style direction grounded in references.

## Decision Heuristics

- Start with `reference-match` if the user is unclear on taste.
- Start with `design-system` if the user is clear on product intent but needs a buildable system.
- Start with `design-spec-html` if the user explicitly wants a visual spec artifact or HTML deliverable.
- Start with `page-override` if the system exists and the page is the only moving part.
- Start with `ui-review` if the artifact already exists.

Template adherence heuristic:
- If the requested file name or output type is `design-spec.html`, never swap in a custom application layout in its place.
- If you need to show a more concrete UI concept, add a second artifact rather than mutating the spec artifact into something else.

Default artifact heuristic:
- `design-system` should usually end by generating both `design-spec.html` and `DESIGN.md` unless the user asked for a different deliverable.
