# Paper 02 — Phase Roadmap (RPF v2.0)

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** The Research Planning Framework (RPF) **v2.0.0** — reference: `paper/meta/RPF_v2.0.md`
**Status:** P00–P05 closed (P05 **CERTIFIED_PASS**) · **P06 blocked on remediation (production not authorized)**
**Date:** 2026-08-27 (Pre-Phase 06 Remediation Active)
**Decision Context:** Successor to Paper 01 v2 (submitted to TMLR on OpenReview). Addresses the microscopic modeling conjecture by deriving and experimentally validating the critical compositional pressure law $\lambda_{\text{crit}} = b_C / a_C \iff R_0 = 1$ under continuous gradient flow.
**Strategy:** Evidence-bound execution under RPF v2.0. No downstream writing or scaling outruns the P03 Mechanism Gate verdict.
**Target Venue:** NeurIPS / ICLR (Primary), JMLR (Secondary).
**Migration note:** Phases P00–P02 were executed under RPF v1.0.0 and are annotated "closed under v1, migrated"; their exit artifacts were re-checked against v2.0 acceptance criteria where feasible (2026-08-23).

---

## Deliverables & Phase Table

| # | Deliverable | Path | Phase | Git tag | Status |
|---|-------------|------|-------|---------|:------:|
| D00 | Project skeleton & environment pinning | `paper/meta/*` | P00 | `p00-done` | ✅ Closed (v1, migrated) |
| D0.5 | Inherited evidence audit & grounding | `paper/planning/literature-audit.md` | P0.5 | `p0.5-grounded` | ✅ Closed (v1, migrated) |
| DCC | Standards codification & compliance matrix | `paper/planning/standards.md` | PCC | `pcc-standards-v1` | ✅ v1 closed; **v2.0 restructured 2026-08-23** |
| D01 | Literature survey & gap memo | `paper/planning/literature-audit.md` (+§8, §9), `survey_table.csv` | P01 | `p01-survey-done` | ✅ **Closed** (ADR-004 & PI Novelty Approval) |
| D02 | Falsifiable hypothesis & risk scoring | `paper/decisions/ADR-003_hypothesis_and_observable_signatures.md` | P02 | `p02-hypothesis` | ✅ Closed (v1, migrated) |
| D02.5 | Pre-registration of gate metrics & statistical plan | `paper/planning/preregistration.md` | P02.5 | `p02.5-preregistered` | ✅ Pre-registration locked |
| **D03** | **Mechanism-Gate Result (Separatrix validation)** | `paper/planning/gate-result.md` | **P03** | `p03-gate-passed` | ✅ **GATE PASSED** (ADR-006 & PI Directive) |
| D03.1 | Sub-gate resolution (only if INCONCLUSIVE) | `paper/planning/phases/P03.1_subgate.md` | P03.1 | `p03.1-resolved` | ✅ **Closed** (ADR-006 & PI Directive) |
| D04 | Experimental protocol specification | `paper/planning/phases/P04_experimental_design.md` | P04 | `p04-protocol` | ✅ **Closed** (ADR-007..009 & PI Directive) |
| D05 | Deterministic continuous ODE & PyTorch implementations + unit tests | `paper/src/` | P05 | `p05-implemented` | ✅ **Closed** (ADR-010, ADR-011 & 109 unit tests pass) |
| D06 | High-throughput multi-seed data tensors (Tiered Matrix) | `paper/data/` | P06 | `p06-data-complete` | ⏸ **BLOCKED_ON_REMEDIATION** (Production Gated) |
| D07 | Representation geometry & Hessian diagnostics | `paper/writing/figures/` | P07 | `p07-analysis-done` | ⬜ Pending (locked by P06) |
| D08 | Complete manuscript draft (NeurIPS/ICLR format) | `paper/writing/manuscript.tex` | P08 | `p08-draft-v1` | ⬜ Pending (locked by P07) |
| D09 | Red-team review report & compliance audit | `paper/planning/phases/P09_review.md` | P09 | `p09-reviewed` | ⬜ Pending |
| D09.5 | Co-author reconciliation (conditional) | `paper/planning/phases/P09.5_coauthor.md` | P09.5 | `p09.5-reconciled` | ⬜ Conditional template |
| D10 | Independent verification report | `paper/planning/verification-report.md` | P10 | `p10-verified` | ⬜ Pending |
| D11 | Pre-submission packaging & supplementary zip | `paper/writing/supplementary/` | P11 | `p11-packaged` | ⬜ Pending |
| D11.5 | Preprint / press package (conditional) | `paper/planning/phases/P11.5_preprint.md` | P11.5 | `p11.5-preprint` | ⬜ Conditional template |
| D12 | Submission receipt & Paper 03 seeding | `paper/planning/roadmap_v3_draft.md` | P12 | `p12-submitted` + `v1.0-submitted` | ⬜ Pending |
| D13 | Revision loop (conditional) | `paper/planning/phases/P13_revision.md` | P13 | `p13-revision-N` | ⬜ Conditional template |
| D14 | Post-publication monitoring (ongoing) | `paper/planning/phases/P14_postpub.md` | P14 | — | ⬜ Template |

