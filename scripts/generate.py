#!/usr/bin/env python3
r"""
Primary generation entry point for uiux-design-system outputs.

Default behavior:
    1. Read reference-style context from awesome-design-md.
    2. Read structured design-system output from ui-ux-pro-max-skill.
    3. Synthesize both into one shared design-system dataset.
    4. Write that shared dataset as an intermediate generation bundle.

Final DESIGN.md and design-spec.html should be created after an LLM reads the
bundle and then renders the final artifacts intentionally.

This script is the recommended top-level command.
"""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"

if str(ROOT_DIR / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR / "scripts"))
if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from finalize_manifest import finalize_run  # type: ignore  # noqa: E402
from reasoning import build_generation_bundle  # type: ignore  # noqa: E402
from render_artifacts import render_run  # type: ignore  # noqa: E402


def _default_run_dir() -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    return ROOT_DIR / "artifacts" / stamp


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


def _write_manifest(run_dir: Path, bundle: dict, files: dict[str, Path]) -> None:
    manifest = {
        "query": bundle.get("query"),
        "project_name": bundle.get("project_name"),
        "run_dir": str(run_dir),
        "final_output_dir": str(run_dir),
        "reference_summary": bundle.get("reference_context", {}).get("reference_summary", ""),
        "structured_query": bundle.get("structured_query"),
        "source_pipeline": bundle.get("final_design_system", {}).get("source_pipeline", {}),
        "workflow_stage": "bundle-generated",
        "next_step": "Use render_artifacts.py on this run directory so DESIGN.md, design-spec.html, and app-preview.html are rendered from generation-bundle.json in the same final_output_dir.",
        "outputs": {name: str(path) for name, path in files.items()},
    }
    _write_text(
        run_dir / "manifest.json",
        json.dumps(manifest, ensure_ascii=False, indent=2),
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Primary generator entry point. Builds the intermediate generation bundle used by the final LLM-authored DESIGN.md and design-spec.html."
    )
    parser.add_argument("query", help='Brief such as "AI SaaS dashboard"')
    parser.add_argument("--project-name", "-p", default=None, help="Project name shown in outputs")
    parser.add_argument(
        "--format",
        "-f",
        choices=["bundle", "design-system-json"],
        default="bundle",
        help="Output format. Defaults to the intermediate generation bundle.",
    )
    parser.add_argument(
        "--output",
        "-o",
        default=None,
        help="Primary output file path.",
    )
    parser.add_argument(
        "--workflow",
        choices=["bundle", "complete"],
        default="complete",
        help="Whether to stop after bundle generation or also render final artifacts. Defaults to complete.",
    )
    args = parser.parse_args()

    bundle = build_generation_bundle(args.query, args.project_name)
    run_dir = _default_run_dir()

    if args.format == "design-system-json":
        output_path = _resolve_output_path(args.output, run_dir / "design-system.json")
        _write_text(
            output_path,
            json.dumps(bundle["final_design_system"], ensure_ascii=False, indent=2),
        )
        _write_manifest(run_dir, bundle, {"design-system.json": output_path})
        print(f"Generated design-system JSON: {output_path}")
        print(f"Generated manifest: {run_dir / 'manifest.json'}")
        return 0

    output_path = _resolve_output_path(args.output, run_dir / "generation-bundle.json")
    _write_text(output_path, json.dumps(bundle, ensure_ascii=False, indent=2))
    _write_manifest(run_dir, bundle, {"generation-bundle.json": output_path})
    print(f"Generated generation bundle: {output_path}")
    print(f"Generated manifest: {run_dir / 'manifest.json'}")
    if args.workflow == "complete":
        render_run(run_dir)
        finalize_run(run_dir)
        print(f"Rendered DESIGN.md: {run_dir / 'DESIGN.md'}")
        print(f"Rendered design-spec.html: {run_dir / 'design-spec.html'}")
        print(f"Rendered app-preview.html: {run_dir / 'app-preview.html'}")
        print(f"Finalized manifest: {run_dir / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
