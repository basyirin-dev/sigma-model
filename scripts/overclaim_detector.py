#!/usr/bin/env python3
"""Scans manuscript and documentation text for overclaiming language prohibited by CC.3."""

import re
import sys
from pathlib import Path

FORBIDDEN_PATTERNS = [
    (r"\bproves\b", "Replace 'proves' with 'provides evidence for' or 'demonstrates within the tested regime' (unless formal math theorem)."),
    (r"\bguarantees\b", "Replace 'guarantees' with 'bounds' or 'empirically supports'."),
    (r"\bfundamentally solves\b", "Unbounded claim."),
    (r"\bfirst ever\b", "Avoid unsubstantiated novelty claims; qualify with 'to our knowledge'."),
    (r"\bunquestionably\b", "Subjective certainty marker."),
    (r"\bexact origin of\b", "Grand theory claim; use 'a mechanistic account of'."),
]

def scan_file(file_path: Path):
    violations = []
    text = file_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    for line_idx, line in enumerate(lines, 1):
        for pattern, suggestion in FORBIDDEN_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                violations.append((line_idx, line.strip(), suggestion))
    return violations

def main():
    root = Path(".")
    files_to_scan = list(root.glob("paper/**/*.tex"))
    
    total_violations = 0
    for f in files_to_scan:
        viols = scan_file(f)
        if viols:
            print(f"\n[VIOLATIONS FOUND] {f}:")
            for line_no, text, suggestion in viols:
                print(f"  Line {line_no}: \"{text}\"")
                print(f"    --> Suggestion: {suggestion}")
            total_violations += len(viols)

    if total_violations == 0:
        print("[PASS] Zero overclaiming patterns detected across manuscripts.")
        sys.exit(0)
    else:
        print(f"\n[WARNING] Found {total_violations} potential overclaim markers.")
        sys.exit(0)

if __name__ == "__main__":
    main()
