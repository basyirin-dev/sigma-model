#!/usr/bin/env python3
"""
Paper 01 — Phase 8: validation-sample dual-scorer IRR (Task 8.2.5).

Independent second-rater scoring on the 20% validation sample
(research/charting/validation-sample.csv, 254 papers, fixed seed), mirroring
the 8.1.5 pilot IRR protocol:

  - rater 1 = external-AI raw scores (quality-batches/ai-output/batch-*.jsonl)
  - rater 2 = independent rater scoring quality-batches/validation/validation-01.jsonl
    -> research/charting/quality-batches/validation/rater2-validation.jsonl
  - the two 8.1.5 pilot overlaps (P003, P1036) are excluded from kappa/ICC
    (effective sample 252); they are already dual-scored under the pilot.

Metrics:
  - Cohen's kappa + raw agreement per dimension (D2/D3/D4/D5/D7/D8);
    null-pairs excluded per dimension (rater-1 nulls its D5/D8 on
    metadata-only papers under the contract null clause).
  - ICC(2,1) (two-way random, single measures, absolute agreement) on the
    D6-renormalized composite — identical definition to composite.py
    (scripted D1/D6 shared by both raters; rater dims per rater).
  - ≥1-point per-dimension gaps flagged for reconciliation, with
    reconcile:dim=value audit notes written to quality-scores.csv when a
    reconciled-value file is supplied (--reconciled jsonl).

Output: research/charting/quality-validation-report.md
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
VALIDATION_CSV = BASE / "research" / "charting" / "validation-sample.csv"
SCORES_CSV = BASE / "research" / "quality-scores.csv"
BATCHES_DIR = BASE / "research" / "charting" / "quality-batches"
REPORT_MD = BASE / "research" / "charting" / "quality-validation-report.md"
CONFIG_YAML = BASE / "research" / "charting" / "rubric-config.yaml"

DIMS = ["D2", "D3", "D4", "D5", "D7", "D8"]
SCRIPTED_DIMS = ["D1", "D6"]
ALL_DIMS = SCRIPTED_DIMS + DIMS
PILOT_IDS = {"P002", "P003", "P032", "P034", "P040",
             "P073", "P1030", "P1036", "P1170", "P635"}
GAP = 1  # >=1 point difference triggers a reconciliation flag


def parse_score(v) -> int | None:
    if v is None:
        return None
    if isinstance(v, bool):
        return None
    if isinstance(v, int):
        return v
    s = str(v).strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None


def load_rater1() -> dict[str, dict[str, int | None]]:
    """raw rater-1 scores per paper_id (D2-D8), from ai-output/batch-*.jsonl."""
    out: dict[str, dict[str, int | None]] = {}
    for f in sorted(BATCHES_DIR.glob("ai-output/batch-*.jsonl")):
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            pid = obj["paper_id"]
            out[pid] = {d: parse_score(obj.get(d)) for d in DIMS}
    return out


def load_rater2(path: Path) -> dict[str, dict[str, int | None]]:
    out: dict[str, dict[str, int | None]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        out[obj["paper_id"]] = {d: parse_score(obj.get(d)) for d in DIMS}
    return out


def cohen_kappa(a: list[int], b: list[int]) -> float:
    """Plain (unweighted) Cohen's kappa. Assumes len(a)==len(b) >= 1."""
    n = len(a)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    labels = sorted(set(a) | set(b))
    pa = Counter(a)
    pb = Counter(b)
    pe = sum(pa.get(label, 0) * pb.get(label, 0) for label in labels) / (n * n)
    if pe == 1:
        return 1.0
    return (po - pe) / (1 - pe) if (1 - pe) != 0 else 0.0


