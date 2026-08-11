#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.3.2/7.3.3, CC.1.6): inter-extractor agreement.

Compares extractor 1 (post-AI merged charted-data-main.csv) against
extractor 2 (validation-batches/ai-output/batch-01.jsonl) on the 20% sample:
  - Cohen's kappa + raw agreement per categorical study field
  - ICC(2,1) for continuous fields (accuracies, seeds, effect sizes, scores)
  - per-field disagreement examples for reconciliation (Task 7.3.4)

Thresholds (phase-doc exit criteria): kappa >= 0.80, ICC >= 0.90.

Output: research/charting/validation-report.md
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTING = BASE / "research" / "charting"
MAIN_CSV = BASE / "research" / "charted-data-main.csv"
SAMPLE_CSV = CHARTING / "validation-sample.csv"
EX2_JSONL = CHARTING / "validation-batches" / "ai-output" / "batch-01.jsonl"
SCHEMA_YAML = CHARTING / "charted-schema.yaml"
REPORT_MD = CHARTING / "validation-report.md"


def cohen_kappa(a: list[str], b: list[str]) -> float:
    """Cohen's kappa for two raters (binary/multinomial agreement)."""
    n = len(a)
    if n == 0:
        return 0.0
    cats = set(a) | set(b)
    agree = sum(1 for x, y in zip(a, b) if x == y)
    po = agree / n
    pe = 0.0
    for c in cats:
        pa = sum(1 for x in a if x == c) / n
        pb = sum(1 for x in b if x == c) / n
        pe += pa * pb
    return (po - pe) / (1 - pe) if pe < 1.0 else 0.0


def icc21(a: list[float], b: list[float]) -> float:
    """ICC(2,1) two-way random, single measures (ANOVA-based)."""
    n = len(a)
    if n < 2:
        return float("nan")
    k = 2
    gm = (sum(a) + sum(b)) / (n * k)
    ss_total = sum((x - gm) ** 2 for x in a + b)
    ss_rows = sum((x + y) ** 2 for x, y in zip(a, b)) / k - n * gm * gm
    ss_cols = (sum(a) ** 2 + sum(b) ** 2) / n - n * k * gm * gm
    ss_err = ss_total - ss_rows - ss_cols
    ss_rows, ss_err = max(0.0, ss_rows), max(0.0, ss_err)
    df_r, df_c, df_e = n - 1, k - 1, (n - 1) * (k - 1)
    ms_r = ss_rows / df_r if df_r else 0.0
    ms_c = ss_cols / df_c if df_c else 0.0
    ms_e = ss_err / df_e if df_e else 0.0
    denom = ms_r + ms_c + ms_e
    if denom == 0:
        return 1.0  # degenerate: perfect agreement
    return (ms_r - ms_e) / denom


def load_ex2() -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not EX2_JSONL.exists():
        return out
    for line in EX2_JSONL.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        out[obj["study_id"]] = obj
    return out


