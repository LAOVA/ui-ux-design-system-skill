#!/usr/bin/env python3
r"""
Build a DESIGN.md artifact from the same normalized design-system data used by
the HTML exporter.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from build_design_spec import normalize_design_system  # type: ignore  # noqa: E402
from reasoning import generate_design_system  # type: ignore  # noqa: E402


def default_output_path(filename: str = "DESIGN.md") -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return ROOT_DIR / "artifacts" / stamp / filename


COLOR_ROWS = [
    ("Primary", "primary", "--color-primary"),
    ("On Primary", "on_primary", "--color-on-primary"),
    ("Secondary", "secondary", "--color-secondary"),
    ("Accent", "accent", "--color-accent"),
    ("Background", "background", "--color-background"),
    ("Foreground", "foreground", "--color-foreground"),
    ("Muted", "muted", "--color-muted"),
    ("Border", "border", "--color-border"),
    ("Destructive", "destructive", "--color-destructive"),
]


def render_markdown(design_system: dict) -> str:
    normalized = normalize_design_system(design_system)
    colors = design_system.get("colors", {})
    pattern = design_system.get("pattern", {})
    typography = design_system.get("typography", {})

    lines: list[str] = []
    lines.append(f"# DESIGN.md: {normalized['project_name']}")
    lines.append("")
    lines.append("## Visual Theme and Atmosphere")
    lines.append("")
    lines.append(f"- **Category:** {normalized['category']}")
    lines.append(f"- **Style Direction:** {normalized['style_name']}")
    lines.append(f"- **Summary:** {normalized['summary']}")
    lines.append(f"- **Key Effects:** {normalized['key_effects']}")
    if design_system.get("reference_summary"):
        lines.append(f"- **Reference Styles:** {design_system.get('reference_summary')}")
    if design_system.get("reference_direction"):
        lines.append(f"- **Reference Direction:** {design_system.get('reference_direction')}")
    lines.append("")
    lines.append("## Color Palette and Semantic Roles")
    lines.append("")
    lines.append("| Role | Hex | CSS Variable |")
    lines.append("|------|-----|--------------|")
    for label, key, token in COLOR_ROWS:
        value = colors.get(key)
        if value:
            lines.append(f"| {label} | `{value}` | `{token}` |")
    lines.append("")
    lines.append("## Typography Rules")
    lines.append("")
    lines.append(f"- **Heading Font:** {typography.get('heading', normalized['heading_font'])}")
    lines.append(f"- **Body Font:** {typography.get('body', normalized['body_font'])}")
    lines.append(f"- **Mood:** {typography.get('mood', normalized['typography_mood'])}")
    if typography.get("best_for"):
        lines.append(f"- **Best For:** {typography.get('best_for')}")
    if typography.get("google_fonts_url"):
        lines.append(f"- **Google Fonts:** {typography.get('google_fonts_url')}")
    lines.append("")
    lines.append("## Component Styling Rules")
    lines.append("")
    lines.append(f"- **Buttons:** {normalized['button_guidance']}")
    lines.append(f"- **Cards:** {normalized['card_guidance']}")
    lines.append(f"- **Inputs:** {normalized['input_guidance']}")
    lines.append("")
    lines.append("## Layout Principles")
    lines.append("")
    lines.append(f"- **Pattern Name:** {pattern.get('name', normalized['pattern_name'])}")
    lines.append(f"- **Section Order:** {pattern.get('sections', normalized['pattern_sections'])}")
    lines.append(f"- **CTA Placement:** {pattern.get('cta_placement', normalized['cta_placement'])}")
    if pattern.get("color_strategy"):
        lines.append(f"- **Color Strategy:** {pattern.get('color_strategy')}")
    if pattern.get("conversion"):
        lines.append(f"- **Conversion Focus:** {pattern.get('conversion')}")
    lines.append("")
    lines.append("## Depth and Elevation")
    lines.append("")
    lines.append("- `shadow-card`: `0 10px 30px rgba(15, 23, 42, 0.10)`")
    lines.append("- `shadow-popover`: `0 18px 48px rgba(15, 23, 42, 0.18)`")
    lines.append("- `radius-sm`: `8px`")
    lines.append("- `radius-md`: `12px`")
    lines.append("- `radius-lg`: `16px`")
    lines.append("")
    lines.append("## Do and Do-Not Rules")
    lines.append("")
    lines.append("### Do")
    for item in normalized["accessibility_rules_list"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("### Do Not")
    for item in normalized["anti_patterns_list"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Responsive Behavior")
    lines.append("")
    for item in normalized["responsive_rules_list"]:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Agent Prompt Guide")
    lines.append("")
    lines.append(
        f"- Use a {normalized['style_name']} direction with {typography.get('heading', normalized['heading_font'])} for headings and "
        f"{typography.get('body', normalized['body_font'])} for body copy."
    )
    lines.append(
        f"- Keep the pattern aligned to {pattern.get('name', normalized['pattern_name'])} and preserve the section order: "
        f"{pattern.get('sections', normalized['pattern_sections'])}."
    )
    lines.append(
        f"- Use semantic colors led by primary `{colors.get('primary', normalized['primary'])}`, accent `{colors.get('accent', normalized['accent'])}`, "
        f"and background `{colors.get('background', normalized['background'])}`."
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a DESIGN.md artifact.")
    parser.add_argument("query", help='Brief such as "AI SaaS dashboard"')
    parser.add_argument("--project-name", "-p", default=None, help="Project name shown in the output")
    parser.add_argument("--output", "-o", default=None, help="Output Markdown path")
    args = parser.parse_args()

    design_system = generate_design_system(args.query, args.project_name)

    output_path = default_output_path() if not args.output else Path(args.output)
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_markdown(design_system), encoding="utf-8")
    print(f"Generated DESIGN.md: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
