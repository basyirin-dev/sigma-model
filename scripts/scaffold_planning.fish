#!/usr/bin/env fish
# RPF v2.0 core planning artifacts scaffold — NON-DESTRUCTIVE.
#
# NOTE: fish has NO <<EOF heredocs (confirmed on fish 4.8.1; see `man fish-doc`,
# "Heredocs" section). Content is carried as single-quoted fish list elements and
# written with `printf '%s\n'` — the fish-documented equivalent. Single quotes =
# zero expansion: no $var, no backticks, no escape surprises.
#
# P00 EXIT CONSTRAINT: scripts/check_phase_exit.py requires planning/standards.md
# to contain >= 50 rules matching `- **CC.N.M:**` — the proposed standards block
# below contains 56 rules (8 per category x 7 categories).

# --- Helper: create file if missing, else warn + print proposed content ---
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

# --- 1. planning/roadmap.md --------------------------------------------------
set -l roadmap \
    '# RPF v2.0 Master Roadmap' \
    '' \
    '## Header Block' \
    '' \
    '| Field | Value |' \
    '|-------|-------|' \
    '| Date | <PIN: YYYY-MM-DD> |' \
    '| Status | <PIN: DRAFT / ACTIVE / COMPLETE> |' \
    '| Decision Context | <PIN: why this roadmap exists and what it decides> |' \
    '| Triggering Event | <PIN: what started this project> |' \
    '| Chosen Strategy | <PIN: e.g. narrow sigma-Trap paper first, two-subspace law second> |' \
    '| Constraints | <PIN: compute caps, deadline, venue, token budget> |' \
    '' \
    '## Phase Dependency Graph' \
    '' \
    '```' \
    'P00 -> P0.5 -> PCC -> P01 -> P02 -> P02.5 -> P03 [HUMAN-GATE] -> P04 -> P05 -> P06 -> P07 -> P08 -> P09 -> P10 -> P11 -> P12 -> P13 -> P14' \
    '```' \
    '' \
    'Legend: P00 setup, P0.5 seed/pinning, PCC pre-commit checks, P03 gates preregistration.' \
    'Phase documents live in `planning/phases/`; exit criteria enforced by `scripts/check_phase_exit.py`.' \
    '' \
    '## Total Project Budget Tracking' \
    '' \
    '| Phase | GPU hrs | TPU hrs | Agent tokens | Wall-clock (days) | Human hrs |' \
    '|-------|---------|---------|--------------|-------------------|-----------|' \
    '| P00 | 0 | 0 | 0 | 0 | 0 |' \
    '| P0.5 | 0 | 0 | 0 | 0 | 0 |' \
    '| PCC | 0 | 0 | 0 | 0 | 0 |' \
    '| P01 | 0 | 0 | 0 | 0 | 0 |' \
    '| P02 | 0 | 0 | 0 | 0 | 0 |' \
    '| P02.5 | 0 | 0 | 0 | 0 | 0 |' \
    '| P03 | 0 | 0 | 0 | 0 | 0 |' \
    '| P04 | 0 | 0 | 0 | 0 | 0 |' \
    '| P05 | 0 | 0 | 0 | 0 | 0 |' \
    '| P06 | 0 | 0 | 0 | 0 | 0 |' \
    '| P07 | 0 | 0 | 0 | 0 | 0 |' \
    '| P08 | 0 | 0 | 0 | 0 | 0 |' \
    '| P09 | 0 | 0 | 0 | 0 | 0 |' \
    '| P10 | 0 | 0 | 0 | 0 | 0 |' \
    '| P11 | 0 | 0 | 0 | 0 | 0 |' \
    '| P12 | 0 | 0 | 0 | 0 | 0 |' \
    '| P13 | 0 | 0 | 0 | 0 | 0 |' \
    '| P14 | 0 | 0 | 0 | 0 | 0 |' \
    '| **TOTAL** | 0 | 0 | 0 | 0 | 0 |' \
    '' \
    'Authoritative resource tracking lives in `planning/budget.md`; alert thresholds: 80% warning, 100% halt.'

merge_file "planning/roadmap.md" $roadmap

