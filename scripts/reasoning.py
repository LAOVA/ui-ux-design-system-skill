#!/usr/bin/env python3
r"""
Reference-and-rules reasoning layer for uiux-design-system.

Workflow:
1. Read reference-style candidates from awesome-design-md.
2. Read structured design-system output from ui-ux-pro-max-skill.
3. Synthesize both into one final design-system object.
4. Hand that single object to downstream renderers.
"""

from __future__ import annotations

import copy
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except Exception:  # pragma: no cover - fallback when PyYAML is unavailable
    yaml = None


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"
REFERENCE_README = ROOT_DIR / "awesome-design-md" / "README.md"
REFERENCE_DETAIL_ROOT = ROOT_DIR / "awesome-design-md" / "design-md"

if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from design_system import DesignSystemGenerator  # type: ignore  # noqa: E402


REFERENCE_LINE_RE = re.compile(r"- \[\*\*(?P<name>.+?)\*\*\]\(.+?\) - (?P<summary>.+)")
HEX_COLOR_RE = re.compile(r"#[0-9A-Fa-f]{6}")
REDIRECT_RE = re.compile(r"details have been moved to:\s*(?P<url>https?://\S+)", re.IGNORECASE)


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9\.\-\+]+", text.lower())


def _parse_design_md_frontmatter(content: str) -> dict:
    if not content or yaml is None:
        return {}
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    try:
        end_index = lines[1:].index("---") + 1
    except ValueError:
        return {}
    frontmatter = "\n".join(lines[1:end_index])
    try:
        payload = yaml.safe_load(frontmatter) or {}
    except Exception:
        return {}
    return payload if isinstance(payload, dict) else {}


def _extract_font_name(font_value: object) -> str:
    text = str(font_value or "").strip()
    if not text:
        return ""
    match = re.search(r"'([^']+)'", text)
    if match:
        return match.group(1).strip()
    first = text.split(",")[0].strip().strip('"').strip("'")
    return first


def _is_bmw_m_variant(query: str) -> bool:
    lowered = query.lower()
    return any(
        term in lowered
        for term in ["bmw-m", "bmw m", "motorsport", "m style", "m-performance", "m performance"]
    )


def _apply_reference_overrides(design_system: dict, reference_context: dict, query: str) -> dict:
    design_md = reference_context.get("_primary_reference_design_md", "")
    frontmatter = _parse_design_md_frontmatter(design_md)
    if not frontmatter:
        return design_system

    colors = frontmatter.get("colors", {}) or {}
    typography = frontmatter.get("typography", {}) or {}
    is_bmw_m = _is_bmw_m_variant(query)

    def token(*keys: str) -> str:
        for key in keys:
            value = colors.get(key)
            if value:
                return str(value)
        return ""

    overrides_applied: list[str] = []
    ds_colors = design_system.setdefault("colors", {})
    ds_type = design_system.setdefault("typography", {})

    primary = token("primary")
    secondary = token("m-blue-light", "primary-active", "secondary")
    accent = token("m-red", "accent", "primary-active")
    background = token("surface-dark", "canvas") if is_bmw_m else token("canvas", "surface-soft")
    foreground = token("on-dark", "ink", "body-strong") if is_bmw_m else token("ink", "body-strong", "body")
    muted = token("surface-dark-elevated", "muted") if is_bmw_m else token("surface-soft", "muted")
    border = token("hairline", "hairline-strong")
    on_primary = token("on-primary", "on-dark")
    destructive = token("error")

    if is_bmw_m and token("m-blue-dark"):
        primary = token("m-blue-dark")

    color_map = {
        "primary": primary,
        "secondary": secondary,
        "accent": accent,
        "background": background,
        "foreground": foreground,
        "muted": muted,
        "border": border,
        "on_primary": on_primary,
        "destructive": destructive,
    }
    for key, value in color_map.items():
        if value:
            ds_colors[key] = value
            overrides_applied.append(f"colors.{key}")

    heading_font = _extract_font_name(
        (typography.get("display-xl") or {}).get("fontFamily")
        or (typography.get("display-lg") or {}).get("fontFamily")
    )
    body_font = _extract_font_name(
        (typography.get("body-md") or {}).get("fontFamily")
        or (typography.get("body-sm") or {}).get("fontFamily")
    )
    if heading_font:
        ds_type["heading"] = heading_font
        overrides_applied.append("typography.heading")
    if body_font:
        ds_type["body"] = body_font
        overrides_applied.append("typography.body")

    if frontmatter.get("description"):
        ds_type["mood"] = str(frontmatter["description"])
        overrides_applied.append("typography.mood")

    if "forum" in query.lower() and design_system.get("reference_summary", "").startswith("BMW"):
        design_system["category"] = "Automotive Community / Forum"
        overrides_applied.append("category")

    if ds_colors:
        ds_colors["notes"] = f"Reference-constrained palette from {frontmatter.get('name', 'brand')} DESIGN.md"
        overrides_applied.append("colors.notes")

    design_system["reference_overrides_applied"] = overrides_applied
    return design_system


