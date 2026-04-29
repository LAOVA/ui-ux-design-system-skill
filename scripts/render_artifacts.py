#!/usr/bin/env python3
r"""
Render final DESIGN.md and design-spec.html directly from a generated bundle.

This keeps the Markdown and HTML artifacts aligned to the same normalized
design-system payload and avoids drift from hand-authored outputs.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))

from build_design_md import render_markdown  # type: ignore  # noqa: E402
from build_app_preview import render_html as render_app_preview_html  # type: ignore  # noqa: E402
from build_design_spec import render_html  # type: ignore  # noqa: E402


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _resolve_run_dir(path_arg: str) -> Path:
    path = Path(path_arg)
    if not path.is_absolute():
        path = Path.cwd() / path
    return path


def _bundle_path(run_dir: Path) -> Path:
    return run_dir / "generation-bundle.json"


def _manifest_path(run_dir: Path) -> Path:
    return run_dir / "manifest.json"


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def render_run(run_dir: Path) -> Path:
    bundle = _load_json(_bundle_path(run_dir))
    manifest = _load_json(_manifest_path(run_dir))
    final_design_system = bundle["final_design_system"]

    design_md_path = run_dir / "DESIGN.md"
    design_spec_path = run_dir / "design-spec.html"
    app_preview_path = run_dir / "app-preview.html"

    _write_text(design_md_path, render_markdown(final_design_system))
    _write_text(design_spec_path, render_html(final_design_system))
    _write_text(app_preview_path, render_app_preview_html(final_design_system))

    outputs = manifest.setdefault("outputs", {})
    outputs["DESIGN.md"] = str(design_md_path)
    outputs["design-spec.html"] = str(design_spec_path)
    outputs["app-preview.html"] = str(app_preview_path)
    manifest["final_output_dir"] = str(run_dir)
    manifest["workflow_stage"] = "final-artifacts-rendered"
    manifest["next_step"] = "Run rendered from generation-bundle.json. Run finalize_manifest.py to verify and mark completion."
    _write_text(_manifest_path(run_dir), json.dumps(manifest, ensure_ascii=False, indent=2))
    return run_dir


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render final DESIGN.md and design-spec.html from an existing generation bundle."
    )
    parser.add_argument(
        "run_dir",
        help="Artifact run directory containing generation-bundle.json and manifest.json",
    )
    args = parser.parse_args()

    run_dir = _resolve_run_dir(args.run_dir)
    render_run(run_dir)
    design_md_path = run_dir / "DESIGN.md"
    design_spec_path = run_dir / "design-spec.html"
    app_preview_path = run_dir / "app-preview.html"
    print(f"Rendered DESIGN.md: {design_md_path}")
    print(f"Rendered design-spec.html: {design_spec_path}")
    print(f"Rendered app-preview.html: {app_preview_path}")
    print(f"Updated manifest: {_manifest_path(run_dir)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
