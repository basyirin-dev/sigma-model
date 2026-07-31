#!/usr/bin/env python3
"""
Paper 01 — Phase 5 Deterministic Screener

Applies the I/E criteria (screening_config.py) to classify each record:
  Include / Exclude / Uncertain, with a reason code per criterion.

Pipeline per record:
  1. I2 date check (hard)          -> Exclude R-DATE / flag R-YEAR
  2. I1/E2 language check (hard)   -> Exclude R-LANG
  3. I3 subdomain vocabulary scan  -> 0 hits => Exclude R-SUBJ (title+abstract+keywords)
  4. I5 structural framing scan    -> 0 hits => Exclude R-STRUCT
  5. E1 narrow-only / E5 capability-only / E3 opinion heuristics -> Exclude w/ reason
  6. Otherwise -> Include; borderline -> Uncertain
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import screening_config as C  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCREENING_CSV = BASE / "research" / "clean-library" / "paper01-library-screening.csv"
OUT_CSV = BASE / "research" / "screening-results" / "paper01-title-screening.csv"
OUT_CSV.parent.mkdir(parents=True, exist_ok=True)


# ── Text utilities ────────────────────────────────────────────────────

def has_non_latin(text: str) -> bool:
    for ch in text:
        cp = ord(ch)
        for lo, hi in C.NON_LATIN_RANGES:
            if lo <= cp <= hi:
                return True
    return False


def token_hits(text: str, patterns: list[str]) -> list[str]:
    """Return which patterns occur in the lowercased text.

    Word-boundary anchored at pattern start: 'corrigib' matches
    'corrigibility' but not 'incorrigibility' (avoid legal-term FP).
    Short AI terms (ai/ml/gpt) are word-boundary anchored both sides.
    """
    t = text.lower()
    hits = []
    for p in patterns:
        if p in C.AI_SHORT_TERMS:
            if re.search(rf"\b{re.escape(p)}\b", t):
                hits.append(p)
        else:
            if re.search(rf"\b{re.escape(p)}", t):
                hits.append(p)
    return hits


# ── Classification ────────────────────────────────────────────────────

def classify(record: dict) -> tuple[str, str, list[str]]:
    """Return (decision, reason_code, matched_subdomains)."""
    title = record.get("title", "") or ""
    abstract = record.get("abstract", "") or ""
    keywords = record.get("keywords", "") or ""
    year_str = (record.get("year", "") or "").strip()
    journal = record.get("journal", "") or ""

    combined = f"{title} {abstract} {keywords}"
    title_kw = f"{title} {keywords}"

    reasons: list[str] = []

    # ── 1. I2 date check ────────────────────────────────────────────
    if not year_str:
        reasons.append("R-YEAR")
    else:
        try:
            year = int(re.match(r"(\d{4})", year_str).group(1))
        except (AttributeError, ValueError):
            reasons.append("R-YEAR")
            year = None

        if year is not None:
            if year < C.DATE_MIN:
                return C.EXCLUDE, "R-DATE", []
            if year > C.DATE_MAX:
                return C.EXCLUDE, "R-DATE", []

    # ── 1b. Collection/proceedings-volume exclusion ─────────────────
    # A proceedings volume (collection of many papers), not an individual
    # contribution, is not a screenable study per I4.
    if re.search(r"(the proceedings contain|proceedings of the \d+ (nd|rd|th)|conference proceedings|volume of proceedings)", combined, re.I):
        if not re.search(r"\b(presents|proposes|introduces|we (show|present|propose|study|introduce)|this (paper|work|study))", abstract, re.I):
            return C.EXCLUDE, "R-SUBJ", []

    # ── 2. I1/E2 language check ─────────────────────────────────────
    if has_non_latin(title + abstract):
        return C.EXCLUDE, "R-LANG", []

    # ── 3. I3 subdomain vocabulary scan ─────────────────────────────
    matched = []
    for subdomain, patterns in C.SUBDOMAINS.items():
        hits = token_hits(combined, patterns)
        if hits:
            matched.append(subdomain)

    if len(matched) < C.SUBJECT_HITS_REQUIRED:
        return C.EXCLUDE, "R-SUBJ", matched

    # ── 3b. Precision gate: core AGI-safety indicator required ──────
    struct_hits = token_hits(combined, C.STRUCTURAL_SAFETY_TERMS)
    core_hits = token_hits(combined, C.CORE_INDICATORS)
    # Ambiguous core indicators (e.g. "value alignment", "interpretability",
    # "reward model") require an AI term in TITLE+KEYWORDS (strong context),
    # not merely an incidental mention in the abstract.
    ambiguous = [t for t in core_hits if t in (
        "value alignment", "value-aligned", "interpretability", "mechanistic interpretab",
        "reward model", "reward models", "rlhf", "ai alignment", "aligning ai",
        "misalignment", "misaligned", "corrigib", "incorrigib",
    )]
    unambiguous = [t for t in core_hits if t not in (
        "value alignment", "value-aligned", "interpretability", "mechanistic interpretab",
        "reward model", "reward models", "rlhf", "ai alignment", "aligning ai",
        "misalignment", "misaligned", "corrigib", "incorrigib",
    )]
    title_kw = f"{title} {keywords}".lower()
    ai_ctx_title = token_hits(title_kw, C.AI_CONTEXT_TERMS)
    ai_ctx_any = token_hits(combined, C.AI_CONTEXT_TERMS)

    # Narrow-domain exclusion: business/psych/medical markers with only
    # ambiguous value-language core evidence => not AGI safety.
    narrow_domain = token_hits(combined, C.NARROW_DOMAIN_TERMS)
    strong_technical = bool(unambiguous)
    if narrow_domain and not strong_technical and not ai_ctx_title:
        return C.EXCLUDE, "R-STRUCT", matched

    # Rescue rule: ambiguous core indicator (e.g. "value alignment") with an
    # AI term ANYWHERE in the text is genuine AGI-safety unless narrow-domain
    # markers are present. Recovers e.g. "Policy Aggregation" (AI value
    # alignment in abstract) while keeping HRM/CSR papers excluded.
    has_core = (bool(unambiguous)
                or (bool(ambiguous) and bool(ai_ctx_title))
                or (bool(ambiguous) and bool(ai_ctx_any) and not narrow_domain))

    if not has_core:
        # No strong AGI-safety indicator: only keep if unambiguous evidence
        # from a technical-alignment subdomain match + structural framing,
        # otherwise exclude as not-structural / narrow-only.
        strong_subdomains = [s for s in matched if s in (
            "AI Alignment", "AGI Safety", "Mesa-optimisation", "Deceptive Alignment",
            "Corrigibility", "Goal Preservation", "Inner Alignment", "Outer Alignment",
            "Specification Gaming", "Reward Hacking", "Coherent Extrapolated Volition",
            "Indirect Normativity", "Schema Coherence", "Natural Abstractions",
            "Latent Ontology",
        )]
        if strong_subdomains and struct_hits:
            return C.UNCERTAIN, "", matched
        return C.EXCLUDE, "R-STRUCT", matched

    # ── 4. I5 structural safety framing ─────────────────────────────
    if len(struct_hits) < C.STRUCTURAL_TERMS_REQUIRED:
        return C.EXCLUDE, "R-STRUCT", matched

    # ── 4b. Confidence triage ───────────────────────────────────────
    # Strong technical-alignment core => Include (high precision).
    # Ambiguous-only core (value alignment / ai alignment / interpretability /
    # reward model / rlhf) => Uncertain: abstract screening must decide,
    # because e.g. "value alignment" is polysemous (AGI safety vs HCI vs org).
    if not strong_technical:
        # Ambiguous-only evidence: defer to abstract screening (Uncertain)
        # unless a technical-alignment subdomain is explicitly matched AND
        # the abstract is unavailable (title-only).
        technical_subdomains = [s for s in matched if s in (
            "AI Alignment", "AGI Safety", "Mesa-optimisation", "Deceptive Alignment",
            "Corrigibility", "Goal Preservation", "Inner Alignment", "Outer Alignment",
            "Specification Gaming", "Reward Hacking", "Coherent Extrapolated Volition",
            "Indirect Normativity", "Schema Coherence", "Compositional Generalisation",
            "Internal Representation Structure", "Natural Abstractions", "Latent Ontology",
            "Feature Geometry",
        )]
        if not abstract.strip() and technical_subdomains:
            return C.INCLUDE, "", matched
        return C.UNCERTAIN, "", matched

    # ── 5a. E1 narrow-only check ────────────────────────────────────
    narrow_hits = token_hits(combined, C.NARROW_SAFETY_PATTERNS)
    # Narrow-only is exclusion IF no structural AGI safety term present
    structural_strong = any(p in combined.lower() for p in [
        "alignment", "mesa-optim", "deceptive", "corrigib", "goal misgeneraliz",
        "reward hacking", "specification gaming", "mechanistic interpretab",
        "existential risk", "agi safety", "superintelligence",
    ])
    if narrow_hits and not structural_strong:
        return C.EXCLUDE, "R-STRUCT", matched

    # ── 5b. E5 capability-only check ────────────────────────────────
    cap_hits = token_hits(combined, C.CAPABILITY_ONLY_PATTERNS)
    if cap_hits and not structural_strong and len(matched) <= 1:
        return C.EXCLUDE, "R-CAP", matched

    # ── 5c. E3 opinion check ────────────────────────────────────────
    op_hits = token_hits(title, C.OPINION_PATTERNS)
    has_substance = token_hits(abstract, C.STRUCTURAL_SAFETY_TERMS)
    if op_hits and not has_substance:
        return C.UNCERTAIN, "R-OPIN", matched

    # ── Borderline: weak abstract / single marginal hit ─────────────
    if not abstract.strip():
        # Title-only: include if title strongly matches, else uncertain
        if len(matched) >= 1 and struct_hits:
            return C.INCLUDE, "", matched
        return C.UNCERTAIN, "", matched

    if len(matched) == 1 and not struct_hits:
        return C.UNCERTAIN, "", matched

    # ── Default: include ────────────────────────────────────────────
    return C.INCLUDE, "", matched


# ── Main ──────────────────────────────────────────────────────────────

def main():
    with open(SCREENING_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    from collections import Counter
    decision_counts = Counter()
    reason_counts = Counter()
    results = []

    for rec in records:
        decision, reason, matched = classify(rec)
        rec["decision"] = decision
        rec["reason_code"] = reason
        rec["notes"] = "; ".join(matched) if matched else ("title-only" if not rec.get("abstract", "").strip() else "")
        results.append(rec)
        decision_counts[decision] += 1
        if reason:
            reason_counts[reason] += 1

    # Save title-screening results
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames)
        w.writeheader()
        w.writerows(results)

    # Also write decisions back to the screening CSV
    with open(SCREENING_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=reader.fieldnames)
        w.writeheader()
        w.writerows(results)

    print(f"Title screening complete: {len(results)} records")
    print(f"\nDecisions:")
    for d, c in decision_counts.most_common():
        print(f"  {d:10s} {c:5d} ({c/len(results)*100:.1f}%)")
    print(f"\nExclusion reasons:")
    for r, c in reason_counts.most_common():
        print(f"  {r:10s} {c:5d}  ({C.REASON_CODES.get(r, '')})")
    print(f"\nOutput: {OUT_CSV}")


if __name__ == "__main__":
    main()