def load_reference_catalog() -> list[dict]:
    if not REFERENCE_README.exists():
        return []

    catalog: list[dict] = []
    current_group = "General"
    for raw_line in REFERENCE_README.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("### "):
            current_group = line.replace("### ", "", 1).strip()
            continue

        match = REFERENCE_LINE_RE.match(line)
        if not match:
            continue

        name = match.group("name").strip()
        summary = match.group("summary").strip()
        slug = name.lower().replace(" ", "-")
        keywords = _tokenize(f"{name} {current_group} {summary}")
        catalog.append(
            {
                "name": name,
                "slug": slug,
                "group": current_group,
                "summary": summary,
                "keywords": keywords,
            }
        )
    return catalog


def _slug_variants(name: str, slug: str) -> list[str]:
    variants = {
        slug.lower(),
        name.lower().replace(" ", "-"),
        name.lower().replace(" ", ""),
        name.lower(),
    }
    return [item for item in variants if item]


def _resolve_reference_detail_path(name: str, slug: str) -> Path | None:
    if not REFERENCE_DETAIL_ROOT.exists():
        return None

    entries = [entry for entry in REFERENCE_DETAIL_ROOT.iterdir() if entry.is_dir()]
    entry_map = {entry.name.lower(): entry for entry in entries}
    for variant in _slug_variants(name, slug):
        if variant in entry_map:
            candidate = entry_map[variant] / "README.md"
            if candidate.exists():
                return candidate
    return None


def load_reference_detail(name: str, slug: str) -> dict:
    detail_path = _resolve_reference_detail_path(name, slug)
    if not detail_path:
        return {
            "status": "missing-local-detail",
            "path": None,
            "redirect_url": None,
            "hex_colors": [],
            "excerpt": "",
        }

    content = detail_path.read_text(encoding="utf-8")
    redirect_match = REDIRECT_RE.search(content)
    hex_colors = list(dict.fromkeys(HEX_COLOR_RE.findall(content)))
    non_empty_lines = [line.strip() for line in content.splitlines() if line.strip()]
    excerpt = " ".join(non_empty_lines[:6])[:400]

    if redirect_match and len(non_empty_lines) <= 4 and not hex_colors:
        return {
            "status": "redirect-only-local-detail",
            "path": str(detail_path),
            "redirect_url": redirect_match.group("url"),
            "hex_colors": [],
            "excerpt": excerpt,
        }

    return {
        "status": "local-detail-available",
        "path": str(detail_path),
        "redirect_url": redirect_match.group("url") if redirect_match else None,
        "hex_colors": hex_colors[:12],
        "excerpt": excerpt,
    }