def icc21(papers: list[tuple[float, float]]) -> float:
    """ICC(2,1): two-way random, single measures, absolute agreement.

    rows = papers, cols = raters. Returns ICC; 1.0 if degenerate.
    """
    n = len(papers)
    if n < 2:
        return math.nan
    a = [x for x, _ in papers]
    b = [x for _, x in papers]
    grand = (sum(a) + sum(b)) / (2 * n)
    mean_a = sum(a) / n
    mean_b = sum(b) / n
    row_mean = [(x + y) / 2 for x, y in papers]

    sst = sum((x - grand) ** 2 + (y - grand) ** 2 for x, y in papers)
    ssr = 2 * sum((rm - grand) ** 2 for rm in row_mean)
    ssc = n * ((mean_a - grand) ** 2 + (mean_b - grand) ** 2)
    sse = sst - ssr - ssc
    dfr, dfc, dfe = n - 1, 1, n - 1
    if dfe <= 0:
        return 1.0
    msr = ssr / dfr
    msc = ssc / dfc
    mse = sse / dfe
    k = 2
    denom = msr + (k - 1) * mse + k * (msc - mse) / n
    if denom == 0:
        return 1.0
    return (msr - mse) / denom


def renormalize(weights: dict[str, float], present: list[str]) -> dict[str, float]:
    w = {d: weights[d] for d in present}
    total = sum(w.values())
    if total <= 0:
        return {}
    return {d: v / total for d, v in w.items()}


def composite(scores: dict[str, int | None], ws: dict[str, float],
              renorm_d6: bool) -> float | None:
    present = [d for d in ALL_DIMS if scores.get(d) is not None]
    if renorm_d6 and scores.get("D6") is None and "D6" in present:
        present = [d for d in present if d != "D6"]
    if not present:
        return None
    weights = renormalize(ws, present)
    return sum(scores[d] * weights[d] for d in present)


