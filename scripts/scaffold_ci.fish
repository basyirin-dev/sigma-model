#!/usr/bin/env fish
# RPF v2.0 CI/CD workflow & Git hooks scaffold — NON-DESTRUCTIVE.
#
# NOTE: fish has NO <<EOF heredocs (confirmed on fish 4.8.1; see `man fish-doc`,
# "Heredocs" section). Content is carried as single-quoted fish list elements and
# written with `printf '%s\n'` — the fish-documented equivalent. Single quotes =
# zero expansion (this matters: the pre-commit hook below contains `$()` and
# `$manifest` which must reach the file LITERALLY).
#
# IMPORTANT: the pre-commit hook body is POSIX sh on purpose — git runs hooks
# with /bin/sh, NOT with the interactive fish shell.

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

# --- 1. .antigravity/ci/reproducibility-smoke.yml ---------------------------
# GitHub Actions-style workflow (Antigravity convention) for push + PR.
set -l smoke_workflow \
    'name: RPF v2.0 Reproducibility Smoke Test & Governance CI' \
    '' \
    'on:' \
    '  push:' \
    '    branches: [ main, master ]' \
    '  pull_request:' \
    '    branches: [ main, master ]' \
    '' \
    'jobs:' \
    '  reproducibility-smoke:' \
    '    runs-on: ubuntu-latest' \
    '    steps:' \
    '      - name: Checkout repository' \
    '        uses: actions/checkout@v4' \
    '' \
    '      - name: Set up Python' \
    '        uses: actions/setup-python@v5' \
    '        with:' \
    '          python-version: "3.11"' \
    '          cache: "pip"' \
    '' \
    '      - name: Install dependencies' \
    '        run: |' \
    '          python -m pip install --upgrade pip' \
    '          pip install -r requirements.txt' \
    '          pip install pytest pyyaml' \
    '' \
    '      - name: Run unit tests' \
    '        run: |' \
    '          PYTHONPATH=. pytest tests/unit/ -v' \
    '' \
    '      - name: Validate all manifest schemas' \
    '        run: |' \
    '          found=0' \
    '          for manifest in $(find experiments -name "manifest.yaml" 2>/dev/null); do' \
    '            found=1' \
    '            python scripts/validate_manifest_schema.py "$manifest"' \
    '          done' \
    '          if [ "$found" -eq 0 ]; then' \
    '            echo "No manifest.yaml files found in experiments/ — nothing to validate."' \
    '          fi' \
    '' \
    '      - name: Run RPF compliance linter' \
    '        run: |' \
    '          python scripts/run_compliance_linter.py' \
    '' \
    '      - name: Check conventional commit format' \
    '        run: |' \
    '          commit_msg="$(git log -1 --pretty=%B)"' \
    '          if ! echo "$commit_msg" | grep -qE "^\[[IBRV]\]\[[LCW]\]\[Δ\]"; then' \
    '            echo "::error::Commit message does not match [Tag][Scope][Δ] Description"' \
    '            exit 1' \
    '          fi'

merge_file ".antigravity/ci/reproducibility-smoke.yml" $smoke_workflow

# --- 2. .git/hooks/pre-commit ------------------------------------------------
# POSIX sh hook (git runs hooks with /bin/sh — NEVER fish syntax in hooks).
# Blocks the commit when any staged manifest.yaml fails schema validation.
set -l pre_commit_hook \
    '#!/bin/sh' \
    '# RPF v2.0 pre-commit hook — blocks commits that stage invalid manifest.yaml files.' \
    '# POSIX sh only (NOT fish): git executes hooks with /bin/sh.' \
    '' \
    'staged_manifests="$(git diff --cached --name-only --diff-filter=ACM | grep "manifest\.yaml$" || true)"' \
    '' \
    'if [ -z "$staged_manifests" ]; then' \
    '    exit 0' \
    'fi' \
    '' \
    'for manifest in $staged_manifests; do' \
    '    echo "[PRE-COMMIT] Validating staged manifest: $manifest"' \
    '    if ! python scripts/validate_manifest_schema.py "$manifest"; then' \
    '        echo "[PRE-COMMIT BLOCKED] Manifest $manifest failed RPF v2.0 schema validation." >&2' \
    '        exit 1' \
    '    fi' \
    'done' \
    '' \
    'echo "[PRE-COMMIT] All staged manifests valid."' \
    'exit 0'

merge_file ".git/hooks/pre-commit" $pre_commit_hook

# Rule 4: executable hooks must be chmod +x (harmless if the file already existed)
chmod +x ".git/hooks/pre-commit"

echo "RPF v2.0 CI/CD & hooks pass complete."