def load_remote_reference_detail(name: str, slug: str) -> dict:
    with tempfile.TemporaryDirectory(prefix=f"getdesign-{slug}-") as tmp_dir:
        tmp_path = Path(tmp_dir)
        out_path = tmp_path / "DESIGN.md"
        npx_executable = shutil.which("npx") or shutil.which("npx.cmd")
        if sys.platform.startswith("win"):
            if npx_executable:
                cmd = [
                    npx_executable,
                    "--yes",
                    "getdesign@latest",
                    "add",
                    slug,
                    "--out",
                    str(out_path),
                ]
            else:
                cmd = [
                    "cmd",
                    "/c",
                    "npx",
                    "--yes",
                    "getdesign@latest",
                    "add",
                    slug,
                    "--out",
                    str(out_path),
                ]
        else:
            cmd = [
                npx_executable or "npx",
                "--yes",
                "getdesign@latest",
                "add",
                slug,
                "--out",
                str(out_path),
            ]
        try:
            result = subprocess.run(
                cmd,
                cwd=tmp_path,
                capture_output=True,
                text=True,
                encoding="utf-8",
                timeout=120,
                check=False,
            )
        except Exception as exc:
            return {
                "status": "remote-fetch-error",
                "source": "getdesign-cli",
                "design_md": "",
                "hex_colors": [],
                "excerpt": "",
                "error": str(exc),
            }

        if result.returncode != 0 or not out_path.exists():
            return {
                "status": "remote-fetch-failed",
                "source": "getdesign-cli",
                "design_md": "",
                "hex_colors": [],
                "excerpt": "",
                "error": (result.stderr or result.stdout).strip(),
            }

        content = out_path.read_text(encoding="utf-8")
        hex_colors = list(dict.fromkeys(HEX_COLOR_RE.findall(content)))
        lines = [line.strip() for line in content.splitlines() if line.strip()]
        excerpt = " ".join(lines[:12])[:700]
        return {
            "status": "remote-detail-available",
            "source": "getdesign-cli",
            "design_md": content,
            "hex_colors": hex_colors[:24],
            "excerpt": excerpt,
            "error": "",
        }


def _summarize_reference(ref: dict) -> dict:
    local_detail = ref.get("local_detail", {})
    remote_detail = ref.get("remote_detail", {})
    return {
        "name": ref.get("name"),
        "slug": ref.get("slug"),
        "group": ref.get("group"),
        "summary": ref.get("summary"),
        "local_detail": {
            "status": local_detail.get("status"),
            "path": local_detail.get("path"),
            "redirect_url": local_detail.get("redirect_url"),
            "hex_colors": local_detail.get("hex_colors", []),
            "excerpt": local_detail.get("excerpt", ""),
        },
        "remote_detail": {
            "status": remote_detail.get("status"),
            "source": remote_detail.get("source", ""),
            "hex_colors": remote_detail.get("hex_colors", []),
            "excerpt": remote_detail.get("excerpt", ""),
            "error": remote_detail.get("error", ""),
        },
    }


def match_reference_styles(query: str, limit: int = 3) -> list[dict]:
    query_tokens = _tokenize(query)
    query_lower = query.lower()
    ranked: list[tuple[int, dict]] = []

    for item in load_reference_catalog():
        score = 0
        name_lower = item["name"].lower()
        slug_lower = item["slug"].lower()
        summary_lower = item["summary"].lower()
        group_lower = item["group"].lower()

        if name_lower in query_lower or slug_lower in query_lower:
            score += 20

        for token in query_tokens:
            if token == name_lower or token == slug_lower:
                score += 12
            elif token in summary_lower:
                score += 4
            elif token in group_lower:
                score += 3
            elif token in item["keywords"]:
                score += 2

        if score > 0:
            ranked.append((score, item))

    ranked.sort(key=lambda pair: (-pair[0], pair[1]["name"]))
    return [item for _, item in ranked[:limit]]


def _reference_query_suffix(references: list[dict]) -> str:
    if not references:
        return ""
    return " ".join(ref["name"] for ref in references[:2])


def collect_reference_context(query: str, limit: int = 3) -> dict:
    references = match_reference_styles(query, limit=limit)
    enriched_references = []
    for ref in references:
        enriched = dict(ref)
        enriched["local_detail"] = load_reference_detail(ref["name"], ref["slug"])
        enriched_references.append(enriched)

    references = enriched_references
    if references and references[0]["local_detail"]["status"] in {"redirect-only-local-detail", "missing-local-detail"}:
        references[0]["remote_detail"] = load_remote_reference_detail(references[0]["name"], references[0]["slug"])
    elif references:
        references[0]["remote_detail"] = {
            "status": "not-needed",
            "source": "",
            "hex_colors": [],
            "excerpt": "",
            "error": "",
        }

    primary_reference = references[0] if references else None
    summarized_references = [_summarize_reference(ref) for ref in references]
    return {
        "query": query,
        "references": summarized_references,
        "reference_summary": ", ".join(ref["name"] for ref in references),
        "reference_direction": (
            f"Primary reference: {primary_reference['name']} - {primary_reference['summary']}"
            if primary_reference
            else "No direct brand reference match found."
        ),
        "primary_reference_detail_status": (
            primary_reference.get("local_detail", {}).get("status")
            if primary_reference
            else "no-reference-match"
        ),
        "primary_reference_detail_path": (
            primary_reference.get("local_detail", {}).get("path")
            if primary_reference
            else None
        ),
        "primary_reference_redirect_url": (
            primary_reference.get("local_detail", {}).get("redirect_url")
            if primary_reference
            else None
        ),
        "primary_reference_hex_colors": (
            primary_reference.get("local_detail", {}).get("hex_colors", [])
            if primary_reference
            else []
        ),
        "primary_reference_remote_detail_status": (
            primary_reference.get("remote_detail", {}).get("status")
            if primary_reference
            else "no-reference-match"
        ),
        "primary_reference_remote_hex_colors": (
            primary_reference.get("remote_detail", {}).get("hex_colors", [])
            if primary_reference
            else []
        ),
        "_primary_reference_design_md": (
            primary_reference.get("remote_detail", {}).get("design_md", "")
            if primary_reference
            else ""
        ),
        "primary_reference_design_md_excerpt": (
            primary_reference.get("remote_detail", {}).get("excerpt", "")
            if primary_reference
            else ""
        ),
        "query_suffix": _reference_query_suffix(references),
    }


