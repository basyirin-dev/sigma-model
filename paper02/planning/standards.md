# Standards & Cross-Cutting Governance (CC.N.M) — RPF v2.0

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Version:** 2.0.0
**Framework:** The Research Planning Framework (RPF **v2.0.0**) — reference: `paper02/meta/RPF_v2.0.md`
**Migration:** Restructured 2026-08-23 from RPF v1.0.0 (16 rules) to v2.0 (≥50 rules). Every rule carries `verifiable_by`, `enforcement_phase`, `origin`, `delta_from`. Compliance matrix auto-generatable per `scripts/generate_compliance_matrix.py` (script not yet implemented — matrix maintained manually below; flagged `TOOLING-PENDING`).

---

## 1. Compliance Matrix (rows = phases P00–P14, columns = CC.1–CC.7)

| Phase | CC.1 Repro | CC.2 Numerical | CC.3 Writing | CC.4 Data | CC.5 Release | CC.6 Agentic | CC.7 Ethics |
|-------|:----------:|:--------------:|:------------:|:---------:|:------------:|:------------:|:-----------:|
| **P00** | Required | — | — | — | — | Required | — |
| **P0.5** | — | — | — | — | — | Required | — |
| **PCC** | — | — | — | — | — | Required | — |
| **P01** | — | — | Required | — | — | Required | — |
| **P02** | — | — | Required | — | — | Required | — |
| **P02.5** | — | — | — | — | — | Required | — |
| **P03** | Required | Required | — | Required | — | Required | — |
| **P03.1** | Required | Required | — | Required | — | Required | — |
| **P04** | Required | Required | — | Required | — | Required | Required |
| **P05** | Required | Required | — | Required | — | Required | — |
| **P06** | Required | Required | — | Required | — | Required | — |
| **P07** | Required | Required | Required | Required | — | Required | — |
| **P08** | — | — | Required | — | Required | Required | — |
| **P09** | — | — | Required | — | Required | Required | Required |
| **P09.5** | — | — | Required | — | — | Required | — |
| **P10** | Required | Required | Required | Required | Required | Required | — |
| **P11** | — | — | Required | — | Required | Required | — |
| **P11.5** | — | — | Required | — | Required | Required | — |
| **P12** | — | — | Required | — | Required | Required | — |
| **P13** | Required | Required | Required | Required | Required | Required | — |
| **P14** | — | — | — | — | — | Required | — |

---

## 2. Rule Registry

Legend: `☐` = open checkbox; `verifiable_by`: `script` (automated) or `human` (manual check); `enforcement` = phases where the rule is Required; `origin` = source (RPF v2.0 § / prior rule); `delta_from` = v1.0.0 rule id when carried over, else `new`.

### CC.1 — Reproducibility (8 rules)

| ID | Rule (verifiable statement) | Verif. | Enforcement | Origin | Δ |
|----|-----------------------------|:------:|-------------|--------|---|
| CC.1.1 | Hardware & runtime provenance: every computational output records Python/JAX/PyTorch versions, library versions, CUDA device model, random seed, and Git commit hash. | script | P03, P03.1, P05–P07, P10, P13 | RPF §3.4 / v1 CC.1.1 | v1 CC.1.1 |
| CC.1.2 | Deterministic seed protocol: every multi-seed run derives its seed via `seed = run_id * 42 + 7`; deterministic GPU flags (`torch.backends.cudnn.deterministic = True`, `benchmark = False`) mandatory. | script | P03, P03.1, P05, P06, P10, P13 | RPF §3.4 / v1 CC.1.2 | v1 CC.1.2 |
| CC.1.3 | Scripted re-execution: no computational result is valid unless reproducible from a pinned command-line script in `paper02/src/`; no unversioned interactive cells for production outputs. | script | P03, P03.1, P05–P07, P10, P13 | RPF §3.4 / v1 CC.1.3 | v1 CC.1.3 |
| CC.1.4 | Experiment manifest: every run produces `manifest.yaml` per the RPF v2.0 schema (config hash, seed provenance, hardware, environment, data/output hashes, tracking IDs, numerical sanity) and validates against the schema. | script | P03, P03.1, P05–P07, P10 | RPF §XII | new |
| CC.1.5 | Data versioning: raw and processed data are DVC-tracked; derived data are produced only by idempotent scripts. | script | P06, P07, P10 | RPF §II | new |
| CC.1.6 | Containerization: computational environments are reproducible from a pinned Dockerfile (image hash recorded in manifests). | script | P03, P03.1, P05, P06, P10 | RPF §3.1 | new |
| CC.1.7 | Clean-room rebuild: P10 rebuilds the environment from pinned files only and re-runs ≥1 representative experiment; hashes/metrics must match. | script | P10 | RPF §P10 | new |
| CC.1.8 | Seed registry: all seeds are drawn from `meta/seeds.yaml` with provenance (who/why, phase_created, used_in). | script | P03, P03.1, P05–P07, P10 | RPF §II/meta | new |

