# The Research Planning Framework (RPF) v2.0 — Reference Copy

**Project-local reference copy** of the framework adopted for Paper 02 planning.
**Provenance:** Provided by the PI on 2026-08-23 (source paste, 1704 lines). This file is a condensed-but-complete normative reference; the canonical full text lives in the 2026-08-23 session archive. Planning docs link to this file.
**Version:** 2.0.0 · **Execution model:** 90 % autonomous agent / 10 % human-in-the-loop
**Governance:** Every phase closes on a verifiable exit criterion. Every decision produces a committed artifact. No writing outruns evidence.
**Budget:** ≈ 125 tasks / 90 subtasks across 21 phases (incl. conditional) · 25–45 days wall-clock (excl. P13/P14) · ~54 GPU hrs · ~16 human hrs
**Critical path:** P00 → P0.5 → PCC → P01 → P02 → P02.5 → **P03** → P04 → P05 → P06 → P07 → P08 → P09 → P10 → P11 → P12

---

## I. Core Principles

1. **Evidence gates ambition.** P03 empirically validates the central hypothesis before downstream writing, large-scale simulation, or scope expansion.
2. **Phases close on verifiable exit criteria, not effort.** Machine-checkable conditions + automated acceptance tests.
3. **Three orthogonal planning axes.** Time → Roadmap · Space → Standards (CC.N.M) · Scope → Ledger.
4. **Every consequential decision produces a committed artifact.** ADRs, gate-result docs, ledger — never chat history.
5. **Traceability.** Every constraint cites its origin; every claim links to evidence; ADRs ↔ ledger bidirectionally.
6. **Agent autonomy is default; human intervention is exception.** Humans intervene only at `HUMAN-GATE` checkpoints (SLA 48h, 72h for full-manuscript reviews).
7. **Reproducibility is non-negotiable.** Versioned scripts, pinned containerized environment, clean-room rebuild at P10.
8. **Fail fast, log everything.** Negative results are first-class artifacts tagged `NEGATIVE`.
9. **Scope is controlled.** Any new claim/experiment/deliverable after P03 requires an ADR + ledger update + impact assessment.
10. **The framework improves itself.** Post-mortems feed `standards.md` Deltas; RPF is versioned and re-planned per project.

## II. Document Architecture (key paths)

- `planning/`: `roadmap.md`, `standards.md`, `ledger.md`, `risk-register.md`, `budget.md`, `gate-result.md`, `verification-report.md`, `reproducibility-report.md`, `literature-audit.md`, `preregistration.md`, `phases/P00..P14_*.md`, `compliance-matrix.md` (auto-generated).
- `decisions/`: numbered immutable ADRs (`ADR-TEMPLATE.md` with `affects-ledger-rows`, `affects-phases` fields) + `human-gates/<phase>_<gate-id>.md` decision records.
- `src/` (analysis/, simulation/, utils/), `notebooks/` (Kaggle-pinned), `configs/` (Hydra/OmegaConf), `data/` (raw immutable / processed by script, DVC), `experiments/YYYY-MM-DD_<run-id>/manifest.yaml + outputs/` (+ `run-log.csv`, `negative-results/`, `agent-state/` checkpoints), `literature/` (pdfs/, screening-log.csv PRISMA, knowledge-graph.json, bibliography.bib Zotero), `writing/` (manuscript/Quarto, figures with metadata sidecars, supplementary, plain-language-summary.md), `scripts/` (check_phase_exit.py, compliance_linter.py, generate_compliance_matrix.py, overclaim_detector.py, hash_artifacts.py, transition_checklist.py), `tests/` (unit/integration/reproducibility), `.github|.antigravity/ci/`, `Dockerfile`, `dvc.yaml`, `Snakefile|nextflow.config`, `meta/` (README, AGENT_INSTRUCTIONS, ENVIRONMENT, COLD_START, seeds.yaml), `tags/` (p00-done, p03-gate-passed, v1.0-submitted…).

## III. Toolchain (fallbacks)

