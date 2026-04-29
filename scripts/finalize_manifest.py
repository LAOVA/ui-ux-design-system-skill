#!/usr/bin/env python3
r"""
Finalize a generation run after the LLM has authored final artifacts.

This script verifies that DESIGN.md and design-spec.html exist in the exact
directory recorded by manifest.json.final_output_dir, then updates the manifest
to mark the run as completed.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TEMPLATE_SIGNATURE = "TEMPLATE_SIGNATURE: uiux-design-system/design-spec/v1"


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _require_file(path: Path, label: str) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required {label}: {path}")


def _verify_same_dir(path: Path, expected_dir: Path, label: str) -> None:
    if path.parent.resolve() != expected_dir.resolve():
        raise ValueError(
            f"{label} must be written inside {expected_dir}, but got {path.parent}"
        )


def _verify_html_signature(path: Path) -> None:
    content = path.read_text(encoding="utf-8")
    if TEMPLATE_SIGNATURE not in content:
        raise ValueError(
            f"{path} is not a compliant design-spec artifact because it is missing the required template signature."
        )


def finalize_run(run_dir: Path) -> Path:
    run_dir = run_dir.resolve()
    manifest_path = run_dir / "manifest.json"
    _require_file(manifest_path, "manifest.json")

    manifest = _read_json(manifest_path)
    final_output_dir = Path(manifest.get("final_output_dir") or run_dir).resolve()

    design_md_path = final_output_dir / "DESIGN.md"
    design_spec_path = final_output_dir / "design-spec.html"
    app_preview_path = final_output_dir / "app-preview.html"

    _require_file(design_md_path, "DESIGN.md")
    _require_file(design_spec_path, "design-spec.html")
    _require_file(app_preview_path, "app-preview.html")
    _verify_same_dir(design_md_path, final_output_dir, "DESIGN.md")
    _verify_same_dir(design_spec_path, final_output_dir, "design-spec.html")
    _verify_same_dir(app_preview_path, final_output_dir, "app-preview.html")
    _verify_html_signature(design_spec_path)

    outputs = manifest.get("outputs", {})
    outputs["generation-bundle.json"] = outputs.get("generation-bundle.json", str(run_dir / "generation-bundle.json"))
    outputs["DESIGN.md"] = str(design_md_path)
    outputs["design-spec.html"] = str(design_spec_path)
    outputs["app-preview.html"] = str(app_preview_path)

    manifest["outputs"] = outputs
    manifest["workflow_stage"] = "final-artifacts-authored"
    manifest["next_step"] = "Run completed. Final DESIGN.md, design-spec.html, and app-preview.html were authored in final_output_dir."

    _write_json(manifest_path, manifest)
    return manifest_path


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update manifest.json after final DESIGN.md and design-spec.html are authored."
    )
    parser.add_argument("run_dir", help="Artifacts run directory containing manifest.json")
    args = parser.parse_args()

    manifest_path = finalize_run(Path(args.run_dir))
    print(f"Finalized manifest: {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
