#!/usr/bin/env python3
r"""
Build a browsable design-spec HTML file from the existing UI/UX Pro Max
design-system generator.
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
      color-scheme: {{theme_mode}};
      --page-bg: {{background}};
      --page-fg: {{foreground}};
      --surface-border: {{border}};
      --primary: {{primary}};
      --secondary: {{secondary}};
      --accent: {{accent}};
      --panel-bg: {{panel_bg}};
      --panel-bg-soft: {{panel_bg_soft}};
      --panel-fg: {{panel_fg}};
      --panel-muted: {{panel_muted}};
      --preview-bg: {{preview_bg}};
      --shadow-card: 0 10px 30px rgba(15, 23, 42, 0.10);
      --shadow-popover: 0 18px 48px rgba(15, 23, 42, 0.18);
      --font-heading: {{heading_font_css}};
      --font-body: {{body_font_css}};
      --interactive-primary: {{primary}};
      --interactive-on-primary: {{on_primary}};
      --interactive-primary-shadow: color-mix(in srgb, {{primary}} 22%, transparent);
      --interactive-secondary-fg: {{primary}};
    }
    body[data-page-theme="dark"] {
      color-scheme: dark;
      --page-bg: #020617;
      --page-fg: #F8FAFC;
      --surface-border: #243244;
      --panel-bg: #131C2E;
      --panel-bg-soft: #1A2740;
      --panel-fg: #F8FAFC;
      --panel-muted: #94A3B8;
      --preview-bg: #0B1220;
      --preview-surface: #162033;
      --preview-surface-strong: #10192A;
      --preview-border: #243244;
      --preview-fg: #F8FAFC;
      --preview-muted: #94A3B8;
      --shadow-card: 0 12px 36px rgba(2, 6, 23, 0.42);
      --shadow-popover: 0 20px 54px rgba(2, 6, 23, 0.48);
      --interactive-primary: {{accent}};
      --interactive-on-primary: #04110C;
      --interactive-primary-shadow: color-mix(in srgb, {{accent}} 32%, transparent);
      --interactive-secondary-fg: #D7FBE7;
    }
    body[data-page-theme="light"] {
      color-scheme: light;
      --page-bg: #F8FAFC;
      --page-fg: #0F172A;
      --surface-border: #CBD5E1;
      --panel-bg: #FFFFFF;
      --panel-bg-soft: #F1F5F9;
      --panel-fg: #0F172A;
      --panel-muted: #475569;
      --preview-bg: #FFFFFF;
      --preview-surface: #F8FAFC;
      --preview-surface-strong: #FFFFFF;
      --preview-border: #CBD5E1;
      --preview-fg: #0F172A;
      --preview-muted: #475569;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: var(--font-body);
      background: var(--page-bg);
      color: var(--page-fg);
      transition: background 180ms ease, color 180ms ease;
    }
    h1, h2, h3, h4, strong { font-family: var(--font-heading); }
    code {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
    }
    ul {
      margin: 0;
      padding-left: 18px;
    }
    a {
      color: var(--primary);
      text-underline-offset: 0.16em;
    }
    .page-theme-floating {
      background: color-mix(in srgb, var(--panel-bg) 86%, transparent);
      border-color: color-mix(in srgb, var(--surface-border) 78%, white 22%);
      box-shadow: var(--shadow-popover);
      backdrop-filter: blur(14px);
    }
    .page-theme-switch {
      background: color-mix(in srgb, var(--panel-bg-soft) 88%, white 12%);
      border-color: color-mix(in srgb, var(--surface-border) 72%, white 28%);
    }
    .page-theme-button {
      background: transparent;
      color: var(--panel-muted);
      transition: background 160ms ease, color 160ms ease, transform 160ms ease;
    }
    .page-theme-button:hover,
    .theme-button-primary:hover,
    .theme-button-secondary:hover {
      transform: translateY(-1px);
    }
    .page-theme-button.active {
      background: var(--interactive-primary);
      color: var(--interactive-on-primary);
    }
    .theme-panel {
      background: var(--panel-bg);
      border-color: var(--surface-border);
      color: var(--panel-fg);
      box-shadow: var(--shadow-card);
    }
    .theme-soft {
      background: var(--panel-bg-soft);
      border-color: color-mix(in srgb, var(--surface-border) 76%, white 24%);
      color: var(--panel-fg);
    }
    .theme-muted { color: var(--panel-muted); }
    .theme-chip {
      background: color-mix(in srgb, var(--panel-bg-soft) 92%, white 8%);
      border-color: var(--surface-border);
      color: var(--panel-fg);
      box-shadow: var(--shadow-card);
    }
    .theme-tag {
      background: color-mix(in srgb, var(--accent) 15%, white);
      color: var(--accent);
      border: 1px solid color-mix(in srgb, var(--accent) 25%, transparent);
    }
    .theme-button-primary {
      background: var(--interactive-primary);
      color: var(--interactive-on-primary);
      box-shadow: 0 10px 24px var(--interactive-primary-shadow);
      transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
    }
    .theme-button-secondary {
      background: transparent;
      color: var(--interactive-secondary-fg);
      border: 1px solid color-mix(in srgb, var(--interactive-primary) 25%, var(--surface-border));
      transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
    }
    .swatch-chip { border: 1px solid rgba(15, 23, 42, 0.08); }
    .flow-step {
      border: 1px solid color-mix(in srgb, var(--surface-border) 70%, white 30%);
      background: var(--panel-bg-soft);
    }
    .flow-index {
      background: color-mix(in srgb, var(--primary) 14%, white);
      color: var(--primary);
    }
    .token-bar { background: linear-gradient(90deg, var(--primary), var(--accent)); }
    .radius-box {
      border: 1px solid var(--surface-border);
      background: var(--panel-bg-soft);
    }
    .shadow-box {
      background: var(--panel-bg-soft);
      border: 1px solid color-mix(in srgb, var(--surface-border) 70%, white 30%);
    }
    .theme-input,
    .theme-preview-surface,
    .theme-preview-card,
    .theme-table,
    .theme-nav-item {
      background: var(--preview-surface, var(--panel-bg-soft));
      border-color: var(--preview-border, var(--surface-border));
      color: var(--preview-fg, var(--panel-fg));
    }
    .theme-input::placeholder { color: var(--preview-muted, var(--panel-muted)); }
    .theme-nav-item.active {
      background: var(--interactive-primary);
      color: var(--interactive-on-primary);
      border-color: var(--interactive-primary);
    }
    .theme-status-positive {
      background: color-mix(in srgb, var(--accent) 18%, white);
      color: var(--accent);
    }
    .theme-status-neutral {
      background: color-mix(in srgb, var(--secondary) 18%, white);
      color: var(--secondary);
    }
    .theme-preview-window,
    .theme-preview-surface,
    .theme-preview-card,
    .theme-input,
    .theme-nav-item,
    .theme-table {
      --preview-surface: var(--panel-bg-soft);
      --preview-surface-strong: var(--preview-bg);
      --preview-border: color-mix(in srgb, var(--surface-border) 65%, white 35%);
      --preview-fg: var(--panel-fg);
      --preview-muted: var(--panel-muted);
    }
    .theme-preview-window {
      background: var(--preview-surface-strong);
      border-color: var(--preview-border);
      transition: background 180ms ease, border-color 180ms ease, color 180ms ease;
    }
    .theme-dot { background: color-mix(in srgb, var(--panel-muted) 45%, transparent); }
    .theme-chart {
      background:
        linear-gradient(180deg, color-mix(in srgb, var(--accent) 16%, transparent), transparent),
        linear-gradient(90deg, rgba(255,255,255,0.2) 1px, transparent 1px),
        linear-gradient(180deg, rgba(255,255,255,0.14) 1px, transparent 1px);
      background-size: auto, 18px 18px, 18px 18px;
      background-color: var(--preview-surface-strong);
      border-color: color-mix(in srgb, var(--preview-border) 70%, white 30%);
      position: relative;
      overflow: hidden;
    }
    .theme-chart::after {
      content: "";
      position: absolute;
      inset: auto 10px 18px 10px;
      height: 3px;
      border-radius: 999px;
      background:
        linear-gradient(90deg, var(--accent) 0%, var(--accent) 30%, transparent 30%),
        linear-gradient(90deg, transparent 10%, var(--primary) 10%, var(--primary) 68%, transparent 68%);
      opacity: 0.85;
      transform: skewX(-18deg);
    }
    @media (max-width: 640px) {
      .page-theme-floating {
        width: calc(100% - 24px);
        justify-content: space-between;
      }
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


def _hex_to_rgb(value: str) -> tuple[int, int, int] | None:
    if not value or not isinstance(value, str):
        return None
    raw = value.strip().lstrip("#")
    if len(raw) != 6:
        return None
    try:
        return tuple(int(raw[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return None


def _relative_luminance(value: str) -> float:
    rgb = _hex_to_rgb(value)
    if not rgb:
        return 0.0

    def channel(c: int) -> float:
        s = c / 255
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(part) for part in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def _mix_hex(color_a: str, color_b: str, weight_a: float) -> str:
    rgb_a = _hex_to_rgb(color_a) or (15, 23, 42)
    rgb_b = _hex_to_rgb(color_b) or (255, 255, 255)
    weight_b = 1 - weight_a
    mixed = tuple(
        round((a * weight_a) + (b * weight_b))
        for a, b in zip(rgb_a, rgb_b)
    )
    return "#{:02X}{:02X}{:02X}".format(*mixed)


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
    normalized = _normalize(design_system)
    anti_patterns = [part.strip() for part in normalized["anti_patterns_raw"].split("+") if part.strip()]
    normalized["anti_patterns_list"] = anti_patterns or ANTI_PATTERN_FALLBACK
    normalized["accessibility_rules_list"] = ACCESSIBILITY_RULES
    normalized["responsive_rules_list"] = RESPONSIVE_RULES
    normalized["pattern_steps"] = [
        step.strip()
        for step in str(normalized.get("pattern_sections", "")).replace(">", ",").split(",")
        if step.strip()
    ]

    background = normalized["background"]
    foreground = normalized["foreground"]
    is_dark_theme = _relative_luminance(background) < 0.18

    if is_dark_theme:
        panel_bg = _mix_hex(background, "#FFFFFF", 0.78)
        panel_bg_soft = _mix_hex(background, "#FFFFFF", 0.84)
        panel_fg = _mix_hex(foreground, "#FFFFFF", 0.92)
        panel_muted = _mix_hex(foreground, "#94A3B8", 0.7)
        preview_bg = _mix_hex(background, "#FFFFFF", 0.74)
    else:
        panel_bg = _mix_hex("#FFFFFF", background, 0.92)
        panel_bg_soft = _mix_hex("#FFFFFF", background, 0.86)
        panel_fg = _mix_hex("#0F172A", foreground, 0.88)
        panel_muted = _mix_hex("#475569", foreground, 0.78)
        preview_bg = _mix_hex("#FFFFFF", background, 0.88)

    normalized["panel_bg"] = panel_bg
    normalized["panel_bg_soft"] = panel_bg_soft
    normalized["panel_fg"] = panel_fg
    normalized["panel_muted"] = panel_muted
    normalized["preview_bg"] = preview_bg
    normalized["theme_mode"] = "dark" if is_dark_theme else "light"
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
                    '        <article class="theme-panel rounded-3xl border p-5">',
                    f'          <div class="swatch-chip mb-3 aspect-[16/10] rounded-2xl border" style="background: {_safe(value)};"></div>',
                    f'          <strong class="block text-2xl font-black">{_safe(label)}</strong>',
                    f'          <span class="theme-muted mt-2 block text-sm"><code>{_safe(key)}</code> - {_safe(value)}</span>',
                    "        </article>",
                ]
            )
        )
    return "\n".join(rows)


def _chip_group(values: list[str], fallback: list[str]) -> str:
    items = [value.strip() for value in values if value and value.strip()]
    if not items:
        items = fallback
    return "\n".join(
        f'          <span class="theme-chip inline-flex items-center rounded-full border px-4 py-2 text-sm font-medium">{_safe(item)}</span>'
        for item in items
    )


def _pattern_flow(steps: list[str]) -> str:
    if not steps:
        steps = ["Hero", "Features", "CTA"]
    rows = []
    for index, step in enumerate(steps, 1):
        rows.append(
            "\n".join(
                [
                    '          <div class="flow-step flex items-start gap-3 rounded-2xl border px-3 py-3">',
                    f'            <span class="flow-index inline-flex h-10 w-10 items-center justify-center rounded-xl text-sm font-black">{index:02d}</span>',
                    f'            <div class="pt-2"><strong class="text-base font-bold">{_safe(step)}</strong></div>',
                    '          </div>',
                ]
            )
        )
    return "\n".join(rows)


def _spacing_tokens() -> str:
    values = [
        ("space-1", "4px", 18),
        ("space-2", "8px", 32),
        ("space-3", "16px", 54),
        ("space-4", "24px", 78),
        ("space-5", "40px", 120),
    ]
    return "\n".join(
        "\n".join(
            [
                '          <div class="grid grid-cols-[88px_1fr_60px] items-center gap-3 max-sm:grid-cols-1">',
                f'            <code class="theme-muted">{name}</code>',
                f'            <div class="token-bar h-3 rounded-full" style="width: {width}px;"></div>',
                f'            <span class="text-sm">{size}</span>',
                '          </div>',
            ]
        )
        for name, size, width in values
    )


def _radius_tokens() -> str:
    values = [("radius-sm", "8px"), ("radius-md", "12px"), ("radius-lg", "16px")]
    return "\n".join(
        "\n".join(
            [
                '          <div class="grid grid-cols-[88px_1fr_72px] items-center gap-3 max-sm:grid-cols-1">',
                f'            <code class="theme-muted">{name}</code>',
                f'            <div class="radius-box h-11 rounded-2xl" style="border-radius: {size};"></div>',
                f'            <span class="text-sm">{size}</span>',
                '          </div>',
            ]
        )
        for name, size in values
    )


def _shadow_tokens() -> str:
    values = [
        ("shadow-card", "0 10px 30px rgba(15, 23, 42, 0.10)"),
        ("shadow-popover", "0 18px 48px rgba(15, 23, 42, 0.18)"),
    ]
    return "\n".join(
        "\n".join(
            [
                '          <div class="grid grid-cols-[88px_1fr_72px] items-center gap-3 max-sm:grid-cols-1">',
                f'            <code class="theme-muted">{name}</code>',
                f'            <div class="shadow-box h-[52px] rounded-2xl" style="box-shadow: {shadow};"></div>',
                '            <span class="text-sm">Preview</span>',
                '          </div>',
            ]
        )
        for name, shadow in values
    )


def render_html(design_system: dict) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    normalized = normalize_design_system(design_system)
    styles = DEFAULT_STYLES
    for key, value in normalized.items():
        if key == "anti_patterns_raw":
            continue
        styles = styles.replace(f"{{{{{key}}}}}", str(value))

    replacements = {
        **{k: _safe(v) for k, v in normalized.items() if k != "anti_patterns_raw"},
        "styles": styles.rstrip(),
        "hero_tags": _chip_group(
            [normalized["category"], normalized["style_name"], normalized["heading_font"], normalized["body_font"]],
            ["System", "UI", "Design"],
        ),
        "style_keyword_chips": _chip_group(
            [part.strip() for part in str(design_system.get("style", {}).get("keywords", "")).split(",") if part.strip()],
            ["clear hierarchy", "semantic color", "low-noise surfaces"],
        ),
        "style_best_for": _safe(design_system.get("style", {}).get("best_for", "Digital products that need clarity and direction.")),
        "style_performance": _safe(design_system.get("style", {}).get("performance", "Balanced for production delivery.")),
        "style_accessibility": _safe(design_system.get("style", {}).get("accessibility", "Respect motion and contrast constraints.")),
        "pattern_flow": _pattern_flow(normalized["pattern_steps"]),
        "pattern_conversion": _safe(design_system.get("pattern", {}).get("conversion", "Guide users toward the primary action without clutter.")),
        "pattern_color_strategy": _safe(design_system.get("pattern", {}).get("color_strategy", "Use semantic colors deliberately rather than decoratively.")),
        "color_swatches": _color_swatches(design_system.get("colors", {})),
        "color_notes": _safe(design_system.get("colors", {}).get("notes", "Keep color semantic and intentional across surfaces, text, states, and actions.")),
        "typography_best_for": _safe(design_system.get("typography", {}).get("best_for", "Interfaces that need structured hierarchy and high readability.")),
        "google_fonts_url": _safe(design_system.get("typography", {}).get("google_fonts_url", "https://fonts.google.com/")),
        "spacing_tokens": _spacing_tokens(),
        "radius_tokens": _radius_tokens(),
        "shadow_tokens": _shadow_tokens(),
        "navigation_guidance": _safe("Keep primary navigation stable, make active state obvious, and ensure dense data views stay easy to scan."),
        "accessibility_rules": _list_items(ACCESSIBILITY_RULES, []),
        "responsive_rules": _list_items(RESPONSIVE_RULES, []),
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