Repo: Google Antigravity + Git (fallback GitHub/GitLab) · Heavy compute: Kaggle Notebooks GPU/TPU (fallback local GPU/Colab) · Literature grounding: Consensus (fallback Semantic Scholar) · Source-grounded QA: NotebookLM (fallback manual) · Citation graph: ResearchRabbit / Semantic Scholar · References: Zotero + BibTeX · Data versioning: DVC · Experiment tracking: MLflow/W&B · Orchestration: Snakemake/Nextflow · Config: Hydra/OmegaConf · Container: Docker/Apptainer · Archival: Zenodo + Software Heritage.
**Engines (P05–P07):** Diffrax (JAX), DifferentialEquations.jl (+Flux/SciML), PyHessian/Curvlinops, Geomstats/TAGTorch, Giotto-tda/Ripser, TransformerLens/PRISM.
**Solver tolerance presets (CC.2):** Stiff ODE (Julia Rodas5/CVODE_BDF): atol/rtol 1e-10, max steps 1e6 · Neural ODE (JAX Dopri5/Tsit5): 1e-8/1e-8/1e5 · SDE (JAX Euler/Milstein): 1e-6/1e-6/1e5 · SDE (Julia SRIW1/SOSRI): 1e-8/1e-8/1e6 · CDE (JAX Heun/Dopri5): 1e-8/1e-8/1e5.
**Environment pinning (non-negotiable):** Python/Julia/JAX exact versions, locked deps, Docker image hash, Kaggle kernel ID+version, seeds from `meta/seeds.yaml`, hardware, MLflow/W&B run ID.

## IV. Dependency & Parallelism Rules

P00–P02.5 strictly sequential · **P03 strictly sequential; nothing downstream until gate verdict** · P03.1 only if P03=INCONCLUSIVE (bounded budget, binary outcome) · P04–P07 strictly sequential after P03 PASS · P05 arms parallel, P06 Kaggle runs parallel, P07 analyses parallel (geometric ∥ topological ∥ interpretability) · P08 sequential · P09/P09.5 sequential · P10 sequential (independent re-derivation) · P11/P11.5 sequential · P12 sequential · P13 triggered by reviewers, sequential · P14 ongoing.

## V. Total Project Budget (`planning/budget.md`)

| Resource | P00 | P0.5 | PCC | P01 | P02 | P02.5 | P03 | P04 | P05 | P06 | P07 | P08 | P09 | P10 | P11 | P12 | P13 | Total |
|----------|-----|------|-----|-----|-----|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------|
| **GPU hrs** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 4 | 20 | 8 | 0 | 0 | 2 | 0 | 0 | 4 | 40 |
| **TPU hrs** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| **Agent tokens** | 50k | 80k | 40k | 120k | 60k | 30k | 100k | 80k | 150k | 100k | 200k | 180k | 120k | 80k | 60k | 40k | 100k | 1.49M |
| **Wall-clock (days)** | 0.5 | 1.5 | 0.5 | 2.5 | 1.5 | 1 | 2.5 | 2.5 | 4 | 4 | 4 | 4 | 2.5 | 1.5 | 1.5 | 1 | 10 | 45 |
| **Human hrs** | 0.5 | 1 | 0.5 | 0.5 | 1 | 0.5 | 1 | 1 | 0.5 | 0.5 | 1 | 1.5 | 2 | 0.5 | 0.5 | 1 | 3 | 16 |
| **Kaggle kernels** | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 5 | 15 | 8 | 0 | 0 | 2 | 0 | 0 | 3 | 35 |

Alert: 80 % → warn; 100 % → halt + human approval. Slack: +20 % wall-clock on critical path.

## VI. Phase Definitions (condensed — full task lists live in `planning/phases/`)

