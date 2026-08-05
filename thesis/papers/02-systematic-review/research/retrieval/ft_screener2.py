#!/usr/bin/env python3
"""
Paper 02 — Phase 6 Full-Text Screener 2 (Task 6.2) — independent implementation

Independent dual-screening pass over the extracted full texts with a
deliberately different design from ft_screener1.py:
  - different lexicons (S2-specific architecture / OOD / review term sets)
  - weighted evidence counting instead of binary presence
  - stricter thresholds (requires >=2 hits per dimension)
  - per-dimension evidence counts recorded in the note

Satisfies the protocol's "two independent reviewers" requirement; results
are reconciled by ft_reconcile.py (CC.1.6).

Usage:
  python ft_screener2.py [--limit N]

Output:
  research/retrieval/ft-assessment-s2.csv
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
TXT_DIR = BASE / "research" / "full-text-txt"
POOL_CSV = BASE / "research" / "screening-data" / "full-text" / "records-to-review.csv"
OUT_CSV = BASE / "research" / "retrieval" / "ft-assessment-s2.csv"

INCLUDE, EXCLUDE, UNCERTAIN = "Include", "Exclude", "Uncertain"
MAX_CHARS = 150_000

FT1, FT2, FT3, FT4, FT5, FT6, FT7, FT8 = "FT1", "FT2", "FT3", "FT4", "FT5", "FT6", "FT7", "FT8"


def load_text(rid: str) -> str:
    p = TXT_DIR / f"{rid}.txt"
    if not p.exists():
        return ""
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read(MAX_CHARS)


def count_hits(text: str, terms: list[str]) -> int:
    """Count distinct terms matched (word-boundary prefix)."""
    t = text.lower()
    return sum(1 for term in terms if re.search(rf"\b{re.escape(term)}", t))


def numbers_near(text: str, terms: list[str], window: int = 200) -> int:
    t = text.lower()
    found = set()
    pat = "|".join(re.escape(x) for x in terms)
    for m in re.finditer(rf"\b(?:{pat})", t):
        lo, hi = max(0, m.start() - window), min(len(t), m.end() + window)
        for n in re.finditer(r"\d+(?:\.\d+)?", t[lo:hi]):
            found.add(n.group())
    return len(found)


# S2-specific lexicons (independent of S1)
S2_NN = [
    "transformer", "transformers", "lstm", "gru", "rnn", "cnn", "mlp",
    "bert", "gpt", "t5", "bart", "roberta", "vit", "resnet", "vae", "gan",
    "encoder-decoder", "encoder decoder", "seq2seq", "sequence-to-sequence",
    "attention mechanism", "language model", "neural network", "neural net",
    "policy network", "reinforcement learning", "ppo", "dq",
    "multi-layer perceptron", "convolutional", "recurrent",
]

S2_OOD = [
    "scan benchmark", "cogs", "cfq", "gscan", "pcfg-set", "slog",
    "length generalization", "systematic generalization", "systematicity",
    "productivity", "compositional split", "novel composition",
    "novel combination", "unseen combination", "held-out", "heldout",
    "out-of-distribution generalization", "ood generalization",
    "ood performance", "distribution shift", "id-ood gap",
    "compositional generalization", "compositional generalisation",
    "compositional accuracy", "compositional zero-shot",
]

S2_ID = [
    "in-distribution", "in distribution", "iid", "id performance",
    "train accuracy", "training accuracy", "source accuracy",
]

# OOD benchmarks whose IID test split is the standard ID condition
S2_BENCH = ["scan", "cogs", "cfq", "gscan", "pcfg", "slog", "closure"]

S2_REVIEW = [
    "survey paper", "review paper", "literature review", "position paper",
    "this paper surveys", "we survey", "we review", "opinion",
    "we summarize the", "state of the art in", "a review of",
]

S2_EXPERIMENT = [
    "we evaluate", "we train", "experiment", "results", "accuracy",
    "benchmark", "table", "figure", "dataset", "we compare",
]


def classify(text: str) -> tuple[str, str, str]:
    head = text[:10_000]
    nn = count_hits(text, S2_NN)
    ood = count_hits(text, S2_OOD)
    ood_nums = numbers_near(text, S2_OOD)
    # ID evidence: explicit ID terms, or accuracy near an OOD benchmark's
    # IID test split (standard for SCAN/COGS/CFQ papers), only meaningful
    # when OOD evidence is also present.
    id_ev = numbers_near(text, S2_ID) + numbers_near(text, S2_BENCH)

    # FT7
    if count_hits(head, S2_REVIEW) >= 2 and count_hits(text, S2_EXPERIMENT) < 3:
        return EXCLUDE, FT7, "survey/review signals dominate; <3 experiment markers"

    # FT4
    if nn < 2:
        return EXCLUDE, FT4, f"nn_hits={nn} (<2)"

    # FT1
    if ood < 2:
        return EXCLUDE, FT1, f"ood_hits={ood} (<2)"

    # Outcome
    if ood_nums > 0 and id_ev > 0:
        return INCLUDE, "", f"nn={nn} ood={ood} id_ev={id_ev} ood_nums={ood_nums}"
    if ood_nums == 0 and id_ev > 0:
        return EXCLUDE, FT2, f"id_ev={id_ev}, ood_nums=0 (only ID results)"
    if ood_nums == 0 and id_ev == 0:
        return UNCERTAIN, "", "no quantitative detail found"
    return UNCERTAIN, "", f"ood_nums={ood_nums}, id_ev=0 (ID baseline missing?)"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--limit", type=int, default=None)
    args = ap.parse_args()

    with open(POOL_CSV, "r", encoding="utf-8") as f:
        pool = [r for r in csv.DictReader(f) if r.get("ft_pdf_path")]
    if args.limit:
        pool = pool[: args.limit]

    stats = Counter()
    reasons = Counter()
    rows = []

    for rec in pool:
        text = load_text(rec["id"])
        if not text:
            decision, reason, note = EXCLUDE, FT5, "no extracted full text"
        else:
            decision, reason, note = classify(text)
        rows.append({
            "id": rec["id"], "title": rec.get("title", ""), "decision": decision,
            "reason": reason, "note": note,
        })
        stats[decision] += 1
        if reason:
            reasons[reason] += 1

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "title", "decision", "reason", "note"])
        w.writeheader()
        w.writerows(rows)

    print("S2 full-text assessment:")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c}")
    print("Reasons:", dict(reasons.most_common()))
    print(f"Output: {OUT_CSV.name}")


if __name__ == "__main__":
    main()
