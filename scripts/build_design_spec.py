#!/usr/bin/env python3
r"""
Build a browsable design-spec HTML file from the existing UI/UX Pro Max
design-system generator.

Usage:
    py .\scripts\build_design_spec.py "AI SaaS dashboard" --project-name "Orbit"
    py .\scripts\build_design_spec.py "Fintech app" --output .\artifacts\design-spec.html
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"
TEMPLATE_PATH = ROOT_DIR / "templates" / "design-spec.html"

if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from design_system import DesignSystemGenerator  # type: ignore  # noqa: E402


DEFAULT_STYLES = """
    :root {
      color-scheme: light;
      --page-bg: {{background}};
      --page-fg: {{foreground}};
      --surface: {{card}};
      --surface-border: {{border}};
      --primary: {{primary}};
      --secondary: {{secondary}};
      --accent: {{accent}};
      --muted: {{muted}};
      --muted-fg: {{muted_foreground}};
      --shadow-card: 0 10px 30px rgba(15, 23, 42, 0.10);
      --shadow-popover: 0 18px 48px rgba(15, 23, 42, 0.18);
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --space-1: 4px;
      --space-2: 8px;
      --space-3: 16px;
      --space-4: 24px;
      --space-5: 40px;
      --font-heading: {{heading_font_css}};
      --font-body: {{body_font_css}};
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: var(--font-body);
      background: linear-gradient(180deg, {{background}}, {{card}});
      color: var(--page-fg);
    }
    .page {
      max-width: 1180px;
      margin: 0 auto;
      padding: 48px 20px 72px;
    }
    .hero, .section { margin-bottom: 28px; }
    .eyebrow {
      display: inline-flex;
      padding: 6px 10px;
      border: 1px solid var(--surface-border);
      border-radius: 999px;
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted-fg);
      background: rgba(255,255,255,0.5);
    }
    h1, h2, h3, strong { font-family: var(--font-heading); }
    h1 {
      margin: 14px 0 12px;
      font-size: clamp(2.5rem, 7vw, 4.5rem);
      line-height: 0.96;
      letter-spacing: -0.04em;
    }
    h2 {
      margin: 0 0 16px;
      font-size: 1.4rem;
      letter-spacing: -0.02em;
    }
    h3 {
      margin: 0 0 10px;
      font-size: 1rem;
    }
    p, li {
      color: var(--page-fg);
      opacity: 0.92;
      line-height: 1.6;
    }
    .lede {
      max-width: 62ch;
      margin: 0 0 18px;
      color: var(--muted-fg);
      font-size: 1.03rem;
    }
    .hero-grid, .detail-grid, .token-grid, .component-grid, .swatch-grid {
      display: grid;
      gap: 16px;
    }
    .hero-grid { grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); }
    .detail-grid, .token-grid, .component-grid { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
    .swatch-grid { grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); }
    .panel, .stat-card, .swatch, .card-preview {
      background: color-mix(in srgb, var(--surface) 88%, white 12%);
      border: 1px solid var(--surface-border);
      border-radius: var(--radius-lg);
      box-shadow: var(--shadow-card);
    }
    .panel, .stat-card, .swatch { padding: 18px; }
    .label, .meta {
      display: block;
      margin-bottom: 8px;
      color: var(--muted-fg);
      font-size: 0.8rem;
    }
    .swatch-chip {
      width: 100%;
      aspect-ratio: 16 / 10;
      border-radius: var(--radius-md);
      border: 1px solid rgba(15, 23, 42, 0.08);
      margin-bottom: 12px;
    }
    .sample-title {
      margin: 10px 0 0;
      font-size: 1.8rem;
      line-height: 1.08;
      letter-spacing: -0.03em;
    }
    .sample-body { margin: 10px 0 0; }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
    }
    ul {
      margin: 0;
      padding-left: 18px;
    }
    .button-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 12px;
    }
    .btn {
      appearance: none;
      border-radius: var(--radius-md);
      padding: 12px 18px;
      border: 1px solid transparent;
      font: inherit;
      font-weight: 600;
      cursor: pointer;
      transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
    }
    .btn:hover { transform: translateY(-1px); }
    .btn-primary {
      background: var(--primary);
      color: {{on_primary}};
      box-shadow: 0 10px 24px color-mix(in srgb, var(--primary) 22%, transparent);
    }
    .btn-secondary {
      background: transparent;
      color: var(--primary);
      border-color: color-mix(in srgb, var(--primary) 25%, var(--surface-border));
    }
    .card-preview {
      padding: 18px;
      margin-bottom: 12px;
    }
    .card-tag {
      display: inline-flex;
      padding: 5px 9px;
      margin-bottom: 12px;
      border-radius: 999px;
      background: color-mix(in srgb, var(--accent) 15%, white);
      color: var(--accent);
      font-size: 0.82rem;
      font-weight: 600;
    }
    .input-label {
      display: block;
      margin-bottom: 8px;
      font-size: 0.9rem;
      color: var(--muted-fg);
    }
    .input-preview {
      width: 100%;
      padding: 12px 14px;
      border-radius: var(--radius-md);
      border: 1px solid var(--surface-border);
      background: rgba(255,255,255,0.75);
      color: var(--page-fg);
      margin-bottom: 12px;
    }
    @media (max-width: 640px) {
      .page { padding: 28px 14px 48px; }
      .panel, .stat-card, .swatch { padding: 16px; }
    }
