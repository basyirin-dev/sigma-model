# ADR-014: Scientific Manuscript Framing, Theoretical Positioning & Evidence Synthesis

**Date:** 2026-08-27  
**Status:** ACCEPTED (Phase 08 Manuscript Draft Complete)  
**Phase:** P08 (Manuscript Writing & Section Assembly)  
**Deciders:** Principal Investigator & Lead Research Agent  
**Prerequisites:** ADR-001, ADR-004, ADR-006, ADR-010, ADR-011, ADR-013, `paper02/planning/ledger.md`

---

## 1. Context & Problem Statement

Following the successful generation of 960 multi-seed production runs (Phase 06) and statistical verification of the pre-registered phase-boundary criteria (Phase 07), Phase 08 requires assembling the complete, authoritative scientific manuscript (`paper02/writing/manuscript.tex`) and bibliography (`paper02/writing/bibliography.bib`). 

The manuscript must synthesize the Two-Subspace Continuous Gradient Flow Law, rigorous stability proofs of the transcritical bifurcation, empirical change-point validation, representation geometry order parameters (CKA / whitened GCA), and Hessian spectral dynamics into a unified, high-impact narrative adhering strictly to RPF v2.0 claim discipline standards (CC.3.3).

---

## 2. Decision Drivers

- **Driver 1 (Paradigmatic Framing):** Establish compositional generalization as a macroscopic phase-boundary control problem governed by continuous vector fields, contrasting against stochastic grokking and unguided curriculum hypotheses.
- **Driver 2 (Phenomenological Guardrail CC.3):** Maintain strict category separation between mathematical theorems (derived from continuous gradient flow), empirical observations (measured on benchmark sweeps), and conceptual interpretations.
- **Driver 3 (Bidirectional Ledger Synchronization):** Ensure all in-scope claims (CLM-001 through CLM-007) in `paper02/planning/ledger.md` are completely grounded in the text, tables, and figures, while deferred claims (CLM-008 through CLM-012) are formally scoped to future research.
- **Driver 4 (Venue & Layout Standards):** Target premier publication standards (TMLR / NeurIPS layout) with strict abstract word bounds ($\le 250$ words, CC.3.1), 0 undefined citations, and vector figures with complete metadata sidecars.

---

## 3. Considered Options

- **Option 1 (Unified Phase-Boundary Narrative):** Present the Two-Subspace Law as the foundational analytical engine in Section 3, followed by empirical change-point validation in Section 4, microscopic representation geometry in Section 5, multi-benchmark / multi-architecture generality in Section 6, and loss surface curvature in Section 7. Full proofs and data cards are housed in Appendices A–E.
- **Option 2 (Purely Empirical Report):** Focus primarily on benchmark score comparisons across pressure levels $\lambda$, treating continuous ODE derivations as an optional supplementary modeling exercise.

---

## 4. Decision Outcome & Structural Architecture

**Chosen Option:** Option 1 — Unified Phase-Boundary Narrative with complete analytical foundations and empirical change-point falsification.

### 4.1 Narrative & Structural Outline

1. **Title & Abstract:**
   - Title: *Critical Compositional Pressure: A Phase-Boundary Law for Neural Representation Formation*
   - Abstract: Exactly 220 words ($\le 250$ words limit), declaring both analytical model theorems and empirical bifurcation verifications.
2. **Section 1 (Introduction):**
   - Framing: ERM shortcut entrapment ($E_S$) as an asymptotic stability phenomenon.
   - Tripartite contributions: (1) Analytical Two-Subspace Law ($\lambda_{\text{crit}} = b_C / a_C \iff R_0 = 1$), (2) Empirical Separatrix ($k = 70.6 \ge 15.0, 100\%$ recovery), and (3) Representation Geometry Order Parameters ($\Delta t \approx 150$ steps).
3. **Section 2 (Related Work):**
   - Systematic contrast against Grokking (deterministic stability exchange vs stochastic drift), Singular Learning Theory (vector fields vs singular strata), and Edge of Stability (cross-subspace coordination vs scalar sharpness saturation).
