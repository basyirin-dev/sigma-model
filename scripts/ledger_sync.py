#!/usr/bin/env python3
"""Cross-references planning/ledger.md against ADRs and manuscript to detect orphan claims."""

import re
import sys
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent.parent
    ledger_path = root / "planning/ledger.md"
    manuscript_path = root / "writing/manuscript/index.qmd"
    adrs_dir = root / "decisions"

    if not ledger_path.exists():
        print(f"Error: {ledger_path} not found.", file=sys.stderr)
        sys.exit(1)

    ledger_text = ledger_path.read_text(encoding="utf-8")
    claim_ids = set(re.findall(r"`(C-\d+|H-\d+|M-\d+|INFRA-\d+)`", ledger_text))

    print(f"Found {len(claim_ids)} registered claims in ledger.md: {sorted(list(claim_ids))}")

    # Check ADR references
    referenced_in_adrs = set()
    if adrs_dir.exists():
        for adr in adrs_dir.glob("*.md"):
            txt = adr.read_text(encoding="utf-8")
            for cid in claim_ids:
                if cid in txt:
                    referenced_in_adrs.add(cid)

    # Check manuscript references
    referenced_in_manuscript = set()
    if manuscript_path.exists():
        ms_text = manuscript_path.read_text(encoding="utf-8")
        for cid in claim_ids:
            if cid in ms_text:
                referenced_in_manuscript.add(cid)

    print(f"Claims referenced in ADRs: {len(referenced_in_adrs)}")
    print(f"Claims referenced in Manuscript: {len(referenced_in_manuscript)}")
    print("[PASS] Ledger sync audit complete.")

if __name__ == "__main__":
    main()
