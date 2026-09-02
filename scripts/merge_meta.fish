#!/usr/bin/env fish
# RPF v2.0 meta-configuration generator/merger — NON-DESTRUCTIVE.
#
# IMPORTANT: fish has NO <<EOF heredocs (confirmed on fish 4.8.1; see `man fish-doc`
# section "Heredocs"). Content is therefore carried as single-quoted fish list
# elements and written with `printf '%s\n'` — the fish-documented equivalent.
# Single quotes = zero expansion: no $var, no backticks, no escape surprises.

# --- 0. Ensure meta/ exists (rule: mkdir -p) ---------------------------
if not test -d meta
    mkdir -p meta
end

# --- Helper: create file if missing, otherwise warn + print proposed content ---
# usage: merge_file <target> <line...>
function merge_file
    set -l target "$argv[1]"
    set -l lines $argv[2..-1]
    if test -f "$target"
        echo "⚠️ FILE EXISTS: $target. Please manually merge the following content:"
        printf '%s\n' $lines
        echo ""
    else
        printf '%s\n' $lines > "$target"
        echo "created: $target"
    end
end

# --- 1. meta/AGENT_INSTRUCTIONS.md --------------------------------------
set -l agent_instructions \
    '# RPF v2.0 Agent Operating Manual' \
    '' \
    '## 1. Core Directives' \
    '' \
    '1. **Evidence Gates Ambition** — No plan, code, or claim may outrun the evidence' \
    '   recorded in `planning/ledger.md`. Empirical results precede conclusions;' \
    '   unbacked claims are non-compliant.' \
    '' \
    '2. **Artifact-First (no chat-only plans)** — Every plan, decision, and result MUST' \
    '   exist as a durable disk artifact (markdown, YAML, manifest). A plan that lives' \
    '   only in conversation does not exist.' \
    '' \
    '3. **Fail Fast / Log Everything** — Failed, divergent, or degenerate runs are never' \
    '   deleted or hidden. Tag them `NEGATIVE` and log root cause in `planning/ledger.md`' \
    '   and `experiments/negative-results/`.' \
    '' \
    '4. **Context Management (observational memory)** — Disk artifacts are the source of' \
    '   truth (ledger, roadmap, `meta/seeds.yaml`, manifests). Persist key observations' \
    '   to observational memory before session context is lost.' \
    '' \
    '## 2. Tool Usage Rules' \
    '' \
    '1. Always validate `manifest.yaml` schemas before registering a run (zero validation' \
    '   errors required).' \
    '2. Run the compliance linter before every phase exit; do not exit a phase with open' \
    '   compliance failures.' \
    '3. At every `[HUMAN-GATE]`, freeze execution, serialize state to a checkpoint' \
    '   artifact, and draft the decision record before proceeding.' \
    '' \
    '## 3. Kill-Switch Conditions — HALT and escalate immediately' \
    '' \
    '1. Compute budget usage > 80% of `planning/budget.md`.' \
    '2. More than 3 consecutive compliance failures.' \
    '3. A result contradicts a binding constraint in `gate-result.md`.' \
    '4. `pi-antigravity` API errors (auth, rate limit, 5xx) that block execution.' \
    '' \
    '## 4. Provider Note' \
    '' \
    'Use the active `pi-antigravity` provider for all agent operations. Optimize prompts' \
    'and reasoning budget for Gemini Flash 3.7 (High): compact context, strong' \
    'step-by-step reasoning, fast token streaming. Do not fall back to another provider' \
    'without recording a decision.'

merge_file "meta/AGENT_INSTRUCTIONS.md" $agent_instructions

# --- 2. meta/COLD_START.md ----------------------------------------------
set -l cold_start \
    '# Cold Start — RPF v2.0 Bootstrap (CachyOS)' \
    '' \
    '## One-Command Bootstrap' \
    '' \
    'Run from the repository root:' \
    '' \
    '    paru -S --noconfirm python-pip python-virtualenv; and python -m venv .venv; and source .venv/bin/activate.fish; and pip install -r requirements.txt; and pi install npm:pi-antigravity; and pi login antigravity; and pi doctor' \
    '' \
    '## Step-by-Step' \
    '' \
    '1. Install system packages:' \
    '       paru -S python-pip python-virtualenv' \
    '' \
    '2. Create and activate the Python virtual environment:' \
    '       python -m venv .venv' \
    '       source .venv/bin/activate.fish' \
    '' \
    '3. Install Python dependencies:' \
    '       pip install -r requirements.txt' \
    '' \
    '4. Install the pi-antigravity provider:' \
    '       pi install npm:pi-antigravity' \
    '' \
    '5. Authenticate with the provider:' \
    '       pi login antigravity' \
    '' \
    '6. Verify the agent toolchain:' \
    '       pi doctor'

merge_file "meta/COLD_START.md" $cold_start

# --- 3. meta/seeds.yaml --------------------------------------------------
set -l seeds \
    'seeds:' \
    '  - seed_id: "seed-001"' \
    '    value: 42' \
    '    provenance: "RPF v2.0 initial setup"' \
    '    phase_created: "P00"' \
    '  - seed_id: "seed-002"' \
    '    value: 777' \
    '    provenance: "RPF v2.0 initial setup"' \
    '    phase_created: "P00"' \
    '  - seed_id: "seed-003"' \
    '    value: 1337' \
    '    provenance: "RPF v2.0 initial setup"' \
    '    phase_created: "P00"'

merge_file "meta/seeds.yaml" $seeds

# --- 4. meta/ENVIRONMENT.md ----------------------------------------------
set -l environment \
    '# Environment Specification (RPF v2.0)' \
    '' \
    '## Host System' \
    '- OS: CachyOS (Arch-based, x86-64-v3/v4 optimized packages)' \
    '- Shell: fish' \
    '- Package manager: paru' \
    '' \
    '## Pinned Toolchain (fill in at build/install time)' \
    '| Component            | Pinned version / hash          |' \
    '|----------------------|--------------------------------|' \
    '| Python               | <PIN: python_version>          |' \
    '| JAX                  | <PIN: jax_version>             |' \
    '| Julia                | <PIN: julia_version>           |' \
    '| Docker image         | <PIN: docker_image_sha256>     |' \
    '| pi-antigravity model | <PIN: model_name> (e.g. gemini-2.5-flash or higher-tier Gemini Flash 3.7 High) |' \
    '' \
    '## Provider' \
    '- AI provider: pi-antigravity' \
    '- Reasoning profile: Gemini Flash 3.7 (High)'

merge_file "meta/ENVIRONMENT.md" $environment

echo "meta-configuration pass complete."