# --- 2. planning/standards.md ------------------------------------------------
set -l standards \
    '# RPF v2.0 Standards Codification (CC.N.M)' \
    '' \
    'This document codifies the enforceable standards. Format must match the' \
    'compliance linter pattern: `- **CC.N.M:** description`.' \
    '' \
    '## CC.1 Reproducibility' \
    '' \
    '- **CC.1.1:** Every execution (simulation, benchmark, or diagnostic) must log a validated `manifest.yaml` adhering to RPF v2.0 schema in `experiments/<run-id>/`.' \
    '- **CC.1.2:** All random operations must use pre-registered seeds sourced from `meta/seeds.yaml` with documented provenance.' \
    '- **CC.1.3:** Unseeded or dynamically seeded runs without registry entry are strictly forbidden in production phases (P06+).' \
    '- **CC.1.4:** Environment lockfiles (`requirements-lock.txt`, Dockerfile SHA-256) must be pinned and updated on every dependency change.' \
    '- **CC.1.5:** Raw data must never be committed; provenance pointers (dataset IDs, SHA-256) are recorded in manifests.' \
    '- **CC.1.6:** Experiments must declare deterministic flags (`torch.backends.cudnn.deterministic = True`) in code and manifests.' \
    '- **CC.1.7:** Generated figures and tables must map to a reproducible script or notebook; hand-edited plots are forbidden.' \
    '- **CC.1.8:** Docker clean-room builds must pin base image digests and rebuild deterministically.' \
    '' \
    '## CC.2 Numerical Integrity' \
    '' \
    '- **CC.2.1:** All ODE solvers must report residual norms and step-rejection rates at every checkpoint.' \
    '- **CC.2.2:** NaN/Inf or divergent runs must be tagged `NEGATIVE` and archived, never silently discarded.' \
    '- **CC.2.3:** Default tolerances are atol/rtol = 1e-10 unless justified in the manifest.' \
    '- **CC.2.4:** Energy, Lyapunov, or symplectic invariants must be tracked at every checkpoint.' \
    '- **CC.2.5:** Gradient norms must stay within declared bounds; explosions trigger kill-switch review.' \
    '- **CC.2.6:** Solver step-rejection rates above 25% require automatic fallback to stiff solvers (Radau/Tsit5).' \
    '- **CC.2.7:** Numerical results must be re-verified with a second method or higher precision before claim promotion.' \
    '- **CC.2.8:** Hardware-induced floating-point nondeterminism must be documented in manifests.' \
    '' \
    '## CC.3 Writing Quality' \
    '' \
    '- **CC.3.1:** No claim may outrun the evidence; evidence gates ambition.' \
    '- **CC.3.2:** Model theorem, empirical observation, and interpretation must be clearly separated in the text.' \
    '- **CC.3.3:** No grand-theory or origin claims are permitted in the narrow paper.' \
    '- **CC.3.4:** Every substantive claim must reference a ledger row or artifact.' \
    '- **CC.3.5:** Statistical results must report effect sizes and p-values or credible intervals.' \
    '- **CC.3.6:** Figures must be legible at venue size and carry complete captions.' \
    '- **CC.3.7:** Overclaiming verbs (proves, guarantees, derives) require a formal proof.' \
    '- **CC.3.8:** The phenomenological status of the posited ODEs must be stated precisely.' \
    '' \
    '## CC.4 Data Hygiene' \
    '' \
    '- **CC.4.1:** `data/raw/` is append-only after phase completion; modification requires an ADR.' \
    '- **CC.4.2:** Data must carry provenance (source URL, dataset ID, generation script, seed).' \
    '- **CC.4.3:** Synthetic data generation must be seeded and logged in the manifest.' \
    '- **CC.4.4:** PII or proprietary data must be excluded or sanitized before any processing.' \
    '- **CC.4.5:** Data splits must be seeded and fixed at preregistration (P03).' \
    '- **CC.4.6:** Large binaries must not enter the repository; use LFS or external stores.' \
    '- **CC.4.7:** Data versions are tracked via git tags and SHA-256 manifests.' \
    '- **CC.4.8:** Superseded or deleted datasets must be documented in the ledger.' \
    '' \
    '## CC.5 Release-Readiness' \
    '' \
    '- **CC.5.1:** Code must pass `ruff check` and pyright type checks before phase exit.' \
    '- **CC.5.2:** Unit and integration tests must pass before phase exit.' \
    '- **CC.5.3:** The reproducibility smoke test must pass in CI.' \
    '- **CC.5.4:** Manifests for all runs must validate against the RPF v2.0 schema.' \
    '- **CC.5.5:** Docs (README, `meta/ENVIRONMENT.md`, `meta/COLD_START.md`) must be current.' \
    '- **CC.5.6:** The CI workflow (`.antigravity/ci/reproducibility-smoke.yml`) must be present and green.' \
    '- **CC.5.7:** Submission bundles must be regenerable via `make` targets.' \
    '- **CC.5.8:** License and attribution must be present and correct.' \
    '' \
    '## CC.6 Agentic Protocol' \
    '' \
    '- **CC.6.1:** `planning/ledger.md` is the source of truth; every claim or scope change is a ledger row.' \
    '- **CC.6.2:** Phase exits require `python scripts/check_phase_exit.py <PHASE_ID>` with zero open failures.' \
    '- **CC.6.3:** `[HUMAN-GATE]` halts execution; state is serialized to `experiments/agent-state/`.' \
    '- **CC.6.4:** Kill-switch conditions trigger immediate halt and operator intervention.' \
    '- **CC.6.5:** Agents must never hallucinate PASS results or fabricate artifacts.' \
    '- **CC.6.6:** Agent token usage is budgeted and tracked in `planning/budget.md`.' \
    '- **CC.6.7:** Decisions are recorded as ADRs with bidirectional linkage (affects-phases, affects-ledger-rows).' \
    '- **CC.6.8:** Observational memory is persisted to disk before session context is lost.' \
    '' \
    '## CC.7 Ethics & Compliance' \
    '' \
    '- **CC.7.1:** No fabrication, falsification, or plagiarism in any artifact.' \
    '- **CC.7.2:** Data licenses must be respected and credited.' \
    '- **CC.7.3:** Compute usage must comply with platform quotas (e.g. Kaggle).' \
    '- **CC.7.4:** AI-assisted contributions must be disclosed per venue policy.' \
    '- **CC.7.5:** Peer-review integrity: no fake reviews and no coordinated pressure campaigns.' \
    '- **CC.7.6:** Conflicts of interest must be declared.' \
    '- **CC.7.7:** Human data requires privacy protection and consent.' \
    '- **CC.7.8:** Venue policies (e.g. TMLR) must be followed for submission and anonymity.' \
    '' \
    '## Compliance Matrix (auto-generated)' \
    '' \
    'Placeholder — regenerate with:' \
    '' \
    '    python scripts/generate_compliance_matrix.py --standards planning/standards.md --output planning/compliance-matrix.md'

