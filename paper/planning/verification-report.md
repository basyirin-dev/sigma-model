# Verification Report — Phase 11 (Verification & Internal Review)

**Document**: `paper/planning/verification-report.md` (deliverable D10)
**Manuscript**: *The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation*
**Target venue**: TMLR (also arXiv preprint)
**Date**: Phase 11, 2026-08-16 (post P09–P10)
**Status**: Verification complete — all findings actioned; **one item pending: user stranger-test sign-off** (see §7)

This report records the Phase 11 verification pass: stranger-test / self-containment audit
(§1), claim audit against the locked ledger (§2), notation-consistency sweep (§3), rebuild
and page-budget record (§4), literature re-scan closing the P03 residual risk (§5), and the
independent review of the diff with dispositions (§6). Every finding logged here was either
fixed in `paper/manuscript.tex` / `paper/figures/figure3-phases.tex` in this phase or was
already satisfied at phase entry (marked accordingly).

---

## 1. Stranger-Test / Self-Containment Audit

The manuscript states (§1, end of Contributions): *"The present paper is self-contained and
does not rely on [the companion]."* The audit maps each section to its in-paper evidence and
flags every forward-reference to the companion.

### Paragraph → Evidence Map

| § / Paragraph | Claim / Content | Supporting Evidence (in-paper) | Self-contained? |
|---|---|---|---|
| Abstract | σ-trap reproducible; model descriptive; SGD connection unproven | Table 1; Props 2–4; Conj 1 | ✅ |
| §1 ¶1 | High-ID/low-OOD dissociation across benchmarks | Cites Lake & Baroni 2018; COGS; PCFG-SET | ✅ |
| §1 ¶2 | Two-quantity framing (δ_A, σ_A); σ-trap defined as non-formation | Defined §3.1.1–3.1.2; clarification added P11 | ✅ |
| §1 ¶3 | Phenomenological model; Conj 1 unproven | §3 preamble; Conj 1 block | ✅ |
| §1 RQ + Contributions 1–3 | Model, gate, negative leading-indicator | §3, §7, §7 | ✅ |
| §1 final ¶ | Companion complementary; paper self-contained | Stated; verified below | ✅ |
| §2.1–2.4 | Gap analysis: no prior model of σ_A as dynamical variable | Literature citations (19 refs) | ✅ |
| §3.1.1–3.1.2 | State variables; Stage-1 proxy measurement sketch | Eqs (1)–(2); GCA/RGA/AC sketch added P11 | ✅ |
| §3.2 | Mastery set; decay | Eq (3)–(5); θ_δ/θ_σ defined at first use (P11) | ✅ |
| §3.3.1–3.3.2 | Growth ODEs | Eqs (6)–(8); η_max, a, b defined at first use (P11) | ✅ |
| §3.4 | Lemmas 1–2, Props 2–4; clamped-dynamics qualifier | Proofs in Appendix C; Lemma 2 scoped to clamped dynamics (P11) | ✅ |
| §3.5 | Numerical integration (Euler + clip) | Solver description; Lemma 2 | ✅ |
| §4 | Phase 0–2 structure; bifurcation trigger; P3–P5 scoped to companion | Prop 4; Eq (11); Fig 4 annotation (P11) | ✅ |
| §4.1 | Empirical inflection signature (Prediction 9) | §7 segmented regression | ✅ |
| §5 | Prediction 9 operationalised (residual e_t) | Eq in §5; §7 results | ✅ |
| §6 | Benchmark, design, power | H-Bar description; Tables 1–2 | ✅ |
| §7 | Gate results; four arms; negative leading-indicator; GCA-at-init discussion | Tables 1–2; Figures 1–3; added discussion (P11) | ✅ |
| §8 | Claim status; circularity; open questions | Table 3; §8.2–8.3 | ✅ |
| §9 | Conclusion; three next steps | Supported by §7 + Table 3 | ✅ |
| Appendix A | Notation reference | Complete table | ✅ |
| Appendix B | IMEX-RK stability; Jacobian symbols defined; solver bridge | Preamble added P11 (ν_M…κ_{I,Ξ}; Euler-vs-ARS note) | ✅ |
| Appendix C | Proofs of Lemma 1–2, Props 2–4 | Full proofs | ✅ |

### Companion-Dependency Findings

