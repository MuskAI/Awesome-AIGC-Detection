#!/usr/bin/env python3
"""Validate structured data for Awesome-AIGC-Detection."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
AREAS = {"Image", "Video", "Text", "Audio", "Multimodal"}
PAPER_REQUIRED = {
    "id",
    "title",
    "year",
    "month",
    "area",
    "venue",
    "paper_url",
    "arxiv_id",
    "code_url",
    "project_url",
    "methods",
    "tags",
    "is_landmark",
    "notes",
}
DATASET_REQUIRED = {
    "id",
    "year",
    "name",
    "url",
    "real_count",
    "fake_count",
    "real_sources",
    "generation_methods",
    "notes",
}
TOOL_REQUIRED = {"id", "name", "category", "url", "language", "platform", "description"}
URL_RE = re.compile(r"^https?://[^\s]+$", re.IGNORECASE)
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$", re.IGNORECASE)
ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
PLACEHOLDERS = {"https://arxiv.org/abs/", "https://github.com/"}


def load_json(path: Path) -> list[dict[str, Any]]:
    try:
        with path.open(encoding="utf-8") as f:
            data = json.load(f)
    except Exception as exc:  # noqa: BLE001
        raise ValueError(f"{path.relative_to(ROOT)} is not valid JSON: {exc}") from exc
    if not isinstance(data, list):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON list")
    if not all(isinstance(item, dict) for item in data):
        raise ValueError(f"{path.relative_to(ROOT)} must contain only JSON objects")
    return data


def normalize_title(title: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", title).strip().lower())


def check_required(item: dict[str, Any], required: set[str], label: str, errors: list[str]) -> None:
    missing = sorted(required - set(item))
    extra = sorted(set(item) - required)
    if missing:
        errors.append(f"{label}: missing fields {missing}")
    if extra:
        errors.append(f"{label}: unknown fields {extra}")


def check_url(value: Any, label: str, errors: list[str], *, allow_empty: bool = True) -> None:
    if value == "" and allow_empty:
        return
    if not isinstance(value, str) or not URL_RE.match(value):
        errors.append(f"{label}: expected http(s) URL, got {value!r}")
        return
    if value in PLACEHOLDERS:
        errors.append(f"{label}: placeholder URL is not allowed")


def validate_papers(papers: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids: Counter[str] = Counter()
    title_years: Counter[tuple[str, int]] = Counter()

    for idx, paper in enumerate(papers):
        label = f"data/papers.json[{idx}]"
        check_required(paper, PAPER_REQUIRED, label, errors)
        if not PAPER_REQUIRED.issubset(paper):
            continue

        paper_id = paper["id"]
        ids[paper_id] += 1
        if not isinstance(paper_id, str) or not ID_RE.match(paper_id):
            errors.append(f"{label}.id: expected kebab-case id, got {paper_id!r}")

        if not isinstance(paper["title"], str) or not paper["title"].strip():
            errors.append(f"{label}.title: must be a non-empty string")

        if not isinstance(paper["year"], int) or paper["year"] < 1900 or paper["year"] > 2100:
            errors.append(f"{label}.year: expected reasonable integer year")
        if not isinstance(paper["month"], int) or not 1 <= paper["month"] <= 12:
            errors.append(f"{label}.month: expected integer 1-12")

        if paper["area"] not in AREAS:
            errors.append(f"{label}.area: expected one of {sorted(AREAS)}, got {paper['area']!r}")
        if not isinstance(paper["venue"], str) or not paper["venue"].strip():
            errors.append(f"{label}.venue: must be a non-empty string")

        for field in ("paper_url", "code_url", "project_url"):
            check_url(paper[field], f"{label}.{field}", errors)

        arxiv_id = paper["arxiv_id"]
        if arxiv_id and (not isinstance(arxiv_id, str) or not ARXIV_RE.match(arxiv_id)):
            errors.append(f"{label}.arxiv_id: invalid arXiv id {arxiv_id!r}")
        if arxiv_id and paper["paper_url"] == "":
            errors.append(f"{label}.paper_url: required when arxiv_id is present")

        for field in ("methods", "tags"):
            if not isinstance(paper[field], list) or not all(isinstance(x, str) for x in paper[field]):
                errors.append(f"{label}.{field}: expected list of strings")

        if not isinstance(paper["is_landmark"], bool):
            errors.append(f"{label}.is_landmark: expected boolean")
        if not isinstance(paper["notes"], str):
            errors.append(f"{label}.notes: expected string")

        if isinstance(paper["year"], int) and isinstance(paper["title"], str):
            title_years[(normalize_title(paper["title"]), paper["year"])] += 1

    for paper_id, count in ids.items():
        if count > 1:
            errors.append(f"data/papers.json: duplicate id {paper_id!r}")
    for (title, year), count in title_years.items():
        if count > 1:
            errors.append(f"data/papers.json: duplicate paper title/year {year} {title!r}")
    return errors


def validate_datasets(datasets: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids: Counter[str] = Counter()
    for idx, item in enumerate(datasets):
        label = f"data/datasets.json[{idx}]"
        check_required(item, DATASET_REQUIRED, label, errors)
        if not DATASET_REQUIRED.issubset(item):
            continue
        ids[item["id"]] += 1
        if not isinstance(item["id"], str) or not ID_RE.match(item["id"]):
            errors.append(f"{label}.id: expected kebab-case id")
        if not isinstance(item["year"], int):
            errors.append(f"{label}.year: expected integer")
        if not isinstance(item["name"], str) or not item["name"].strip():
            errors.append(f"{label}.name: must be non-empty")
        check_url(item["url"], f"{label}.url", errors)
        for field in ("real_count", "fake_count", "real_sources", "generation_methods", "notes"):
            if not isinstance(item[field], str):
                errors.append(f"{label}.{field}: expected string")
    for item_id, count in ids.items():
        if count > 1:
            errors.append(f"data/datasets.json: duplicate id {item_id!r}")
    return errors


def validate_tools(tools: list[dict[str, Any]]) -> list[str]:
    errors: list[str] = []
    ids: Counter[str] = Counter()
    for idx, item in enumerate(tools):
        label = f"data/tools.json[{idx}]"
        check_required(item, TOOL_REQUIRED, label, errors)
        if not TOOL_REQUIRED.issubset(item):
            continue
        ids[item["id"]] += 1
        if not isinstance(item["id"], str) or not ID_RE.match(item["id"]):
            errors.append(f"{label}.id: expected kebab-case id")
        for field in ("name", "category", "language", "platform", "description"):
            if not isinstance(item[field], str) or not item[field].strip():
                errors.append(f"{label}.{field}: must be a non-empty string")
        check_url(item["url"], f"{label}.url", errors, allow_empty=False)
    for item_id, count in ids.items():
        if count > 1:
            errors.append(f"data/tools.json: duplicate id {item_id!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    try:
        papers = load_json(ROOT / "data" / "papers.json")
        datasets = load_json(ROOT / "data" / "datasets.json")
        tools = load_json(ROOT / "data" / "tools.json")
    except ValueError as exc:
        print(exc, file=sys.stderr)
        return 1

    errors.extend(validate_papers(papers))
    errors.extend(validate_datasets(datasets))
    errors.extend(validate_tools(tools))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    area_counts = Counter(p["area"] for p in papers)
    print(
        "Validated "
        f"{len(papers)} papers, {len(datasets)} datasets, {len(tools)} tools "
        f"({', '.join(f'{area}={area_counts.get(area, 0)}' for area in sorted(AREAS))})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