| Phase | Tasks/Sub | Duration | GPU | Git tag | Abort threshold | Human gates (SLA 48h unless noted) |
|-------|-----------|----------|-----|---------|-----------------|--------------------------------------|
| P00 Repo & Infra | 8/3 | 0.5d | 0 | `p00-done` | Cannot init repo → escalate | Repo visibility; Kaggle credentials |
| P0.5 User Research | 6/4 | 1.5d | 0 | `p0.5-grounded` | Consensus+NotebookLM down >24h → fallback | Curated doc set; audit completeness |
| PCC Standards | 7/5 | 0.5d | 0 | `pcc-standards-v1` | None | PI approves standards |
| P01 Literature Survey | 8/6 | 2.5d | 0 | `p01-survey-done` | <20 papers → halt | Gap novelty confirmed |
| P02 Hypothesis & Risk | 6/4 | 1.5d | 0 | `p02-hypothesis` | None (pivot if impossible) | PI approves hypothesis+gate target |
| P02.5 Pre-registration | 5/4 | 1d | 0 | `p02.5-preregistered` | None | PI approves preregistration (halt fallback) |
| **P03 GATE** | **7/10** | **2.5d** | **2** | `p03-gate-*` | Compute >2× → halt; p>α & effect<min → FAIL | PI directive PROCEED/RE-GATE/ABORT (48h, fallback RE-GATE) |
| P03.1 Sub-gate (cond.) | 3/2 | 1d | 1 | `p03.1-resolved` | — | — |
| P04 Experimental Design | 8/6 | 2.5d | 0 | `p04-protocol` | Gate FAILED → not started | PI approves protocol (halt) |
| P05 Implementation | 10/8 | 4d | 4 | `p05-implemented` | Coverage <80% or lint>0 → halt | None (novel algorithm → ADR+gate) |
| P06 Data Generation | 9/7 | 4d | 30 | `p06-data-complete` | NaN/Inf → halt arm; budget >20% → halt all | Anomaly flagging |
| P07 Analysis | 12/10 | 4d | 8 | `p07-analysis-done` | Analysis contradicts gate → halt | PI reviews figures/interpretation |
| P08 Writing | 10/6 | 4d | 0 | `p08-draft-v1` | >5 `keep` claims missing after 2 passes → halt | PI full-draft review (72h) |
| P09 Internal Review | 9/6 | 2.5d | 0 | `p09-reviewed` | >10 red-team issues after 2 passes → halt | PI approves revisions (72h); co-authors |
| P09.5 Co-author (cond.) | 5/3 | 1.5d | 0 | `p09.5-reconciled` | Unresolvable conflict → escalate | Co-author sign-off (72h) |
| P10 Verification | 8/5 | 1.5d | 2 | `p10-verified` | Any non-negotiable FAIL → halt | PI GO/NO-GO (fallback NO-GO) |
| P11 Pre-submission | 9/5 | 1.5d | 0 | `p11-packaged` | Venue format fail ×2 → escalate | PI approves package |
| P11.5 Preprint (cond.) | 5/3 | 0.5d | 0 | `p11.5-preprint` | — | PI approves preprint/social |
| P12 Submission & Close | 8/5 | 1d | 0 | `p12-submitted` + `v1.0-submitted` | Portal error >3 → manual | PI executes submission; approves v2 roadmap (72h) |
| P13 Revision (cond.) | 8/6 | 5–15d | 4 | `p13-revision-N` | — | PI approves revision (72h) |
| P14 Post-pub (ongoing) | 4/2 | Ongoing | 0 | — | — | PI responds to challenges (7d) |

**P03 gate verdict logic:** PASS (primary metric meets threshold, secondary consistent) → unlock P04 · FAIL → halt, return to P02 or terminate · INCONCLUSIVE (within pre-specified ambiguity band) → **P03.1 sub-gate**: ≤3 runs, distinct seeds, ≤1 GPU hr total, binary ≥2/3 PASS→PASS else FAIL; no further iteration.
**P03 gate-result mandatory fields:** hypothesis_id, gate_date, pre_registration_ref, adr_ref, design (toolkit, config_hash, seed, docker_hash), primary_metric (name/threshold/observed/p/effect_size/verdict), secondary_results[], exploratory_results[], exclusions, verdict, binding_constraints[], claim_dependency_flags[], power_analysis (method/power/effect_size/n_runs).

## VII. Standards Document (CC.N.M) — v2

Groups (≥50 rules total): CC.1 Reproducibility ≥8 (DVC, Docker, Kaggle pinning, clean-room, Snakemake, Hydra) · CC.2 Numerical integrity ≥7 (tolerance presets, sanity checks, unit tests for analysis scripts) · CC.3 Writing ≥8 (colorblind-safe, alt text, figure provenance metadata, overclaim prohibition, Quarto) · CC.4 Data hygiene ≥7 (DVC, SHA-256, hidden test sets, unblinding, raw immutable) · CC.5 Release ≥8 (Zenodo DOI, SWH, software/data citation, availability statements, badges, plain-language summary) · CC.6 Agentic ≥8 (kill-switch, state serialization, SLA, context mgmt, performance metrics) · CC.7 Ethics ≥4 (IRB, competing interests, funding, data-use agreements).
Per rule: `id, statement, verifiable_by (script|human), enforcement_phase[], origin, delta_from`. Compliance matrix auto-generated (`scripts/generate_compliance_matrix.py`), linter `scripts/compliance_linter.py` (PASS/FAIL/N/A per rule; CI fails on Required-rule FAIL).

