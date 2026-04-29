#!/usr/bin/env python3
r"""
Build a deterministic app-preview HTML artifact from the synthesized design system.
"""

from __future__ import annotations

import argparse
import html
import sys
from datetime import datetime
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from build_design_spec import normalize_design_system  # type: ignore  # noqa: E402
from reasoning import generate_design_system  # type: ignore  # noqa: E402


def default_output_path(filename: str = "app-preview.html") -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return ROOT_DIR / "artifacts" / stamp / filename


def _safe(value: object, fallback: str = "") -> str:
    return html.escape(str(value or fallback))


def _hero_title(project_name: str) -> str:
    return project_name.replace("-", " ").replace("_", " ")


def render_html(design_system: dict) -> str:
    normalized = normalize_design_system(design_system)
    pattern_steps = normalized.get("pattern_steps", []) or ["Hero", "Projects", "About", "Contact"]
    first_font = normalized["heading_font"]
    second_font = normalized["body_font"]
    colors = design_system.get("colors", {})
    category = normalized["category"]
    style_name = normalized["style_name"]
    summary = normalized["summary"]
    primary = normalized["primary"]
    accent = normalized["accent"]
    background = normalized["background"]
    foreground = normalized["foreground"]
    border = normalized["border"]
    muted = normalized["muted"]
    project_name = normalized["project_name"]
    page_title = _hero_title(project_name)

    chips = "\n".join(
        f'<span class="chip">{_safe(item)}</span>'
        for item in [category, style_name, first_font, second_font]
    )
    project_cards = "\n".join(
        f"""
        <article class="project-card">
          <div class="project-kicker">0{index}</div>
          <h3>{_safe(step)}</h3>
          <p>{_safe(summary)}</p>
        </article>
        """
        for index, step in enumerate(pattern_steps[:3] or ["Project"], 1)
    )
    nav_items = "\n".join(f"<span>{_safe(step)}</span>" for step in pattern_steps[:4])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{_safe(project_name)} App Preview</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    :root {{
      --bg: {background};
      --fg: {foreground};
      --primary: {primary};
      --accent: {accent};
      --border: {border};
      --muted: {muted};
      --panel: color-mix(in srgb, {background} 86%, white 14%);
      --panel-strong: color-mix(in srgb, {background} 78%, white 22%);
      --font-heading: '{_safe(first_font)}', ui-sans-serif, system-ui, sans-serif;
      --font-body: '{_safe(second_font)}', ui-sans-serif, system-ui, sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: var(--font-body);
      background:
        radial-gradient(circle at top left, color-mix(in srgb, var(--accent) 18%, transparent), transparent 32%),
        linear-gradient(180deg, color-mix(in srgb, var(--bg) 92%, black 8%), var(--bg));
      color: var(--fg);
    }}
    h1, h2, h3, strong {{ font-family: var(--font-heading); }}
    .shell {{
      min-height: 100vh;
      padding: 32px;
    }}
    .frame {{
      max-width: 1240px;
      margin: 0 auto;
      border: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      background: color-mix(in srgb, var(--panel) 82%, transparent);
      backdrop-filter: blur(14px);
      border-radius: 28px;
      overflow: hidden;
      box-shadow: 0 28px 80px rgba(0, 0, 0, 0.28);
    }}
    .topbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      padding: 18px 24px;
      border-bottom: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      background: color-mix(in srgb, var(--panel-strong) 88%, transparent);
    }}
    .brand {{
      display: flex;
      gap: 12px;
      align-items: center;
      font-size: 14px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }}
    .brand-mark {{
      width: 12px;
      height: 12px;
      border-radius: 999px;
      background: var(--accent);
      box-shadow: 0 0 24px color-mix(in srgb, var(--accent) 60%, transparent);
    }}
    .topnav {{
      display: flex;
      gap: 18px;
      flex-wrap: wrap;
      color: color-mix(in srgb, var(--fg) 74%, transparent);
      font-size: 13px;
    }}
    .hero {{
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 24px;
      padding: 32px;
    }}
    .hero-copy {{
      padding: 12px 0;
    }}
    .eyebrow {{
      display: inline-flex;
      padding: 8px 12px;
      border-radius: 999px;
      border: 1px solid color-mix(in srgb, var(--border) 65%, transparent);
      color: color-mix(in srgb, var(--fg) 70%, transparent);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.14em;
    }}
    .hero h1 {{
      margin: 18px 0 12px;
      font-size: clamp(3rem, 8vw, 6.2rem);
      line-height: 0.92;
      letter-spacing: -0.05em;
    }}
    .hero p {{
      max-width: 58ch;
      color: color-mix(in srgb, var(--fg) 72%, transparent);
      line-height: 1.7;
      font-size: 16px;
    }}
    .chip-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 20px;
    }}
    .chip {{
      border: 1px solid color-mix(in srgb, var(--border) 65%, transparent);
      background: color-mix(in srgb, var(--panel-strong) 76%, transparent);
      border-radius: 999px;
      padding: 8px 12px;
      font-size: 13px;
    }}
    .actions {{
      display: flex;
      gap: 12px;
      margin-top: 24px;
      flex-wrap: wrap;
    }}
    .button-primary, .button-secondary {{
      padding: 12px 18px;
      border-radius: 14px;
      border: 1px solid color-mix(in srgb, var(--border) 65%, transparent);
      font-weight: 600;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .button-primary {{
      background: var(--primary);
      color: var(--bg);
    }}
    .button-secondary {{
      background: transparent;
      color: var(--fg);
    }}
    .preview-panel {{
      border: 1px solid color-mix(in srgb, var(--border) 65%, transparent);
      border-radius: 24px;
      padding: 18px;
      background: color-mix(in srgb, var(--panel-strong) 82%, transparent);
    }}
    .terminal {{
      border: 1px solid color-mix(in srgb, var(--border) 55%, transparent);
      border-radius: 18px;
      overflow: hidden;
      background: color-mix(in srgb, black 72%, var(--bg));
      min-height: 320px;
    }}
    .terminal-bar {{
      display: flex;
      gap: 8px;
      padding: 12px 14px;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .dot {{
      width: 10px;
      height: 10px;
      border-radius: 999px;
      background: color-mix(in srgb, var(--accent) 75%, white 25%);
    }}
    .terminal-body {{
      padding: 18px;
      font-family: var(--font-heading);
      font-size: 14px;
      line-height: 1.8;
      color: color-mix(in srgb, white 90%, var(--fg) 10%);
    }}
    .terminal-accent {{ color: var(--accent); }}
    .content {{
      display: grid;
      grid-template-columns: 280px 1fr;
      gap: 0;
      border-top: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
    }}
    .sidebar {{
      padding: 24px;
      border-right: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      background: color-mix(in srgb, var(--panel-strong) 88%, transparent);
    }}
    .sidebar h2 {{
      margin: 0 0 14px;
      font-size: 18px;
    }}
    .sidebar-list {{
      display: grid;
      gap: 10px;
      color: color-mix(in srgb, var(--fg) 74%, transparent);
      font-size: 14px;
    }}
    .workspace {{
      padding: 24px;
    }}
    .stats {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
    }}
    .stat-card, .project-card {{
      border: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      background: color-mix(in srgb, var(--panel) 88%, transparent);
      border-radius: 18px;
      padding: 18px;
    }}
    .stat-card strong {{
      display: block;
      font-size: 30px;
      margin-top: 10px;
    }}
    .projects {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 14px;
      margin-top: 18px;
    }}
    .project-kicker {{
      color: var(--accent);
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.16em;
    }}
    .project-card h3 {{
      margin: 14px 0 8px;
      font-size: 22px;
    }}
    .project-card p {{
      margin: 0;
      color: color-mix(in srgb, var(--fg) 72%, transparent);
      line-height: 1.65;
      font-size: 14px;
    }}
    @media (max-width: 980px) {{
      .hero, .content {{
        grid-template-columns: 1fr;
      }}
      .sidebar {{
        border-right: none;
        border-bottom: 1px solid color-mix(in srgb, var(--border) 70%, transparent);
      }}
      .projects, .stats {{
        grid-template-columns: 1fr;
      }}
    }}
  </style>
</head>
<body>
  <div class="shell">
    <div class="frame">
      <header class="topbar">
        <div class="brand">
          <span class="brand-mark"></span>
          <strong>{_safe(project_name)}</strong>
        </div>
        <nav class="topnav">{nav_items}</nav>
      </header>

      <section class="hero">
        <div class="hero-copy">
          <span class="eyebrow">App Preview</span>
          <h1>{_safe(page_title)}</h1>
          <p>{_safe(summary)}</p>
          <div class="chip-row">{chips}</div>
          <div class="actions">
            <a class="button-primary" href="#">Open Projects</a>
            <a class="button-secondary" href="#">Read Notes</a>
          </div>
        </div>

        <div class="preview-panel">
          <div class="terminal">
            <div class="terminal-bar">
              <span class="dot"></span>
              <span class="dot"></span>
              <span class="dot"></span>
            </div>
            <div class="terminal-body">
              <div><span class="terminal-accent">$</span> whoami</div>
              <div>designer-engineer / systems thinker / builder</div>
              <div><span class="terminal-accent">$</span> ls ./featured-work</div>
              <div>01_{_safe(pattern_steps[0] if pattern_steps else "hero")}.tsx</div>
              <div>02_{_safe(pattern_steps[1] if len(pattern_steps) > 1 else "projects")}.md</div>
              <div>03_{_safe(pattern_steps[2] if len(pattern_steps) > 2 else "about")}.json</div>
            </div>
          </div>
        </div>
      </section>

      <section class="content">
        <aside class="sidebar">
          <h2>Navigation</h2>
          <div class="sidebar-list">
            <span>~/overview</span>
            <span>~/projects</span>
            <span>~/writing</span>
            <span>~/contact</span>
          </div>
        </aside>

        <div class="workspace">
          <div class="stats">
            <article class="stat-card">
              <span>Repos</span>
              <strong>42</strong>
            </article>
            <article class="stat-card">
              <span>Systems</span>
              <strong>12</strong>
            </article>
            <article class="stat-card">
              <span>Years</span>
              <strong>8+</strong>
            </article>
          </div>

          <div class="projects">
            {project_cards}
          </div>
        </div>
      </section>
    </div>
  </div>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Build an app-preview HTML artifact.")
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

    print(f"Generated app-preview HTML: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