---

## Budget Summary (RPF v2.0 §V)

| Resource | Total budget (P00–P13) | Actual to date (P00–P03.2) | Alert threshold |
|----------|:---:|:---:|:---:|
| GPU hrs | 40 | 0 (smoke tests, local) | 80 % / 100 % |
| TPU hrs | 14 | 0 | 80 % / 100 % |
| Agent tokens | 1.49M | ~0.5M (est.) | 80 % / 100 % |
| Wall-clock (days) | 45 | ~5 | 80 % / 100 % |
| Human hrs | 16 | ~3 | 80 % / 100 % |

Full per-phase tracking: `paper/planning/budget.md`.

---

## Non-Negotiables (RPF v2.0 Governance)

1. **Evidence Gates Ambition:** No downstream writing (P08), large-scale multi-benchmark sweep (P06), or scope expansion begins before the P03 Gate verdict (`planning/gate-result.md`) is committed with a verified **PASS** and a `[HUMAN-GATE]` PROCEED directive.
2. **Phases close on verifiable exit criteria, not effort:** Every phase has machine-checkable exit criteria (see `planning/phases/PXX_*.md`); gate phases additionally require a committed `gate-result.md`.
3. **Pre-registration binds the gate:** The P03 evaluation must be scored against `planning/preregistration.md` (P02.5); any deviation requires an ADR + PI approval.
4. **Reproducibility:** Every empirical result is generated by versioned scripts in `paper/src/` with explicit seeds (`seed = run_id * 42 + 7`) and pinned environment specs in `meta/ENVIRONMENT.md`; manifests follow the RPF v2.0 schema.
5. **Traceability:** Every claim in `paper/writing/manuscript.tex` maps to a `planning/ledger.md` row with provenance and status; ADRs link bidirectionally to ledger rows.
6. **Data Immutability:** Raw experiment outputs in `paper/data/raw/` are immutable after P06 data generation (SHA-256 hashed).
7. **Independent Verification:** P10 independently re-derives checks (clean-room rebuild), ensuring zero-discrepancy binding between **Ledger ↔ Code/Data ↔ Manuscript**.
8. **Scope is controlled:** Any new claim, experiment, or deliverable after P03 requires an ADR + ledger update + risk/budget impact assessment + HUMAN-GATE approval.
9. **Fail fast, log everything:** Negative results are committed with the `NEGATIVE` tag, never discarded.
10. **Next Cycle Seeding:** The project concludes at P12 by seeding the Paper 03 roadmap (*Autonomous Schema Induction & Continual Reasoning*).

---

## Framework Version History

| Date | Version | Change |
|------|---------|--------|
| 2026-08-22 | RPF v1.0.0 | Paper 02 initiated under v1 |
| 2026-08-23 | RPF v2.0.0 | Migration: P02.5/P03.1/P09.5/P11.5/P13/P14 phases, risk-register + budget + preregistration docs, ≥50 CC.N.M rules, ledger provenance/dependency-graph, per-phase RACI/abort-thresholds/tags, `[PX][Scope][Δ]` commit convention. Deltas recorded in `planning/standards.md`. |
