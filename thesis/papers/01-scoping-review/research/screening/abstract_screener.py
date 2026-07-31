#!/usr/bin/env python3
"""
Paper 01 — Phase 5 Abstract Screening (Task 5.3)

Takes the title-stage Include + Uncertain pool and applies the I/E
criteria to the abstract text, stage-aware:

  Title-Include records (631): title evidence was already strong;
    keep Include unless the abstract reveals narrow-domain markers with
    no technical core -> downgrade to Uncertain.

  Title-Uncertain records (919): decide from the abstract —
    - abstract strong technical core term      -> Include
    - abstract narrow markers, no technical    -> Exclude (R-STRUCT)
    - abstract ambiguous core + AI context +
      non-trivial structural framing           -> Include
    - otherwise                                -> Uncertain (full-text)
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent))
import screening_config as C  # noqa: E402
from screener import token_hits, has_non_latin  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
TITLE_CSV = BASE / "research" / "screening-results" / "paper01-title-screening.csv"
OUT_CSV = BASE / "research" / "screening-results" / "paper01-abstract-screening.csv"

# Decisive technical AGI-safety terms (abstract-stage Include signal).
# NOTE: "corrigib"/"incorrigib" excluded here — polysemous (linguistics,
# juvenile law); handled in AMBIGUOUS_CORE_TERMS requiring AI context.
ABSTRACT_STRONG_TERMS = [
    "mesa-optim", "deceptive alignment", "alignment faking", "sleeper agent",
    "reward hacking", "specification gaming", "goal misgeneraliz",
    "inner alignment", "outer alignment", "shutdown problem", "off-switch",
    "coherent extrapolated volition", "indirect normativity",
    "existential risk", "superintelligence", "artificial general intelligence",
    "agi safety", "x-risk", "alignment problem", "scalable oversight",
    "weak-to-strong", "reward model over-optimization", "alignment tax",
]

# Ambiguous core terms — AGI-safety only when AI context co-occurs.
AMBIGUOUS_CORE_TERMS = [
    "value alignment", "value-aligned", "ai alignment", "aligning ai",
    "misalignment", "misaligned", "interpretability", "mechanistic interpretab",
    "reward model", "reward models", "rlhf", "corrigib", "incorrigib",
    "alignment research", "alignment of ai",
]

# Structural terms that actually indicate safety framing (non-trivial);
# excludes generic words like "value"/"safety"/"risk" that co-occur trivially.
MEANINGFUL_STRUCTURAL = [
    "alignment", "aligning", "corrigib", "mesa", "deceptive", "goal misgeneraliz",
    "specification gaming", "reward hacking", "reward model", "mechanistic",
    "interpretability", "inner alignment", "outer alignment", "off-switch",
    "shutdown", "existential", "superintelligence", "agi", "x-risk",
    "misalignment", "misaligned", "constitutional ai", "scalable oversight",
    "rlhf", "value alignment", "coherent extrapolated volition", "normativ",
]


def abstract_decision(record: dict, title_decision: str) -> tuple[str, str]:
    title = record.get("title", "") or ""
    abstract = record.get("abstract", "") or ""
    keywords = record.get("keywords", "") or ""
    combined = f"{title} {abstract} {keywords}"
    ab = abstract.lower()

    # Hard gates (defense in depth)
    if has_non_latin(title + abstract):
        return C.EXCLUDE, "R-LANG"
    year = record.get("year", "").strip()
    if year:
        try:
            y = int(re.match(r"(\d{4})", year).group(1))
            if y < C.DATE_MIN or y > C.DATE_MAX:
                return C.EXCLUDE, "R-DATE"
        except (AttributeError, ValueError):
            pass

    strong = token_hits(combined, ABSTRACT_STRONG_TERMS)
    ambiguous_core = token_hits(combined, AMBIGUOUS_CORE_TERMS)
    ai_ctx = token_hits(combined, C.AI_CONTEXT_TERMS)
    narrow = token_hits(combined, C.NARROW_DOMAIN_TERMS)
    struct = token_hits(ab, MEANINGFUL_STRUCTURAL)

    # No abstract: cannot refine — keep title-stage decision.
    if not abstract.strip():
        return C.INCLUDE if title_decision == C.INCLUDE else C.UNCERTAIN, ""

    # ── Title-Include records ───────────────────────────────────────
    if title_decision == C.INCLUDE:
        # Title evidence strong; downgrade if abstract shows narrow-domain
        # markers without STRONG technical core (ambiguous-only evidence
        # does NOT rescue from narrow-domain application contexts).
        if narrow and not strong:
            return C.UNCERTAIN, ""
        return C.INCLUDE, ""

    # ── Title-Uncertain records ─────────────────────────────────────
    # 1. Strong technical core -> Include
    if strong:
        return C.INCLUDE, ""

    # 2. Ambiguous core + AI context + meaningful structural framing -> Include
    #    (but narrow-domain markers override ambiguous-only evidence)
    if ambiguous_core and ai_ctx and struct and not narrow:
        return C.INCLUDE, ""

    # 3. Narrow markers with no strong technical core -> Exclude
    if narrow and not strong:
        return C.EXCLUDE, "R-STRUCT"

    # 4. Remain Uncertain (full-text stage)
    return C.UNCERTAIN, ""


def main():
    with open(TITLE_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    stats = Counter()
    reasons = Counter()
    results = []

    for rec in records:
        title_decision = rec.get("decision", "")
        if title_decision in ("Include", "Uncertain"):
            decision, reason = abstract_decision(rec, title_decision)
            rec["decision"] = decision
            rec["reason_code"] = reason
            rec["stage"] = "abstract"
        else:
            rec["stage"] = "title-excluded"
        results.append(rec)
        stats[rec["decision"]] += 1
        if rec.get("reason_code"):
            reasons[rec["reason_code"]] += 1

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames + ["stage"],
                           extrasaction="ignore")
        w.writeheader()
        w.writerows(results)

    print("Abstract screening complete:")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c:5d} ({c/len(results)*100:.1f}%)")
    print(f"Output: {OUT_CSV}")


if __name__ == "__main__":
    main()