| Item referenced in companion | In-paper treatment | Risk (post-P11) |
|---|---|---|
| Stage-1 proxy architecture (GCA, RGA, AC) | Measurement sketch in §3.1.2 (what each signal computes, normalisation, fusion) + full protocol pointer | ✅ Low — logic *and* measurement sketch now in-paper |
| Two-stage calibration protocol | Pointer to companion; sketch notes gate used the GCA+RGA sub-fusion | ✅ Low |
| Multi-domain machinery Ψ_A | Explicitly out of scope (§4, §5) | ✅ Acceptable |
| Phases beyond P2 | "treated in the companion" (§4) + Fig 4 greyed P3–P5 annotation | ✅ Acceptable |
| N = 500 replication protocol | "community replication resource" (§6) | ✅ Acceptable |
| Adoption guide / failure-mode catalogue | "outside the scope of this paper" (§8) | ✅ Acceptable |
| Extended predictions 1–8, H6.1–6.3, M1 | "stated and analysed in the companion" (§5) | ✅ Acceptable |

**Verdict**: The paper is self-contained — no argument requires the companion. The one
Medium item from the phase-entry audit (Stage-1 proxy measurement was a black box) was
closed by the §3.1.2 measurement sketch (V-1, §6).

---

## 2. Claim Audit vs. Locked Ledger

### Abstract / Intro claims

| # | Claim (abstract/intro) | Evidence in paper | Level locked? | Status |
|---|---|---|---|---|
| A1 | "σ-trap is a reproducible behavioural pattern" | Table 1 baseline: ID 90.2 %, OOD 45.9 %, gap 44.3 pp | Descriptive | ✅ |
| A2 | "a two-variable dynamical model describes" | Props 2–4; phase-2 inflection in §7 | Descriptive (model-conditional) | ✅ |
| A3 | "claim level is descriptive" | Stated abstract; Table 3 | — | ✅ |
| A4 | "whether SGD instantiates the posited dynamics remains an open conjecture" | Conj 1 block; §8.1 | Open | ✅ |
| C1 | Contribution 1: dynamical model + σ_critical + bifurcation | §3.4 | Proven in model | ✅ |
| C2 | Contribution 2: gate experiment; fixed-weight matches σ-modulated (p = 0.99) | Table 2 row 4; wording states scheduling not necessary | Empirical | ✅ |
| C3 | Contribution 3: negative leading-indicator; RGA tracks exposure | §7 partial-correlation; §7 RGA paragraph | Empirical | ✅ |

### Table 3 internal consistency check (post-fix)

| Row | Claim | Tagged status | Evidence column | Issue? |
|---|---|---|---|---|
| 1 | Stable low-σ equilibrium | proven in model | Props 2–3 | ✅ |
| 2 | Stability of trap | proven under assumptions | Prop 3 (γ_σ, clamped dynamics) | ✅ |
| 3 | σ_critical bifurcation | proven under assumptions | Prop 4 | ✅ |
| 4 | *Compositional-loss exposure closes the OOD gap; σ_A describes the trajectory* | empirically supported (descriptive) | gate: comp exposure closes the gap; σ̃_A itself does *not* lead | ✅ fixed (V-2a) |
| 5 | SGD necessarily produces σ-trap | not established | Conj 1; fixed-weight equivalence | ✅ |
| 6 | σ unique construct vs. grokking/SLT | open | sharpness/LLC not measured | ✅ |
| 7 | Generalises across architectures | open | single benchmark | ✅ |

> **V-2a (fixed this phase)**: The claim column previously read *"σ predicts compositional
> OOD behaviour"* while the evidence column said *"σ̃_A itself does not lead"* — a direct
> contradiction. Reworded to *"Compositional-loss exposure closes the OOD gap; σ_A describes
> the trajectory"*, retagged **empirically supported (descriptive)**, "predicts" removed.

### Cut-item re-introduction check

No ledger-`cut` item (Ψ_A dynamics, β_A, D*, multi-domain navigation, metacognitive
variables, extended predictions 1–8, H6.1–6.3, M1) appears as an active claim. All are
explicitly deferred with boundary sentences (§4, §5, §8). The Stage-2 diagnostic σ̂_A remains
restricted to post-hoc descriptive use with circularity statements at each use (§7 pointer,
§8.2 canonical). **No re-introduction detected.** ✅

---

## 3. Notation-Consistency Sweep

### Findings actioned this phase

