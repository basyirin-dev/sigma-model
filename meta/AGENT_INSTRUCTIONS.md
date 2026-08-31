# Agent Instructions & Operating Manual — RPF v2.0

## 1. Operating Philosophy & Core Directives

All autonomous agents operating within this repository must adhere strictly to the Research Planning Framework (RPF) v2.0 standards. The following core directives govern every action, tool execution, and code change:

1. **Evidence Gates Ambition (CC.3 & CC.6):**
   - No code, experiment, or manuscript claim may outrun documented evidence recorded in `planning/ledger.md`.
   - Never generate downstream conclusions or commit text asserting strong theoretical claims ("proves", "guarantees", "derives") unless grounded in verified proofs, numerical convergence tables, or formal empirical findings with recorded p-values/effect sizes.

2. **Artifact-First Governance (CC.1):**
   - Every computational step, experiment run, analysis, or human decision MUST produce a version-controlled or immutable disk artifact.
   - Code execution without a corresponding `manifest.yaml` in `experiments/<run-id>/` is prohibited.
   - Unregistered ad-hoc parameter sweeps or unseeded runs are non-compliant.

3. **Fail Fast and Log Everything (CC.2 & CC.4):**
   - Failed, divergent, or degenerate runs must never be silently discarded.
   - Any run encountering NaN/Inf, divergence in numerical integration, or loss explosion must be tagged as `NEGATIVE` and archived in `experiments/negative-results/` with a documented root-cause analysis and corresponding ledger update.

4. **Strict Context Management:**
   - Maintain clean session state. Rely on deterministic disk artifacts (`planning/ledger.md`, `planning/roadmap.md`, `meta/seeds.yaml`) as the source of truth rather than transient conversational context.

---

## 2. Tool Usage & Execution Protocols

### A. Manifest Validation
- Every experiment run (script or notebook) must generate a fully compliant `manifest.yaml` under `experiments/<run-id>/manifest.yaml`.
- The manifest must include:
  - `schema_version`: "2.0"
  - `run_id`, `phase`, `timestamp`
  - `config`: Full hyperparameter tree and configuration hash
  - `seed`: Valid `seed_id` registered in `meta/seeds.yaml`
  - `hardware`: CPU/GPU metadata, VRAM footprint
  - `environment`: Git commit hash, Python/Julia package versions, Docker SHA-256
  - `data`: Input data paths and SHA-256 hashes
  - `numerical_sanity`: Residual norms, energy conservation checks, gradient norm bounds
  - `status`: SUCCESS | FAILED | DIVERGED | ABORTED
- Run `python -m pi.tools.validate_manifest_schema <path_to_manifest>` to ensure zero validation errors.

### B. Phase Exit Gating
- Before claiming completion of any phase (P00 through P14), execute:
  ```bash
  python scripts/check_phase_exit.py <PHASE_ID>
  ```
- If any check fails, the agent must not progress. It must produce a structured remediation plan and resolve every failing check.

### C. Human Gate Handoffs (`[HUMAN-GATE]`)
- When reaching a designated human gate:
  1. Freeze execution context.
  2. Serialize active state to `experiments/agent-state/<phase>_checkpoint.json`.
  3. Generate a structured draft decision record in `decisions/human-gates/<phase>_<gate-id>.md` using `decisions/ADR-TEMPLATE.md`.
  4. Present clear, mutually exclusive decision paths with trade-off analysis.
  5. Await explicit human approval before altering downstream artifacts.

---

## 3. Kill-Switch Conditions & Emergency Halts

The agent and automated harness must immediately HALT and request operator intervention if any of the following occur:

1. **Budget Overrun:** Compute budget exceeds 80% warning threshold or 120% hard cap in `planning/budget.md`.
2. **Consecutive Verification Failures:** Three (3) consecutive unit, integration, or phase exit test failures occur.
3. **Data Integrity Violation (CC.4):** Attempt to modify `data/raw/` when git tag `p06-data-complete` is present.
4. **Unlogged Numerical Anomalies (CC.2):** Undetected NaN/Inf or ODE solver step rejection rates exceeding 25% without automatic fallback to stiff solvers.
5. **Gate Contradiction:** Experimental data explicitly falsifies a preregistered hypothesis without an ADR reconciliation.

---

## 4. Conventional Commit & Git Discipline

All commits must follow the RPF conventional commit format:
```text
[<PHASE>][<Category>][<ACTION>] <Description>
```
- `<PHASE>`: P00 to P14 (e.g. `[P00]`, `[P05]`, `[P10]`)
- `<Category>`: `Infrastructure`, `Theory`, `Simulation`, `Analysis`, `Writing`, `Audit`, `Governance`
- `<ACTION>`: `INIT`, `FEAT`, `FIX`, `REFACTOR`, `TEST`, `DOCS`, `GATE`, `CLEAN`

Examples:
- `[P00][Infrastructure][INIT] Initialized RPF v2.0 workspace and Pi agent ecosystem`
- `[P02][Theory][FEAT] Added two-subspace separation proof to appendix`
- `[P06][Simulation][FIX] Fallback to Radau solver on stiff ODE boundary`

---

## 5. Numerical Integrity & Solver Tolerances (CC.2)

- Default explicit solvers: `atol = 1e-10`, `rtol = 1e-10`.
- Stiff dynamical systems (e.g. sigma-trap bifurcation regimes): Use implicit/Radau/Tsit5 with adaptive stepping.
- Invariant preservation: Track Lyapunov spectra, symplectic invariants, or energy conservation metrics at every checkpoint.
