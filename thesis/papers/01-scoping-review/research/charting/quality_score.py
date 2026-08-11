#!/usr/bin/env python3
"""
Paper 01 — Phase 8: scripted credibility scoring pass (Task 8.2.1).

Computes the SCRIPTED dimensions of the Phase 0.5 credibility rubric
(quality-criteria.md §6) for all 1,268 included papers:

  D1  venue / peer-review tier baseline   (heuristic from venue/doi strings)
  D6  citation / field uptake baseline    (time-normalized: citation_count
                                          percentile within year cohort)

and emits the `research/quality-scores.csv` skeleton with paper_id,
bibliographic echo, weight_set, and blank D2–D8 / composite / tier columns
to be filled by the rater/AI pass (Task 8.2.2) and finalize step (8.2.3).

Config: research/charting/rubric-config.yaml (ADR 0004). No hardcoded params.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
CONFIG_YAML = Path(__file__).resolve().parent / "rubric-config.yaml"
SCORES_CSV = BASE / "research" / "quality-scores.csv"

OUT_COLUMNS = [
    "paper_id", "year", "publication_type", "evidence_basis", "citation_count",
    "D1", "D6", "D2", "D3", "D4", "D5", "D7", "D8",
    "composite", "tier", "weight_set", "notes",
]

PUBTYPE_TO_WEIGHTSET = {
    "empirical": "empirical",
    "theoretical": "theoretical",
    "position": "pos_review",
    "opinion": "pos_review",
    "review": "pos_review",
    "other": "pos_review",
}


def _load_config() -> dict:
    with open(CONFIG_YAML, encoding="utf-8") as f:
        return yaml.safe_load(f)


def _parse_int(value: str) -> int | None:
    v = (value or "").strip()
    if not v or v.upper() in ("NA", "N/A", "NULL", "NONE"):
        return None
    try:
        return int(float(v))
    except ValueError:
        return None


def d1_venue_baseline(venue: str, doi: str, rules: list[dict]) -> tuple[int, str]:
    """First matching rule wins (ordered priority). Returns (score, label).

    Rules may carry `keywords` (substring match) and/or `keywords_re`
    (regex match); either set matching satisfies the rule.
    """
    haystack = f"{(venue or '').lower()} {(doi or '').lower()}"
    for rule in rules:
        if any(kw in haystack for kw in rule.get("keywords", [])):
            return int(rule["score"]), rule["label"]
        if any(re.search(p, haystack) for p in rule.get("keywords_re", [])):
            return int(rule["score"]), rule["label"]
    return int(rules[-1]["score"]), rules[-1]["label"]  # unknown default


def d6_citations_baseline(
    citation_count: str, pct: float, bands: list[dict],
    zero_grace: bool = False,
) -> tuple[int | None, str]:
    """Citation percentile -> score (bands in config). Missing data -> (None, note)."""
    cc = _parse_int(citation_count)
    if cc is None:
        return None, ("citation_count missing; AF/LW inbound supplement "
                      "required (quality-criteria.md §8.2)")
    if cc == 0 and not zero_grace:
        return 0, "zero citations after grace period"
    for band in bands:
        if pct >= float(band["percentile_ge"]):
            return int(band["score"]), f"p{int(pct)}"
    return 0, f"p{int(pct)}"


def build_cohort_percentiles(rows: list[dict]) -> dict[int, tuple[int, dict[int, float]]]:
    """Per-year cohort -> (n, {citation_count: percentile}).

    percentile = share of non-missing citation counts in the same year
    cohort that are <= count, expressed as a percentage (0–100).
    """
    per_year: dict[int, list[int]] = {}
    for r in rows:
        cc = _parse_int(r.get("citation_count", ""))
        y = _parse_int(r.get("year", ""))
        if cc is not None and y is not None:
            per_year.setdefault(y, []).append(cc)
    percentiles: dict[int, tuple[int, dict[int, float]]] = {}
    for y, vals in per_year.items():
        vals.sort()
        n = len(vals)
        pct_map = {c: 100.0 * (sum(1 for v in vals if v <= c) / n) for c in vals}
        percentiles[y] = (n, pct_map)
    return percentiles


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Phase 8 scripted credibility pass (Task 8.2.1)")
    parser.add_argument("--summary", action="store_true",
                        help="print D1/D6 distribution summary to stdout")
    args = parser.parse_args(argv)

    cfg = _load_config()
    with open(CHARTED_CSV, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    cohort = build_cohort_percentiles(rows)
    all_cc = sorted(c for c in (_parse_int(r.get("citation_count", "")) for r in rows)
                    if c is not None)
    global_n = len(all_cc)
    global_pct: dict[int, float] = {}
    if global_n:
        for c in all_cc:
            global_pct[c] = 100.0 * (sum(1 for v in all_cc if v <= c) / global_n)

    out: list[dict] = []
    d1_counts: Counter = Counter()
    d6_counts: Counter = Counter()
    max_year = max(_parse_int(r.get("year", "")) or 0 for r in rows)
    grace_years = int(cfg["d6"]["zero_citation_grace_years"])
    grace_cutoff = max_year - grace_years + 1  # years >= cutoff are within grace
    prev = {}
    if SCORES_CSV.exists():
        with open(SCORES_CSV, encoding="utf-8") as f:
            prev = {p["paper_id"]: p for p in csv.DictReader(f)}
    for r in rows:
        year = _parse_int(r.get("year", "")) or 0
        d1, d1_label = d1_venue_baseline(r.get("venue", ""), r.get("doi", ""),
                                         cfg["d1_venue"])
        cc = _parse_int(r.get("citation_count", ""))
        cohort_n, cohort_pct_map = cohort.get(year, (0, {}))
        if cohort_n >= int(cfg["d6"]["min_cohort_size"]) and cc is not None:
            pct = cohort_pct_map.get(cc, 0.0)
            pct_src = "cohort"
        elif cc is not None and global_n:
            pct = global_pct.get(cc, 0.0)
            pct_src = "global(fallback)"
        else:
            pct, pct_src = 0.0, "n/a"
        d6, d6_note = d6_citations_baseline(
            r.get("citation_count", ""), pct, cfg["d6"]["bands"],
            zero_grace=(year >= grace_cutoff))
        ws = PUBTYPE_TO_WEIGHTSET.get((r.get("publication_type") or "").strip(), "pos_review")
        notes = (r.get("notes") or "").strip()
        flags = []
        if d1_label != "unknown":
            flags.append(f"d1:{d1_label}")
        if d6_note:
            flags.append(f"d6:{pct_src} {d6_note}")
        if d6 is not None:
            d6_counts[d6] += 1
        d1_counts[d1] += 1
        prior = prev.get(r.get("paper_id", ""), {})
        rater_dims = {d: prior.get(d, "") for d in ("D2", "D3", "D4", "D5", "D7", "D8")}
        # Preserve the audit trail from a previous run (scored:, reconcile:,
        # pilot=, ai-revised:, ft_file=) while refreshing d1:/d6: flags.
        prior_notes = (prior.get("notes") or "").strip()
        kept = [n.strip() for n in prior_notes.split("|")
                if n.strip() and not n.strip().startswith(("d1:", "d6:"))]
        kept.append(notes)
        notes = " | ".join([n for n in kept if n]).strip(" |")
        out.append({
            "paper_id": r.get("paper_id", ""),
            "year": year or "",
            "publication_type": r.get("publication_type", ""),
            "evidence_basis": r.get("evidence_basis", ""),
            "citation_count": r.get("citation_count", ""),
            "D1": d1,
            "D6": "" if d6 is None else d6,
            "D2": rater_dims["D2"], "D3": rater_dims["D3"], "D4": rater_dims["D4"],
            "D5": rater_dims["D5"], "D7": rater_dims["D7"], "D8": rater_dims["D8"],
            "composite": prior.get("composite", ""), "tier": prior.get("tier", ""),
            "weight_set": ws,
            "notes": (" | ".join([notes] + flags)).strip(" |") if flags else notes,
        })

    with open(SCORES_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUT_COLUMNS)
        writer.writeheader()
        writer.writerows(out)

    print(f"wrote {len(out)} rows -> {SCORES_CSV.relative_to(BASE)}")
    if args.summary:
        print(f"D1 venue baseline: {dict(sorted(d1_counts.items()))}")
        print(f"D6 citations baseline (non-missing): {dict(sorted(d6_counts.items()))}")
        missing_d6 = sum(1 for r in out if r["D6"] == "")
        print(f"D6 missing (needs AF/LW supplement): {missing_d6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