merge_file "planning/standards.md" $standards

# --- 3. planning/ledger.md ---------------------------------------------------
set -l ledger \
    '# RPF v2.0 Scope Inventory (Claim Ledger)' \
    '' \
    '## Tag Legend' \
    '' \
    '| Tag | Meaning |' \
    '|-----|---------|' \
    '| keep | Retain in scope as-is |' \
    '| move | Move to another paper/phase |' \
    '| cut | Remove from scope entirely |' \
    '| defer | Postpone to a later phase |' \
    '| decide-at-P03 | Revisit and decide at the P03 gate |' \
    '' \
    '## Impact x Probability Matrix (5x5)' \
    '' \
    '| Impact \\ Prob | 1 | 2 | 3 | 4 | 5 |' \
    '|---------------|-----|-----|-----|-----|-----|' \
    '| 5 | 5 | 10 | 15 | 20 | 25 |' \
    '| 4 | 4 | 8 | 12 | 16 | 20 |' \
    '| 3 | 3 | 6 | 9 | 12 | 15 |' \
    '| 2 | 2 | 4 | 6 | 8 | 10 |' \
    '| 1 | 1 | 2 | 3 | 4 | 5 |' \
    '' \
    'Score = Impact x Probability. Rows scoring >= 12 are gate items (decide at P03).' \
    '' \
    '## Claims & Promises' \
    '' \
    '| ID | Category | Description | Source | Disposition | Rationale | Provenance | Impact | Prob | Depends_on | Verified_at | SHA-256 |' \
    '|----|----------|-------------|--------|-------------|-----------|------------|--------|------|------------|-------------|---------|' \
    '' \
    '## Scope Change Control' \
    '' \
    '1. Any new claim, experiment, or scope change after P03 MUST be a new ledger row before any other artifact.' \
    '2. All 12 columns MUST be populated; missing fields are a compliance failure.' \
    '3. Dispositions are decided at gates (P03, P10); `decide-at-P03` items cannot proceed past P03 unresolved.' \
    '4. Silent scope creep is forbidden: unlogged work is non-compliant and will be tagged `cut` on review.' \
    '5. Each row requires a `provenance` link to a durable artifact (manifest, ADR, or commit).' \
    '6. Rows are immutable once verified; amendments require a new row plus an ADR.'

