#!/usr/bin/env python3
"""
Paper 01 — Phase 6: apply user-download reconciliation to retrieval-status.csv.

Marks user-downloaded PDFs as retrieved-manual, flags confirmed paywalled,
detects duplicates, and writes a reconciliation summary for the user.
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
STATUS_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
OUT_CSV = BASE / "research" / "retrieval" / "retrieval-status.csv"
SUMMARY_MD = BASE / "research" / "retrieval" / "manual-download-reconciliation.md"

# study_id -> (pdf filename, prior note) from the matcher + manual mapping
NEW_RETRIEVALS = {
    "P1151": "Aliman_2019.pdf",
    "P020": "Assistant, K.R_2026.pdf",
    "P1246": "Bereska_2023.pdf",
    "P162": "Chen_2026.pdf",
    "P255": "Christian_2025.pdf",
    "P225": "Dung_2024.pdf",
    "P219": "Harris_2025.pdf",
    "P364": "Helliwell_2024.pdf",
    "P166": "Hernandez-Espinosa_2026.pdf",
    "P311": "Hildebrandt_2025.pdf",
    "P074": "Jiang_2026.pdf",
    "P1207": "Jinnai_2025.pdf",
    "P409": "Kan_2025.pdf",
    "P138": "Lee_2026.pdf",
    "P055": "Li_2026.pdf",
    "P294": "Liu_2026.pdf",          # NOTE: Liu_2026 is Chinese-language; flagged
    "P257": "McKinlay_2024.pdf",
    "P308": "Moret_2025.pdf",
    "P483": "Safron_2023.pdf",       # Value Cores (was the unmatched paste title)
    "P547": "Holtman_2020.pdf",
    "P076": "Torgbi Agbemabiese_2026.pdf",
    "P193": "Aoki_2026.pdf",         # NOTE: Aoki_2026 is Japanese-language; flagged
    "P276": "Snetkov_2025.pdf",      # NOTE: Russian-language version; flagged
    "P1029": "Sun_2024.pdf",
    "P566": "Edwards_2024.pdf",
    "P1059": "Safron_2023.pdf",      # dup mapping guard
}

# study_id -> pdf filename for confirmed duplicates (already retrieved)
DUPLICATES = {
    "P573": "Aliman_2019_Orthogonality.pdf",
    "P653": "Beigi_2026.pdf",
    "P316": "Cao_2025.pdf",
    "P426": "D_Alessandro_2025.pdf",
    "P523": "Dung_2023.pdf",
    "P318": "Growiec_2024.pdf",
    "P109": "Growiec_2026.pdf",
    "P009": "Hadfield-Menell_2019.pdf",
    "P342": "Hellrigel-Holderbaum_2025.pdf",
    "P643": "Hong_2026.pdf",
    "P113": "Li_2026_Step-GRPO.pdf",
    "P237": "Lindstrom_2025.pdf",
    "P646": "MacDiarmid_2025.pdf",
    "P096": "Melo_2025.pdf",
    "P309": "Milliere_2025.pdf",
    "P651": "Rashidinejad_2024.pdf",
    "P624": "Reis_2026.pdf",
    "P628": "Sharma_2024.pdf",
    "P382": "Southan_2025.pdf",
    "P305": "Stenseke_2025.pdf",
    "P091": "Su_2026.pdf",
    "P585": "Sutrop_2020.pdf",
    "P638": "Taylor_2025.pdf",
    "P207": "Ueda_2026.pdf",
    "P642": "Wang.J_2026.pdf",
    "P502": "Wang_2024.pdf",
    "P352": "Wang_2025.pdf",
    "P442": "Wang_2025_ACL25.pdf",
    "P039": "Wang_2026.pdf",
    "P028": "Zhao_2026.pdf",
    "P645": "Cagatan_2026.pdf",
    "P420": "Bradley_2025.pdf",
    "P307": "Gupta_2025.pdf",
}

CONFIRMED_PAYWALLED_IDS = {"P01_2387", "P01_0460", "P01_0539", "P01_0597",
                           "P01_0992", "P01_1216", "P01_1305"}
CONFIRMED_PAYWALLED_TITLES = {"The Many Faces of AI Alignment",
                              "Could We Control Superintelligent AI?"}


def main():
    with open(STATUS_CSV, "r", encoding="utf-8") as f:
        status_rows = list(csv.DictReader(f))
    status_by_id = {r["id"]: r for r in status_rows}
    with open(INCLUDED_CSV, "r", encoding="utf-8") as f:
        included = list(csv.DictReader(f))
    study_to_id = {r["study_id"]: r["id"] for r in included}
    title_to_id = {}
    for r in included:
        title_to_id.setdefault(r["title"].strip().lower(), r["id"])

    updates = []
    # 1. New retrievals
    for sid, pdf in NEW_RETRIEVALS.items():
        rid = study_to_id.get(sid)
        if rid and rid in status_by_id:
            status_by_id[rid]["status"] = "retrieved-manual"
            status_by_id[rid]["pdf_path"] = f"research/pdfs/{pdf}"
            updates.append(f"NEW {sid} {pdf}")
    # 2. Duplicates (already retrieved; note the extra file)
    for sid, pdf in DUPLICATES.items():
        rid = study_to_id.get(sid)
        if rid and rid in status_by_id:
            st = status_by_id[rid]
            if not st["status"].startswith("retrieved"):
                st["status"] = "retrieved-manual"
                st["pdf_path"] = f"research/pdfs/{pdf}"
                updates.append(f"NEW(dup-mapped) {sid} {pdf}")
    # 3. Confirmed paywalled by user
    for pid in CONFIRMED_PAYWALLED_IDS:
        if pid in status_by_id:
            status_by_id[pid]["status"] = "paywalled-confirmed"
    for t in CONFIRMED_PAYWALLED_TITLES:
        rid = title_to_id.get(t.strip().lower())
        if rid and rid in status_by_id:
            status_by_id[rid]["status"] = "paywalled-confirmed"

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(status_rows[0].keys()))
        w.writeheader()
        w.writerows(status_rows)

    dist = Counter(r["status"] for r in status_rows)
    print("Status distribution:", dict(dist))
    print(f"Updates applied: {len(updates)}")

    # Summary report
    with open(SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Manual Download Reconciliation (user feedback)\n\n")
        f.write("**Date**: 2026-08-01\n\n")
        f.write("## Summary\n\n")
        f.write(f"- User downloaded top-500-by-relevance PDFs into `research/pdfs/`\n")
        f.write(f"- {len(NEW_RETRIEVALS)} records newly retrieved (was paywalled/no-doi/oa-link-failed)\n")
        f.write(f"- {len(DUPLICATES)} duplicate downloads detected (paper already retrieved automatically)\n")
        f.write(f"- {len(CONFIRMED_PAYWALLED_IDS) + len(CONFIRMED_PAYWALLED_TITLES)} records confirmed paywalled by user\n\n")
        f.write("## Confirmed Paywalled (user)\n\n")
        for pid in sorted(CONFIRMED_PAYWALLED_IDS):
            r = status_by_id.get(pid, {})
            f.write(f"- {pid}: {r.get('title','')[:70]}\n")
        for t in CONFIRMED_PAYWALLED_TITLES:
            f.write(f"- {t}\n")
        f.write("\n## New Retrievals (user downloads)\n\n")
        for sid, pdf in sorted(NEW_RETRIEVALS.items()):
            f.write(f"- {sid}: `{pdf}`\n")
        f.write("\n## Duplicates (already retrieved)\n\n")
        for sid, pdf in sorted(DUPLICATES.items()):
            f.write(f"- {sid}: `{pdf}` (duplicate of automated retrieval)\n")
        f.write("\n## Language Flags\n\n")
        f.write("- `Aoki_2026.pdf` (P193): Japanese-language version of Mechanistic Interpretability paper\n")
        f.write("- `Snetkov_2025.pdf` (P276): Russian-language version of METAETHICAL FOUNDATIONS\n")
        f.write("- `Liu_2026.pdf` (P294): Chinese-language journal paper — verify English record exists\n")
        f.write("- `Jin_2025.pdf`: Chinese-language psychology journal — likely an extra download, "
                "NOT in included list; verify\n")
        f.write("\n## New Status Distribution\n\n")
        for s, c in dist.most_common():
            f.write(f"- {s}: {c}\n")

    print(f"Summary: {SUMMARY_MD.name}")


if __name__ == "__main__":
    main()
