#!/usr/bin/env python3
"""Automated Phase Exit Checker for Research Planning Framework (RPF) v2.0.

Validates that all necessary deliverables, exit criteria, and governance gates
for a specified phase (P00 through P14) are met.
"""

import argparse
import os
import re
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent

def check_p00() -> tuple[bool, list[str]]:
    """P00: Repository and Toolchain Setup."""
    issues = []

    # 1. Agent instructions >= 50 lines
    agent_inst = WORKSPACE / "meta/AGENT_INSTRUCTIONS.md"
    if not agent_inst.exists():
        issues.append("meta/AGENT_INSTRUCTIONS.md is missing.")
    else:
        lines = [l for l in agent_inst.read_text(encoding="utf-8").splitlines() if l.strip()]
        if len(lines) < 50:
            issues.append(f"meta/AGENT_INSTRUCTIONS.md must have >= 50 lines (found {len(lines)}).")

    # 2. Seeds registry with >= 1 seed
    seeds_file = WORKSPACE / "meta/seeds.yaml"
    if not seeds_file.exists():
        issues.append("meta/seeds.yaml is missing.")
    else:
        content = seeds_file.read_text(encoding="utf-8")
        if "seed_id:" not in content or "value:" not in content:
            issues.append("meta/seeds.yaml does not contain valid seed entries.")

    # 3. Standards >= 50 rules
    standards_file = WORKSPACE / "planning/standards.md"
    if not standards_file.exists():
        issues.append("planning/standards.md is missing.")
    else:
        rules = re.findall(r"^-\s+\*\*(CC\.\d+\.\d+):\*\*", standards_file.read_text(encoding="utf-8"), re.MULTILINE)
        if len(rules) < 50:
            issues.append(f"planning/standards.md must contain >= 50 CC.N.M rules (found {len(rules)}).")

    # 4. Planning core docs
    for doc in ["roadmap.md", "ledger.md", "risk-register.md", "budget.md", "compliance-matrix.md"]:
        if not (WORKSPACE / "planning" / doc).exists():
            issues.append(f"planning/{doc} is missing.")

    # 5. CI Workflow
    ci_file = WORKSPACE / ".antigravity/ci/reproducibility-smoke.yml"
    if not ci_file.exists():
        issues.append(".antigravity/ci/reproducibility-smoke.yml is missing.")

    # 6. ADR template
    adr_tmpl = WORKSPACE / "decisions/ADR-TEMPLATE.md"
    if not adr_tmpl.exists():
        issues.append("decisions/ADR-TEMPLATE.md is missing.")
    else:
        c = adr_tmpl.read_text(encoding="utf-8")
        if "affects-phases" not in c or "affects-ledger-rows" not in c:
            issues.append("decisions/ADR-TEMPLATE.md missing bidirectional linkage fields.")

    # 7. Pi ecosystem files
    for pi_file in [
        ".pi/extensions/rpf-guard.ts",
        ".pi/extensions/human-gate.ts",
        ".pi/extensions/manifest-enforcer.ts",
        ".pi/tools/validate_manifest_schema.py",
        ".pi/tools/run_compliance_linter.py",
    ]:
        if not (WORKSPACE / pi_file).exists():
            issues.append(f"{pi_file} is missing.")

    return len(issues) == 0, issues

def check_p01() -> tuple[bool, list[str]]:
    """P01: Literature Audit & Claim Taxonomy."""
    issues = []
    if not (WORKSPACE / "literature/screening-log.csv").exists():
        issues.append("literature/screening-log.csv is missing.")
    if not (WORKSPACE / "literature/knowledge-graph.json").exists():
        issues.append("literature/knowledge-graph.json is missing.")
    if not (WORKSPACE / "planning/literature-audit.md").exists():
        issues.append("planning/literature-audit.md is missing.")
    return len(issues) == 0, issues

def check_p02() -> tuple[bool, list[str]]:
    """P02: Theoretical Foundations & ODE Derivations."""
    issues = []
    theory_files = list(WORKSPACE.glob("src/simulation/*.py")) + list(WORKSPACE.glob("code/sigma_align/ode/*.py"))
    if not theory_files:
        issues.append("No theoretical ODE simulation modules found in src/simulation/ or code/sigma_align/ode/.")
    return len(issues) == 0, issues

def check_p03() -> tuple[bool, list[str]]:
    """P03: Gate Formulation & Preregistration."""
    issues = []
    prereg = WORKSPACE / "planning/preregistration.md"
    if not prereg.exists():
        issues.append("planning/preregistration.md is missing.")
    return len(issues) == 0, issues