merge_file "planning/ledger.md" $ledger

# --- 4. planning/risk-register.md --------------------------------------------
set -l risk_register \
    '# RPF v2.0 Risk Register' \
    '' \
    'Score = Prob x Impact. Open items with score >= 12 are blocking; >= 8 require mitigation plan.' \
    '' \
    '| ID | Description | Prob (1-5) | Impact (1-5) | Score | Owner | Due | Mitigation | Trigger | Contingency | Status |' \
    '|----|-------------|------------|--------------|-------|-------|-----|------------|---------|-------------|--------|' \
    '| R-001 | Kaggle GPU quota exceeded during P06 data generation | 3 | 3 | 9 | agent | P06 | Pre-quota budget in `planning/budget.md`; batching runs by quota window | quota warning at 80% | Shift to CPU-friendly workloads; defer non-critical runs to next quota window | OPEN |' \
    '| R-002 | Gate experiment underpowered to detect the sigma-trap effect | 3 | 4 | 12 | agent | P03 | Power analysis at preregistration; effect-size priors from pilot runs | pilot effect size below preregistered bound | Record NEGATIVE, expand N, or revise gate with ADR | OPEN |' \
    '| R-003 | ODE solver divergence in stiff bifurcation regime | 2 | 4 | 8 | agent | P05 | Implicit/Radau fallback; tolerance defaults per CC.2.3 | step-rejection rate > 25% | Auto-fallback to stiff solver; tag NEGATIVE if unresolved | OPEN |' \
    '| R-004 | Reviewer rejects the sigma-trap claim as under-motivated | 3 | 3 | 9 | human | P09 | Red-team review at P09; claim ledger discipline; related-work audit | red-team flags the claim as unsupported | Cut or scope the claim to the supported core (ADR) | OPEN |' \
    '| R-005 | Agent token budget exhausted before P08 manuscript | 2 | 3 | 6 | agent | ongoing | Token budget tracking in `planning/budget.md`; compress context via disk artifacts | usage > 80% of allocated tokens | Halt compute, serialize state, request operator decision | OPEN |'

merge_file "planning/risk-register.md" $risk_register

# --- 5. planning/budget.md ---------------------------------------------------
set -l budget \
    '# RPF v2.0 Resource Tracking Sheet' \
    '' \
    '## Resource Budget by Phase' \
    '' \
    '| Phase | GPU hrs | TPU hrs | Agent tokens | Wall-clock (days) | Human hrs | Kaggle kernels |' \
    '|-------|---------|---------|--------------|-------------------|-----------|----------------|' \
    '| P00 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P0.5 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| PCC | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P01 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P02 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P02.5 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P03 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P04 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P05 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P06 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P07 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P08 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P09 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P10 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P11 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P12 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P13 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| P14 | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '| **TOTAL** | 0 | 0 | 0 | 0 | 0 | 0 |' \
    '' \
    '## Alert Thresholds' \
    '' \
    '| Threshold | Action |' \
    '|-----------|--------|' \
    '| 80% of any resource | WARNING — halt new work, notify operator, serialize state |' \
    '| 100% of any resource | HALT — kill-switch, stop all agent activity until operator decision |' \
    '' \
    '## Agent Performance Metrics' \
    '' \
    '| Metric | Target | Current | Notes |' \
    '|--------|--------|---------|-------|' \
    '| Tokens per phase | <PIN> | 0 | Tracked from provider logs |' \
    '| Phase exit pass rate | 100% | 0 | From `scripts/check_phase_exit.py` |' \
    '| Unit test pass rate | 100% | 0 | CI pytest run |' \
    '| Compliance linter score | 100% | 0 | From `scripts/compliance_linter.py` |' \
    '| Kill-switch triggers | 0 | 0 | Every trigger logged with root cause |' \
    '| Hallucination incidents | 0 | 0 | Includes fabricated PASS or artifacts |' \
    '| NEGATIVE results logged | >= 1 per failure | 0 | No silent discards |'

merge_file "planning/budget.md" $budget

echo "RPF v2.0 planning artifacts pass complete."
