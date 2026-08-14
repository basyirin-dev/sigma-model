# External Assessment Response — Monograph Research Programme

**Date**: 2026-08-14
**Sources**: (A) AI review of the monograph manuscript (28-page development document);
(B) FastTrack comprehensive audit of the monograph + FastTrack materials (GIFT, Convergence,
claim–evidence ledger, minimum viable PhD, P0–P3 action plan).
**Status**: Decisions adopted and partially implemented; see Implementation Status at the end.

---

## Verdict Accepted

Both assessments converge: **conceptually brilliant but overextended**; the central claim is
currently stronger than the evidence visible in the document. Accepted corrective: sharpen the
thesis into a cumulative claim hierarchy, make **σ → compositional generalisation** the
experimentally demonstrated core, make **σ → safety-relevant optimisation** the major extension,
and bound the AGI implication. The thesis is not abandoned; it is restructured.

---

## Claim Strategy (adopted)

### Three-tier claim hierarchy (replaces the single "same phenomenon" statement)

1. **Primary thesis**: *Schema coherence is a measurable property of learned representation
   structure whose deterioration can produce a stable low-coherence regime (the σ-trap)
   associated with systematic generalisation failure.*
2. **Secondary thesis (extension)**: *The same mechanism provides a testable account of some
   safety-relevant forms of objective divergence.*
3. **Long-term implication (bounded)**: *If these relationships persist in more capable systems,
   schema-coherent training may constitute a candidate component of alignment strategy.*
   (No longer: "the optimal path to safe AGI.")

### Hypothesis trichotomy (from FastTrack §2)

| Hypothesis | Form | Status |
|------------|------|--------|
| Identity | CG failure ≡ alignment failure ≡ σ-trap | **Rejected as working claim**; documented as the strong form the thesis does not need |
| Mechanistic | σ-trap → CG failure; σ-trap → safety-relevant optimisation failure | Demonstrated core (Ch 5, 7, 8) |
| Unified framework | σ is a common structural variable across both domains | The defensible overarching claim (Ch 4) |

Every arrow in the CG → mesa-optimisation → alignment bridge carries an evidential-status tag:
**literature-supported / observed / modelled / experimentally manipulated / inferred / speculative**.

### Falsifiability criterion (adopted; FastTrack §21, rec. 1)

A falsifying result is one where σ is measured, interventions demonstrably raise σ, and the
predicted outcome (compositional generalisation or safety-relevant divergence) does **not**
change. Concretely: if a low-σ regime is observed with intact systematic generalisation, or if
raising σ does not change CG in a mediation analysis, the mechanism claim is falsified.
Counterexamples to the *secondary* thesis are explicitly allowed (some alignment failures lie
outside the framework — see Ch 9).

---

## Dispositions — Assessment A (monograph review)

| # | Concern | Disposition | Implementation |
|---|---------|-------------|----------------|
| A1 | "Same phenomenon" too strong | **Adopt** — mechanism-identity reformulation via claim hierarchy | narrative.md, Ch 1, abstract, READMEs |
| A2 | JAIR desk-rejection of Ch 7 | **Adopt** — non-toy validation required (Transformer/SSM), not only ODE/MLP | Ch 7 plan |
| A3 | σ measurement problem | **Adopt** — operational definition spec (construct/unit/metric/range/invariance) + 4 validity tests | Ch 4 plan, CC.3.4 |
| A4 | Meta-analysis pooling apples/oranges | **Adopt** — effect families A–E + subgroup/leave-one-construct-out/high-quality sensitivities | Ch 6 plan |
| A5 | Single-author/LLM bottleneck | **Adopt** — independent human adjudication + sensitivity analyses | CC.3 additions |
| B1 | Mesa-opt leap | **Adopt** — proxy-vs-mesa distinction + diagnostic criteria | Ch 8 plan |
| B2 | Falsifiability absent | **Adopt** — explicit falsification conditions | Ch 1 + Ch 4 plan |
| B3 | Toy-to-Transformer gap | **Adopt** — σ approximated in a Transformer architecture | Ch 7 plan |
| B4 | Lens vs ontology separation | **Adopt** — maintained (Ch 2 discipline), reinforced in wording | Ch 2 prose |
| B5 | Goal misgeneralization absent | **Adopt** — reconciliation task added to Ch 3/8 | Ch 3 plan, Ch 2 prose |

## Dispositions — Assessment B (FastTrack audit)