def check_p04() -> tuple[bool, list[str]]:
    """P04: Experimental Design."""
    issues = []
    if not (WORKSPACE / "configs").exists():
        issues.append("configs/ directory missing.")
    return len(issues) == 0, issues

def check_p05() -> tuple[bool, list[str]]:
    """P05: Implementation & Computational Kernels."""
    issues = []
    if not (WORKSPACE / "src").exists():
        issues.append("src/ module directory missing.")
    return len(issues) == 0, issues

def check_p06() -> tuple[bool, list[str]]:
    """P06: Data Generation."""
    issues = []
    if not (WORKSPACE / "data/raw").exists():
        issues.append("data/raw/ missing.")
    return len(issues) == 0, issues

def check_p07() -> tuple[bool, list[str]]:
    """P07: Diagnostic Analysis."""
    issues = []
    if not (WORKSPACE / "data/processed").exists():
        issues.append("data/processed/ missing.")
    return len(issues) == 0, issues

def check_p08() -> tuple[bool, list[str]]:
    """P08: Manuscript Drafting."""
    issues = []
    qmd = WORKSPACE / "writing/manuscript/index.qmd"
    tex = WORKSPACE / "paper01/manuscript.tex"
    if not qmd.exists() and not tex.exists():
        issues.append("Manuscript source file missing in writing/manuscript/ or paper01/.")
    return len(issues) == 0, issues

def check_p09() -> tuple[bool, list[str]]:
    """P09: Red-team review."""
    issues = []
    agent_file = WORKSPACE / ".pi/agents/redteam-reviewer.md"
    if not agent_file.exists():
        issues.append(".pi/agents/redteam-reviewer.md missing.")
    return len(issues) == 0, issues

def check_p10() -> tuple[bool, list[str]]:
    """P10: Clean-room verification."""
    issues = []
    if not (WORKSPACE / "Dockerfile").exists():
        issues.append("Dockerfile missing.")
    if not (WORKSPACE / "planning/verification-report.md").exists():
        issues.append("planning/verification-report.md missing.")
    return len(issues) == 0, issues

def check_p11() -> tuple[bool, list[str]]:
    """P11: Submission packaging."""
    issues = []
    if not (WORKSPACE / "writing").exists():
        issues.append("writing/ directory missing.")
    return len(issues) == 0, issues

def check_p12() -> tuple[bool, list[str]]:
    """P12: Rebuttal & revisions."""
    issues = []
    if not (WORKSPACE / "planning/phases/P12_rebuttal_and_revision.md").exists():
        issues.append("P12 phase document missing.")
    return len(issues) == 0, issues

def check_p13() -> tuple[bool, list[str]]:
    """P13: Camera ready."""
    issues = []
    if not (WORKSPACE / "planning/phases/P13_camera_ready.md").exists():
        issues.append("P13 phase document missing.")
    return len(issues) == 0, issues

def check_p14() -> tuple[bool, list[str]]:
    """P14: Post-publication."""
    issues = []
    if not (WORKSPACE / "planning/phases/P14_postpub.md").exists():
        issues.append("P14 phase document missing.")
    return len(issues) == 0, issues

CHECKERS = {
    "P00": check_p00,
    "P01": check_p01,
    "P02": check_p02,
    "P03": check_p03,
    "P04": check_p04,
    "P05": check_p05,
    "P06": check_p06,
    "P07": check_p07,
    "P08": check_p08,
    "P09": check_p09,
    "P10": check_p10,
    "P11": check_p11,
    "P12": check_p12,
    "P13": check_p13,
    "P14": check_p14,
}

def main():
    parser = argparse.ArgumentParser(description="RPF v2.0 Phase Exit Verification Engine")
    parser.add_argument("phase", choices=list(CHECKERS.keys()), help="Phase ID to verify (e.g. P00)")
    args = parser.parse_args()

    phase = args.phase.upper()
    checker = CHECKERS[phase]

    print(f"============================================================")
    print(f"Running RPF v2.0 Phase Exit Acceptance Checks for: {phase}")
    print(f"============================================================")

    passed, issues = checker()

    if passed:
        print(f"\n>>> [PASS] All exit criteria satisfied for phase {phase}.")
        sys.exit(0)
    else:
        print(f"\n>>> [FAIL] Phase {phase} failed acceptance checks:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nPlease remediate the above items before exiting phase.")
        sys.exit(1)

if __name__ == "__main__":
    main()
