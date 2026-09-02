#!/usr/bin/env python3
"""RPF v2.0 compliance linter wrapper.

Executes scripts/compliance_linter.py when present; otherwise falls back to
checking key RPF artifacts. Always prints a structured JSON report of
CC.N.M rules (PASS / FAIL / N/A) to stdout. Exit code 0 on successful run.
"""

import json
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
LINTER = WORKSPACE / "scripts" / "compliance_linter.py"

FALLBACK_CHECKS = [
    ("CC.1.1", "planning/standards.md", "Standards document present"),
    ("CC.1.2", "meta/seeds.yaml", "Seed registry present"),
    ("CC.2.1", "planning/risk-register.md", "Risk register present"),
    ("CC.5.6", ".antigravity/ci/reproducibility-smoke.yml", "CI reproducibility workflow present"),
    ("CC.6.1", "planning/ledger.md", "Claim ledger present"),
]


def fallback_report() -> dict:
    report = {
        "status": "PASS",
        "total_rules": len(FALLBACK_CHECKS),
        "passed_rules": 0,
        "failed_rules": 0,
        "na_rules": 0,
        "rules": [],
    }
    for rule_id, rel_path, desc in FALLBACK_CHECKS:
        ok = (WORKSPACE / rel_path).exists()
        entry = {
            "id": rule_id,
            "description": desc,
            "status": "PASS" if ok else "FAIL",
            "notes": "Artifact present" if ok else f"{rel_path} missing",
        }
        report["rules"].append(entry)
        if ok:
            report["passed_rules"] += 1
        else:
            report["failed_rules"] += 1
            report["status"] = "FAIL"
    report["rules"].append({
        "id": "CC.*",
        "description": "Full rule coverage",
        "status": "N/A",
        "notes": "scripts/compliance_linter.py absent; artifact checks only",
    })
    report["na_rules"] = 1
    return report


def main() -> int:
    if LINTER.is_file():
        try:
            result = subprocess.run(
                [sys.executable, str(LINTER), "--json"],
                capture_output=True, text=True, cwd=str(WORKSPACE), check=False,
            )
            report = json.loads(result.stdout) if result.stdout.strip() else {
                "status": "FAIL",
                "error": result.stderr.strip() or "linter produced no output",
                "rules": [],
            }
        except Exception as exc:
            report = {"status": "FAIL", "error": str(exc), "rules": []}
    else:
        report = fallback_report()

    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