### CC.2 — Numerical Integrity (7 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.2.1 | Solver tolerances: continuous-time gradient-flow integration enforces `atol <= 1e-8`, `rtol <= 1e-8` (stiff/bifurcation: `1e-10`) per the RPF v2.0 tolerance presets. | script | P03, P03.1, P05–P07, P10, P13 | RPF §3.3 / v1 CC.2.1 | v1 CC.2.1 |
| CC.2.2 | Kernel unit testing: every custom numerical kernel, loss projection, or CKA metric function has ≥3 passing unit tests before production deployment. | script | P03, P03.1, P05, P06, P10 | RPF §P05 / v1 CC.2.2 | v1 CC.2.2 |
| CC.2.3 | Equivalence testing: any empirical-equivalence claim is validated via TOST within a pre-registered margin (default ±2.5 %); `p > 0.05` alone never proves equality. | script | P03, P03.1, P07, P08 | RPF §P02.5 / v1 CC.2.3 | v1 CC.2.3 |
| CC.2.4 | Convergence criteria: every solver run records convergence status; non-converged runs are excluded per pre-registered exclusion criteria and logged. | script | P03, P03.1, P05–P07, P10 | RPF §P03 T5 | new |
| CC.2.5 | Analysis-script unit testing: every analysis script in `src/analysis/` has unit tests (not just kernels). | script | P07, P10 | RPF §CC.2 | new |
| CC.2.6 | Numerical sanity checks: energy conservation, invariant preservation, and residual norms are monitored for every solver call; any failure invalidates the run per exclusion criteria. | script | P03, P03.1, P06, P07, P10 | RPF §P03 T5 | new |
| CC.2.7 | Statistical reporting: effect sizes and confidence intervals reported alongside p-values; multiple-hypothesis correction specified when >1 test. | script | P03, P07, P08 | RPF §P02.5/P07 T8 | new |

### CC.3 — Writing Quality (8 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.3.1 | Abstract constraint: manuscript abstract ≤250 words and states the claim level (descriptive, model theorem, empirical) explicitly. | script | P08, P09 | RPF §P08 T2 / v1 CC.3.1 | v1 CC.3.1 |
| CC.3.2 | Vector graphics & units: every publication figure is compiled vector (TikZ/PGFPlots or 300+ DPI PNG) with labeled axes, units, and explicit error bands (95 % CI). | human | P07, P08 | RPF §P07 / v1 CC.3.2 | v1 CC.3.2 |
| CC.3.3 | Tripartite claim separation: text strictly separates (i) model theorems, (ii) empirical findings, (iii) open conjectures. | human | P08, P09, P10 | v1 CC.3.3 | v1 CC.3.3 |
| CC.3.4 | Figure provenance metadata: every figure has a `*.metadata.json` sidecar (script hash, data hash, params, seed) and a caption that cites it. | script | P07, P08 | RPF §P07 T10 | new |
| CC.3.5 | Colorblind-safe palettes: all figures pass a colorblind-safety check (no red-green-only encoding). | script | P07, P08 | RPF §P07 T10 | new |
| CC.3.6 | Alt text: every figure includes alt text for accessibility. | human | P07, P08 | RPF §P07 T10 | new |
| CC.3.7 | Overclaim prohibition: absolute terms ("proves", "always", "never", "guarantees") are scanned (`overclaim_detector.py`) and resolved against ledger evidence strength; 0 unresolved flags before P09 close. | script | P08, P09 | RPF §P08 T5 | new |
| CC.3.8 | Orphan-claim prohibition: every ledger `keep` claim appears in the manuscript; every manuscript claim maps to a ledger row or cited source. | script | P08, P09, P10 | RPF §P08 T9/P09 T4 | new |