"""


COLOR_KEYS = [
    ("primary", "Primary"),
    ("secondary", "Secondary"),
    ("accent", "Accent"),
    ("background", "Background"),
    ("foreground", "Foreground"),
    ("card", "Card"),
    ("muted", "Muted"),
    ("border", "Border"),
    ("destructive", "Destructive"),
]

ACCESSIBILITY_RULES = [
    "Contrast ratio 4.5:1 or better for body text.",
    "Visible focus states on all interactive elements.",
    "Minimum touch target around 44 by 44 pixels.",
]

RESPONSIVE_RULES = [
    "Use mobile-first layouts and avoid horizontal scrolling.",
    "Adapt density and gutters at tablet and desktop widths.",
    "Preserve readable line length and safe tap spacing.",
]

ANTI_PATTERN_FALLBACK = [
    "Do not rely on emoji icons for core UI.",
    "Do not use layout-shifting hover effects.",
    "Do not hide focus states.",
]


def _safe(value: object, fallback: str = "") -> str:
    text = str(value or fallback)
    return html.escape(text)


def _font_css(font_name: str, fallback: str) -> str:
    if not font_name:
        return fallback
    return f"'{font_name}', {fallback}"


def _normalize(design_system: dict) -> dict:
    colors = design_system.get("colors", {})
    style = design_system.get("style", {})
    pattern = design_system.get("pattern", {})
    typography = design_system.get("typography", {})

    return {
        "project_name": design_system.get("project_name", "Untitled Project"),
        "category": design_system.get("category", "General"),
        "summary": (
            f"{style.get('name', 'Minimalism')} direction for "
            f"{design_system.get('category', 'a digital product')} with "
            f"{style.get('effects', 'subtle interactive polish').lower()}."
        ),
        "style_name": style.get("name", "Minimalism"),
        "pattern_name": pattern.get("name", "Hero + Features + CTA"),
        "pattern_sections": pattern.get("sections", "Hero > Features > CTA"),
        "cta_placement": pattern.get("cta_placement", "Above fold"),
        "key_effects": design_system.get("key_effects") or style.get("effects") or "Subtle hover transitions",
        "heading_font": typography.get("heading", "Inter"),
        "body_font": typography.get("body", "Inter"),
        "typography_mood": typography.get("mood", "Clean and readable"),
        "button_guidance": (
            f"Primary buttons should use {colors.get('primary', '#2563EB')} and stay visually calm but obvious."
        ),
        "card_guidance": "Use soft boundaries, moderate radius, and structure-led hierarchy over decorative noise.",
        "input_guidance": "Inputs should remain highly legible, with clear labels and visible focus treatment.",
        "background": colors.get("background", "#F8FAFC"),
        "foreground": colors.get("foreground", "#0F172A"),
        "card": colors.get("card", "#FFFFFF"),
        "border": colors.get("border", "#E2E8F0"),
        "primary": colors.get("primary", "#2563EB"),
        "secondary": colors.get("secondary", "#3B82F6"),
        "accent": colors.get("accent", "#F97316"),
        "muted": colors.get("muted", "#E2E8F0"),
        "muted_foreground": colors.get("muted_foreground", colors.get("foreground", "#475569")),
        "on_primary": colors.get("on_primary", "#FFFFFF") or "#FFFFFF",
        "heading_font_css": _font_css(typography.get("heading", "Inter"), "ui-sans-serif, system-ui, sans-serif"),
        "body_font_css": _font_css(typography.get("body", "Inter"), "ui-sans-serif, system-ui, sans-serif"),
        "anti_patterns_raw": design_system.get("anti_patterns", ""),
    }


def normalize_design_system(design_system: dict) -> dict:
    """Expose a normalized representation for other exporters."""
    normalized = _normalize(design_system)
    anti_patterns = [part.strip() for part in normalized["anti_patterns_raw"].split("+") if part.strip()]
    normalized["anti_patterns_list"] = anti_patterns or ANTI_PATTERN_FALLBACK
    normalized["accessibility_rules_list"] = ACCESSIBILITY_RULES
    normalized["responsive_rules_list"] = RESPONSIVE_RULES
    return normalized


def _list_items(items: list[str], fallback: list[str]) -> str:
    values = [item.strip() for item in items if item and item.strip()]
    if not values:
        values = fallback
    return "\n".join(f"            <li>{_safe(item)}</li>" for item in values)


def _anti_pattern_items(raw: str) -> str:
    items = [part.strip() for part in raw.split("+") if part.strip()]
    return _list_items(items, ANTI_PATTERN_FALLBACK)


def _color_swatches(colors: dict) -> str:
    rows = []
    for key, label in COLOR_KEYS:
        value = colors.get(key)
        if not value:
            continue
        rows.append(
            "\n".join(
                [
                    '        <article class="swatch">',
                    f'          <div class="swatch-chip" style="background: {_safe(value)};"></div>',
                    f"          <strong>{_safe(label)}</strong>",
                    f'          <span class="meta"><code>{_safe(key)}</code> - {_safe(value)}</span>',
                    "        </article>",
                ]
            )
        )
    return "\n".join(rows)


def render_html(design_system: dict) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    normalized = _normalize(design_system)
    styles = DEFAULT_STYLES
    for key, value in normalized.items():
        if key == "anti_patterns_raw":
            continue
        styles = styles.replace(f"{{{{{key}}}}}", str(value))

    replacements = {
        **{k: _safe(v) for k, v in normalized.items() if k != "anti_patterns_raw"},
        "styles": styles.rstrip(),
        "color_swatches": _color_swatches(design_system.get("colors", {})),
        "accessibility_rules": _list_items(
            ACCESSIBILITY_RULES,
            [],
        ),
        "responsive_rules": _list_items(
            RESPONSIVE_RULES,
            [],
        ),
        "anti_patterns": _anti_pattern_items(normalized["anti_patterns_raw"]),
    }

    output = template
    for key, value in replacements.items():
        output = output.replace(f"{{{{{key}}}}}", value)
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a design-spec HTML artifact.")
    parser.add_argument("query", help='Brief such as "AI SaaS dashboard"')
    parser.add_argument("--project-name", "-p", default=None, help="Project name shown in the output")
    parser.add_argument("--output", "-o", default="design-spec.html", help="Output HTML path")
    args = parser.parse_args()

    generator = DesignSystemGenerator()
    design_system = generator.generate(args.query, args.project_name)

    output_path = Path(args.output)
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_html(design_system), encoding="utf-8")

    print(f"Generated design-spec HTML: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
