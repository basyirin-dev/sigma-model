# Paper 02 — Phase Roadmap (RPF v2.0)

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)
**Framework:** The Research Planning Framework (RPF) **v2.0.0** — reference: `paper/meta/RPF_v2.0.md`
**Status:** **P08 Unified Manuscript Assembly Complete** · **P11.5 SSRN & arXiv Preprint Ready** · **P13 Round 8 Peer Review Revisions Complete**
**Date:** 2026-09-01 (Manuscript Unified: Complete 40-page monograph + SSRN/arXiv preprint bundles packaged; Round 8 multi-specialist resolutions complete; formal journal submission deferred to a later date)
**Decision Context:** Merged Paper 01 (narrow $\sigma$-Trap manuscript) and Paper 02 (Two-Subspace Law & 960-run multi-benchmark empirical matrix) into a single authoritative manuscript (`writing/manuscript.pdf`, 40 pages). Due to journal policy restrictions on AI assistance, formal journal peer review is deferred; priority is established immediately via SSRN CompSciRN and arXiv preprint archives.
**Strategy:** Evidence-bound execution under RPF v2.0. Full mathematical proofs (Appendices A–F), complete 146-test regression suite passing, and all 5 publication figures with error bars and metadata sidecars.
**Target Venue:** Immediate Preprint Archives: SSRN CompSciRN (DOI-indexed) + arXiv (Computer Science: AI / LG / CL). Peer review targets deferred for future submission (e.g. TMLR, JMLR, Neural Computation).

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
| D06 | High-throughput multi-seed data tensors (Tiered Matrix) | `paper/data/` | P06 | `p06-data-complete` | ✅ **Closed** (960 production runs complete) |
| D07 | Representation geometry & Hessian diagnostics | `paper/writing/figures/` | P07 | `p07-analysis-done` | ✅ **Closed** (Figures 1–5 & sidecars verified) |
| D08 | Complete manuscript draft | `paper/writing/manuscript.tex` | P08 | `p08-draft-v1` | ✅ **Closed** (Unified manuscript compiled) |
| D09 | Red-team review report & compliance audit | `paper/planning/phases/P09_review.md` | P09 | `p09-reviewed` | ✅ **Closed** (Peer review feedback addressed) |
| D09.5 | Co-author reconciliation (conditional) | `paper/planning/phases/P09.5_coauthor.md` | P09.5 | `p09.5-reconciled` | ✅ **Closed** |
| D10 | Independent verification report | `paper/planning/verification-report.md` | P10 | `p10-verified` | ✅ **Closed** (Clean-room checks pass) |
| D11 | Pre-submission packaging & supplementary zip | `paper/writing/supplementary/` | P11 | `p11-packaged` | ✅ **Closed** (Zip bundle verified) |
| D11.5 | Preprint / press package (SSRN CompSciRN) | `paper/submission_ssrn/` | P11.5 | `p11.5-preprint` | ✅ **Closed** (SSRN package ready) |
| D12 | Submission receipt & Paper 03 seeding (AAIML) | `paper/submission_aaiml/` | P12 | `p12-submitted` + `v1.0-submitted` | ✅ **Closed** (AAIML package ready) |
| D13 | Revision loop (Round 7 Peer Review Resolution) | `paper/planning/phases/P13_revision.md` | P13 | `p13-revision-7` | ✅ **Closed** (All Round 7 Multi-Specialist Reviewer & Editorial feedback resolved: (1) Analytical Hessian curvature sign reconciliation ($a_C > 0$), projector consistency ($P_{\mathcal{U}} + P_{\mathcal{V}} + P_{\mathcal{W}_\perp} = I_D$), Figure 1 origin flow correction (removing false $(0,0)$ equilibrium label), and formal distinction between physical curvature coupling and generic bilinear imperfect bifurcation; (2) transparent 960-run production hierarchy accounting ledger (Table 6), benchmark-disaggregated baseline reporting in Table 4, seed-level binomial log-likelihood model selection in Table 8 ($\text{AIC}_{\text{seed}} = -214.6$), escape threshold sensitivity grid, and Kramers vs 20k-step anti-grokking reconciliation; (3) negative permutation control ablation in §4.6 and Table 3 ($32.4\% \pm 4.1\%$), benchmark-specific $\mathcal{L}_{\text{comp}}$ formalizations in Appendix D.2, contextualized literature baselines in Table 2, and complete LSTM Seq2Seq reporting in Table 4, §6.2, and Appendix D.3; (4) permanent removal of broken Zenodo DOI across all files, pinning GitHub repository and release archive `v2.0-paper02` (commit `540c992`), immutable preregistration commit provenance in Appendix E, and 4-level epistemic stratification alignment.) |
| D14 | Post-publication monitoring (ongoing) | `paper/planning/phases/P14_postpub.md` | P14 | — | 🔄 Ongoing |

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
