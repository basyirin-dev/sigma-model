"""Paper 01 — duplicate-version reconciliation (Phase A, round responding to external P5 audit).

Detects the same study charted twice (arXiv preprint + published version) in
charted-data.csv and collapses each version-cluster to one row.

Rules (documented):
- Cluster key: normalized title (NFKD, lowercase, alphanumerics only).
- A cluster is a version-cluster iff it contains >= 1 strict pair:
  shared author token AND (year within +/-1 or either year missing).
- Within a cluster, the kept row is the best available:
  1. DOI-bearing version over non-DOI (published over preprint),
  2. fuller evidence basis (full-text > abstract > metadata),
  3. lower paper_id (earlier charted) as the final tiebreak.
- Non-version clusters (same normalized title, no shared author / far years)
  are left untouched.

Outputs (written to research/charting/):
- charted-data-unique.csv  — the analysis corpus (one row per study)
- version-removals.csv     — every removed row with its kept row + reason
- version-reconciliation.md — summary report
Raw charted-data.csv is left untouched (audit trail).
"""
from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
RAW = BASE / "charted-data.csv"
OUT = BASE / "charted-data-unique.csv"
REMOVALS = Path(__file__).resolve().parent / "version-removals.csv"
REPORT = Path(__file__).resolve().parent / "version-reconciliation.md"

EVIDENCE_RANK = {"full_text": 3, "abstract": 2, "metadata": 1, "": 0}


def norm_title(t: str) -> str:
    t = unicodedata.normalize("NFKD", t).lower()
    t = re.sub(r"[^a-z0-9 ]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def author_tokens(s: str) -> set[str]:
    return set(re.findall(r"[a-z]{4,}", (s or "").lower()))


def year_int(v: str) -> int | None:
    v = (v or "").strip()
    return int(v) if v.isdigit() else None


def row_key(r: dict[str, str]) -> tuple:
    doi = 1 if (r.get("doi") or "").strip() else 0
    ev = EVIDENCE_RANK.get((r.get("evidence_basis") or "").strip().lower(), 0)
    pid = int(re.sub(r"\D", "", r["paper_id"] or "0") or 0)
    return (doi, ev, pid)


def main() -> None:
    with open(RAW, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    n = len(rows)
    print(f"raw rows: {n}")

    by_title: dict[str, list[dict[str, str]]] = {}
    for r in rows:
        by_title.setdefault(norm_title(r["title"]), []).append(r)

    clusters: list[list[dict[str, str]]] = []
    for group in by_title.values():
        if len(group) < 2:
            continue
        strict = False
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                a, b = group[i], group[j]
                ya, yb = year_int(a["year"]), year_int(b["year"])
                shared = author_tokens(a["authors"] + a.get("first_author", "")) & author_tokens(
                    b["authors"] + b.get("first_author", "")
                )
                close = (ya is None or yb is None) or abs((ya or 0) - (yb or 0)) <= 1
                if shared and close:
                    strict = True
        if strict:
            clusters.append(group)

    removed: list[dict[str, str]] = []
    kept_ids: set[str] = set()
    for group in clusters:
        group.sort(key=row_key, reverse=True)
        keep = group[0]
        kept_ids.add(keep["paper_id"])
        for r in group[1:]:
            removed.append(
                {
                    "removed_id": r["paper_id"],
                    "kept_id": keep["paper_id"],
                    "normalized_title": norm_title(r["title"]),
                    "removed_title": r["title"][:120],
                    "kept_title": keep["title"][:120],
                    "removed_doi": (r.get("doi") or "").strip(),
                    "kept_doi": (keep.get("doi") or "").strip(),
                    "removed_year": (r.get("year") or "").strip(),
                    "kept_year": (keep.get("year") or "").strip(),
                    "removed_evidence": (r.get("evidence_basis") or "").strip(),
                    "kept_evidence": (keep.get("evidence_basis") or "").strip(),
                    "reason": "version pair: same study charted as preprint+published"
                    if (keep.get("doi") or "").strip()
                    else "version cluster (no DOI-bearing row)",
                }
            )

    cluster_ids = {r["paper_id"] for g in clusters for r in g}
    unique = [r for r in rows if r["paper_id"] not in cluster_ids] + [
        g[0] for g in clusters if g[0]["paper_id"] in kept_ids
    ]
    unique_ids = {r["paper_id"] for r in unique}
    assert len(unique) == len(unique_ids), "kept rows must be unique"
    assert len(unique) == n - len(removed), f"count mismatch: {len(unique)} != {n - len(removed)}"

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader()
        w.writerows(sorted(unique, key=lambda r: r["paper_id"]))
    with open(REMOVALS, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(removed[0].keys()) if removed else ["removed_id"])
        w.writeheader()
        w.writerows(removed)

    with open(REPORT, "w") as f:
        f.write("# Duplicate-version reconciliation — Paper 01\n\n")
        f.write(f"- Raw included records: **{n}**\n")
        f.write(f"- Version-clusters (normalized-title groups with >=1 strict pair): "
                f"**{len(clusters)}**\n")
        f.write(f"- Rows removed: **{len(removed)}**\n")
        f.write(f"- Unique studies (analysis corpus): **{len(unique)}**\n\n")
        f.write("Rule: cluster key = normalized title; strict pair = shared author token AND "
                "year within +/-1 (or missing). Kept row = DOI-bearing version, else fuller "
                "evidence basis, else lower paper_id. Raw `charted-data.csv` is untouched "
                "(audit trail); all analysis now reads `charted-data-unique.csv`.\n\n")
        f.write(f"Full removal log: `version-removals.csv` ({len(removed)} rows).\n")
    print(f"clusters: {len(clusters)} | removed: {len(removed)} | unique: {len(unique)}")


if __name__ == "__main__":
    main()