4. **Section 3 (Theoretical Foundations):**
   - Formalization of the Two-Subspace Continuous Gradient Flow system and Theorem 1 (Transcritical Bifurcation of Representation Space).
5. **Section 4 (Empirical Phase Boundary):**
   - 720 Tier 1 runs ($n=30$ seeds per cell), logistic change-point fit ($k=70.6, R^2=0.942$), TOST statistical equivalence ($\Delta \mu = 0.42\%$), and late-onset intervention recovery ($100\%$ at $t_{\text{int}}=1000$).
6. **Section 5 (Representation Geometry):**
   - Resolution of the step-0 whitened GCA artifact ($g_A^{\text{proj}}(0) = 0.001 \pm 0.007$) and Granger causality proof of geometric precedence ($F=3.716, p < 0.01$).
7. **Section 6 (Cross-Benchmark & Architecture Universality):**
   - Generality across $\hbar$, SCAN, COGS, and PCFG-SET at $\hat{\lambda}_{\text{crit}} \in [0.015, 0.025]$, plus capacity scaling (Transformer 4L) and non-attention recurrence (GRU Seq2Seq).
8. **Section 7 (Hessian Dynamics & EOS Ceiling):**
   - Lanczos spectrum analysis confirming strict bounding below the Edge of Stability ceiling ($\lambda_{\text{max}} \le 1680.4 \ll 2/\eta = 2000.0$).
9. **Section 8 (Discussion & Limitations):**
   - Scope boundaries (continuous flow vs SGD noise), deferred horizons (CLM-008 autonomous discovery, CLM-009 continual manifolds), and ethical impact statement.
10. **Appendices A–E:**
    - Full notation taxonomy, uncompressed mathematical proof of Theorem 1 (Jacobian spectra and Lyapunov functions), RK45 solver implementation, benchmark grammar definitions with cryptographic support disjointness proofs, and raw per-seed statistical grids.

---

## 5. Bidirectional Claim Reconciliation Matrix

| Claim ID | Category | Description | Manuscript Section | Empirical / Proof Grounding |
|---|---|---|---|---|
| **CLM-001** | Theory | Transcritical stability exchange at $\lambda_{\text{crit}} = b_C / a_C$ | Section 3, Theorem 1, Appendix B | Analytical Jacobian spectrum & Lyapunov proof |
| **CLM-002** | Theory | Isomorphism with basic reproductive ratio $R_0 = 1$ | Section 1, Section 3 | Topological equivalence mapping |
| **CLM-003** | Empirical | Sharp empirical separatrix ($k \ge 15.0$) | Section 4, Table 1, Figure 2a | Non-linear logistic fit ($k = 70.6, R^2 = 0.942$) |
| **CLM-004** | Empirical | Late-onset recovery ($t_{\text{int}}=1000$) | Section 4, Figure 2b | $100\%$ ($30/30$) recovery under $\lambda = 0.05$ |
| **CLM-005** | Diagnostic | Geometric Granger lead-lag ($\Delta t \approx 150$ steps) | Section 5, Table 2, Figure 3b | CKA Granger causality ($F = 3.716, p < 0.01$) |
| **CLM-006** | Diagnostic | Whitened GCA initialization calibration | Section 5, Table 2, Figure 3c | Projection operator $P_{\perp}^{\text{emb}}$ yields $g_A(0) \approx 0.00$ |
| **CLM-007** | Scope | Cross-benchmark and architecture invariance | Section 6, Table 3, Figure 4 | Universal transition across 4 suites & 3 architectures |

---

## 6. Verification & Quality Gates

- **Compilation Status:** `make -C paper02 pdf` exits with code 0; generates 18-page publication PDF (`paper02/writing/manuscript.pdf`).
- **LaTeX Cleanliness:** 0 undefined citations, 0 undefined references, 0 overfull boxes.
- **Word Count:** Abstract contains 220 words (passing CC.3.1 limit of 250 words).
- **Code & Figure Provenance:** All 5 publication figures in `paper02/writing/figures/` are generated from verified data tables with complete JSON metadata sidecars.