| ID | Finding | Disposition |
|---|---|---|
| V-3a | Appendix B Jacobian entries ν_M, κ_P, κ_I, ξ_M, κ_{P,Ξ}, κ_{I,Ξ} were **undefined** | **Fixed**: preamble added at the top of Appendix B defining each symbol, with state order (M̂_A, Ξ_P, Ξ_I) and semantics matched to the companion (ν_M self-model tracking gain; ξ_M shortcut-pressure erosion on the self-model; κ_P, κ_I executive-control tracking rates; κ_{P,Ξ}, κ_{I,Ξ} off-diagonal couplings at E_C). |
| V-3b | θ_δ, θ_σ (Eq. 3) and η_max, a, b (Eq. 7) used before their Notation-table definition | **Fixed**: parenthetical definitions at first use in §3.2 and §3.3.1 with Appendix A pointers. |
| V-3c | ε used both for the regression residual (§5) and the timescale-separation parameter (App B) | **Fixed**: regression residual renamed ε_t → e_t. |

### Residual checks

- **Defined before first use**: after the fixes, every symbol is defined at or before its
  first use (δ_A, σ_A, Δ, δ^relative, M_A, λ_c, γ_σ, r_A, f_learn, η, T_A, ρ, P_A, α_A,
  ϵ_σ, Ω_SL, R_0, σ_critical, σ̃_A, σ̂_A, θ_δ, θ_σ, η_max, a, b, ν_M, κ_*, ξ_M).
