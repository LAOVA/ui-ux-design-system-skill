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

## 3. Page Override

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

## 4. UI Review

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
- Start with `page-override` if the system exists and the page is the only moving part.
- Start with `ui-review` if the artifact already exists.
