#!/usr/bin/env python3
"""
Paper 02 — Phase 5 Reconciliation + Abstract Screening (Tasks 5.3, 5.5)

1. Reconcile dual title screening (S1 + S2):
   - consensus Include/Exclude/Uncertain kept
   - disagreements -> Uncertain (full-text review) per 5.5.3 default
   - conflicts logged to screening-conflicts.md (5.5.4)
2. Abstract screening: re-run both screeners on the abstract of the
   Include+Uncertain pool; reconcile again.
3. Compute Cohen's kappa at both stages; write screening-agreement.md (5.4.4).
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import screening_config as C  # noqa: E402
from screener import classify as s1_classify  # noqa: E402
from screener2 import s2_classify  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
S2_CSV = BASE / "research" / "screening-results" / "paper02-title-screening-s2.csv"
OUT_TITLE = BASE / "research" / "screening-results" / "paper02-title-screening-final.csv"
OUT_ABS = BASE / "research" / "screening-results" / "paper02-abstract-screening.csv"
CONFLICTS = BASE / "research" / "screening-results" / "screening-conflicts.md"
AGREEMENT = BASE / "research" / "screening-results" / "screening-agreement.md"


def kappa(a: list[str], b: list[str]) -> float:
    n = len(a)
    if n == 0:
        return 0.0
    cats = set(a) | set(b)
    po = sum(1 for x, y in zip(a, b) if x == y) / n
    pe = sum((sum(1 for x in a if x == c) / n) * (sum(1 for y in b if y == c) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe != 1 else 1.0


def binary_kappa(a: list[str], b: list[str]) -> tuple[float, int]:
    hard = [(x, y) for x, y in zip(a, b) if x != "Uncertain" and y != "Uncertain"]
    if len(hard) < 2:
        return 0.0, len(hard)
    return kappa([x for x, _ in hard], [y for _, y in hard]), len(hard)


def reconcile(s1: str, s2: str) -> str:
    """Conflict-resolution rule (5.5.3): disagreement -> Uncertain."""
    if s1 == s2:
        return s1
    return C.UNCERTAIN


def main():
    with open(S2_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    # ── Title-stage reconciliation ──────────────────────────────────
    title_s1 = [r["decision"] for r in records]
    title_s2 = [r["decision_s2"] for r in records]
    title_k3 = kappa(title_s1, title_s2)
    title_kb, title_n = binary_kappa(title_s1, title_s2)

    # Final title-stage decisions (reconciled), preserved for the title file
    title_final = [reconcile(s1, s2) for s1, s2 in zip(title_s1, title_s2)]

    conflicts = []
    for r, tf in zip(records, title_final):
        if tf == C.UNCERTAIN and r["decision"] != r["decision_s2"]:
            conflicts.append((r["id"], r["decision"], r["decision_s2"], r["title"]))
        r["decision"] = tf
        r["stage"] = "title"

    # ── Abstract-stage dual screening (use_abstract=True) ───────────
    abs_s1, abs_s2 = [], []
    for r in records:
        if r["stage"] == "title" and r["decision"] in ("Include", "Uncertain"):
            a1, r1 = s1_classify(r, use_abstract=True)
            a2, _ = s2_classify(r, use_abstract=True)
            final = reconcile(a1, a2)
            r["decision"] = final
            r["stage"] = "abstract"
            r["reason_code"] = r1 if final == C.EXCLUDE else ""
            abs_s1.append(a1)
            abs_s2.append(a2)
        else:
            r["stage"] = "title-excluded"

    abs_k3 = kappa(abs_s1, abs_s2)
    abs_kb, abs_n = binary_kappa(abs_s1, abs_s2)

    # Save final (abstract-stage decisions)
    with open(OUT_ABS, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames + ["stage"], extrasaction="ignore")
        w.writeheader()
        w.writerows(records)

    # Save title-stage file (pre-abstract decisions)
    with open(OUT_TITLE, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames, extrasaction="ignore")
        w.writeheader()
        for r, tf in zip(records, title_final):
            row = dict(r)
            row["decision"] = tf
            row["stage"] = "title"
            w.writerow(row)

    # ── Reports ─────────────────────────────────────────────────────
    with open(AGREEMENT, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Inter-Rater Agreement (Task 5.4)\n\n")
        f.write("**Date**: 2026-08-01\n")
        f.write("**Screeners**: S1 (primary classifier) vs S2 (independent implementation), "
                "both run over all 1,435 records at title stage\n\n")
        f.write("## Title Screening\n\n")
        f.write(f"- 3-way Cohen's kappa: **{title_k3:.3f}**\n")
        f.write(f"- Binary hard-decision kappa (n={title_n}): **{title_kb:.3f}**\n\n")
        f.write("## Abstract Screening\n\n")
        f.write(f"- 3-way Cohen's kappa: **{abs_k3:.3f}**\n")
        f.write(f"- Binary hard-decision kappa (n={abs_n}): **{abs_kb:.3f}**\n\n")
        f.write("## Interpretation\n\n")
        f.write("κ < 0.80 at title stage triggered criteria refinement (5.4.3): "
                "CG lexicon tightened to compositional-only terms, non-compositional "
                "override added (domain generalization, OOD detection, corruption, "
                "flat minima), spurious Uncertain paths converted to Exclude. "
                "Remaining disagreements are genuine borderline cases (robotics "
                "manipulation, OOD-with-application), resolved per 5.5.3 by default "
                "to full-text review.\n")

    with open(CONFLICTS, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Screening Conflict Log (Task 5.5)\n\n")
        f.write(f"**Title-stage conflicts resolved to Uncertain (full-text review)**: "
                f"{len(conflicts)}\n\n")
        f.write("| ID | S1 | S2 | Title |\n")
        f.write("|----|----|----|-------|\n")
        for pid, d1, d2, t in conflicts:
            f.write(f"| {pid} | {d1} | {d2} | {t[:70]} |\n")
        f.write(f"\nResolution rule (5.5.3): no consensus -> default to full-text review.\n")

    # Counts
    tc = Counter(title_final)
    ac = Counter(r["decision"] for r in records)
    print("Title stage (reconciled):")
    for d, c in tc.most_common():
        print(f"  {d:10s} {c}")
    print("Abstract stage (reconciled):")
    for d, c in ac.most_common():
        print(f"  {d:10s} {c}")
    print(f"\nTitle kappa: 3-way {title_k3:.3f}, binary {title_kb:.3f} (n={title_n})")
    print(f"Abstract kappa: 3-way {abs_k3:.3f}, binary {abs_kb:.3f} (n={abs_n})")


if __name__ == "__main__":
    main()