## VIII. Ledger Structure — v2

Tag legend: `keep | move | cut | defer | decide-at-P03 | re-verify-at-PNN | shipped | missing-from-draft | NEGATIVE`.
Impact×Probability matrix (5×5): Impact 5/Prob 1 → Monitor … Mitigate (standard 5×5 action grid).
Columns: `ID | Category | Description | Source | Disposition | Rationale | Provenance{type,confidence,version} | Impact(1-5) | Prob(1-5) | Depends_on | Verified_at | SHA-256`.
Claim dependency graph (JSON): `{"C001": {"depends_on": [], "children": [...]}}` — parent failure auto-flags children.
Scope change control (post-P03): new ADR + ledger row + risk-register + budget impact + HUMAN-GATE approval. Delete list; Negative Results Registry (run_id, phase, what failed, why, lesson, tag, date).

## IX. Risk Register Structure

`ID | Description | Prob(1-5) | Impact(1-5) | Score | Owner | Due | Mitigation | Trigger | Contingency | Status` — ≥5 risks, each with owner + due date.

## X. Agent Protocol — v2

**Kill-switch:** same phase exit criteria fail 3× → halt+escalate · compute >20% over → halt · output contradicts gate binding constraints → halt+flag · ledger↔artifact mismatch >3 → freeze+re-audit · gate SLA exceeded with no fallback → halt · critical CVE → patch/rollback.
**Human gate SLA:** 48h (72h full manuscript); reminder 24h; escalation Agent → PI → Dept head (>7d); conservative fallback default; state serialized to `experiments/agent-state/<phase>_checkpoint.json` at every gate.
**Decision record template** (`decisions/human-gates/<phase>_<gate-id>.md`): Phase, Gate ID, Decision, Rationale, Date, Decision-maker, Consequences, Sign-off, Agent state path.
**RACI per phase:** R=does work, A=owns outcome, C=consulted, I=informed.
**Context mgmt:** chunk >10k-token docs; 200-token summaries to `agent-state/summaries/`; ledger always loaded fully.
**Performance metrics:** phase time ≤120 % estimate, exit-criteria first-pass ≥80 %, gate wait ≤24h, tokens ≤ budget, kill-switches 0, linter 100 %.
**Tool fallbacks & evaluation criteria:** use ResearchRabbit only when citation chain unresolvable in ≥3 hops; Consensus for quantitative claim verdicts; NotebookLM for source-grounded QA.

## XI. Experiment Manifest Schema (`experiments/<run-id>/manifest.yaml`)

`schema_version, run_id, phase, timestamp, config{hydra_config_hash, config_path, overrides[]}, seed{value, provenance}, hardware{gpu, ram_gb, tpu, kaggle_kernel_id, kaggle_kernel_version}, environment{docker_image_hash, python_version, jax_version, diffrax_version, julia_version, differentialequations_version}, dependencies_hash, data{input_hashes[], output_hashes[]}, tracking{mlflow_run_id, wandb_run_id}, status, compute{gpu_hours, wall_clock_seconds}, numerical_sanity{energy_conservation_error, max_residual_norm, invariant_drift, all_passed}` — CI validates schema; missing fields fail CI.

## XII. CI Pipeline

`reproducibility-smoke.yml` (every commit: docker build, pytest unit, smoke test, manifest schema validation, compliance linter, commit-format check, file-size check, security scan) · `lint-typecheck.yml` (src/ commits: ruff, mypy, coverage) · `security-scan.yml` (weekly + dep changes: CVE + license).

## XIII. Workflow Orchestration

Snakemake/Nextflow chains scripts (simulate → analyze → render) with `resources.gpu_hours`, manifests as rule outputs. Hydra/OmegaConf configs per experiment (`configs/experiment/*.yaml`) with seed provenance. Figures carry `*.metadata.json` sidecars (script hash, data hash, params).

---

*Condensed reference copy — normative content preserved. Deltas applied to this project are recorded in `planning/standards.md` §Deltas.*
