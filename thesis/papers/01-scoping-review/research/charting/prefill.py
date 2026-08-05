#!/usr/bin/env python3
"""
Paper 01 — Phase 7: build the base charted-data.csv (Task 7.2.1).

Prefills the 25-field finalized schema from Phase 6 artifacts:
  - bibliographic fields from research/included-studies.csv
  - relevance_sigma_trap seeded from research/retrieval/annotations.csv
    relevance_score (Phase 6, vocabulary-strength based)
  - evidence_basis: full-text (pdf-map.csv) > abstract (>100 chars) > metadata
  - venue: journal when present, else arXiv preprint / DOI-based derivation

Structured heuristic fields, AI free-text fields, citation_count are filled
by later pipeline stages (heuristic.py, external-AI pass, citations.py).

Output: research/charting/charted-data.csv
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"
PDF_MAP_CSV = BASE / "research" / "charting" / "pdf-map.csv"
SCHEMA_YAML = BASE / "research" / "charting" / "charted-schema.yaml"
OUT_CSV = BASE / "research" / "charting" / "charted-data.csv"

MIN_ABSTRACT = 100  # chars


def load_schema_fields() -> list[str]:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    return [f["name"] for f in cfg["fields"]]


def venue_for(row: dict) -> str:
    if row.get("journal"):
        return row["journal"].strip()
    if row.get("arxiv_id"):
        return "arXiv preprint"
    if row.get("doi"):
        return f"DOI:{row['doi']}"
    return ""


def main() -> None:
    fields = load_schema_fields()
    inc = list(csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8")))
    ann = {r["study_id"]: r for r in
           csv.DictReader(open(ANNOT_CSV, newline="", encoding="utf-8"))}
    pmap = {r["study_id"]: r["pdf_file"] for r in
            csv.DictReader(open(PDF_MAP_CSV, newline="", encoding="utf-8"))}

    rows: list[dict[str, str]] = []
    for s in inc:
        sid = s["study_id"]
        abstract = (s.get("abstract") or "").strip()
        has_abs = len(abstract) > MIN_ABSTRACT
        pdf = pmap.get(sid)
        basis = "full-text" if pdf else ("abstract" if has_abs else "metadata")
        rel = ann.get(sid, {}).get("relevance_score", "")
        rows.append({
            "paper_id": sid,
            "title": s["title"],
            "authors": s["authors"],
            "year": s["year"],
            "venue": venue_for(s),
            "doi": s.get("doi") or "",
            "publication_type": "",
            "subdomains": "",
            "formal_framework": "",
            "mathematical_formalism": "",
            "key_contribution": "",
            "methodology": "",
            "discusses_internal_representations": "",
            "discusses_schema_coherence": "",
            "relevance_sigma_trap": rel,
            "relevance_justification": "",
            "limitations_stated": "",
            "open_questions": "",
            "key_equations_definitions": "",
            "datasets_used": "",
            "sample_size": "",
            "effect_sizes": "",
            "citation_count": "",
            "evidence_basis": basis,
            "notes": f"ft_file={pdf}" if pdf else "",
        })

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    n_ft = sum(1 for r in rows if r["evidence_basis"] == "full-text")
    n_ab = sum(1 for r in rows if r["evidence_basis"] == "abstract")
    n_md = sum(1 for r in rows if r["evidence_basis"] == "metadata")
    print(f"prefilled {len(rows)} rows -> {OUT_CSV.name}")
    print(f"evidence_basis: full-text={n_ft}, abstract={n_ab}, metadata={n_md}")


if __name__ == "__main__":
    sys.exit(main())
