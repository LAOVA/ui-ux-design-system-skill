#!/usr/bin/env python3
r"""
Reference-style reasoning layer for uiux-design-system.

This wraps the upstream UI/UX Pro Max generator with a lightweight
awesome-design-md matcher so generated outputs include explicit brand
reference direction as part of the design-system data.
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


def generate_design_system(query: str, project_name: str | None = None) -> dict:
    references = match_reference_styles(query)
    enriched_query = f"{query} {_reference_query_suffix(references)}".strip()

    generator = DesignSystemGenerator()
    design_system = generator.generate(enriched_query, project_name)

    design_system["original_query"] = query
    design_system["reference_styles"] = references
    design_system["reference_summary"] = ", ".join(ref["name"] for ref in references)

    if references:
        primary_reference = references[0]
        design_system["reference_direction"] = (
            f"Primary reference: {primary_reference['name']} - {primary_reference['summary']}"
        )
        existing_best_for = design_system.get("style", {}).get("best_for", "")
        reference_fit = f"Reference fit: {primary_reference['summary']}"
        design_system["style"]["best_for"] = (
            f"{existing_best_for} {reference_fit}".strip()
            if existing_best_for
            else reference_fit
        )
    else:
        design_system["reference_direction"] = "No direct brand reference match found."

    return design_system