def main() -> int:
    parser = argparse.ArgumentParser(description="Phase 8 validation-sample IRR (Task 8.2.5)")
    parser.add_argument("--rater2", type=Path,
                        default=BATCHES_DIR / "validation" / "rater2-validation.jsonl",
                        help="rater-2 scoring file (default: validation/rater2-validation.jsonl)")
    parser.add_argument("--reconciled", type=Path,
                        help="optional jsonl of reconciled values "
                             "{paper_id: {dim: value}} to append reconcile: notes")
    args = parser.parse_args()

    if not args.rater2.exists():
        print(f"error: rater-2 file not found: {args.rater2}", file=sys.stderr)
        return 1

    cfg = yaml.safe_load(CONFIG_YAML.read_text(encoding="utf-8"))
    weight_sets = cfg["weight_sets"]
    renorm_d6 = bool(cfg.get("renormalize_missing_d6", False))

    sample = list(csv.DictReader(open(VALIDATION_CSV, newline="", encoding="utf-8")))
    sample_pids = [r["paper_id"] for r in sample if r["paper_id"] not in PILOT_IDS]

    rater1 = load_rater1()
    rater2 = load_rater2(args.rater2)

    missing = [p for p in sample_pids if p not in rater2]
    extra = [p for p in rater2 if p not in set(sample_pids)]
    if missing or extra:
        print(f"error: rater-2 missing {len(missing)} sample ids, "
              f"has {len(extra)} non-sample ids", file=sys.stderr)
        if missing:
            print("  missing:", sorted(missing)[:10], file=sys.stderr)
        if extra:
            print("  extra:", sorted(extra)[:10], file=sys.stderr)
        return 1

    # Scripted dims (shared by both raters) from quality-scores.csv.
    sc = {r["paper_id"]: r for r in csv.DictReader(open(SCORES_CSV, newline="", encoding="utf-8"))}

    rows = []
    for pid in sample_pids:
        wsc = sc[pid]
        wset = wsc.get("weight_set", "")
        ws = weight_sets.get(wset, weight_sets["pos_review"])
        s1 = {d: rater1[pid][d] for d in DIMS}
        s2 = {d: rater2[pid][d] for d in DIMS}
        for d in SCRIPTED_DIMS:
            s1[d] = parse_score(wsc.get(d))
            s2[d] = s1[d]
        rows.append({
            "paper_id": pid,
            "pubtype": wsc.get("publication_type", ""),
            "weight_set": wset,
            "r1": s1, "r2": s2,
            "c1": composite(s1, ws, renorm_d6),
            "c2": composite(s2, ws, renorm_d6),
        })

    lines: list[str] = []
    lines.append("# Validation-sample IRR report — Paper 01 Phase 8 (Task 8.2.5)\n")
    lines.append(f"- Sample: **{len(sample)}** papers (fixed seed, "
                 f"{Counter(r['evidence_basis'] for r in sample)}); "
                 f"pilot overlaps excluded (P003, P1036) -> **{len(rows)}** scored.")
    lines.append("- Rater 1: external-AI raw scores (ai-output/batch-*.jsonl).")
    lines.append(f"- Rater 2: {args.rater2.name}.")
    lines.append("- Kappa: Cohen's unweighted, per dimension, null-pairs excluded.")
    lines.append("- ICC(2,1): two-way random, single measures, absolute agreement, "
                 "on the D6-renormalized composite.\n")

    # Per-dimension kappa.
    lines.append("## Per-dimension inter-rater agreement\n")
    lines.append("| Dim | n pairs | exact match | kappa | >=1pt gaps |")
    lines.append("|-----|--------:|------------:|------:|-----------:|")
    per_dim_pairs: dict[str, list[tuple[int, int]]] = {d: [] for d in DIMS}
    gaps: list[tuple[str, str, int, int]] = []
    for r in rows:
        for d in DIMS:
            a = r["r1"][d]
            b = r["r2"][d]
            if a is None or b is None:
                continue
            per_dim_pairs[d].append((a, b))
            if abs(a - b) >= GAP:
                gaps.append((r["paper_id"], d, a, b))
    kappas: dict[str, float] = {}
    for d in DIMS:
        pairs = per_dim_pairs[d]
        n = len(pairs)
        if n == 0:
            kappas[d] = math.nan
            lines.append(f"| {d} | 0 | — | — | — |")
            continue
        a = [x for x, _ in pairs]
        b = [y for _, y in pairs]
        exact = sum(1 for x, y in zip(a, b) if x == y) / n
        k = cohen_kappa(a, b)
        kappas[d] = k
        ng = sum(1 for x, y in zip(a, b) if abs(x - y) >= GAP)
        lines.append(f"| {d} | {n} | {exact:.0%} | {k:.3f} | {ng} |")

    # ICC on composite.
    comp_pairs = [(r["c1"], r["c2"]) for r in rows
                  if r["c1"] is not None and r["c2"] is not None]
    icc = icc21(comp_pairs)
    n_comp = len(comp_pairs)
    lines.append("\n## Composite ICC\n")
    lines.append(f"- Composite ICC(2,1) over {n_comp} papers "
                 f"(D6-renormalized): **{icc:.3f}**\n")

    # Gaps for reconciliation.
    lines.append(f"## Reconciliation queue ({len(gaps)} gaps >= {GAP}pt)\n")
    if gaps:
        lines.append("| paper_id | dim | rater1 | rater2 |")
        lines.append("|----------|-----|-------:|-------:|")
        for pid, d, a, b in sorted(gaps):
            lines.append(f"| {pid} | {d} | {a} | {b} |")
    else:
        lines.append("None.\n")

    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {REPORT_MD.relative_to(BASE)}")
    print("kappa:", {d: (f"{k:.3f}" if not math.isnan(k) else "n/a")
                     for d, k in kappas.items()})
    print(f"ICC(2,1) composite: {icc:.3f} (n={n_comp})")
    print(f"gaps >= {GAP}pt: {len(gaps)}")

    # Optional reconciliation notes.
    if args.reconciled:
        rec: dict[str, dict] = {}
        for line in args.reconciled.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                obj = json.loads(line)
                rec[obj["paper_id"]] = obj
        rw = {r["paper_id"]: r for r in
              csv.DictReader(open(SCORES_CSV, newline="", encoding="utf-8"))}
        fields = list(rw[next(iter(rw))].keys())
        applied = 0
        for pid, dims in rec.items():
            if pid not in rw:
                continue
            row = rw[pid]
            notes = []
            for d, v in dims.items():
                if d in DIMS:
                    notes.append(f"reconcile:{d}={v}")
            if notes:
                row["notes"] = (row["notes"].strip(" |") + " | " +
                                "; ".join(notes)).strip(" |")
                applied += 1
        with open(SCORES_CSV, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=fields)
            w.writeheader()
            w.writerows(rw.values())
        print(f"applied reconcile: notes on {applied} rows of {SCORES_CSV.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
