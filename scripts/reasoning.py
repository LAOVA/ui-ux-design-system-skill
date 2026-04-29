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

import re
import sys
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
UPSTREAM_SCRIPTS = ROOT_DIR / "ui-ux-pro-max-skill" / "scripts"
REFERENCE_README = ROOT_DIR / "awesome-design-md" / "README.md"

if str(UPSTREAM_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_SCRIPTS))

from design_system import DesignSystemGenerator  # type: ignore  # noqa: E402


REFERENCE_LINE_RE = re.compile(r"- \[\*\*(?P<name>.+?)\*\*\]\(.+?\) - (?P<summary>.+)")


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9\.\-\+]+", text.lower())


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
    primary_reference = references[0] if references else None
    return {
        "query": query,
        "references": references,
        "reference_summary": ", ".join(ref["name"] for ref in references),
        "reference_direction": (
            f"Primary reference: {primary_reference['name']} - {primary_reference['summary']}"
            if primary_reference
            else "No direct brand reference match found."
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
    design_system = structured_result

    design_system["original_query"] = query
    design_system["reference_styles"] = references
    design_system["reference_summary"] = reference_context.get("reference_summary", "")
    design_system["reference_direction"] = reference_context.get(
        "reference_direction",
        "No direct brand reference match found.",
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

    return design_system


def build_generation_bundle(query: str, project_name: str | None = None) -> dict:
    reference_context = collect_reference_context(query)
    structured_query = f"{query} {reference_context.get('query_suffix', '')}".strip()
    structured_result = collect_structured_result(structured_query, project_name)
    final_design_system = synthesize_design_system(
        query=query,
        project_name=project_name,
        reference_context=reference_context,
        structured_result=structured_result,
    )
    return {
        "query": query,
        "project_name": project_name or final_design_system.get("project_name"),
        "reference_context": reference_context,
        "structured_query": structured_query,
        "structured_result": structured_result,
        "final_design_system": final_design_system,
    }


def generate_design_system(query: str, project_name: str | None = None) -> dict:
    return build_generation_bundle(query, project_name)["final_design_system"]
