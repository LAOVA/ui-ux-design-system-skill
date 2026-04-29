#!/usr/bin/env python3
r"""
Build a browsable design-spec HTML file from the existing UI/UX Pro Max
design-system generator.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import html
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"
TEMPLATE_PATH = ROOT_DIR / "templates" / "design-spec.html"

if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from reasoning import generate_design_system  # type: ignore  # noqa: E402


def default_output_path(filename: str = "design-spec.html") -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return ROOT_DIR / "artifacts" / stamp / filename


REQUIRED_TEMPLATE_MARKERS = [
    "TEMPLATE_SIGNATURE: uiux-design-system/design-spec/v1",
    "<!-- Required spec sections begin -->",
    "<!-- Required spec sections end -->",
    "System Snapshot",
    "Visual Direction",
    "Flow and Layout",
    "Color Palette",
    "Typography",
    "Tokens",
    "Component Gallery",
    "Rules and Risks",
]


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
      --shadow-card: {{shadow_card}};
      --shadow-popover: {{shadow_popover}};
      --font-heading: {{heading_font_css}};
      --font-body: {{body_font_css}};
      --interactive-primary: {{primary}};
      --interactive-on-primary: {{on_primary}};
      --interactive-primary-shadow: {{interactive_primary_shadow}};
      --interactive-secondary-fg: {{interactive_secondary_fg}};
      --page-accent-wash: {{page_accent_wash}};
      --page-accent-glow: {{page_accent_glow}};
      --page-grid-line: {{page_grid_line}};
      --panel-radius: {{panel_radius}};
      --chip-radius: {{chip_radius}};
      --button-radius: {{button_radius}};
      --panel-border-width: {{panel_border_width}};
      --panel-shadow: {{panel_shadow}};
      --panel-soft-shadow: {{panel_soft_shadow}};
      --heading-case: {{heading_case}};
      --heading-spacing: {{heading_spacing}};
      --body-spacing: {{body_spacing}};
      --heading-style: {{heading_style}};
      --heading-weight: {{heading_weight}};
      --panel-backdrop: {{panel_backdrop}};
      --surface_noise: {{surface_noise}};
      --nav-active-accent: {{nav_active_accent}};
      --nav-active-shadow: {{nav_active_shadow}};
      --nav-item-radius: {{nav_item_radius}};
      --panel_gradient: {{panel_gradient}};
      --soft_panel_gradient: {{soft_panel_gradient}};
      --hero_kicker_color: {{hero_kicker_color}};
      --tag_bg: {{tag_bg}};
      --tag_fg: {{tag_fg}};
      --tag_border: {{tag_border}};
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: var(--font-body);
      background:
        var(--surface_noise),
        linear-gradient(180deg, color-mix(in srgb, var(--page-bg) 96%, black 4%), var(--page-bg)),
        radial-gradient(circle at top left, var(--page-accent-wash), transparent 34%),
        radial-gradient(circle at top right, var(--page-accent-glow), transparent 30%);
      color: var(--page-fg);
      transition: background 180ms ease, color 180ms ease;
      letter-spacing: var(--body-spacing);
    }
    body::before {
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      background-image:
        linear-gradient(var(--page-grid-line, transparent) 1px, transparent 1px),
        linear-gradient(90deg, var(--page-grid-line, transparent) 1px, transparent 1px);
      background-size: 28px 28px;
      opacity: 0.28;
      mask-image: linear-gradient(180deg, rgba(0,0,0,0.28), transparent 48%);
    }
    h1, h2, h3, h4, strong { font-family: var(--font-heading); }
    h1, h2, h3, h4 {
      letter-spacing: var(--heading-spacing);
      text-transform: var(--heading-case);
      font-style: var(--heading-style);
      font-weight: var(--heading-weight);
    }
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
    .theme-button-primary:hover,
    .theme-button-secondary:hover {
      transform: translateY(-1px);
    }
    .theme-panel {
      background: var(--panel_gradient);
      border-color: var(--surface-border);
      border-width: var(--panel-border-width);
      color: var(--panel-fg);
      box-shadow: var(--panel-shadow);
      border-radius: var(--panel-radius) !important;
      backdrop-filter: var(--panel-backdrop);
    }
    .theme-soft {
      background: var(--soft_panel_gradient);
      border-color: color-mix(in srgb, var(--surface-border) 76%, white 24%);
      color: var(--panel-fg);
      box-shadow: var(--panel-soft-shadow);
    }
    .theme-muted { color: var(--panel-muted); }
    .theme-chip {
      background: color-mix(in srgb, var(--panel-bg-soft) 92%, white 8%);
      border-color: var(--surface-border);
      color: var(--panel-fg);
      box-shadow: var(--shadow-card);
      border-radius: var(--chip-radius) !important;
    }
    .theme-tag {
      background: var(--tag_bg);
      color: var(--tag_fg);
      border: 1px solid var(--tag_border);
    }
    .theme-button-primary {
      background: var(--interactive-primary);
      color: var(--interactive-on-primary);
      box-shadow: 0 10px 24px var(--interactive-primary-shadow);
      transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
      border-radius: var(--button-radius) !important;
    }
    .theme-button-secondary {
      background: transparent;
      color: var(--interactive-secondary-fg);
      border: 1px solid color-mix(in srgb, var(--interactive-primary) 25%, var(--surface-border));
      transition: transform 160ms ease, box-shadow 160ms ease, background 160ms ease;
      border-radius: var(--button-radius) !important;
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
      box-shadow: var(--nav-active-shadow);
    }
    .theme-nav-item {
      border-radius: var(--nav-item-radius) !important;
      transition: transform 160ms ease, border-color 160ms ease, background 160ms ease, box-shadow 160ms ease;
    }
    .theme-nav-item:hover {
      transform: translateX(2px);
      border-color: color-mix(in srgb, var(--nav-active-accent) 40%, var(--surface-border));
    }
    .theme-status-positive {
      background: color-mix(in srgb, var(--accent) 18%, white);
      color: var(--accent);
    }
    .theme-status-neutral {
      background: color-mix(in srgb, var(--secondary) 18%, white);
      color: var(--secondary);
    }
    .theme-input,
    .theme-nav-item,
    .theme-table {
      --preview-surface: var(--panel-bg-soft);
      --preview-surface-strong: var(--preview-bg);
      --preview-border: color-mix(in srgb, var(--surface-border) 65%, white 35%);
      --preview-fg: var(--panel-fg);
      --preview-muted: var(--panel-muted);
    }
    .theme-kicker { color: var(--hero_kicker_color); }
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

COMPONENT_SPEC_ROWS = [
    ("Primary Button", "Action", "Solid emphasis for the primary decision on a surface.", "Default, hover, focus, pressed"),
    ("Secondary Button", "Action", "Lower-emphasis path for alternate actions and escape hatches.", "Default, hover, focus"),
    ("Card", "Container", "Groups related content with clear boundary and stable hierarchy.", "Default, hover"),
    ("Input", "Form", "Accepts user data with strong legibility and visible feedback.", "Default, focus, error, disabled"),
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


def _style_profile(style_name: str, keywords: str, effects: str, heading_font: str) -> dict[str, str]:
    style_text = " ".join([style_name, keywords, effects, heading_font]).lower()
    profile = {
        "page_accent_wash": "color-mix(in srgb, var(--accent) 10%, transparent)",
        "page_accent_glow": "color-mix(in srgb, var(--primary) 8%, transparent)",
        "page_grid_line": "transparent",
        "panel_radius": "32px",
        "chip_radius": "999px",
        "button_radius": "18px",
        "panel_border_width": "1px",
        "panel_shadow": "0 16px 42px rgba(15, 23, 42, 0.08)",
        "panel_soft_shadow": "0 10px 24px rgba(15, 23, 42, 0.05)",
        "heading_case": "none",
        "heading_spacing": "-0.04em",
        "body_spacing": "0",
        "heading_style": "normal",
        "heading_weight": "800",
        "panel_backdrop": "none",
        "surface_noise": "none",
        "nav_active_accent": "var(--accent)",
        "nav_active_shadow": "0 10px 24px color-mix(in srgb, var(--accent) 20%, transparent)",
        "nav_item_radius": "20px",
        "panel_gradient": "linear-gradient(180deg, var(--panel-bg), var(--panel-bg))",
        "soft_panel_gradient": "linear-gradient(180deg, var(--panel-bg-soft), var(--panel-bg-soft))",
        "hero_kicker_color": "var(--panel-muted)",
        "tag_bg": "color-mix(in srgb, var(--accent) 15%, white)",
        "tag_fg": "var(--accent)",
        "tag_border": "color-mix(in srgb, var(--accent) 25%, transparent)",
    }

    if any(token in style_text for token in ["glass", "gloss", "frosted"]):
        profile.update({
            "panel_backdrop": "blur(18px)",
            "panel_shadow": "0 18px 48px rgba(15, 23, 42, 0.12)",
            "panel_soft_shadow": "0 12px 28px rgba(15, 23, 42, 0.08)",
            "page_accent_wash": "color-mix(in srgb, var(--accent) 16%, transparent)",
            "page_accent_glow": "color-mix(in srgb, white 18%, transparent)",
        })

    if any(token in style_text for token in ["geek", "terminal", "mono", "code", "cyber", "developer"]):
        profile.update({
            "page_grid_line": "color-mix(in srgb, var(--accent) 10%, transparent)",
            "panel_radius": "24px",
            "chip_radius": "14px",
            "button_radius": "14px",
            "panel_border_width": "1.5px",
            "panel_shadow": "0 18px 44px rgba(2, 6, 23, 0.18)",
            "panel_soft_shadow": "0 10px 24px rgba(2, 6, 23, 0.10)",
            "heading_case": "uppercase",
            "heading_spacing": "-0.03em",
            "body_spacing": "0.01em",
            "heading_weight": "700",
            "surface_noise": "linear-gradient(180deg, color-mix(in srgb, var(--accent) 4%, transparent), transparent)",
            "nav_item_radius": "12px",
            "panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg) 94%, black 6%), var(--panel-bg))",
            "soft_panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg-soft) 90%, black 10%), var(--panel-bg-soft))",
            "hero_kicker_color": "var(--accent)",
        })

    if any(token in style_text for token in ["editorial", "luxury", "cinematic", "serif"]):
        profile.update({
            "panel_radius": "20px",
            "chip_radius": "999px",
            "button_radius": "999px",
            "panel_shadow": "0 20px 54px rgba(15, 23, 42, 0.10)",
            "heading_spacing": "-0.05em",
            "body_spacing": "0.005em",
            "page_accent_wash": "color-mix(in srgb, var(--accent) 8%, transparent)",
            "page_accent_glow": "color-mix(in srgb, #ffffff 10%, transparent)",
            "heading_weight": "600",
            "panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg) 88%, white 12%), var(--panel-bg))",
            "soft_panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg-soft) 84%, white 16%), var(--panel-bg-soft))",
        })

    if any(token in style_text for token in ["block", "brutal", "grid", "industrial"]):
        profile.update({
            "panel_radius": "18px",
            "chip_radius": "12px",
            "button_radius": "12px",
            "panel_border_width": "2px",
            "panel_shadow": "0 10px 0 rgba(15, 23, 42, 0.16)",
            "panel_soft_shadow": "0 6px 0 rgba(15, 23, 42, 0.10)",
            "heading_spacing": "-0.03em",
            "nav_item_radius": "10px",
        })

    if any(token in style_text for token in ["ferrari", "bmw", "bugatti", "automotive", "motorsport", "racing"]):
        profile.update({
            "page_accent_wash": "color-mix(in srgb, var(--primary) 18%, transparent)",
            "page_accent_glow": "color-mix(in srgb, #7a0f06 24%, transparent)",
            "page_grid_line": "color-mix(in srgb, var(--primary) 6%, transparent)",
            "panel_radius": "18px",
            "chip_radius": "999px",
            "button_radius": "10px",
            "panel_border_width": "1px",
            "panel_shadow": "0 18px 40px rgba(0, 0, 0, 0.34)",
            "panel_soft_shadow": "0 10px 22px rgba(0, 0, 0, 0.24)",
            "heading_case": "uppercase",
            "heading_spacing": "-0.035em",
            "heading_style": "italic",
            "heading_weight": "700",
            "body_spacing": "0.01em",
            "surface_noise": "linear-gradient(90deg, color-mix(in srgb, var(--primary) 4%, transparent), transparent 42%)",
            "nav_active_accent": "var(--primary)",
            "nav_active_shadow": "inset 3px 0 0 var(--primary)",
            "nav_item_radius": "10px",
            "panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg) 94%, black 6%), color-mix(in srgb, var(--panel-bg) 88%, #2a0c09 12%))",
            "soft_panel_gradient": "linear-gradient(180deg, color-mix(in srgb, var(--panel-bg-soft) 94%, black 6%), color-mix(in srgb, var(--panel-bg-soft) 88%, #2a0c09 12%))",
            "hero_kicker_color": "color-mix(in srgb, var(--primary) 70%, white 30%)",
            "tag_bg": "color-mix(in srgb, var(--primary) 14%, transparent)",
            "tag_fg": "color-mix(in srgb, white 92%, var(--primary) 8%)",
            "tag_border": "color-mix(in srgb, var(--primary) 35%, transparent)",
        })

    return profile


def _normalize(design_system: dict) -> dict:
    colors = design_system.get("colors", {})
    style = design_system.get("style", {})
    pattern = design_system.get("pattern", {})
    typography = design_system.get("typography", {})
    style_keywords = str(style.get("keywords", ""))
    style_effects = str(style.get("effects", ""))
    heading_font = typography.get("heading", "Inter")
    profile = _style_profile(str(style.get("name", "Minimalism")), style_keywords, style_effects, str(heading_font))

    def color_value(key: str, fallback: str) -> str:
        value = colors.get(key)
        text = str(value or "").strip()
        return text or fallback

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
        "background": color_value("background", "#F8FAFC"),
        "foreground": color_value("foreground", "#0F172A"),
        "card": color_value("card", "#FFFFFF"),
        "border": color_value("border", "#E2E8F0"),
        "primary": color_value("primary", "#2563EB"),
        "secondary": color_value("secondary", "#3B82F6"),
        "accent": color_value("accent", "#F97316"),
        "muted": color_value("muted", "#E2E8F0"),
        "muted_foreground": color_value("muted_foreground", color_value("foreground", "#475569")),
        "on_primary": color_value("on_primary", "#FFFFFF"),
        "heading_font_css": _font_css(typography.get("heading", "Inter"), "ui-sans-serif, system-ui, sans-serif"),
        "body_font_css": _font_css(typography.get("body", "Inter"), "ui-sans-serif, system-ui, sans-serif"),
        "anti_patterns_raw": design_system.get("anti_patterns", ""),
        "reference_summary": design_system.get("reference_summary", ""),
        "reference_direction": design_system.get("reference_direction", ""),
        **profile,
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
        panel_bg = _mix_hex(background, "#FFFFFF", 0.88)
        panel_bg_soft = _mix_hex(background, "#FFFFFF", 0.92)
        panel_fg = _mix_hex(foreground, "#FFFFFF", 0.96)
        panel_muted = _mix_hex(foreground, "#94A3B8", 0.78)
        preview_bg = _mix_hex(background, "#FFFFFF", 0.86)
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
    normalized["shadow_card"] = "0 18px 40px rgba(0, 0, 0, 0.22)" if is_dark_theme else "0 10px 30px rgba(15, 23, 42, 0.10)"
    normalized["shadow_popover"] = "0 22px 56px rgba(0, 0, 0, 0.34)" if is_dark_theme else "0 18px 48px rgba(15, 23, 42, 0.18)"
    normalized["interactive_primary_shadow"] = f"color-mix(in srgb, {normalized['primary']} 28%, transparent)" if is_dark_theme else f"color-mix(in srgb, {normalized['primary']} 22%, transparent)"
    normalized["interactive_secondary_fg"] = _mix_hex(normalized["foreground"], normalized["primary"], 0.4) if is_dark_theme else normalized["primary"]
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


def _token_table_rows(values: list[tuple[str, str, str]]) -> str:
    return "\n".join(
        "\n".join(
            [
                '<div class="token-table-row grid grid-cols-[120px_110px_minmax(0,1fr)] gap-3 border-b px-4 py-3 text-sm max-sm:grid-cols-1">',
                f'  <code class="font-semibold">{_safe(name)}</code>',
                f'  <span class="theme-muted">{_safe(value)}</span>',
                f'  <span class="theme-muted">{_safe(note)}</span>',
                '</div>',
            ]
        )
        for name, value, note in values
    )


def _color_role_table(colors: dict) -> str:
    rows = []
    role_notes = {
        "primary": "Main action and highest-emphasis interactive color.",
        "secondary": "Secondary action, support surfaces, or quieter emphasis.",
        "accent": "Highlight, status emphasis, or editorial punch color.",
        "background": "Page canvas and primary app backdrop.",
        "foreground": "Primary text and high-contrast content color.",
        "muted": "Low-contrast surfaces or secondary UI backplates.",
        "border": "Hairlines, separators, and neutral edge definition.",
        "destructive": "Error, destructive action, or risk state.",
    }
    for key, label in COLOR_KEYS:
        value = colors.get(key)
        if value:
            rows.append((label, str(value), role_notes.get(key, "Semantic design token.")))
    return _token_table_rows(rows)


def _typography_scale_rows(normalized: dict) -> str:
    values = [
        ("Display", normalized["heading_font"], "Large-format system headlines and hero moments."),
        ("Heading", normalized["heading_font"], "Section titles and content hierarchy anchors."),
        ("Body", normalized["body_font"], "Primary reading text, paragraphs, and longer labels."),
        ("UI Label", normalized["body_font"], "Controls, meta labels, small annotations, and captions."),
    ]
    return _token_table_rows(values)


def _component_spec_rows() -> str:
    return "\n".join(
        "\n".join(
            [
                '<div class="token-table-row grid grid-cols-[140px_100px_1fr_180px] gap-3 border-b px-4 py-3 text-sm max-xl:grid-cols-1">',
                f'  <strong>{_safe(name)}</strong>',
                f'  <span class="theme-muted">{_safe(group)}</span>',
                f'  <span class="theme-muted">{_safe(role)}</span>',
                f'  <span class="theme-muted">{_safe(states)}</span>',
                '</div>',
            ]
        )
        for name, group, role, states in COMPONENT_SPEC_ROWS
    )


def _implementation_checks() -> str:
    items = [
        "Map all UI surfaces to semantic tokens before implementation begins.",
        "Keep component variants constrained and name them before coding one-off exceptions.",
        "Review contrast, focus visibility, and spacing density before shipping.",
        "Validate responsive collapse order on mobile, tablet, and desktop breakpoints.",
    ]
    return _list_items(items, [])


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
            [normalized["category"], normalized["style_name"], normalized["reference_summary"], normalized["heading_font"], normalized["body_font"]],
            ["System", "UI", "Design"],
        ),
        "style_keyword_chips": _chip_group(
            [part.strip() for part in str(design_system.get("style", {}).get("keywords", "")).split(",") if part.strip()],
            ["clear hierarchy", "semantic color", "low-noise surfaces"],
        ),
        "style_best_for": _safe(
            design_system.get("reference_direction")
            or design_system.get("style", {}).get("best_for", "Digital products that need clarity and direction.")
        ),
        "style_performance": _safe(design_system.get("style", {}).get("performance", "Balanced for production delivery.")),
        "style_accessibility": _safe(design_system.get("style", {}).get("accessibility", "Respect motion and contrast constraints.")),
        "pattern_flow": _pattern_flow(normalized["pattern_steps"]),
        "pattern_conversion": _safe(design_system.get("pattern", {}).get("conversion", "Guide users toward the primary action without clutter.")),
        "pattern_color_strategy": _safe(design_system.get("pattern", {}).get("color_strategy", "Use semantic colors deliberately rather than decoratively.")),
        "color_swatches": _color_swatches(design_system.get("colors", {})),
        "color_role_rows": _color_role_table(design_system.get("colors", {})),
        "color_notes": _safe(design_system.get("colors", {}).get("notes", "Keep color semantic and intentional across surfaces, text, states, and actions.")),
        "typography_best_for": _safe(design_system.get("typography", {}).get("best_for", "Interfaces that need structured hierarchy and high readability.")),
        "typography_scale_rows": _typography_scale_rows(normalized),
        "google_fonts_url": _safe(design_system.get("typography", {}).get("google_fonts_url", "https://fonts.google.com/")),
        "spacing_tokens": _spacing_tokens(),
        "radius_tokens": _radius_tokens(),
        "shadow_tokens": _shadow_tokens(),
        "component_spec_rows": _component_spec_rows(),
        "implementation_checks": _implementation_checks(),
        "navigation_guidance": _safe("Keep primary navigation stable, make active state obvious, and ensure dense data views stay easy to scan."),
        "accessibility_rules": _list_items(ACCESSIBILITY_RULES, []),
        "responsive_rules": _list_items(RESPONSIVE_RULES, []),
        "anti_patterns": _anti_pattern_items(normalized["anti_patterns_raw"]),
    }

    output = template
    for key, value in replacements.items():
        output = output.replace(f"{{{{{key}}}}}", value)
    _validate_rendered_html(output)
    return output


def _validate_rendered_html(output: str) -> None:
    missing = [marker for marker in REQUIRED_TEMPLATE_MARKERS if marker not in output]
    if missing:
        raise ValueError(
            "Rendered design-spec.html is missing required template markers: "
            + ", ".join(missing)
        )
    if "{{" in output or "}}" in output:
        raise ValueError("Rendered design-spec.html still contains unreplaced template placeholders.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a design-spec HTML artifact.")
    parser.add_argument("query", help='Brief such as "AI SaaS dashboard"')
    parser.add_argument("--project-name", "-p", default=None, help="Project name shown in the output")
    parser.add_argument("--output", "-o", default=None, help="Output HTML path")
    args = parser.parse_args()

    design_system = generate_design_system(args.query, args.project_name)

    output_path = default_output_path() if not args.output else Path(args.output)
    if not output_path.is_absolute():
        output_path = Path.cwd() / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(render_html(design_system), encoding="utf-8")

    print(f"Generated design-spec HTML: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
