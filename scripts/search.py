#!/usr/bin/env python3
r"""
Unified entry point for uiux-design-system outputs.

Default behavior:
    Generate both a browsable design-spec HTML artifact and a matching DESIGN.md file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"
DEFAULT_HTML_OUTPUT = ROOT_DIR / "artifacts" / "design-spec.html"
DEFAULT_MD_OUTPUT = ROOT_DIR / "artifacts" / "DESIGN.md"

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from build_design_md import render_markdown  # type: ignore  # noqa: E402
from build_design_spec import render_html  # type: ignore  # noqa: E402
from design_system import DesignSystemGenerator  # type: ignore  # noqa: E402


def _resolve_output_path(output: str | None, default_path: Path) -> Path:
    if not output:
        return default_path
    candidate = Path(output)
    if candidate.is_absolute():
        return candidate
    return Path.cwd() / candidate


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate design-system outputs. Defaults to design-spec HTML."
    )
    parser.add_argument("query", help='Brief such as "AI SaaS dashboard"')
    parser.add_argument("--project-name", "-p", default=None, help="Project name shown in outputs")
    parser.add_argument(
        "--format",
        "-f",
        choices=["all", "html", "markdown", "json"],
        default="all",
        help="Output format. Defaults to all (html + markdown).",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Primary output file path. For default all-mode, this controls the HTML path.",
    )
    args = parser.parse_args()

    generator = DesignSystemGenerator()
    design_system = generator.generate(args.query, args.project_name)

    if args.format == "all":
        html_path = _resolve_output_path(args.output, DEFAULT_HTML_OUTPUT)
        md_path = DEFAULT_MD_OUTPUT
        _write_text(html_path, render_html(design_system))
        _write_text(md_path, render_markdown(design_system))
        print(f"Generated design-spec HTML: {html_path}")
        print(f"Generated DESIGN.md: {md_path}")
        return 0

    if args.format == "html":
        output_path = _resolve_output_path(args.output, DEFAULT_HTML_OUTPUT)
        _write_text(output_path, render_html(design_system))
        print(f"Generated design-spec HTML: {output_path}")
        return 0

    if args.format == "json":
        content = json.dumps(design_system, ensure_ascii=False, indent=2)
        if args.output:
            output_path = _resolve_output_path(
                args.output,
                Path.cwd() / "artifacts" / "design-system.json",
            )
            _write_text(output_path, content)
            print(f"Generated design-system JSON: {output_path}")
            return 0
        print(content)
        return 0

    markdown = render_markdown(design_system)
    if args.output:
        output_path = _resolve_output_path(
            args.output,
            Path.cwd() / "artifacts" / "DESIGN.md",
        )
        _write_text(output_path, markdown)
        print(f"Generated design-system Markdown: {output_path}")
        return 0
    print(markdown)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
