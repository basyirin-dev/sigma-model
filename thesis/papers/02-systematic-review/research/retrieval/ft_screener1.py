#!/usr/bin/env python3
"""
Paper 02 — Phase 6 Full-Text Screener 1 (Task 6.2)

Deterministic rule-cascade full-text eligibility assessor (S1). Applies the
PICO criteria to the extracted full text and codes each retrieved record:

  P  does the study train neural networks?                 -> else FT4
  I/C does it report OOD/compositional generalization?     -> else FT1
  O  quantitative results for BOTH ID and OOD?             -> FT2 (ID only)
                                                              FT3 (no numbers)
  FT7 review/opinion without original results
  else Include / Uncertain (flag for discussion)

S2 (ft_screener2.py) is an independent implementation with different
lexicons and thresholds; ft_reconcile.py combines them (CC.1.6).

Records without retrieved full text are NOT assessed here — the reconcile
step codes them Exclude FT5 (task 6.1.4/6.2.4).

Usage:
  python ft_screener1.py [--limit N]

Output:
  research/retrieval/ft-assessment-s1.csv
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
TXT_DIR = BASE / "research" / "full-text-txt"
POOL_CSV = BASE / "research" / "screening-data" / "full-text" / "records-to-review.csv"
OUT_CSV = BASE / "research" / "retrieval" / "ft-assessment-s1.csv"

INCLUDE, EXCLUDE, UNCERTAIN = "Include", "Exclude", "Uncertain"
MAX_CHARS = 150_000

# FT codes (per phases/06_full_text.md Task 6.2.4)
FT1, FT2, FT3, FT4, FT5, FT6, FT7, FT8 = "FT1", "FT2", "FT3", "FT4", "FT5", "FT6", "FT7", "FT8"


def load_text(rid: str) -> str:
    p = TXT_DIR / f"{rid}.txt"
    if not p.exists():
        return ""
    with open(p, "r", encoding="utf-8", errors="replace") as f:
        return f.read(MAX_CHARS)


def hits(text: str, terms: list[str]) -> list[str]:
    """Word-boundary-prefix hits (Phase 5 token_hits style)."""
    t = text.lower()
    out = []
    for term in terms:
        if re.search(rf"\b{re.escape(term)}", t):
            out.append(term)
    return out


def numbers_near(text: str, terms: list[str], window: int = 160) -> int:
    """Count distinct numeric tokens within `window` chars of any term."""
    t = text.lower()
    found = set()
    for m in re.finditer(rf"\b(?:{'|'.join(re.escape(x) for x in terms)})", t):
        lo, hi = max(0, m.start() - window), min(len(t), m.end() + window)
        for n in re.finditer(r"\d+(?:\.\d+)?", t[lo:hi]):
            found.add(n.group())
    return len(found)


# S1 lexicons
NN_TERMS = [
    "neural network", "neural net", "deep learning", "deep net", "transformer",
    "lstm", "rnn", "gru", "cnn", "mlp", "bert", "gpt", "t5", "word2vec",
    "encoder-decoder", "seq2seq", "sequence-to-sequence", "attention",
    "language model", "language models", "llm", "backpropagation", "back-prop",
    "gradient descent", "adam", "sgd", "fine-tun", "pretrain", "pre-train",
    "reinforcement learning", "policy gradient", "ppo", "dqn",
    "convolutional", "recurrent", "resnet", "vit", "vae", "gan", "diffusion",
]

OOD_TERMS = [
    "out-of-distribution", "out of distribution", "ood generalization",
    "ood performance", "ood accuracy", "compositional generalization",
    "compositional generalisation", "systematic generalization",
    "systematic generalisation", "length generalization",
    "compositional split", "held-out", "held out", "unseen combination",
    "novel composition", "novel combination", "recombina",
    "systematicity", "id-ood", "zero-shot", "distribution shift",
]

ID_TERMS = [
    "in-distribution", "in distribution", "id accuracy", "iid",
    "train accuracy", "training accuracy", "seen accuracy",
]

REVIEW_TERMS = [
    "this survey", "this review", "we review", "we survey", "review of",
    "position paper", "opinion paper", "we summarize", "categorize",
    "taxonomy of", "overview of",
]

EXPERIMENT_TERMS = [
    "experiment", "we evaluate", "we train", "results on", "baseline",
    "accuracy", "benchmark", "evaluation", "our method", "we propose",
]

BENCHMARK_TERMS = [
    "scan", "cogs", "cfq", "gscan", "pcfg", "slog", "cocogen",
    "closure", "navigate", "emergent", "compositional task",
]


def classify(text: str) -> tuple[str, str, str]:
    """Return (decision, reason, note) for one extracted full text."""
    head = text[:12_000]

    # 1. FT7: review/opinion without original results
    if hits(head, REVIEW_TERMS) and not hits(text, EXPERIMENT_TERMS):
        return EXCLUDE, FT7, "review/opinion markers; no experiment markers"

    # 2. FT4: population — neural network models?
    nn = hits(text, NN_TERMS)
    if not nn:
        return EXCLUDE, FT4, "no neural-network markers in full text"

    # 3. FT1: intervention — OOD/compositional split reported?
    ood = hits(text, OOD_TERMS)
    if not ood:
        return EXCLUDE, FT1, "no OOD/compositional split vocabulary"

    # 4. Outcome: quantitative results for both ID and OOD?
    id_nums = numbers_near(text, ID_TERMS)
    ood_nums = numbers_near(text, OOD_TERMS)
    bench = hits(text, BENCHMARK_TERMS)

    if id_nums > 0 and ood_nums == 0:
        return EXCLUDE, FT2, "only in-distribution numbers found"
    if id_nums == 0 and ood_nums == 0:
        if not bench:
            return UNCERTAIN, "", "OOD terms present but no quantitative detail"
        return EXCLUDE, FT3, "no extractable accuracy numbers"

    # 5. Compositional signal strength: OOD vocab without any benchmark/
    #    split context or numbers is ambiguous -> flag for discussion.
    if ood_nums == 0 and not bench:
        return UNCERTAIN, "", "OOD split mentioned but no numbers/benchmark"
    if not bench and len(ood) <= 2:
        return UNCERTAIN, "", f"weak OOD evidence ({ood})"

    return INCLUDE, "", f"nn={len(nn)} ood={len(ood)} id_nums={id_nums} ood_nums={ood_nums}"


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
            # no extracted text: handled by reconcile as FT5
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

    print("S1 full-text assessment:")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c}")
    print("Reasons:", dict(reasons.most_common()))
    print(f"Output: {OUT_CSV.name}")


if __name__ == "__main__":
    main()
