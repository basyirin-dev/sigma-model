# Standards & Cross-Cutting Governance (CC.N.M) — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Version:** 2.0.0 (Synchronized to Compliance Linter: 54 Rules)
**Framework:** The Research Planning Framework (RPF **v2.0.0**) — reference: `paper/meta/RPF_v2.0.md`
**Rule Count Reconciliation:** `standards.md` rule count = **54** · `run_compliance_linter` rule count = **54** (100% synchronized).

---

## 1. Compliance Matrix (rows = phases P00–P14, columns = CC.1–CC.7)

| Phase | CC.1 Repro (8) | CC.2 Numerical (10) | CC.3 Writing (8) | CC.4 Data (8) | CC.5 Release (6) | CC.6 Agentic (8) | CC.7 Ethics (6) |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **P00** | — | — | — | — | Required | Required | — |
| **P0.5** | — | — | — | — | — | Required | — |
| **PCC** | — | — | — | — | — | Required | — |
| **P01** | — | — | — | — | — | Required | — |
| **P02** | — | — | — | — | — | Required | — |
| **P02.5** | — | — | — | — | — | Required | — |
| **P03** | Required | Required | — | — | — | Required | — |
| **P03.1** | Required | Required | — | — | — | Required | — |
| **P04** | — | — | — | Required | — | Required | Required |
| **P05** | Required | Required | — | — | — | Required | — |
| **P06** | Required | Required | — | Required | — | Required | Required |
| **P07** | Required | Required | Required | Required | — | Required | — |
| **P08** | — | Required | Required | — | Required | Required | Required |
| **P09** | — | — | Required | — | — | Required | Required |
| **P09.5** | — | — | — | — | — | Required | — |
| **P10** | Required | Required | Required | Required | — | Required | — |
| **P11** | — | — | — | — | Required | Required | Required |
| **P11.5** | — | — | — | — | — | Required | — |
| **P12** | — | — | — | — | Required | Required | — |
| **P13** | Required | Required | — | — | — | Required | — |
| **P14** | — | — | — | — | — | Required | — |

---

## 2. Rule Registry (54 Operational Rules)

### CC.1 — Reproducibility (8 rules)
- **CC.1.1:** Every execution (simulation, benchmark, or diagnostic) must log a validated `manifest.yaml` adhering to RPF v2.0 schema in `experiments/<run-id>/`.
- **CC.1.2:** All random operations must use pre-registered seeds sourced from `meta/seeds.yaml` with documented provenance (`seed = run_id * 42 + 7`).
- **CC.1.3:** Unseeded or dynamically seeded runs without registry entry are strictly forbidden in production phases (P06+).
- **CC.1.4:** Environment lockfiles (`requirements-lock.txt`, Dockerfile SHA-256) must be pinned and updated on every dependency change.
- **CC.1.5:** PyTorch deterministic mode must be enforced (`torch.backends.cudnn.deterministic = True`, `torch.backends.cudnn.benchmark = False`).
- **CC.1.6:** Hardware metadata, GPU model, CUDA driver version, and host OS must be recorded in run manifests.
- **CC.1.7:** Snakemake workflow pipelines (`Snakefile`) must be capable of executing all data processing and figure generation in a single command.
- **CC.1.8:** Unit and integration test suites in `tests/` must pass 100% in a clean-room Docker container prior to phase exit P10.

### CC.2 — Numerical Integrity (10 rules)
- **CC.2.1:** Standard explicit ODE integrations must use strict tolerances: `atol <= 1e-10` and `rtol <= 1e-10`.
- **CC.2.2:** Stiff dynamical regimes must employ implicit or adaptive stiff solvers (e.g. Radau, Tsit5 with stiffness detection) to prevent spurious limit cycles.
- **CC.2.3:** Integrators must monitor invariant preservation (energy conservation, symplectic 2-form, or Lyapunov spectrum residuals).
- **CC.2.4:** Integrator step rejection rates exceeding 25% must trigger an automatic fallback warning and switch to stiff solvers.
- **CC.2.5:** Any simulation output containing `NaN` or `Inf` must immediately halt the pipeline and serialize diagnostics to `experiments/negative-results/`.
- **CC.2.6:** Loss and gradient norm bounds must be logged at every epoch; gradient clipping must be explicitly documented with clipping thresholds.
- **CC.2.7:** Hessian spectral radius and top-k eigenvalues must be computed with Lanczos iteration depth $\ge 100$.
- **CC.2.8:** Floating-point precision for reference ODE trajectories must be `float64` (`torch.float64` / `Float64` in Julia/JAX).
- **CC.2.9:** Numerical integration grid spacing must be subjected to mesh-refinement sensitivity checks (halving $\Delta t$ must yield relative error $< 10^{-6}$).
- **CC.2.10:** Numerical sanity checks must be recorded under `numerical_sanity` section in every run manifest.

