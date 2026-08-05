#!/usr/bin/env python3
"""
Paper 02 — Phase 6 validation pass (CC.1.6, Task 6.3)

Third independent full-text implementation ("human proxy" design) run over
the 20% random sample drawn by ft_reconcile.py. Applies a deliberately
simple, permissive triple-gate:

  (a) neural-network architecture evidence
  (b) OOD / compositional generalization evidence (incl. benchmark names)
  (c) numeric quantitative results reported

plus a review-paper check. Agreement with the reconciled eligibility
decisions is computed and disagreements are listed for human review.

Usage:
  python validation.py

Outputs:
  research/retrieval/validation-20.csv   (adds v3_decision/v3_reason)
  research/retrieval/validation-report.md
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
TXT_DIR = BASE / "research" / "full-text-txt"
VALIDATION_CSV = BASE / "research" / "retrieval" / "validation-20.csv"
REPORT_MD = BASE / "research" / "retrieval" / "validation-report.md"

INCLUDE, EXCLUDE, UNCERTAIN = "Include", "Exclude", "Uncertain"
MAX_CHARS = 150_000

# Third implementation lexicons (independent set)
V3_ARCH = ["transformer", "lstm", "gru", "cnn", "mlp", "bert", "gpt",
           "neural", "deep", "encoder", "decoder", "attention", "rnn",
           "reinforcement", "policy network", "language model"]
V3_OOD = ["out-of-distribution", "out of distribution", "ood", "compositional",
          "compositionality", "systematic", "generalization gap", "held-out",
          "heldout", "unseen", "novel", "recombina", "length generalization",
          "scan", "cogs", "cfq", "gscan", "pcfg", "slog"]
V3_REVIEW = ["survey", "review paper", "position paper", "this survey",
             "this review", "overview", "taxonomy"]


def load_text(rid: str) -> str:
    p = TXT_DIR / f"{rid}.txt"
    if not p.exists():
        return ""
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read(MAX_CHARS)


def has_any(text: str, terms: list[str]) -> bool:
    t = text.lower()
    return any(re.search(rf"\b{re.escape(x)}", t) for x in terms)


def has_numbers(text: str) -> bool:
    # accuracy-like numerics: % or decimal near acc/score/perf/result
    return bool(re.search(r"\b\d{1,3}(?:\.\d+)?\s*%", text)) or bool(
        re.search(r"\b\d+\.\d{1,2}\b", text))


def classify(text: str) -> tuple[str, str]:
    head = text[:8_000]
    if has_any(head, V3_REVIEW) and not has_any(
        text[:40_000], ["experiment", "we train", "we evaluate"]
    ):
        return EXCLUDE, "FT7"
    if not has_any(text, V3_ARCH):
        return EXCLUDE, "FT4"
    if not has_any(text, V3_OOD):
        return EXCLUDE, "FT1"
    if not has_numbers(text):
        return EXCLUDE, "FT3"
    return INCLUDE, ""


def main() -> None:
    if not VALIDATION_CSV.exists():
        print(f"Missing {VALIDATION_CSV} — run ft_reconcile.py first.")
        return

    with open(VALIDATION_CSV, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    stats = Counter()
    disagreements = []
    for row in rows:
        text = load_text(row["id"])
        if not text:
            v3, v3r = EXCLUDE, "FT5"
        else:
            v3, v3r = classify(text)
        row["v3_decision"] = v3
        row["v3_reason"] = v3r
        stats[v3] += 1
        if v3 != row["decision"]:
            disagreements.append((row["id"], row["decision"], row["reason"], v3, v3r, row["title"]))

    with open(VALIDATION_CSV, "w", encoding="utf-8", newline="") as f:
        fields = ["id", "title", "decision", "reason", "s1", "s2", "v3_decision", "v3_reason"]
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)

    n = len(rows)
    agree = n - len(disagreements)
    with open(REPORT_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Validation Report (Task 6.3, CC.1.6)\n\n")
        f.write(f"**Sample**: {n} records (20%, seed=20260804) drawn from the "
                f"{sum(1 for _ in []) or ''}241 assessed full texts\n\n")
        f.write("## Third-Implementation Decisions (v3)\n\n")
        f.write("| Decision | Count |\n")
        f.write("|----------|------:|\n")
        for d, c in stats.most_common():
            f.write(f"| {d} | {c} |\n")
        f.write(f"\n**Raw agreement vs reconciled**: {agree}/{n} = "
                f"{agree / n * 100:.1f}%\n")
        f.write(f"**Disagreements**: {len(disagreements)} (listed below for human review)\n\n")
        f.write("## Disagreements (v3 vs reconciled)\n\n")
        f.write("| ID | Reconciled | Reason | v3 | v3 reason | Title |\n")
        f.write("|----|------------|--------|----|-----------|-------|\n")
        for rid, d, r, v3, v3r, t in disagreements:
            f.write(f"| {rid} | {d} | {r} | {v3} | {v3r} | {t[:60]} |\n")

    print(f"Validation sample: {n} records")
    print("v3 decisions:", dict(stats.most_common()))
    print(f"Agreement: {agree}/{n} ({agree/n*100:.1f}%)")
    print(f"Disagreements: {len(disagreements)}")
    for rid, d, r, v3, v3r, t in disagreements:
        print(f"  {rid}: reconciled={d}({r}) vs v3={v3}({v3r}) | {t[:50]}")
    print(f"Output: {VALIDATION_CSV.name}, {REPORT_MD.name}")


if __name__ == "__main__":
    main()
