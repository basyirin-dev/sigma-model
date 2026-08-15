# Paper 06 v2 — Claim Ledger

**Date**: 2026-08-16
**Source**: `paper/manuscript.tex` (JAIR-format working tree, pre-rewrite)
**Purpose**: Enumerate every formal result and framework component; tag each as keep-in-narrow / move-to-companion / cut / defer / decide-at-P05. Re-checked at Phase 11 against the rewritten manuscript (CC.3.7 / adapted CC.4.9).

**Tag legend**: `keep` = stays in the narrow σ-Trap paper · `companion` = moves to the arXiv companion technical report · `cut` = removed entirely · `defer` = future work, mentioned at most · `decide` = decision deferred to Phase 05 blueprint.

---

## A. Mathematical results

| Result | Claim marker | Location (§/eq) | Tag | Notes |
|:-------|:-------------|:----------------|:----|:------|
| Prop 3.1 — Local Existence and Uniqueness | C-022 | §3.7 | **keep** | Relabel **Lemma** (standard Picard–Lindelöf application); proof → appendix |
| Prop 3.2 — Forward Invariance and Boundedness | C-023 | §3.7 | **keep** | Relabel **Lemma**; proof → appendix |
| Prop 3.3 — Fast–Slow Decomposition (Fenichel) | C-024 | §3.7 | **decide** | Consultations split; two-variable core may not need timescale separation. Default: companion unless bifurcation analysis requires it |
| Prop 3.4 — Single-Domain Equilibria | C-025 | §3.7 | **keep** | Core to the bifurcation argument |
| Prop 3.5 — Numerical Stability | C-026 | §3.7 | **cut** | One-line footnote or drop; standard integrator suffices for two variables |
| Prop 3.6 — Estimator Consistency | C-027 | §3.1.4 | **companion** | Proxy-architecture result; measurement paper seed |
| Prop 3.7 — Error Propagation in ODE System | C-028 | §3.1.4 | **companion** | Same |
| Theorem 4.1 — SGD-induced σ-suppression | C-029 | §4.1 | **keep (relabel)** | Relabel **model-conditional Proposition**: "under the proposed dynamics, standard training conditions yield a stable low-σ equilibrium". No claim about real SGD |
| Prop 4.1 — σ_critical Derivation | C-030 | §7 | **keep** | Main theorem of the narrow paper (transcritical bifurcation at R₀ = 1) |
| Prop 4.2 — Depth Threshold Derivation | C-031 | §7 | **companion** | Phase 2→3 machinery removed |
| Prop 4.3 — Hysteresis and Reverse Transitions | C-032 | §7 | **decide** | Consultations: conjecture/remark if space allows; default companion |
| Prop 4.4 — Noise Sensitivity | C-033 | §7 | **companion** | Defer with SDE extension |
| Theorem 4.2 — Faculty–Validity Correspondence | C-034 | §7.4 | **companion** | Algebra dressed as theorem; flagged by multiple consultations |
| Lemma 4.2 — Faculty Omission Penalty | C-035 | §7.4 | **companion** | Faculty machinery removed |
| Prop 4.5 — Compensation Analysis | C-036 | §7.4 | **companion** | Same |
| Conjecture (new) — SGD↔ODE mapping | — | new | **keep (new)** | Add explicit conjecture stating the modelling assumption connecting real SGD trajectories to the posited ODEs |

## B. Predictions

| Result | Location | Tag | Notes |
|:-------|:---------|:----|:------|
| Prediction 1 — Schema Quality at Intersections | §9 | **companion** | Requires Ψ_A (removed) |
| Prediction 2 — AI Augmentation and Schema Suppression | §9 | **companion** | Requires β_A (removed) |
| Prediction 3 — Relative Mastery as Resilience | §9 | **companion** | Multi-domain machinery |
| Prediction 4 — Shortcut Threshold Expansion | §9 | **companion** | Requires D* (removed) |
| Prediction 5 — Phase-3 Compression | §9 | **companion** | Phase 3 removed |
| Prediction 6 — Multiplicative vs Additive σ_A (Ψ_A) | §9 | **decide** | Consultation #3 keeps it; majority cuts. Default: companion (Ψ_A removed) |
| Hypotheses 6.1–6.3 | §9 | **companion** | Sub-hypotheses of Prediction 6 |
| Prediction 7 — Benchmark Validity Cross-Model | §9 | **companion** | Requires V_A (removed) |
| Prediction 8 — Cross-Modal Schema Transfer | §9 | **companion** | Requires Θ_A (removed) |
| Prediction 9 — Phase-2 Entry Inflection | §9 | **keep** | **Flagship** — the single empirical prediction of the narrow paper |
| Meta-Prediction M1 — Incidental σ_A Elevation | §9 | **companion** | Overarching intervention claim; future programme |

## C. Framework components