### CC.4 — Data Hygiene (7 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.4.1 | Raw data immutability: raw tensors/logs in `paper02/data/raw/` are write-once; all processed tables come from idempotent scripts. | script | P06, P07, P10 | RPF §II / v1 CC.4.1 | v1 CC.4.1 |
| CC.4.2 | Zero test-set leakage: zero-shot OOD splits have zero overlap with training primitives; support disjointness formally audited. | script | P04, P06, P10 | v1 CC.4.2 | v1 CC.4.2 |
| CC.4.3 | SHA-256 hashing: every data file and run output has a recorded SHA-256 hash. | script | P06, P07, P10 | RPF §P06 T6 | new |
| CC.4.4 | Hidden test set: final-evaluation data is held out and inaccessible to model selection. | human | P04, P06, P10 | RPF §P04 T7 | new |
| CC.4.5 | Unblinding protocol: any planned comparison that requires blinded evaluation defines when/how unblinding occurs, before data analysis. | human | P04, P07 | RPF §CC.4 | new |
| CC.4.6 | NaN/Inf screening: automated check that no output tensor contains NaN/Inf; failures logged with the `NEGATIVE` tag. | script | P06, P07, P10 | RPF §P06 | new |
| CC.4.7 | Negative-results registry: failed/aborted runs are documented (what failed, why, lesson) with the `NEGATIVE` tag, never discarded. | script | P06, P07, P10 | RPF §P06 T9 | new |

### CC.5 — Release Readiness (8 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.5.1 | Self-contained repository: the codebase builds and runs on a clean machine per `meta/README.md` without private API dependencies. | script | P11, P12 | v1 CC.5.1 | v1 CC.5.1 |
| CC.5.2 | Double-blind compliance: submitted manuscripts strip identifying metadata, author names, affiliations, and private URLs. | human | P08, P11 | v1 CC.5.2 | v1 CC.5.2 |
| CC.5.3 | Licenses: code and data licenses are declared (LICENSE files) at P00. | human | P00, P11 | RPF §P00 T2 | new |
| CC.5.4 | Archival DOIs: code + data archived on Zenodo (DOI) and Software Heritage (identifier) at P11. | human | P11 | RPF §P11 T3 | new |
| CC.5.5 | Software & data citation: all toolkits and datasets cited with papers/DOIs in the manuscript. | human | P08, P11 | RPF §P08 T8 | new |
| CC.5.6 | Availability statements: code and data availability statements are mandatory manuscript sections. | script | P08, P11 | RPF §P08 T6 | new |
| CC.5.7 | Open-science badges: eligibility for Open Data/Open Code/Preregistered badges assessed and recorded at P11. | human | P11 | RPF §P11 T4 | new |
| CC.5.8 | Plain-language summary: `writing/plain-language-summary.md` (≤500 words, no jargon) at P11. | script | P11 | RPF §P11 T5 | new |