def collect_structured_result(query: str, project_name: str | None = None) -> dict:
    generator = DesignSystemGenerator()
    return generator.generate(query, project_name)


def synthesize_design_system(
    query: str,
    project_name: str | None,
    reference_context: dict,
    structured_result: dict,
) -> dict:
    references = reference_context.get("references", [])
    design_system = copy.deepcopy(structured_result)

    design_system["original_query"] = query
    design_system["reference_styles"] = references
    design_system["reference_summary"] = reference_context.get("reference_summary", "")
    design_system["reference_direction"] = reference_context.get(
        "reference_direction",
        "No direct brand reference match found.",
    )
    design_system["reference_detail_status"] = reference_context.get(
        "primary_reference_detail_status",
        "no-reference-match",
    )
    design_system["reference_detail_path"] = reference_context.get("primary_reference_detail_path")
    design_system["reference_detail_redirect_url"] = reference_context.get("primary_reference_redirect_url")
    design_system["reference_hex_colors"] = reference_context.get("primary_reference_hex_colors", [])
    design_system["reference_remote_detail_status"] = reference_context.get(
        "primary_reference_remote_detail_status",
        "no-reference-match",
    )
    design_system["reference_remote_hex_colors"] = reference_context.get(
        "primary_reference_remote_hex_colors",
        [],
    )
    design_system["reference_design_md_excerpt"] = reference_context.get(
        "primary_reference_design_md_excerpt",
        "",
    )
    design_system["project_name"] = design_system.get("project_name") or project_name or "Untitled Project"
    design_system["source_pipeline"] = {
        "reference_source": "awesome-design-md",
        "structured_source": "ui-ux-pro-max-skill",
        "synthesis": "scripts/reasoning.py",
    }

    if references:
        primary_reference = references[0]
        existing_best_for = design_system.get("style", {}).get("best_for", "")
        reference_fit = f"Reference fit: {primary_reference['summary']}"
        design_system["style"]["best_for"] = (
            f"{existing_best_for} {reference_fit}".strip()
            if existing_best_for
            else reference_fit
        )

    return _apply_reference_overrides(design_system, reference_context, query)


def build_generation_bundle(query: str, project_name: str | None = None) -> dict:
    reference_context = collect_reference_context(query)
    full_reference_design_md = reference_context.get("_primary_reference_design_md", "")
    structured_query = f"{query} {reference_context.get('query_suffix', '')}".strip()
    structured_result = collect_structured_result(structured_query, project_name)
    final_design_system = synthesize_design_system(
        query=query,
        project_name=project_name,
        reference_context=reference_context,
        structured_result=structured_result,
    )
    reference_context.pop("_primary_reference_design_md", None)
    return {
        "query": query,
        "project_name": project_name or final_design_system.get("project_name"),
        "reference_context": reference_context,
        "structured_query": structured_query,
        "structured_result": structured_result,
        "final_design_system": final_design_system,
        "reference_assets": {
            "primary_reference_design_md": full_reference_design_md,
        },
    }


def generate_design_system(query: str, project_name: str | None = None) -> dict:
    return build_generation_bundle(query, project_name)["final_design_system"]