### CC.3 — Writing Discipline (8 rules)
- **CC.3.1:** Evidence gates ambition: every claim in `writing/` must map directly to a verified row in `planning/ledger.md`.
- **CC.3.2:** Explicit distinction must be maintained between *Model Theorem* (mathematical deductions from posited ODEs), *Empirical Observation* (experimental findings on neural networks), and *Interpretation* (theoretical conjectures).
- **CC.3.3:** Unbounded universal statements ("proves", "guarantees", "derives fundamental truth") are prohibited unless accompanied by formal mathematical proofs.
- **CC.3.4:** All empirical claims must report sample sizes ($N \ge 5$ random seeds; $N=30$ for primary Phase 06 cells), central tendency, confidence intervals (95% CI or bootstrap), and exact p-values.
- **CC.3.5:** Manuscript drafting must adhere to double-blind anonymity standards prior to acceptance (no un-anonymized author institutions or self-identifying URLs).
- **CC.3.6:** Every figure in `writing/figures/` must be generated programmatically from tracked code with figure captions explaining axes, units, and uncertainty bands.
- **CC.3.7:** Negative and null results must be given equal prominence in the text when addressing preregistered hypotheses.
- **CC.3.8:** Plain-language summary in `writing/plain-language-summary.md` must be kept updated to accurately reflect the latest accepted findings.

### CC.4 — Data Hygiene (8 rules)
- **CC.4.1:** Raw benchmark datasets stored in `data/raw/` are strictly immutable once the dataset creation milestone is reached (`p06-data-complete` tag).
- **CC.4.2:** Any preprocessing applied to `data/raw/` must be deterministic, automated via scripts in `src/data/` or `src/utils/`, and output to `data/processed/`.
- **CC.4.3:** Data leakage audits must be executed to ensure zero overlap between train, validation, and out-of-distribution (OOD) test splits ($\forall i \neq j: \text{supp}(\mathcal{D}_i) \cap \text{supp}(\mathcal{D}_j) = \emptyset$).
- **CC.4.4:** Synthetic data generated for toy dynamical tests must reside in `data/synthetic/` with generative code and parameter configs tracked in Git.
- **CC.4.5:** Large binary artifacts, checkpoints, and intermediate pickle files must be excluded from Git commits via `.gitignore`.
- **CC.4.6:** Datasets must include a `metadata.json` or `README.md` documenting schema, token vocabularies, sequence lengths, and creation timestamps.
- **CC.4.7:** Checksum integrity (SHA-256) of all input datasets must be verified before experiment execution (`paper/data/raw/checksums.sha256`).
- **CC.4.8:** Data ablation splits must be pre-stratified and indexed deterministically.

### CC.5 — Code Quality & Release Readiness (6 rules)
- **CC.5.1:** Python package `sigma_align` / `src` must install cleanly in editable mode via `pip install -e .` without unhandled dependency conflicts.
- **CC.5.2:** All public functions, classes, and computational kernels must feature type hints (Python 3.11+ syntax) and Sphinx/Google docstrings.
- **CC.5.3:** Codebase must pass `ruff check` with zero errors under configured rule-sets (`E,F,I,N,W`).
- **CC.5.4:** Codebase must pass `pyright` type checks on basic mode without critical diagnostic failures in core source directories.
- **CC.5.5:** Open-source release bundle must include a valid `LICENSE` (e.g. MIT/Apache-2.0) and citation guidelines (`CITATION.cff` or BibTeX).
- **CC.5.6:** Continuous integration pipeline (`reproducibility-smoke.yml`) must run and pass on push and pull requests.

### CC.6 — Agentic Governance & Safety (8 rules)
- **CC.6.1:** Autonomous agents must check `planning/ledger.md` before initiating new tasks to prevent duplicate or conflicting exploration.
- **CC.6.2:** At every `[HUMAN-GATE]`, agent context must be serialized to `experiments/agent-state/<phase>_checkpoint.json`.
- **CC.6.3:** Agents must generate a draft Architecture Decision Record (`decisions/human-gates/<phase>_<gate-id>.md`) prior to prompting the human lead.
- **CC.6.4:** Agents must never forge or hallucinate human sign-offs; human approval blocks must remain blank until explicitly approved.
- **CC.6.5:** Conventional commit message format `[<PHASE>][<Category>][<ACTION>] <Description>` must be strictly enforced for all agent commits.
- **CC.6.6:** When encountering an unrecoverable failure or budget breach (>80%), the agent must halt and execute a structured handoff.
- **CC.6.7:** Agents must record token consumption and compute resource usage in `planning/budget.md`.
- **CC.6.8:** Changes to planning or governance documents must be recorded with bidirectional references to relevant ADRs and ledger items.

### CC.7 — Ethics, Security & Dual-Use (6 rules)
- **CC.7.1:** Theoretical findings must be analyzed for dual-use implications regarding steering or adversarial exploitation of neural representations.
- **CC.7.2:** Public dataset scraping must comply with API terms of service and robot exclusion protocols without collecting personal identifiable information (PII).
- **CC.7.3:** No proprietary or copyrighted test splits from private benchmark suites may be committed without explicit licensing clearance.
- **CC.7.4:** Computational footprint and environmental carbon impact must be estimated and disclosed in the manuscript supplementary material.
- **CC.7.5:** Research protocols involving human evaluators or red-teaming reviews must ensure informed consent and anonymized logging.
- **CC.7.6:** Research artifacts must undergo security scanning to prevent accidental inclusion of API keys, tokens, or private endpoints.

---

## 3. Summary Count Verification
- **Total Enforced Rules:** $8 + 10 + 8 + 8 + 6 + 8 + 6 = \mathbf{54\text{ rules}}$.
- **Operational Verification:** Automated by `run_compliance_linter`.
