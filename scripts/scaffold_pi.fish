#!/usr/bin/env fish
# RPF v2.0 custom skills & tools scaffold — NON-DESTRUCTIVE.
#
# NOTE: fish has NO <<EOF heredocs (confirmed on fish 4.8.1; see `man fish-doc`,
# "Heredocs" section). Content is carried as single-quoted fish list elements and
# written with `printf '%s\n'` — the fish-documented equivalent. Single quotes =
# zero expansion: no $var, no backticks, no escape surprises (incl. Python code).

# --- Helper: create file (with parents) if missing, else warn + print content ---
# usage: merge_file <target> <line...>
function merge_file
    set -l target "$argv[1]"
    set -l lines $argv[2..-1]
    if test -f "$target"
        echo "⚠️ FILE EXISTS: $target. Please manually merge the following content:"
        printf '%s\n' $lines
        echo ""
    else
        mkdir -p (path dirname "$target")
        printf '%s\n' $lines > "$target"
        echo "created: $target"
    end
end

# --- 1. .pi/skills/phase-exit-validator/SKILL.md ---------------------------
set -l phase_exit_skill \
    '---' \
    'name: phase-exit-validator' \
    'description: Validates phase exit criteria before allowing progression.' \
    '---' \
    '' \
    '# Phase Exit Validator' \
    '' \
    '## Mandate' \
    'Before marking ANY phase complete, the agent MUST locate and execute:' \
    '' \
    '    python scripts/check_phase_exit.py <PHASE_ID>' \
    '' \
    '## Rules' \
    '' \
    '1. Run the checker for the target phase (P00..P14) before any completion claim.' \
    '2. If the script reports ANY failure, the agent MUST produce a structured' \
    '   remediation plan that addresses EVERY failing check.' \
    '3. The agent MUST NEVER hallucinate a PASS if the script fails or errors.' \
    '   A failed or errored run is a FAIL.' \
    '4. Do not proceed past the phase gate until the script exits 0.'

merge_file ".pi/skills/phase-exit-validator/SKILL.md" $phase_exit_skill

# --- 2. .pi/skills/ledger-update/SKILL.md -----------------------------------
set -l ledger_skill \
    '---' \
    'name: ledger-update' \
    'description: Enforces scope control and artifact generation for new claims.' \
    '---' \
    '' \
    '# Ledger Update' \
    '' \
    '## Mandate' \
    'Any new claim, experiment, or scope change proposed after phase P03 MUST be' \
    'recorded as a new row in `planning/ledger.md`.' \
    '' \
    '## Required Fields' \
    'The agent MUST populate every column of the new row:' \
    '' \
    '| Field         | Meaning                              |' \
    '|---------------|--------------------------------------|' \
    '| id            | Unique row identifier                |' \
    '| category      | claim / experiment / scope-change    |' \
    '| description   | What is claimed or proposed          |' \
    '| disposition   | accepted / rejected / deferred       |' \
    '| provenance    | Link to the supporting artifact      |' \
    '| impact        | Severity rating 1-5                 |' \
    '| probability   | Likelihood rating 1-5               |' \
    '| depends_on    | Prerequisite row IDs (or NONE)       |' \
    '' \
    '## Rules' \
    '' \
    '1. No post-P03 claim is valid without a ledger row.' \
    '2. Missing fields are a compliance failure; do not proceed.' \
    '3. Write the ledger row BEFORE code, experiments, or writing that depend on it.'

merge_file ".pi/skills/ledger-update/SKILL.md" $ledger_skill

# --- 3. .pi/skills/human-gate-serializer/SKILL.md ---------------------------
set -l human_gate_skill \
    '---' \
    'name: human-gate-serializer' \
    'description: Handles [HUMAN-GATE] checkpoints.' \
    '---' \
    '' \
    '# Human Gate Serializer' \
    '' \
    '## Mandate' \
    'When a `[HUMAN-GATE]` marker is reached, the agent MUST:' \
    '' \
    '1. HALT execution immediately; no downstream artifact may be touched.' \
    '2. Serialize current state (phase, task index, pending decisions) to' \
    '   `experiments/agent-state/<phase>_checkpoint.json`.' \
    '3. Generate a draft decision file at `decisions/human-gates/<phase>_HG.md`' \
    '   using the RPF decision template (`decisions/ADR-TEMPLATE.md`), leaving the' \
    '   `Decision` and `Sign-off` fields BLANK for the human.' \
    '' \
    '## Rules' \
    '' \
    '1. Never fill in the human-only fields.' \
    '2. Present the draft with clear, mutually exclusive options and trade-offs.' \
    '3. Await explicit human approval before continuing.'

merge_file ".pi/skills/human-gate-serializer/SKILL.md" $human_gate_skill

