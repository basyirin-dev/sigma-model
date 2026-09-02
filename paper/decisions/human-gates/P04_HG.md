# HG-P04: [HUMAN-GATE] Decision Record

- **Status:** RESOLVED
- **Date:** 2026-08-25
- **affects-phases:** P04, P05
- **affects-ledger-rows:** CLM-005, CLM-006, CLM-007

---

## Context and Problem Statement
Phase 04 Multi-Benchmark Protocol Specification complete (0 GPU hrs). Experimental matrix specified in ADR-007 and matrix_p04.yaml encoding locked lambda_crit = 0.025 +- 0.005. Diagnostic toolchains (CKA, HE, Subspace Angles, HVP Power Iteration, Circuit Probing) implemented in ADR-008 and paper/src/analysis/. Axiomatic Chomsky grammar G_hbar, 3-way decoupled generator, pairwise strict zero-leakage auditor (audit_leakage.py), and formal Dataset Card (hbar_benchmark.md) committed. Statistical power sized (n=30, MDES d=0.58, TOST power >= 0.99) and multiple-comparison control pre-registered in ADR-009. 109/109 unit tests pass. Compliance linter passes 54/54. Pending PI decision.

## Considered Options
  1. **Approve Multi-Benchmark Experimental Design & Protocol Specification (P04) and authorize Phase 05 (Continuous Formulation & SDE Solver).** — trade-offs: Locks the multi-benchmark factorial matrix (4 suites x 3 architectures x 17 conditions x 30 seeds), pairwise zero-leakage protocol, diagnostic engines, and pre-registered statistical analysis plan, unlocking Phase 05 SDE solver implementation.
  2. **Require modifications to benchmark suites or architecture matrix configurations.** — trade-offs: Allows adjusting benchmark splits or model parameters prior to continuous solver and production setup.
  3. **Require adjustments to diagnostic toolchains or statistical pre-registration controls.** — trade-offs: Permits fine-tuning CKA, Hessian Lanczos, or TOST parameters before Phase 05.

## Decision Outcome
**Chosen Option:** Option 1 — Approve Multi-Benchmark Experimental Design & Protocol Specification (P04) and authorize Phase 05 (Continuous Formulation & SDE Solver).

### Positive Consequences
- Formally locks the multi-benchmark factorial matrix across all 4 benchmark suites and 3 architecture classes in ADR-007 and `matrix_p04.yaml`.
- Enforces locked empirical threshold $\hat{\lambda}_{\text{crit}} = 0.025 \pm 0.005$ with subcritical ($\le 0.020$), boundary ($[0.020, 0.030]$), and supercritical ($\ge 0.030$) regime classifications.
- Pre-registers statistical power ($n=30$, MDES $d=0.58$, $\text{Power}_{\text{TOST}} \ge 0.99$) and multiple-comparison correction (Holm-Bonferroni FWER for primary family, Benjamini-Hochberg FDR for exploratory diagnostics) in ADR-009.
- Establishes pairwise strict zero-leakage audit $\forall i \neq j: \text{supp}(\mathcal{D}_i) \cap \text{supp}(\mathcal{D}_j) = \emptyset$ in `audit_leakage.py` and publishes formal Dataset Card (`hbar_benchmark.md`).
- Closes Phase 04 and authorizes immediate progression to Phase 05.

### Negative Consequences / Risks
- Factorial matrix size ($6,120$ runs) requires disciplined batch orchestration during Phase 06 production execution.

## Human Gate Sign-off
- **Gate ID:** [HUMAN-GATE-P04]
- **Approver:** Principal Investigator (PI)
- **Timestamp:** 2026-08-25T15:30:00Z
- **Verdict:** APPROVED (PASS)

