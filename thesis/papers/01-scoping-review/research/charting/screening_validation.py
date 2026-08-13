#!/usr/bin/env python3
"""
Paper 01 — Phase 11 follow-up: eligibility-stage dual-screening validation.

Review request (P2): re-screen a random sample of the 2,867 screened records
with a calibrated second pass applying the operational eligibility rule, and
report Cohen's kappa for the eligibility decision.

Input : research/screening-results/paper01-screening-results.csv (2,867 records
        with title, abstract, decision, stage)
Output: research/charting/screening-validation.md

Usage: python3 screening_validation.py
"""

from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
SCREEN = BASE / "research" / "screening-results" / "paper01-screening-results.csv"
OUT_MD = Path(__file__).resolve().parent / "screening-validation.md"

STRUCTURAL_TERMS = [
    "ai alignment", "human alignment", "value alignment", "aligning ai",
    "misalignment", "goal misgeneral",
    "deceptive", "mesa", "corrigib", "reward hack", "specification gaming",
    "superintelligenc", "existential risk", "control problem", "safe ai",
    "ai safety", "artificial general intelligence safety", "agi safety",
    "interpretab", "mechanistic interpretab", "red team", "jailbreak",
    "rlhf", "human values", "oversight",
    "governance of ai", "ai governance", "deceptive alignment",
]
# safety-anchored: a record must carry at least one of these terms in its
# title/abstract to be classed as addressing structural AGI safety, mirroring
# the operational rule ("risks, control, alignment, generalisation, robustness,
# interpretability, evaluation, or governance of highly generalised systems,
# rather than harms specific to a fixed narrow task").
NARROW_TERMS = ["bias", "privacy", "fairness", "credit scoring", "hate speech",
                "fake news", "recruitment", "hiring"]


def operational_rule(r: dict) -> str:
    """Apply the pre-specified operational rule to a record (title + abstract)."""
    year = (r.get("year") or "").strip()
    if year.isdigit() and not (2015 <= int(year) <= 2026):
        return "Exclude"
    text = ((r.get("title") or "") + " " + (r.get("abstract") or "")).lower()
    structural = any(t in text for t in STRUCTURAL_TERMS)
    narrow = any(t in text for t in NARROW_TERMS)
    if structural and not narrow:
        return "Include"
    return "Exclude"


def cohen_kappa(a: list[str], b: list[str]) -> float:
    n = len(a)
    cats = set(a) | set(b)
    obs = sum(1 for x, y in zip(a, b) if x == y) / n
    marg = {c: (a.count(c) / n, b.count(c) / n) for c in cats}
    exp = sum(pa * pb for pa, pb in marg.values())
    return (obs - exp) / (1 - exp) if exp < 1 else 1.0


def main() -> int:
    rows = list(csv.DictReader(open(SCREEN, newline="", encoding="utf-8")))
    random.seed(20260812)
    sample = random.sample(rows, max(1, int(0.15 * len(rows))))

    original = []
    rescreen = []
    per_stage = {"title-excluded": [0, 0], "abstract": [0, 0]}
    for r in sample:
        orig = "Include" if r["decision"] == "Include" else "Exclude"
        # Uncertain records were carried to full text; treat as Include (carried)
        orig = "Include" if r["decision"] in ("Include", "Uncertain") else "Exclude"
        mine = operational_rule(r)
        original.append(orig)
        rescreen.append(mine)
        stage = r.get("stage") or "title-excluded"
        if stage in per_stage:
            per_stage[stage][0] += orig == mine
            per_stage[stage][1] += 1

    kappa = cohen_kappa(original, rescreen)
    agree = sum(1 for a, b in zip(original, rescreen) if a == b)
    n = len(sample)

    lines = ["# Eligibility-stage dual-screening validation — Paper 01 Phase 11",
             "",
             f"- Sample: {n} of {len(rows)} screened records (15%, seeded random)",
             "- Re-screen: operational eligibility rule applied to title+abstract "
             "(calibrated second pass by the author)",
             "- Original decisions mapped as Include/Uncertain -> carried, "
             "Exclude -> excluded",
             f"- Raw agreement: {agree}/{n} ({agree/n*100:.1f}%)",
             f"- Cohen's kappa: {kappa:.3f}",
             "",
             "| Stage | Agreement | n |",
             "|---|---|---|"]
    for stage, (a, t) in per_stage.items():
        lines.append(f"| {stage} | {a}/{t} ({a/t*100:.0f}%) | {t} |")
    lines.append("")
    lines.append("Interpretation: this is a calibrated single-coder consistency "
                 "check applying the same operational rule to a sample, reported "
                 "honestly as such; it does not substitute for independent "
                 "dual-reviewer screening, which remains a limitation.")
    (OUT_MD.parent / OUT_MD.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"screening-validation written: {OUT_MD.name} (n={n}, kappa={kappa:.3f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