# --- 4. scripts/validate_manifest_schema.py -------------------------------
set -l validate_tool \
    '#!/usr/bin/env python3' \
    '"""RPF v2.0 manifest schema validator.' \
    '' \
    'Usage: python scripts/validate_manifest_schema.py <path/to/manifest.yaml>' \
    'Prints PASS or FAIL with field-level errors to stdout.' \
    'Exit code 0 on PASS, 1 on FAIL.' \
    '"""' \
    '' \
    'import argparse' \
    'import re' \
    'import sys' \
    'from pathlib import Path' \
    '' \
    'REQUIRED_FIELDS = [' \
    '    "schema_version", "run_id", "phase", "config", "seed",' \
    '    "hardware", "environment", "data", "tracking", "status",' \
    '    "compute", "numerical_sanity",' \
    ']' \
    '' \
    '' \
    'def main() -> int:' \
    '    parser = argparse.ArgumentParser(description="Validate an RPF v2.0 manifest.yaml")' \
    '    parser.add_argument("manifest", help="Path to the manifest.yaml to validate")' \
    '    args = parser.parse_args()' \
    '' \
    '    path = Path(args.manifest)' \
    '    if not path.is_file():' \
    '        print(f"FAIL: {args.manifest} does not exist or is not a file.")' \
    '        return 1' \
    '' \
    '    try:' \
    '        import yaml' \
    '    except ImportError:' \
    '        print("FAIL: PyYAML is required (pip install pyyaml).")' \
    '        return 1' \
    '' \
    '    raw_lines = path.read_text(encoding="utf-8").splitlines()' \
    '' \
    '    try:' \
    '        with path.open(encoding="utf-8") as fh:' \
    '            data = yaml.safe_load(fh)' \
    '    except yaml.YAMLError as exc:' \
    '        print(f"FAIL: {args.manifest} is not valid YAML.")' \
    '        for line in str(exc).splitlines():' \
    '            print(f"  {line}")' \
    '        return 1' \
    '' \
    '    if not isinstance(data, dict):' \
    '        print("FAIL: manifest root must be a YAML mapping.")' \
    '        return 1' \
    '' \
    '    missing = [' \
    '        field for field in REQUIRED_FIELDS' \
    '        if not any(re.match(rf"^{re.escape(field)}\s*:", line) for line in raw_lines)' \
    '    ]' \
    '' \
    '    if missing:' \
    '        print(f"FAIL: manifest is missing {len(missing)} mandatory field(s):")' \
    '        for field in missing:' \
    '            print(f"  - {field}")' \
    '        print("Expected: " + ", ".join(REQUIRED_FIELDS))' \
    '        return 1' \
    '' \
    '    print(f"PASS: {args.manifest} satisfies the RPF v2.0 manifest schema "' \
    '          f"({len(REQUIRED_FIELDS)} mandatory fields present).")' \
    '    return 0' \
    '' \
    '' \
    'if __name__ == "__main__":' \
    '    sys.exit(main())'

merge_file "scripts/validate_manifest_schema.py" $validate_tool

# --- 5. scripts/run_compliance_linter.py ----------------------------------
set -l linter_tool \
    '#!/usr/bin/env python3' \
    '"""RPF v2.0 compliance linter wrapper.' \
    '' \
    'Executes scripts/compliance_linter.py when present; otherwise falls back to' \
    'checking key RPF artifacts. Always prints a structured JSON report of' \
    'CC.N.M rules (PASS / FAIL / N/A) to stdout. Exit code 0 on successful run.' \
    '"""' \
    '' \
    'import json' \
    'import subprocess' \
    'import sys' \
    'from pathlib import Path' \
    '' \
    'WORKSPACE = Path(__file__).resolve().parent.parent.parent' \
    'LINTER = WORKSPACE / "scripts" / "compliance_linter.py"' \
    '' \
    'FALLBACK_CHECKS = [' \
    '    ("CC.1.1", "planning/standards.md", "Standards document present"),' \
    '    ("CC.1.2", "meta/seeds.yaml", "Seed registry present"),' \
    '    ("CC.2.1", "planning/risk-register.md", "Risk register present"),' \
    '    ("CC.5.6", ".antigravity/ci/reproducibility-smoke.yml", "CI reproducibility workflow present"),' \
    '    ("CC.6.1", "planning/ledger.md", "Claim ledger present"),' \
    ']' \
    '' \
    '' \
    'def fallback_report() -> dict:' \
    '    report = {' \
    '        "status": "PASS",' \
    '        "total_rules": len(FALLBACK_CHECKS),' \
    '        "passed_rules": 0,' \
    '        "failed_rules": 0,' \
    '        "na_rules": 0,' \
    '        "rules": [],' \
    '    }' \
    '    for rule_id, rel_path, desc in FALLBACK_CHECKS:' \
    '        ok = (WORKSPACE / rel_path).exists()' \
    '        entry = {' \
    '            "id": rule_id,' \
    '            "description": desc,' \
    '            "status": "PASS" if ok else "FAIL",' \
    '            "notes": "Artifact present" if ok else f"{rel_path} missing",' \
    '        }' \
    '        report["rules"].append(entry)' \
    '        if ok:' \
    '            report["passed_rules"] += 1' \
    '        else:' \
    '            report["failed_rules"] += 1' \
    '            report["status"] = "FAIL"' \
    '    report["rules"].append({' \
    '        "id": "CC.*",' \
    '        "description": "Full rule coverage",' \
    '        "status": "N/A",' \
    '        "notes": "scripts/compliance_linter.py absent; artifact checks only",' \
    '    })' \
    '    report["na_rules"] = 1' \
    '    return report' \
    '' \
    '' \
    'def main() -> int:' \
    '    if LINTER.is_file():' \
    '        try:' \
    '            result = subprocess.run(' \
    '                [sys.executable, str(LINTER), "--json"],' \
    '                capture_output=True, text=True, cwd=str(WORKSPACE), check=False,' \
    '            )' \
    '            report = json.loads(result.stdout) if result.stdout.strip() else {' \
    '                "status": "FAIL",' \
    '                "error": result.stderr.strip() or "linter produced no output",' \
    '                "rules": [],' \
    '            }' \
    '        except Exception as exc:' \
    '            report = {"status": "FAIL", "error": str(exc), "rules": []}' \
    '    else:' \
    '        report = fallback_report()' \
    '' \
    '    print(json.dumps(report, indent=2))' \
    '    return 0' \
    '' \
    '' \
    'if __name__ == "__main__":' \
    '    sys.exit(main())'

merge_file "scripts/run_compliance_linter.py" $linter_tool

echo "RPF v2.0 skills/tools pass complete."
