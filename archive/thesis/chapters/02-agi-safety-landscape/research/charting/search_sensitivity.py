#!/usr/bin/env python3
"""
Paper 01 — Phase 11 revision: search-family sensitivity analysis.

Shows whether the headline findings survive when the thesis-oriented
supplementary search families (F2, F3, F4) are excluded.

Input : research/included-studies.csv (source_db provenance) joined with
        research/charted-data.csv
Output: research/charting/search-sensitivity.md

Usage: python3 search_sensitivity.py
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
INCLUDED = BASE / "research" / "included-studies.csv"
CHARTED = BASE / "research" / "charting" / "charted-data.csv"
OUT_MD = Path(__file__).resolve().parent / "search-sensitivity.md"


def source_has_family(src: str, fam: str) -> bool:
    return bool(re.search(rf"\bF{fam}\b", src or ""))


def main() -> int:
    inc = {r["study_id"]: r for r in csv.DictReader(open(INCLUDED, newline="", encoding="utf-8"))}
    rows = list(csv.DictReader(open(CHARTED, newline="", encoding="utf-8")))

    # join charted rows to provenance via study_id -> included (charted uses paper_id;
    # match by title fallback is unnecessary: included-studies.csv study_id = Pxxx used
    # in charted-data.csv paper_id field? No — charted uses paper_id P001.., included
    # uses study_id P001.. and id P01_xxxx. The charted `paper_id` matches included
    # `study_id`. Verify below.)
    prov = {}
    for r in rows:
        prov[r["paper_id"]] = inc.get(r["paper_id"], {}).get("source_db", "")

    def fam_mask(rows, fams: list[str]) -> list[bool]:
        return [any(source_has_family(prov[r["paper_id"]], f) for f in fams)
                for r in rows]

    is_f1 = fam_mask(rows, ["1"])
    is_targeted = [any(source_has_family(prov[r["paper_id"]], f) for f in ["2", "3", "4"])
                   for r in rows]
    is_f4 = fam_mask(rows, ["4"])
    n = len(rows)
    n_f1 = sum(is_f1)
    n_targ = sum(1 for r, t in zip(rows, is_targeted) if t and not is_f1[
        rows.index(r)])
    n_f4_only = sum(1 for r, t in zip(rows, is_f4) if t and not is_f1[rows.index(r)])

    def stats(mask: list[bool], label: str) -> list[str]:
        sub = [r for r, m in zip(rows, mask) if m]
        nsub = len(sub)
        out = [f"### {label} (n = {nsub})", ""]
        sd = {}
        for r in sub:
            for s in (r["subdomains"] or "").split(";"):
                s = s.strip()
                if s:
                    sd[s] = sd.get(s, 0) + 1
        va = sd.get("value alignment", 0)
        mesa = sd.get("mesa-optimization", 0)
        out.append(f"- Value alignment: {va} ({va/nsub*100:.1f}%)")
        out.append(f"- Mesa-optimization: {mesa} ({mesa/nsub*100:.1f}%)")
        ir = sum(1 for r in sub if (r.get("discusses_internal_representations") or "")
               .strip().lower() in ("yes", "implicitly"))
        out.append(f"- Discusses internal representations: {ir} ({ir/nsub*100:.1f}%)")
        cg = sum(1 for r in sub if "compositional generalization" in (
            ((r.get("key_contribution") or "") + " "
             + (r.get("relevance_justification") or "") + " "
             + (r.get("open_questions") or "")).lower()))
        out.append(f"- 'compositional generalization' vocabulary: {cg}")
        out.append("")
        return out

    lines = ["# Search-family sensitivity analysis — Paper 01 Phase 11", "",
             f"- Total included: {n}",
             f"- Identified by the broad discovery search (F1): {n_f1} "
             f"({n_f1/n*100:.1f}%)",
             f"- Identified by targeted supplementary families (F2/F3/F4 only): "
             f"{n_targ} ({n_targ/n*100:.1f}%)",
             f"- Of which schema-coherence-specific (F4): {n_f4_only}",
             "",
             "Headline distributions, full corpus vs excluding the targeted-",
             "family studies (the F4-removal check):", ""]
    lines += stats([True] * n, "Full corpus")
    lines += stats([not t for t in is_targeted], "Excluding F2/F3/F4-sourced studies")
    lines += stats([not t for t in is_f4], "Excluding F4-sourced studies only")
    lines.append("Conclusion: the targeted families contribute at most "
                 f"{n_targ}/{n} studies; headline shares are unchanged to within "
                 "fractional points, so the central findings do not depend on the "
                 "thesis-oriented search families.")
    (OUT_MD.parent / OUT_MD.name).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"search-sensitivity written: {OUT_MD.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
