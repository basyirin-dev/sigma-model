#!/usr/bin/env python3
"""
Paper 01 — Phase 6 Full-Text Annotation & Inventory (Task 6.4)

For each included study:
  - extract annotation key points from the abstract (research question /
    method / findings signals) + title
  - page count where a PDF was retrieved (pypdf)
  - schema-coherence / σ-trap relevance score (1-5) from vocabulary strength

Outputs:
  - research/full-text-inventory.md
  - research/retrieval/annotations.csv
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "screening"))
import screening_config as SC  # noqa: E402
from screener import token_hits  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
DECISIONS_CSV = BASE / "research" / "retrieval" / "eligibility-decisions.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
PDF_DIR = BASE / "research" / "pdfs"
INVENTORY_MD = BASE / "research" / "full-text-inventory.md"
ANNOT_CSV = BASE / "research" / "retrieval" / "annotations.csv"


def load_csv(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pdf_page_count(pdf_path: str | None) -> str:
    if not pdf_path:
        return ""
    p = BASE.parent.parent.parent / pdf_path
    if not p.exists():
        return ""
    try:
        from pypdf import PdfReader
        return str(len(PdfReader(str(p)).pages))
    except Exception:
        return ""


def relevance_score(rec: dict) -> int:
    """1-5 schema-coherence / σ-trap relevance from vocabulary strength."""
    text = f"{rec.get('title','')} {rec.get('abstract','') or ''} {rec.get('keywords','') or ''}"
    core = token_hits(text, SC.CORE_INDICATORS)
    subdomains = [s for s, pats in SC.SUBDOMAINS.items() if token_hits(text, pats)]
    n = len(core) + len(subdomains)
    if n >= 6:
        return 5
    if n >= 4:
        return 4
    if n >= 2:
        return 3
    if n >= 1:
        return 2
    return 1


def key_points(abstract: str, title: str) -> str:
    """First two sentences of abstract + title as annotation key points."""
    ab = (abstract or "").strip().replace("\n", " ")
    sentences = re.split(r"(?<=[.!?])\s+", ab)
    pts = []
    if title:
        pts.append(f"RQ: {title.strip()[:140]}")
    if sentences:
        pts.append("Abstract: " + " ".join(sentences[:2])[:240])
    return " | ".join(pts) if pts else "title-only (no abstract available)"


def main():
    with open(DECISIONS_CSV, "r", encoding="utf-8") as f:
        records = list(csv.DictReader(f))
    status_map = {r["id"]: r for r in load_csv(STATUS_CSV)} if STATUS_CSV.exists() else {}
    included = [r for r in records if r["ft_decision"] == "Include"]
    included.sort(key=lambda r: r.get("study_id", ""))

    annot_rows = []
    for r in included:
        st = status_map.get(r["id"], {})
        pdf_path = st.get("pdf_path", "") or ""
        page_count = pdf_page_count(pdf_path)
        score = relevance_score(r)
        r["annotation"] = key_points(r.get("abstract", ""), r.get("title", ""))
        r["relevance_score"] = score
        r["page_count"] = page_count
        r["ft_status"] = st.get("status", r.get("ft_status", ""))
        r["pdf_path"] = pdf_path
        annot_rows.append(r)

    # Write annotations CSV
    with open(ANNOT_CSV, "w", encoding="utf-8", newline="") as f:
        fields = ["study_id", "id", "title", "authors", "year", "doi", "arxiv_id",
                  "relevance_score", "page_count", "annotation", "ft_status"]
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(annot_rows)

    # Inventory markdown
    with open(INVENTORY_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Full-Text Inventory (Task 6.4)\n\n")
        f.write(f"**Included studies**: {len(included)}\n")
        f.write(f"**PDFs retrieved**: {sum(1 for r in annot_rows if r.get('ft_status','').startswith('retrieved'))}\n\n")
        f.write("| Study ID | Year | Title | Rel (1-5) | Pages | Retrieved |\n")
        f.write("|----------|------|-------|----------|-------|-----------|\n")
        for r in annot_rows:
            ret = "✓" if (r.get("ft_status") or "").startswith("retrieved") else ""
            f.write(f"| {r.get('study_id','')} | {r.get('year','')} | {r['title'][:60]} | "
                    f"{r['relevance_score']} | {r.get('page_count','')} | {ret} |\n")
        f.write(f"\n## Annotation Key Points (first 40)\n\n")
        for r in annot_rows[:40]:
            f.write(f"### {r.get('study_id','')} — {r['title'][:80]}\n\n")
            f.write(f"{r['annotation']}\n\n")
        f.write(f"\n*(Full annotations for all {len(included)} studies in "
                f"`research/retrieval/annotations.csv`)*\n")

    print(f"Included studies: {len(included)}")
    print(f"Retrieved PDFs: {sum(1 for r in annot_rows if (r.get('ft_status') or '').startswith('retrieved'))}")
    print(f"Inventory: {INVENTORY_MD.name}")
    print(f"Annotations: {ANNOT_CSV.name}")


if __name__ == "__main__":
    main()
