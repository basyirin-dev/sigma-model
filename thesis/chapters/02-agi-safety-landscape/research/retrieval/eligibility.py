#!/usr/bin/env python3
"""
Paper 01 — Phase 6 Full-Text Eligibility Check (Task 6.2)

For all 1,278 records (1,118 Include + 160 Uncertain from Phase 5):
  - Include records: confirm against I1-I5 from abstract+metadata
    (full-text confirmation noted where a PDF was retrieved)
  - Uncertain records: make final decision from abstract/metadata:
      * clear AGI-safety relevance  -> Include
      * narrow / off-topic          -> Exclude (with reason)
      * unresolvable (weak evidence) -> Exclude FT-UNAVAILABLE
  - Assign study IDs P001-PXXX to included studies

Outputs:
  - research/retrieval/eligibility-decisions.csv  (all 1,278 final decisions)
  - research/retrieval/fulltext-exclusions.md     (exclusion reasons)
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "screening"))
import screening_config as SC  # Paper 1 config
from screener import token_hits  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCREENING_CSV = BASE / "research" / "screening-results" / "paper01-screening-results.csv"
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
OUT_CSV = BASE / "research" / "retrieval" / "eligibility-decisions.csv"
EXCL_MD = BASE / "research" / "retrieval" / "fulltext-exclusions.md"


def load_csv(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def paper_decision(rec: dict, status: str, is_uncertain: bool) -> tuple[str, str]:
    """Return (decision, reason) at full-text eligibility stage."""
    title = rec.get("title", "") or ""
    abstract = rec.get("abstract", "") or ""
    keywords = rec.get("keywords", "") or ""
    text = f"{title} {abstract} {keywords}"

    # Hard re-checks
    year = (rec.get("year") or "").strip()
    if year:
        try:
            y = int(re.match(r"(\d{4})", year).group(1))
            if y < SC.DATE_MIN or y > SC.DATE_MAX:
                return "Exclude", "FT-DATE"
        except (AttributeError, ValueError):
            pass

    # Narrow-domain / business markers -> Exclude (from abstract evidence)
    narrow = token_hits(text, SC.NARROW_DOMAIN_TERMS)
    core = token_hits(text, SC.CORE_INDICATORS)
    ai_ctx = token_hits(text, SC.AI_CONTEXT_TERMS)
    unambiguous = [c for c in core if c not in (
        "value alignment", "value-aligned", "interpretability", "mechanistic interpretab",
        "reward model", "reward models", "rlhf", "ai alignment", "aligning ai",
        "misalignment", "misaligned", "corrigib", "incorrigib")]
    struct = token_hits(text, SC.STRUCTURAL_SAFETY_TERMS)

    # Subdomain vocabulary evidence (21-term §B.1) also counts as core
    # evidence — but only via PRECISE phrases, not loose subdomain patterns
    # ("coherence"/"normativity"/"corrigib" alone match philosophy/medicine
    # texts). Catches e.g. "compositional generalization", "natural
    # abstractions", "schema coherence", "world model".
    precise_subdomain = token_hits(text, [
        "compositional generalization", "compositional generalisation",
        "systematic generalization", "systematic generalisation",
        "schema coherence", "coherent schema", "natural abstraction",
        "latent ontology", "coherent extrapolated volition", "indirect normativity",
        "mechanistic interpretab", "superposition", "world model",
        "goal misgeneraliz", "specification gaming", "reward hacking",
        "mesa-optim", "deceptive alignment", "alignment faking", "sleeper agent",
        "inner alignment", "outer alignment", "off-switch", "shutdown problem",
        "superintelligence", "artificial general intelligence", "existential risk",
        "agi safety", "ai safety", "cirl",
    ])

    has_core = bool(unambiguous) or (bool(core) and bool(ai_ctx)) or bool(precise_subdomain)
    off_topic = bool(narrow) and not has_core

    # Retrieve status
    retrieved = status.startswith("retrieved")

    if is_uncertain:
        # Final decision on Phase-5 Uncertain records
        if off_topic:
            return "Exclude", "FT-NARROW"
        # Title-evidence rescue: title-only records (no abstract/DOI/arXiv)
        # whose title is an unambiguous AGI-safety signal -> Include.
        if not abstract.strip():
            title_signal = token_hits(title + " " + keywords, [
                "corrigib", "inner alignment", "outer alignment", "misalignment",
                "natural abstraction", "mesa-optim", "deceptive alignment",
                "alignment faking", "reward hacking", "specification gaming",
                "goal misgeneraliz", "superintelligence", "artificial general intelligence",
                "existential risk", "agi safety", "ai safety", "coherent extrapolated volition",
                "off-switch", "shutdown problem", "cirl", "value alignment",
                "formal verification for ai safety", "world model", "schema coherence",
            ])
            if title_signal:
                return "Include", ""
        if has_core and (struct or retrieved):
            return "Include", ""
        if has_core:
            # core present but weak structural evidence; paywalled
            if retrieved:
                return "Include", ""
            return "Exclude", "FT-UNAVAILABLE"
        # no core evidence at all
        return "Exclude", "FT-NO-SUBJECT"
    else:
        # Phase-5 Include records: confirm
        if off_topic and not retrieved:
            return "Exclude", "FT-NARROW"
        if not has_core and not retrieved and not abstract.strip():
            return "Exclude", "FT-UNAVAILABLE"
        return "Include", ""


def main():
    screening = load_csv(SCREENING_CSV)
    status_map = {}
    if STATUS_CSV.exists():
        for row in load_csv(STATUS_CSV):
            status_map[row["id"]] = row["status"]

    pool = [r for r in screening if r["decision"] in ("Include", "Uncertain")]
    print(f"Eligibility pool: {len(pool)}")

    decisions = []
    stats = Counter()
    reasons = Counter()
    included = []

    for rec in pool:
        status = status_map.get(rec["id"], "unknown")
        is_uncertain = rec["decision"] == "Uncertain"
        decision, reason = paper_decision(rec, status, is_uncertain)

        row = dict(rec)
        row["ft_status"] = status
        row["ft_decision"] = decision
        row["ft_reason"] = reason
        decisions.append(row)
        stats[decision] += 1
        if reason:
            reasons[reason] += 1
        if decision == "Include":
            included.append(row)

    # Assign study IDs P001-PXXX
    for i, row in enumerate(included, 1):
        row["study_id"] = f"P{i:03d}"

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        fields = list(decisions[0].keys())
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(decisions)

    # Exclusions report
    excl = [d for d in decisions if d["ft_decision"] == "Exclude"]
    with open(EXCL_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Full-Text Exclusions (Task 6.2)\n\n")
        f.write(f"**Total excluded at full-text stage**: {len(excl)}\n\n")
        f.write("| Reason | Count |\n")
        f.write("|--------|------:|\n")
        labels = {
            "FT-DATE": "Outside date range",
            "FT-NARROW": "Abstract reveals narrow/off-topic content (not structural AGI safety)",
            "FT-UNAVAILABLE": "Full text not retrievable (paywalled) and evidence insufficient to confirm",
            "FT-NO-SUBJECT": "No AGI-safety subdomain evidence at full-text stage",
        }
        for r, c in reasons.most_common():
            f.write(f"| {r} | {c} | {labels.get(r, '')} |\n")
        f.write("\n## Excluded Records (first 50)\n\n")
        f.write("| ID | Study | Title | Reason |\n")
        f.write("|----|-------|-------|--------|\n")
        for d in excl[:50]:
            f.write(f"| {d['id']} | {d.get('study_id','')} | {d['title'][:60]} | {d['ft_reason']} |\n")

    print("\nFull-text eligibility:")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c}")
    print("Reasons:", dict(reasons.most_common()))
    print(f"Included for extraction: {len(included)}")
    print(f"Output: {OUT_CSV.name}")


if __name__ == "__main__":
    main()