- **Unused notation**: none — every Appendix A entry is used in the main text or appendices.
- **Symbol collisions**: σ (subscripts disambiguate; "± sd" only in table headers), d (domain
  index vs Cohen's d, contextually clear), ε (timescale parameter now the sole use). No
  remaining collisions. ✅

---

## 4. Rebuild & Page Budget

| Item | Record |
|---|---|
| Command | `make pdf` from `paper/` (latexmk, bibtex) |
| Errors | **0** |
| Undefined references | **0** |
| Warnings | 3 pre-existing hyperref Unicode warnings (unchanged from P10) |
| Page count | **19 pages**: main body pp. 1–14 (incl. Broader Impact p. 14), Appendices A–C pp. 15–17, References pp. 18–19 |
| Blueprint target | ≈ 14 pp (P05 estimate: main ≈ 12.75 + Appendix A ≈ 1.25) — **recorded deviation**: the blueprint predates the split of Appendices B/C and excludes references; current main+appendices = 17 pp, within TMLR norms (no strict limit; typical 15–25 pp). Non-blocking; trim if reviewers push back. |
| Floats | Figures 1–3 pp. 6–11; Figure 4 (bifurcation) pp. 10–11; Figure 5 (phases) p. 12; Tables 1–3 pp. 9–13 — all in the body before references (DEF-03 fix confirmed working) |
| Cross-references | All equation/proposition/table/figure `\ref`s resolve; no `??`; figures numbered consistently (bifurcation = Fig 4, phases = Fig 5 after the DEF-03 move) |

---

## 5. Literature Re-Scan (2025–26) — P03 Residual Risk

Direct arXiv API queries run 2026-08-16 (export.arxiv.org, sorted by submission date desc):

| Query | Results | Reading |
|---|---|---|
| `all:"schema coherence" AND all:"compositional"` | 0 | No schema-coherence dynamical model for composition |
| `all:"order parameter" AND all:"compositional generalization"` | 0 | No compositional order parameter |
| `all:"transcritical bifurcation" AND all:"compositional"` | 0 | No transcritical-bifurcation compositional model |
| `all:"grokking" AND all:"phase transition"` | 36 | 2026 entries: attention specific-heat precursors (Pandey 2026), metastable-phase escape / hysteresis in L2 transitions (2606.17120), Shannon/entropy bottlenecks (2606.30512), norm-separation delay laws — mechanistic, no σ state variable |
| `all:"compositional generalization" AND all:"dynamical"` | 80 | Top 2026 entries: embodied-manipulation systems, diffusion composition (FactorDiff), vector-network architectures, mechanistic three-phase training dynamics (Exoo et al. 2026) — none with a two-variable ODE + transcritical trap |

**Assessment**: No 2025–26 work introduces schema coherence σ_A as a dynamical state
variable with its own evolution equation, suppression mechanism, and critical threshold for
compositional generalisation. The §2 positioning claim is safe; the P03 residual risk is
closed. Closest-adjacent works worth citing in future revisions: Exoo et al. (mechanistic
three-phase training dynamics), Ootani (multi-seed grokking fragility — supports the paper's
per-seed methodology), Pandey (transition-precursor detection).

---

## 6. Independent Review — Findings & Dispositions

### 6.1 Built-in review skill (Phase 11 diff)

The built-in `review` skill was run on the full Phase 11 diff and continued after each
mutation until the final state:

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| RV-1 | §3.1.2 clause "referenced here in one sentence" became false after the measurement sketch was added | Should-fix | **Fixed**: clause reworded; sketch now described as a brief summary of the companion protocol |
| RV-2 | Three-signal sketch (GCA+RGA+AC) vs gate measurement text "GCA+RGA fusion" (3 places) — tension | Should-fix | **Fixed**: §3.1.2 now scopes the gate to the two-signal GCA+RGA sub-fusion; full three-signal protocol in the companion; cross-checked all proxy mentions (0 contradictions) |
| RV-3 | Duplicate "(companion)" label in figure3-phases.tex description row | Nit | **Fixed**: dropped the duplicate; single bar label "P3--P5 (companion)" retained |
| RV-4 | Duplicate companion pointer in adjacent sentences (§3.1.2) | Nit | **Fixed**: merged into a single clause |
| RV-5 | (Final review) Full diff ship-ready: LaTeX structure sound, labels/refs resolve, claims consistent, build corroborated | — | No action needed |

### 6.2 Pre-existing audit findings (from the phase-entry draft audit) — dispositions

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| V-1 | Stage-1 proxy measurement is a black box for the stranger reader | Medium | **Actioned** (§3.1.2 sketch) |
| V-2a | Table 3 row 4 claim/evidence contradiction | Medium | **Actioned** (reworded, §2 above) |
| V-3a/b/c | Notation findings | Med/Low | **Actioned** (§3 above) |
| R-1 | Lemma 2 statement omits the clamped-dynamics qualifier | Medium | **Actioned** (statement now scoped to clamped dynamics, matching its proof) |
| R-2 | Lemma 2 constant-Δ assumption not flagged at point of use | Medium | Already addressed at phase entry: caveat in the proof + Open Question 1 (§8.3). No change needed. |
| R-5 | GCA-at-init degeneracy — the single most likely reviewer objection | High | Mostly addressed at phase entry (§7 + Fig 3 caption report it honestly); **supplemented** with a "why GCA is trivially high at random init" discussion and why the partial-correlation test is decisive |
| R-6 | Contribution 2 wording could read as if the scheduling were validated | Medium | Already addressed at phase entry ("The σ-scheduling is not necessary for the model's descriptive value"). No change needed. |
| R-7 | RGA finding deserves prominence | Medium | Already addressed at phase entry (Contribution 3 leads with the negative result and features the RGA component). No change needed. |
| R-10 | Title "Suppression" vs non-formation mechanism | Low | **Partial action**: §1 ¶2 now states the mechanism is one of non-formation; **title kept** per P05 approval (decision logged here; reversible before submission) |
| R-11 | Fig 4 labels P3–P5 beyond paper scope | Low | **Actioned** (figure greyed + "(companion)" annotation; caption updated) |
| R-12 | App B IMEX analysis is for a solver not used by the gate | Low | **Actioned** (bridge sentence added) |
| DEF-01 | §7/§8.2 circularity duplication | Low | **Actioned**: §7 trimmed to a pointer; §8.2 kept canonical — roadmap non-negotiable #5 ("stated plainly wherever used") preserved |
| DEF-02 | Visible internal checklist tags (CC.3.6)/(CC.3.7) | Trivial | **Actioned** (removed) |
| DEF-03 | Figures 4–5 render after references start | Trivial | **Actioned** (environments moved into §3.4/§4 flow; placement verified p.10–12) |

---

## 7. Blocker Assessment & Exit Criteria

**No hard blockers.** Every finding was addressable with local text/figure edits; no
re-experimentation was required, and none was needed after the fixes (review verdict:
"ship as-is").

| Exit criterion | Status |
|---|---|
| Verification report written (this document) | ✅ |
| Paragraph → evidence map complete | ✅ (§1) |
| Claim audit against locked levels; no overreach | ✅ (§2; V-2a fixed) |
| No ledger-`cut` item re-introduced | ✅ (§2) |
| Notation sweep complete; all findings fixed | ✅ (§3) |
| `make pdf`: 0 errors, 0 undefined references | ✅ (§4; 19 pp) |
| Literature re-scan: no equivalent order-parameter claim | ✅ (§5; P03 residual closed) |
| Independent review run; findings actioned or logged | ✅ (§6) |
| **User stranger-test sign-off on readiness** | ⬜ **PENDING** |

**Recommendation**: proceed to P12 (arXiv bundle + TMLR submission package) once the user
completes the stranger-test sign-off; the only logged item left open is the R-10 title
decision (keep "Suppression" with the non-formation clarification — recommended — or
retitle before submission).

---

*End of Phase 11 verification report.*
