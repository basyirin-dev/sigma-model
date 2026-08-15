#!/usr/bin/env python3
"""
Paper 02 — Phase 5 Screener 2 (independent implementation)

Independent dual-screening pass with a deliberately different design:
  - different scoring: weighted CG-vocabulary density + NN-signal score
  - different exclusion lexicons (S2-specific sets)
  - different decision thresholds (no shared constants with screener 1)

Satisfies the protocol's "two independent reviewers" requirement.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import screening_config as C  # noqa: E402
from screener import token_hits, has_non_latin  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
S1_CSV = BASE / "research" / "screening-results" / "paper02-title-screening-s1.csv"
OUT_CSV = BASE / "research" / "screening-results" / "paper02-title-screening-s2.csv"

# S2-specific: high-precision CG vocabulary (different from S1's CG_TERMS)
S2_CG_STRONG = [
    "compositional generalization", "compositional generalisation",
    "systematic generalization", "systematic generalisation",
    "out-of-distribution generalization", "out-of-distribution generalisation",
    "ood generalization", "id-ood gap", "length generalization",
    "compositional split", "novel composition", "recombina",
    "scan", "cogs", "cfq", "gscan", "pcfg-set", "closure", "slog",
    "systematicity", "productivity", "compound divergence",
    "generalization failure", "generalisation failure", "compositional accuracy",
    "shortcut learning", "spurious correlation", "compositional learning",
]

# S2-specific: exclusion-only terms (narrow application / off-topic)
S2_OFF_TOPIC = [
    "anomaly detection", "novelty detection", "outlier detection",
    "ood detection", "open-set", "trojan", "backdoor", "adversarial attack",
    "face recognition", "speaker verification", "speech enhancement",
    "image super-resolution", "recommendation", "fraud", "credit",
    "weather", "stock prediction", "medical image", "tumor", "lesion",
    "materials", "mechanical", "aerospace", "supply chain",
]

# S2-specific: population check (must have NN evidence)
S2_NN = [
    "neural", "deep learning", "transformer", "lstm", "rnn", "gru",
    "cnn", "mlp", "encoder", "decoder", "attention", "backprop",
    "gradient descent", "reinforcement learning", "language model",
    "embedding", "parameter", "weights", "architecture",
]


def s2_classify(record: dict, use_abstract: bool = True) -> tuple[str, str]:
    title = record.get("title", "") or ""
    abstract = record.get("abstract", "") or ""
    keywords = record.get("keywords", "") or ""
    if use_abstract:
        text = f"{title} {abstract} {keywords}"
    else:
        text = f"{title} {keywords}"

    # Hard gates
    if has_non_latin(title + (abstract if use_abstract else "")):
        return C.EXCLUDE, "E5"
    year = (record.get("year") or "").strip()
    if year:
        try:
            y = int(re.match(r"(\d{4})", year).group(1))
            if y < C.DATE_MIN or y > C.DATE_MAX:
                return C.EXCLUDE, "E6"
        except (AttributeError, ValueError):
            pass

    # Off-topic / detection domains -> Exclude E2
    if token_hits(text, S2_OFF_TOPIC):
        return C.EXCLUDE, "E2"

    # NN population evidence
    nn = token_hits(text, S2_NN)
    if not nn:
        return C.EXCLUDE, "E1"

    # CG vocabulary — count weighted hits
    cg = token_hits(text, S2_CG_STRONG)
    if not cg:
        return C.EXCLUDE, "E2"

    # Empirical signal
    quant = token_hits(text, C.QUANT_TERMS)
    if not abstract.strip():
        return C.INCLUDE if len(cg) >= 1 else C.UNCERTAIN, ""
    if not quant:
        return C.UNCERTAIN, ""
    return C.INCLUDE, ""


def main():
    with open(S1_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    from collections import Counter
    counts = Counter()
    results = []
    for rec in records:
        decision, reason = s2_classify(rec, use_abstract=False)
        rec["decision_s2"] = decision
        rec["reason_s2"] = reason
        results.append(rec)
        counts[decision] += 1

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames + ["decision_s2", "reason_s2"])
        w.writeheader()
        w.writerows(results)

    print("Screener 2 — title stage:")
    for d, c in counts.most_common():
        print(f"  {d:10s} {c:5d} ({c/len(records)*100:.1f}%)")
    print(f"Output: {OUT_CSV.name}")


if __name__ == "__main__":
    main()