def main() -> None:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    sample = [r["study_id"] for r in
              csv.DictReader(open(SAMPLE_CSV, newline="", encoding="utf-8"))]
    ex1 = {r["study_id"]: r for r in
           csv.DictReader(open(MAIN_CSV, newline="", encoding="utf-8"))}
    ex2 = load_ex2()

    cat_fields = [f["name"] for f in cfg["study_fields"]
                  if "vocabulary" in f and f.get("dual", False)]
    cont_fields = [f["name"] for f in cfg["study_fields"]
                   if f.get("data_type") in ("numeric", "integer")
                   and f.get("dual", False)]

    present = [s for s in sample if s in ex2]
    missing = [s for s in sample if s not in ex2]
    lines = [
        "# Extraction validation report — Paper 02 Phase 7 (CC.1.6)",
        "",
        f"- Sample: **{len(sample)}** studies (20%, seed=20261016)",
        f"- Extractor 2 completed: **{len(present)}** of {len(sample)} "
        f"(missing: {', '.join(missing) or '—'})",
        "- Extractor 1: merged AI pass (`charted-data-main.csv`)",
        "- Extractor 2: independent second-AI pass (`validation-batches/ai-output/`)",
        "- Targets: Cohen's kappa >= 0.80; ICC(2,1) >= 0.90",
        "",
        "## Categorical fields (Cohen's kappa)",
        "",
        "| Field | n | Raw agreement | Kappa | Pass (>=0.80) |",
        "|---|---|---|---|---|",
    ]
    cat_results: list[tuple[str, float, bool]] = []
    for f in cat_fields:
        a = [ex1[s][f] for s in present]
        b = [ex2[s][f].get(f, "") if isinstance(ex2[s].get(f), str) else ""
             for s in present]
        n = len(a)
        raw = sum(1 for x, y in zip(a, b) if x == y) / n if n else 0.0
        k = cohen_kappa(a, b) if n else 0.0
        cat_results.append((f, k, k >= 0.80))
        lines.append(f"| {f} | {n} | {raw:.3f} | {k:.3f} | {'YES' if k >= 0.80 else 'no'} |")

    lines += ["", "## Continuous fields (ICC(2,1))", "", "| Field | n | ICC | Pass (>=0.90) |",
              "|---|---|---|---|"]
    cont_results: list[tuple[str, float, bool]] = []
    for f in cont_fields:
        pairs = []
        for s in present:
            try:
                x = float(ex1[s].get(f) or float("nan"))
                y = float(ex2[s].get(f) if isinstance(ex2[s].get(f), str) else
                          float("nan") or float("nan"))
            except (TypeError, ValueError):
                continue
            if x == x and y == y:
                pairs.append((x, y))
        if len(pairs) < 2:
            lines.append(f"| {f} | {len(pairs)} | — | — |")
            continue
        a, b = zip(*pairs)
        icc = icc21(list(a), list(b))
        cont_results.append((f, icc, icc >= 0.90))
        lines.append(f"| {f} | {len(pairs)} | {icc:.3f} | "
                     f"{'YES' if icc >= 0.90 else 'no'} |")

    # overall pass/fail summary
    n_pass = sum(1 for _, k, ok in cat_results if ok)
    n_cont_pass = sum(1 for _, i, ok in cont_results if ok)
    lines += [
        "",
        "## Summary",
        "",
        f"- Categorical fields: {n_pass}/{len(cat_results)} pass kappa >= 0.80",
        f"- Continuous fields: {n_cont_pass}/{len(cont_results)} pass ICC >= 0.90",
        "",
        "**Exit criteria met:** " +
        ("YES" if (n_pass == len(cat_results) and n_cont_pass == len(cont_results))
         else "NO — reconcile below and re-run (Task 7.3.4)"),
    ]

    # disagreement examples (first 8 per field)
    lines += ["", "## Disagreement examples (first 8 per field, for reconciliation)", ""]
    for f in cat_fields:
        shown = 0
        for s in present:
            if shown >= 8:
                break
            v1 = ex1[s][f]
            v2 = ex2[s].get(f, "")
            if v1 != v2:
                lines.append(f"- `{s}` **{f}**: ex1=`{v1}` ex2=`{v2}`")
                shown += 1
        if shown == 0:
            lines.append(f"- {f}: no disagreements")

    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {REPORT_MD.name}")
    for f, k, ok in cat_results:
        print(f"  kappa {f}: {k:.3f} {'PASS' if ok else 'FAIL'}")
    for f, i, ok in cont_results:
        print(f"  icc   {f}: {i:.3f} {'PASS' if ok else 'FAIL'}")
    met = (n_pass == len(cat_results) and n_cont_pass == len(cont_results))
    print(f"  exit criteria: {'MET' if met else 'NOT MET'}")


if __name__ == "__main__":
    sys.exit(main())
