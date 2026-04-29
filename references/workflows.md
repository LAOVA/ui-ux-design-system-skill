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
2. Run a structured search in `ui-ux-pro-max-skill`.
3. Pull supporting references from `awesome-design-md`.
4. Decide one primary direction.
5. Produce:
   - style direction
   - semantic palette
   - typography system
   - spacing and surface rules
   - component rules
   - motion and interaction rules
   - accessibility and responsive constraints
   - anti-patterns

Default output rule:
- If the user asks to generate or create a design system and does not specify a format, generate both `design-spec.html` and `DESIGN.md` and provide a short written summary.
- If the user explicitly asks for `DESIGN.md`, Markdown, JSON, or another format, honor that instead.

## 3. Design-Spec HTML

Use when the user wants a browsable design spec, lightweight style guide page, or HTML artifact that previews the system visually.

Process:
1. Generate or load the design-system data first.
2. Normalize it into a consistent structure for export.
3. Render the HTML from a template instead of freehand markup.
   Default to Tailwind CDN plus utility classes for layout and spacing, with only a small custom CSS theme layer.
4. Include the sections required by [html-spec-contract.md](html-spec-contract.md).
5. Save the artifact to a user-visible path when the user asks for a file output.

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

Default artifact heuristic:
- `design-system` should usually end by generating both `design-spec.html` and `DESIGN.md` unless the user asked for a different deliverable.