| # | Concern | Disposition | Implementation |
|---|---------|-------------|----------------|
| F1 | Hierarchy of claims (C1–C10) | **Adopt** — cumulative structure; primary/secondary/implication | narrative.md, ledger |
| F2 | Ch 3 is a black box | **Adopt** — study-level evidence table (study, construct, operationalisation, design, N, outcome, effect, variance, quality, σ-relevance) before Ch 6 relies on it | Ch 3 plan |
| F3 | Ch 4 must be conceptual centre | **Adopt** — operational definition + construct validity (convergent, discriminant, predictive, intervention) | Ch 4 plan |
| F4 | σcrit needs dynamical-systems treatment | **Adopt** — 7-point checklist (multiple equilibria, control parameter, hysteresis/basin, stability, initial-condition reproducibility, parameterisation robustness, σ-causes-vs-accompanies distinction) | Ch 7 plan |
| F5 | Ch 5 intervention causality | **Adopt** — test all three links (intervention → σ → CG), mediation design, in-distribution + robustness + dynamics measurements | Ch 5 plan |
| F6 | Ch 6 construct heterogeneity | **Adopt** — effect families A–E predefined | Ch 6 plan |
| F7 | Ch 8 mesa-opt diagnostics | **Adopt** — explicit criteria (internally represented objective, optimisation of it, persistence across distributional change, distinction from outer objective, optimisation-vs-correlation evidence) | Ch 8 plan |
| F8 | AGI conclusions outrun scale | **Adopt** — "candidate component"; Ch 9 reframed to "What does the evidence justify concluding about alignment?" | Ch 9 plan, Ch 1 guide |
| F9 | GIFT feasibility/timeline (6/10, 5/10) | **Adopt** — scope convergence: core = σ → CG; alignment/AGI downstream; MVT tracked | narrative.md scope note |
| F10 | Claim–evidence ledger | **Adopt** — `thesis/claim-evidence-ledger.md` as living document | ledger |
| F11 | Minimum viable PhD (§18) | **Adopt** — must-establish 1–7, bonus 8–10, programme 11–15 | narrative.md MVT |
| F12 | Master notation/conceptual figure | **Adopt** — notation registry exists (`back-matter/notation-registry.tex`); master conceptual figure with evidential status added to P2 backlog | P2 backlog |
| F13 | Chapter bookends ("establishes / does not establish") | **Adopt** — CC.4 additions | cross-cutting.md |
| F14 | Competing-hypotheses section | **Adopt** — CC.4 addition | cross-cutting.md |
| F15 | Ch 9 limitations-before-implications | **Adopt** — CC.3 addition | cross-cutting.md |

---

## P0–P3 Action Plan (FastTrack §23) → Repository Mapping

### P0 — Before expanding the thesis
- P0.1 Rewrite central thesis → **done** (this doc; narrative.md, Ch 1, abstract).
- P0.2 Fully operationalise σ → Ch 4 plan (construct/unit/metric/range/invariance).
- P0.3 Define σ-trap precisely → Ch 4 plan (definition + low-σ regime criteria).
- P0.4 Define falsification → **done** (above; Ch 1 + Ch 4 plan).
- P0.5 Separate identity from shared mechanism → **done** (trichotomy above).
- P0.6 Causal DAG intervention → σ → outcome → Ch 5 plan.
- P0.7 Define mesa-optimisation operationally → Ch 8 plan.
- P0.8 Bound the AGI conclusion → **done** (implication tier; Ch 9 plan).

### P1 — Evidence strengthening
- Ch 3 evidence tables → Ch 3 plan.
- Ch 6 effect audit → Ch 6 plan.
- Ch 4 validity tests → Ch 4 plan.
- Ch 7 alternative explanations → Ch 7 plan (σcrit checklist, causes-vs-accompanies).
- Ch 5 mechanism test → Ch 5 plan.
- Ch 8 proxy-vs-mesa distinction → Ch 8 plan.

### P2 — Thesis architecture (backlog, tracked in `phase-roadmap.md` follow-ups)
- Master claim–evidence matrix → `thesis/claim-evidence-ledger.md` (**done**).
- Master notation table → `back-matter/notation-registry.tex` (exists as stub; **extend** to cover all chapters' symbols — tracked follow-up).
- Master conceptual figure with evidential-status tags → **tracked follow-up** (target: `thesis/chapters/01-introduction/figures/master-conceptual-figure.tex`; every arrow tagged literature-supported / observed / modelled / experimentally manipulated / inferred / speculative).
- Chapter bookends → CC.4 (cross-cutting.md).
- Competing-hypotheses section → CC.4 (cross-cutting.md).

### P3 — Writing (only after P0–P2)
- PEER paragraph architecture; introduction/discussion/conclusion/abstract/title tightening.

---

## Minimum Viable PhD (FastTrack §18, adopted)

**Must establish**: (1) σ operationalised; (2) σ construct validity; (3) low-σ regime
identifiable; (4) regime predicts CG failure; (5) intervention alters σ; (6) changing σ changes
the predicted outcome; (7) robustness to alternative explanations.
**Bonus**: (8) meta-analytic support; (9) replication across architectures/tasks; (10) low-σ →
safety-relevant optimisation.
**Long-term programme (not PhD-defining)**: corrigibility, CEV, indirect normativity, safe AGI,
optimality of schema-coherent training.

---

## Implementation Status

- [x] This response doc (Σ-Align/13-external-assessment-response.md)
- [x] thesis/claim-evidence-ledger.md
- [x] thesis/narrative.md (three-tier claim, trichotomy, falsifiability, scope note)
- [x] thesis/cross-cutting.md (CC.3.4 operationalisation; CC.3/CC.4 additions)
- [x] thesis/phase-roadmap.md + root/thesis README.md
- [x] Chapter plans Ch 3–9 (evidence table, operational spec, causal chain, effect families, σcrit checklist, mesa-opt criteria, Ch 9 reframe)
- [x] Draft revisions: Ch 1 (claims + falsifiability), Ch 2 (goal-misgeneralization), abstract, Ch 9 stub
- [ ] P2 backlog: master conceptual figure, notation registry extension
- [ ] P3 writing pass (deferred by design)

Committed in: `[R][T][Δ] Respond to external assessments; restructure thesis claims into three-tier hierarchy …`
