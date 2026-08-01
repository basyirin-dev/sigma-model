#!/usr/bin/env python3
"""
Paper 02 — Phase 5 Screener 1 (primary deterministic classifier)

Applies PICO I/E criteria per screening_config.py:
  1. E6 date check (2017-2026)
  2. E5 language check
  3. E2 OOD-detection disambiguation (exclude detection/anomaly papers)
  4. E1 population check (neural network markers)
  5. E2 intervention/outcome check (CG/OOD vocabulary)
  6. E3 opinion check
  -> Include / Exclude(E-code) / Uncertain
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import screening_config as C  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
SCREENING_CSV = BASE / "research" / "clean-library" / "paper02-screening.csv"
OUT_CSV = BASE / "research" / "screening-results" / "paper02-title-screening-s1.csv"
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)

AI_SHORT = ["llm", "llms", "gpt", "bert", "t5", "rnn", "lstm", "gru", "cnn", "mlp", "ood"]


def has_non_latin(text: str) -> bool:
    for ch in text:
        cp = ord(ch)
        for lo, hi in C.NON_LATIN_RANGES:
            if lo <= cp <= hi:
                return True
    return False


def token_hits(text: str, patterns: list[str]) -> list[str]:
    """Word-boundary-aware pattern matching."""
    t = text.lower()
    hits = []
    for p in patterns:
        if p in AI_SHORT:
            if re.search(rf"\b{re.escape(p)}\b", t):
                hits.append(p)
        else:
            if re.search(rf"\b{re.escape(p)}", t):
                hits.append(p)
    return hits


def classify(record: dict, use_abstract: bool = True) -> tuple[str, str]:
    """Return (decision, reason_code).

    use_abstract=False: title+keywords only (title-screening stage).
    use_abstract=True:  title+abstract+keywords (abstract-screening stage).
    """
    title = record.get("title", "") or ""
    abstract = record.get("abstract", "") or ""
    keywords = record.get("keywords", "") or ""
    if use_abstract:
        combined = f"{title} {abstract} {keywords}"
    else:
        combined = f"{title} {keywords}"

    # 1. E6 date check
    year_str = (record.get("year") or "").strip()
    if year_str:
        try:
            y = int(re.match(r"(\d{4})", year_str).group(1))
            if y < C.DATE_MIN or y > C.DATE_MAX:
                return C.EXCLUDE, "E6"
        except (AttributeError, ValueError):
            pass

    # 2. E5 language check
    if has_non_latin(title + (abstract if use_abstract else "")):
        return C.EXCLUDE, "E5"

    # 3. E2 OOD-detection disambiguation (critical pilot finding)
    if token_hits(combined, C.OOD_DETECTION_TERMS):
        # Exclude unless strong CG/vocabulary co-occurs with a benchmark
        if not token_hits(combined, ["compositional", "systematic", "scan", "cogs", "cfq",
                                     "generalization failure", "generalisation failure"]):
            return C.EXCLUDE, "E2"

    # 4. E1 population check: neural network markers
    nn_hits = token_hits(combined, C.NN_TERMS)
    if not nn_hits:
        # Non-NN domain markers -> E1
        if token_hits(combined, C.NON_NN_DOMAINS):
            return C.EXCLUDE, "E1"
        # No NN markers: if non-compositional/application terms dominate -> E2,
        # else defer to abstract (may clarify NN usage)
        if token_hits(combined, C.NON_COMPOSITIONAL_TERMS):
            return C.EXCLUDE, "E2"
        return C.UNCERTAIN, ""  # maybe NN implied; abstract may clarify

    # 5. E2 intervention/outcome check: CG/OOD vocabulary
    cg_hits = token_hits(combined, C.CG_TERMS)
    if not cg_hits:
        return C.EXCLUDE, "E2"

    # 5b. Non-compositional override (calibration): domain generalization,
    #     OOD detection, corruption robustness, flat minima, transfer
    #     learning, narrow applications -> E2 unless a compositional
    #     benchmark/term strongly dominates (CG hit count > non-CG hits).
    non_cg_hits = token_hits(combined, C.NON_COMPOSITIONAL_TERMS)
    if non_cg_hits and len(cg_hits) <= len(non_cg_hits):
        return C.EXCLUDE, "E2"

    # 6. E3 opinion check
    if token_hits(title, C.OPINION_TERMS) and not token_hits(abstract, C.QUANT_TERMS):
        return C.EXCLUDE, "E3"

    # 7. Off-topic narrow applications (E7)
    if token_hits(combined, C.OFF_TOPIC_DOMAINS) and len(cg_hits) <= 1:
        return C.EXCLUDE, "E7"

    # 8. Quantitative outcome (O): need some empirical signal
    quant = token_hits(combined, C.QUANT_TERMS)
    if not abstract.strip():
        # title-only: include if CG benchmark/vocab strong
        if cg_hits:
            return C.INCLUDE, ""
        return C.UNCERTAIN, ""
    if not quant:
        # No empirical markers: if application/non-CG context -> E2/E3,
        # else defer
        if token_hits(combined, C.NON_COMPOSITIONAL_TERMS):
            return C.EXCLUDE, "E2"
        if token_hits(title, C.OPINION_TERMS):
            return C.EXCLUDE, "E3"
        return C.UNCERTAIN, ""

    return C.INCLUDE, ""


def main():
    with open(SCREENING_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    from collections import Counter
    counts = Counter()
    reasons = Counter()
    results = []

    for rec in records:
        decision, reason = classify(rec, use_abstract=False)
        rec["decision"] = decision
        rec["reason_code"] = reason
        results.append(rec)
        counts[decision] += 1
        if reason:
            reasons[reason] += 1

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames)
        w.writeheader()
        w.writerows(results)

    print("Screener 1 — title stage:")
    for d, c in counts.most_common():
        print(f"  {d:10s} {c:5d} ({c/len(results)*100:.1f}%)")
    print("Reasons:")
    for r, c in reasons.most_common():
        print(f"  {r}: {c}  ({C.REASON_CODES.get(r, '')})")
    print(f"Output: {OUT_CSV.name}")


if __name__ == "__main__":
    main()