| Component | Location | Tag | Notes |
|:----------|:---------|:----|:------|
| Depth δ_A (dimension + ODE) | §3.1, §3.6 | **keep** | One of the two core variables |
| Breadth β_A (dimension + ODE) | §3.1, §3.6 | **companion** | Not needed for the two-variable bifurcation |
| Schema coherence σ_A (dimension + ODE) | §3.1, §3.6 | **keep** | The other core variable |
| Online estimation protocol (two-tier proxy: GCA/RGA/AC fusion + Stage-2 calibration) | §3.1.4 | **companion** | One-sentence reference in the narrow paper + circularity statement; full architecture + Props 3.6–3.7 in companion |
| Mastery set / breadth set | §3.2 | **keep** (mastery) / **companion** (breadth) | Mastery set needed for δ_A; breadth set with β_A |
| Decay architecture (schema-mediated decay, combined depth decay) | §3.3 | **keep** (minimal) | Only what the two-variable ODEs need |
| Growth dynamics (depth growth ODE, σ ODE) | §3.4 | **keep** | Core equations |
| Intersection activation Ψ_A | §3.5 | **companion** | Multi-domain machinery |
| Shortcut threshold D* | §3.6 | **companion** | One-paragraph mention at most |
| Mathematical foundations: state space & vector field | §3.7 | **keep** | Needed for existence/invariance/equilibria |
| Mathematical foundations: timescale separation | §3.7 | **decide** | See Prop 3.3 |
| Mathematical foundations: equilibrium analysis | §3.7 | **keep** | Core |
| Mathematical foundations: numerical integration protocol | §3.7 | **keep** (compressed) | Reproducibility |
| Implementation: required network features | §3.8 | **companion** | |
| Implementation: GCA/RGA/AC signal extraction | §3.8 | **companion** | With §3.1.4 |
| Implementation: ODE-state-modulated training | §3.8 | **keep** (compressed) | Needed to make the intervention reproducible |
| Implementation: complete training algorithm | §3.8 | **companion** | Algorithm box to companion; essence in §11 methods |
| Implementation: computational overhead | §3.8 | **companion** | |
| Extension 1 — Attentional fidelity α_A | §4 | **companion** | May appear as a fixed parameter only |
| Extension 2 — Collective schema field (social) | §4 | **companion** | |
| Extension 3 — Executive control Ξ_A | §4 | **companion** | |
| Extension 4 — Self-model (metacognition) | §4 | **companion** | |
| Extension 5 — Domain × modality product space | §5 | **companion** | |
| Extension 6 — Cross-modal transfer Θ_A | §5 | **companion** | |
| Extension 7 — Benchmark validity V_A | §5 | **companion** | |
| Extension 8 — Benchmark reliability R_A | §6 | **companion** | |
| Phase structure Phases 0–2 + bifurcation | §7 | **keep** | Phase 1→2 transition is the paper's empirical core |
| Phase structure Phases 3–5 | §7 | **companion** | Need Ψ_A / multi-domain machinery |
| Faculty–validity correspondence | §7.4 | **companion** | |
| Five-step benchmark protocol | §8 | **companion** | Prescriptive future work |
| Empirical grounding | §10 | **keep (rebuilt)** | Proof-of-concept framing |
| Empirical validation (pilot n=15) | §11 | **keep (rebuilt)** | 3-arm results from Phase 04 gate |
| Scope/Open Questions + assumption-boundary ledger | §12 | **keep (rebuilt)** | Claim-status table replaces/augments ledger; adoption guide cut |
| Conclusion | §13 | **keep (rewritten)** | No "origin" language |
| Appendix: Notation Reference | App A | **keep (pruned)** | Only symbols used in the narrow paper |
| Appendix: SDE Extension | App B | **decide** | Default companion (consultation split) |
| Appendix: IMEX-RK Stability | App C | **decide** | Keep if it supports numerical rigor (consultation #4); default keep-compressed |

## D. Empirical numbers carried forward (subject to Phase 04 re-verification)

| Quantity | Reported value | Tag |
|:---------|:---------------|:----|
| Baseline OOD accuracy | 44.5 ± 4.7% | verify at Phase 04 |
| σ-coupled OOD accuracy | ~94–97% | verify at Phase 04 |
| Effect sizes | d = 9.08 / 7.57, p < 0.0001 | verify + report per-seed/CI at Phase 04 |
| Phase-2 entry inflection | segmented-regression breakpoint τ | verify at Phase 04 |

## E. Claims to delete outright (framing, per consultations)

- "compositional generalisation failure is a bifurcation phenomenon, not a capacity or data problem" (unqualified)
- "convert every depth-accumulating agent into a principled generaliser"
- "The transition from measuring depth to cultivating coherence is the next frontier in training AI agents that not only know more, but understand better"
- "necessary and sufficient" Phase-2 phrasing → model-scoped "necessary within the model"
- "as the Origin of…" title claim → mechanism-level title
- Any SGD-level universality claim not scoped as model-conditional (Theorem 4.1 relabel)