### CC.6 — Agentic Protocol (8 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.6.1 | Conventional commits: `[Tag][Scope][Δ]` with Tag ∈ {P00..P14, ADR, META, FIX}, Scope ∈ phase canonical names (Infrastructure, Research, Standards, Literature, Hypothesis, PreReg, Gate, Design, Implementation, Data, Analysis, Writing, Review, Reconcile, Verification, Package, Preprint, Close, Revision, PostPub), Δ ∈ {INIT, Δ, HOTFIX}. | script | all | RPF §VI / v1 CC.6.1 (updated) | v1 CC.6.1 |
| CC.6.2 | Artifact-gated mutation: the agent never silently overwrites or discards a prior-phase artifact without an approved superseding ADR or HUMAN-GATE sign-off. | human | all | v1 CC.6.2 | v1 CC.6.2 |
| CC.6.3 | Kill-switch conditions: halt + escalate + serialize state on (a) same exit criteria failing 3×, (b) compute >20 % over budget, (c) output contradicting gate binding constraints, (d) ledger↔artifact mismatch >3, (e) gate SLA exceeded without fallback, (f) critical CVE. | human | all | RPF §XI.1 | new |
| CC.6.4 | State serialization at gates: agent state (phase, task index, ledger snapshot, pending decisions) saved to `experiments/agent-state/<phase>_checkpoint.json` at every HUMAN-GATE. | script | all | RPF §XI.2 | new |
| CC.6.5 | HUMAN-GATE SLA & recording: every gate responds within 48h (72h full manuscript) with a decision record in `decisions/human-gates/`; fallback decisions are conservative (halt/RE-GATE/NO-GO). | human | all | RPF §XI.2–3 | new |
| CC.6.6 | Context management: documents >10k tokens are chunked with 200-token summaries in `agent-state/summaries/`; the ledger is always loaded in full. | human | all | RPF §XI.5 | new |
| CC.6.7 | Agent performance metrics: phase time ≤120 % estimate, exit-criteria first-pass ≥80 %, gate wait ≤24h, tokens ≤ budget, kill-switches 0, compliance linter 100 %, tracked in `planning/budget.md`. | script | all | RPF §XI.6 | new |
| CC.6.8 | Tool fallback protocol: tool outages follow the RPF v2.0 fallback table (e.g., Consensus down >24h → Semantic Scholar + manual), logged when triggered. | human | P0.5, P01, P09 | RPF §XI.7 | new |

### CC.7 — Ethics & Compliance (4 rules)

| ID | Rule | Verif. | Enforcement | Origin | Δ |
|----|------|:------:|-------------|--------|---|
| CC.7.1 | Transparency statement: the manuscript includes a Broader Impact / Ethical Considerations section discussing automated schema induction. | human | P08, P09, P11 | v1 CC.7.1 | v1 CC.7.1 |
| CC.7.2 | IRB / human-subjects compliance: any human-subject data requires IRB approval recorded in the ledger. | human | P04, P09 | RPF §CC.7 | new |
| CC.7.3 | Data-use agreements: third-party data usage respects licenses/terms, documented in `data/` provenance. | human | P04, P06, P09 | RPF §CC.7 | new |
| CC.7.4 | Competing interests & funding: manuscript declares funding sources and competing interests (CRediT). | human | P08, P11 | RPF §P08 T7 | new |

**Rule count: 8 + 7 + 8 + 7 + 8 + 8 + 4 = 50 rules** (≥50 per RPF v2.0 §VIII).

---

## 3. Deltas & Adaptations

| Date | Rule ID | Change from RPF v1.0.0 | Rationale |
|------|---------|------------------------|-----------|
| 2026-08-23 | All | **v1 → v2.0 migration:** rule count 16 → 50; every rule gained `verifiable_by`, `enforcement_phase`, `origin`, `delta_from`; compliance matrix extended to P00–P14 (added P02.5, P03.1, P09.5, P11.5, P13, P14). | RPF v2.0 adopted per PI directive (2026-08-23). |
| 2026-08-23 | CC.6.1 | Commit convention updated: Tag set extended to P00–P14; Scope restricted to phase canonical names; Δ ∈ {INIT, Δ, HOTFIX}. | RPF v2.0 commit examples (`[P01][Literature][INIT]`). |
| 2026-08-23 | CC.2.3 | Unchanged in substance; now linked to `planning/preregistration.md` (P02.5) as the pre-registered margin source. | v2.0 pre-registration phase. |
| 2026-08-23 | CC.1.4/CC.2.6 | New manifest + numerical-sanity rules made binding at P03 (gate) — the in-flight gate must produce `manifest.yaml`-style records and sanity checks before evaluation is accepted. | RPF v2.0 §XII/P03 T5; applies to the pending gate evaluation, not retroactively to smoke runs. |
| 2026-08-23 | Tooling | `generate_compliance_matrix.py` / `compliance_linter.py` / `overclaim_detector.py` / `check_phase_exit.py` / `hash_artifacts.py` / `transition_checklist.py` not yet implemented (flag `TOOLING-PENDING`); matrix maintained manually; commit-format and manifest checks executed ad hoc until scripts land. | Migration scope decision (2026-08-23): governance + phase docs, no automation scripts yet. |
