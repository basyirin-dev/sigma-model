#!/usr/bin/env fish
# RPF v2.0 scaffold — idempotent, non-destructive.
# Skips existing directories; never overwrites existing files; merges .gitignore entries only if missing.

# ---------------------------------------------------------------------------
# 1. Directory scaffolding (skip if already present, mkdir -p otherwise)
# ---------------------------------------------------------------------------
set -l dirs \
    planning/phases \
    decisions \
    src/analysis \
    src/simulation \
    src/utils \
    notebooks \
    configs/experiment \
    configs/environment \
    data/raw \
    data/processed \
    data/synthetic \
    experiments \
    literature/pdfs \
    writing/manuscript \
    writing/figures \
    writing/supplementary \
    scripts \
    tests/unit \
    tests/integration \
    tests/reproducibility \
    .antigravity/ci \
    meta

for dir in $dirs
    if test -d "$dir"
        echo "skip (exists):    $dir"
    else
        mkdir -p "$dir"
        echo "created:          $dir"
    end
end

# ---------------------------------------------------------------------------
# 2. data/raw/.gitkeep — create ONLY if missing AND data/raw/ is empty.
#    If .gitkeep is missing but the dir is non-empty, flag for manual merge.
# ---------------------------------------------------------------------------
set -l gitkeep "data/raw/.gitkeep"

if test -f "$gitkeep"
    echo "skip (exists):    $gitkeep"
else if test -z (ls -A "data/raw")
    touch "$gitkeep"
    echo "created:          $gitkeep"
else
    echo "WARNING: $gitkeep missing but data/raw/ is not empty — add manually (needs merging)."
end

# ---------------------------------------------------------------------------
# 3. .gitignore merge — append each RPF entry ONLY if not already present
#    (whole-line, fixed-string match so entries like '!data/raw/.gitkeep' are exact)
# ---------------------------------------------------------------------------
set -l entries \
    "data/raw/*" \
    "!data/raw/.gitkeep" \
    "experiments/*/outputs/" \
    ".pi/state/" \
    "__pycache__/" \
    ".venv/"

for entry in $entries
    if grep -qxF "$entry" .gitignore
        echo "skip (present):   $entry"
    else
        echo "$entry" >> .gitignore
        echo "appended:         $entry"
    end
end

echo "RPF v2.0 scaffold complete."
