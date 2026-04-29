# Output Contracts

Use these structures when the user wants a deliverable instead of a conversational recommendation.

Default generation rule:
- When the user asks to generate a design system and does not specify an output format, first generate the intermediate bundle, then author both `design-spec.html` and `DESIGN.md`.
- Pair those artifacts with a short summary of the chosen direction and where the files were written.
- Render both artifacts from the same synthesized normalized design-system data so sections stay aligned.
- Write default artifacts under `./artifacts/<timestamp>/` rather than the repository root.
- Write `manifest.json` in that same run directory to record the official inputs and outputs.
- The final `DESIGN.md` and `design-spec.html` must be written into that same run directory, not a sibling folder such as `demo/` and not a second timestamped folder.
- Final delivery is only complete after `scripts/finalize_manifest.py` updates `manifest.json.workflow_stage` to `final-artifacts-authored`.

## Design System Spec

Include these sections in order:

1. Product framing
2. Recommended reference direction
3. Visual theme and atmosphere
4. Color system
5. Typography system
6. Layout and spacing rules
7. Component rules
8. Interaction and motion rules
9. Accessibility and responsive rules
10. Anti-patterns
11. Implementation notes by stack when relevant

## `DESIGN.md`

Keep it implementation-facing. Include:

1. Visual theme and atmosphere
2. Color palette and semantic roles
3. Typography rules
4. Component styling rules
5. Layout principles
6. Depth and elevation
7. Do and do-not rules
8. Responsive behavior
9. Agent prompt guide

Use semantic naming such as:
- `primary`
- `secondary`
- `accent`
- `background`
- `foreground`
- `muted`
- `border`
- `destructive`

## `design-spec.html`

Treat this as a human-browsable artifact generated from the same design-system data as `DESIGN.md`.

Treat the artifact type as fixed:
- It is a design-system specification page.
- It is not a substitute for a product mockup or application prototype.

Include:

1. Project summary
2. Reference direction
3. Color palette swatches
4. Typography preview
5. Token summary for spacing, radius, and shadow
6. Pattern and layout guidance
7. Component guidance for buttons, cards, and inputs
8. Accessibility and responsive rules
9. Anti-patterns

Prefer:
- semantic token labels
- copy-ready rules
- limited but clear component previews
- a single self-contained HTML file unless the user explicitly wants separate assets
- Tailwind CDN plus utility-first markup for most structure and spacing
- only a thin custom CSS layer for theme variables and preview-specific behavior
- a rendered file that still contains the canonical template signature comment

Do not:
- replace the template with a custom landing page, dashboard, editor, CMS, or mobile screen
- remove core spec sections in favor of a more “realistic” app layout
- reinterpret “HTML output” to mean “freeform UI mockup” when the requested artifact is `design-spec.html`

## Page Override

Keep it short. Include only what differs from the global system:

1. Page purpose
2. Layout overrides
3. Section order
4. CTA strategy
5. Component emphasis
6. Page-specific accessibility or UX risks

## Review Report

When reviewing, present:

1. Findings first, ordered by severity
2. Why each issue matters
3. The likely user impact
4. A concrete fix direction

Use concise headings or bullets. Do not hide important findings behind a long summary.
