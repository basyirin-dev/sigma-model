#!/usr/bin/env python3
"""
Paper 01 — Phase 7: validation metrics (Task 7.3.2/7.3.3, CC.1.6).

Compares extractor 1 (heuristic charted-data.csv) against extractor 2
(independent implementation validation-extractor2.csv) on the 20% sample:
  - Cohen's kappa + raw agreement per categorical field
  - per-category kappa for multi-value fields (subdomains, frameworks)
  - ICC(2,1) for continuous field relevance_sigma_trap
  - disagreement examples for the reconciliation log

The external-AI pass on the sample plugs in the same way: drop its output
for sample papers into ai-prompt-batches/ai-output/ (merge_ai.py applies
it), then re-run this script. Run with `--ai` after merging to compute the
relevance_sigma_trap ICC as heuristic-seed vs post-AI value over the sample
(extractor2 does not chart the continuous field, so seed->AI is the rater
pair per Task 7.3.3) and to report AI revisions on the sample.

Output: research/charting/validation-report.md
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
SAMPLE_CSV = BASE / "research" / "charting" / "validation-sample.csv"
EX2_CSV = BASE / "research" / "charting" / "validation-extractor2.csv"
REPORT_MD = BASE / "research" / "charting" / "validation-report.md"
BATCH_DIR = BASE / "research" / "charting" / "ai-prompt-batches"

sys.path.insert(0, str(BASE / "research" / "screening"))
from calibration import cohen_kappa  # noqa: E402

CAT_FIELDS = ["publication_type", "methodology",
              "discusses_internal_representations", "discusses_schema_coherence",
              "limitations_stated"]
MULTI_FIELDS = ["subdomains", "formal_framework", "mathematical_formalism"]
CONT_FIELDS = ["relevance_sigma_trap"]


def icc21(a: list[float], b: list[float]) -> float:
    """ICC(2,1) two-way random, single measures (ANOVA-based).

    Variance components are clamped to >= 0: integer ordinal ratings with no
    within-subject disagreement (e.g. seed == post-AI everywhere) make the
    ANOVA error term negative/zero, so the raw ratio is meaningless — such
    degenerate inputs return 1.0 (perfect agreement).
    """
    n = len(a)
    pairs = list(zip(a, b))
    k = 2
    gm = sum(x for p in pairs for x in p) / (n * k)
    ss_total = sum((x - gm) ** 2 for p in pairs for x in p)
    ss_rows = sum(sum(p) ** 2 for p in pairs) / k - n * gm * gm
    ss_cols = (sum(a) ** 2 + sum(b) ** 2) / n - n * k * gm * gm
    ss_err = ss_total - ss_rows - ss_cols
    ss_rows, ss_err = max(0.0, ss_rows), max(0.0, ss_err)
    df_r, df_c, df_e = n - 1, k - 1, (n - 1) * (k - 1)
    ms_r, ms_c, ms_e = ss_rows / df_r, ss_cols / df_c, ss_err / df_e
    denom = ms_r + ms_c + ms_e
    return (ms_r - ms_e) / denom if denom else 1.0


def split_multi(v: str) -> set[str]:
    return {x.strip() for x in (v or "").split(";") if x.strip()}


def main() -> None:
    sample = [r["paper_id"] for r in csv.DictReader(open(SAMPLE_CSV, newline="", encoding="utf-8"))]
    ex1 = {r["paper_id"]: r for r in
           csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8"))}
    ex2 = {r["paper_id"]: r for r in csv.DictReader(open(EX2_CSV, newline="", encoding="utf-8"))}

    ai_mode = "--ai" in sys.argv
    seeds: dict[str, str] = {}
    if ai_mode:
        for bf in BATCH_DIR.glob("batch-*.jsonl"):
            for line in bf.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line:
                    continue
                obj = json.loads(line)
                seeds[obj["paper_id"]] = obj.get("relevance_seed")

    lines: list[str] = [
        "# Extraction validation report — Paper 01 Phase 7 (CC.1.6)",
        "",
        f"- Sample: **{len(sample)}** papers (20%, seed=20260901)",
        "- Extractor 1: scripted heuristic (`heuristic.py`)",
        "- Extractor 2: independent implementation (`extractor2.py`)",
        "- External-AI pass on the sample: user-run (see README); AI revisions",
        "  already merged into `charted-data.csv` via `merge_ai.py` are included",
        "  in extractor-1 values where applied.",
    ]
    if ai_mode:
        lines += [
            "- ICC mode `--ai`: `relevance_sigma_trap` compared as heuristic seed",
            "  vs post-AI value over the sample (extractor2 charts no continuous",
            "  field; rater pair seed->AI per Task 7.3.3).",
        ]
    lines += ["", "## Categorical fields (Cohen's kappa)", "",
              "| Field | n | Raw agreement | Cohen's kappa |",
              "|---|---|---|---|"]
    kappas: dict[str, float] = {}

    def add_kappa(field: str, a: list[str], b: list[str], label: str) -> None:
        n = len(a)
        raw = sum(1 for x, y in zip(a, b) if x == y) / n
        k = cohen_kappa(a, b) if n else 0.0
        kappas[label] = k
        lines.append(f"| {label} | {n} | {raw:.3f} | {k:.3f} |")

    for f in CAT_FIELDS:
        a = [ex1[p][f] for p in sample]
        b = [ex2[p][f] for p in sample]
        add_kappa(f, a, b, f)

    # multi-value fields: per-category presence kappa
    for f in MULTI_FIELDS:
        buckets: set[str] = set()
        for p in sample:
            buckets |= split_multi(ex1[p][f]) | split_multi(ex2[p][f])
        for bucket in sorted(buckets):
            a = ["1" if bucket in split_multi(ex1[p][f]) else "0" for p in sample]
            b = ["1" if bucket in split_multi(ex2[p][f]) else "0" for p in sample]
            add_kappa(f, a, b, f"{f}::{bucket}")

    # continuous fields (ICC) — relevance is seed + AI-revised. In --ai mode
    # (after the external-AI pass on the sample) compare heuristic seed vs the
    # post-AI charted value; otherwise report as pending (extractor2 charts no
    # continuous field).
    lines += ["", "## Continuous fields (ICC(2,1))", "", "| Field | n | ICC |", "|---|---|---|"]
    for f in CONT_FIELDS:
        if ai_mode:
            pairs = []
            n_rev = 0
            for p in sample:
                seed, val = seeds.get(p), ex1[p].get(f)
                try:
                    x, y = float(seed or float("nan")), float(val or float("nan"))
                except (TypeError, ValueError):
                    continue
                if x == x and y == y:
                    pairs.append((x, y))
                    if seed != val:
                        n_rev += 1
            if pairs:
                a, b = zip(*pairs)
                icc = icc21(list(a), list(b))
                lines.append(
                    f"| {f} | {len(pairs)} | {icc:.3f} | "
                    f"(seed vs post-AI; {n_rev} sample revisions)"
                )
            else:
                lines.append(f"| {f} | — | no numeric pairs |")
            continue
        if f not in ex2[next(iter(ex2))]:
            lines.append(f"| {f} | — | pending external-AI pass on sample |")
            continue
        pairs = []
        for p in sample:
            try:
                x, y = float(ex1[p][f] or float("nan")), float(ex2[p][f] or float("nan"))
                if x == x and y == y:
                    pairs.append((x, y))
            except ValueError:
                pass
        if pairs:
            a, b = zip(*pairs)
            icc = icc21(list(a), list(b))
            lines.append(f"| {f} | {len(pairs)} | {icc:.3f} |")

    # disagreement examples (first 10 per field)
    lines += ["", "## Disagreement examples (first 8 per field, for reconciliation)", ""]
    for f in CAT_FIELDS + MULTI_FIELDS:
        shown = 0
        for p in sample:
            if shown >= 8:
                break
            v1, v2 = ex1[p][f], ex2[p][f]
            if v1 != v2:
                t = ex1[p]["title"][:70]
                lines.append(f"- `{p}` **{f}**: ex1=`{v1}` ex2=`{v2}` — {t}")
                shown += 1
        if shown == 0:
            lines.append(f"- {f}: no disagreements")

    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")

    print(f"wrote {REPORT_MD.name}")
    for label, k in kappas.items():
        print(f"  kappa {label}: {k:.3f}")


if __name__ == "__main__":
    sys.exit(main())
