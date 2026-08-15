# Gap Analysis: Structured Motivation for the Systematic Review

**Document type:** Reference — directly informs Introduction and Discussion
**Purpose:** Synthesizes all prior research into a structured gap analysis demonstrating why the systematic review is necessary and what it uniquely contributes
**Status:** Draft

---

## Summary of Confidence Levels

| Claim | Confidence | Basis |
|---|---|---|
| The σ-trap exists empirically | **High** | 11 studies with extractable ID-OOD numerics; gap range 22–98 points; multiple independent benchmarks |
| Low σ correlates with catastrophic OOD failure | **High** | Consistent pattern across architectures (RNN, LSTM, Transformer) and benchmark families |
| Scale alone does not resolve the σ-trap | **High** | T5-3B still at ~0% on structural COGS; compositionality gap does not decrease with scale |
| Simplicity bias is the strongest theoretical match | **Medium-High** | Converging support from 3+ frameworks; no stronger alternative |
| Representation interventions can partly resolve the σ-trap | **Medium** | HE, LeAR, positional encodings show gains; but small N, narrow benchmarks |
| The σ-trap is a distinct phenomenon from shortcut learning | **Medium** | Taxonomic disambiguation supported but contested; more evidence needed |
| Compositional gen failure is causally linked to alignment failure | **Low-Speculative** | No direct evidence; inferential from mesa-optimization theory and D.1 mappings |
| Existing reviews have not quantified ID-OOD gaps | **High** | C.1 evidence: all 14 reviews are narrative; no pooled effect sizes |

---

## 1. What Is Known

### Claim 1: The σ-trap exists empirically — Confidence: HIGH

**Evidence:** 11 studies with extractable ID-OOD numerics (from `empirical-evidence.md`). Gap range: 22 points (PCFG-SET) to ~98 points (SCAN primitive). Median gap: 60–85 points. Multiple independent benchmark families (SCAN, COGS, CFQ, SLOG, gSCAN, CLOSURE, PCFG-SET) and architectures (RNN, LSTM, GRU, Transformer, CNN-LSTM) reproduce the pattern. The σ-trap is not an artifact of a single benchmark or model family.

**Cross-reference:** See `empirical-evidence.md` §1, `landmark-papers.md` Part I.

### Claim 2: Low σ correlates with catastrophic OOD failure — Confidence: HIGH

**Evidence:** In every study reporting both ID and OOD performance, near-perfect ID accuracy coexists with catastrophic OOD failure (median 60–85 point gap). This pattern holds across the 11 extractable studies and is consistent with the σ-trap prediction that low-schema-coherence models fail under distribution shift.

**Cross-reference:** See `empirical-evidence.md` §1, `sigma-trap-boundary.md` §1.

### Claim 3: Scale alone does not resolve the σ-trap — Confidence: HIGH

**Evidence:** T5-3B shows lexical improvement but the structural gap persists at ~0% on COGS (Qiu et al., 2022). The compositionality gap does not decrease with scale (Press et al., 2023). Depth scaling saturates at ~6 layers (Petty et al., 2024). These negative results demonstrate that simply increasing model capacity does not produce schema-coherent representations.

**Cross-reference:** See `interventions.md` §12 (negative results), `empirical-evidence.md` §1.

### Claim 4: Simplicity bias is the strongest theoretical match — Confidence: MEDIUM-HIGH

**Evidence:** The theoretical-frameworks review (`theoretical-frameworks.md`) evaluates 7 frameworks and finds simplicity bias (Teney et al., 2021; Yang et al., 2023) provides the best conceptual match: SGD prefers simpler predictive features; when spurious correlations are simpler than true mechanisms, models latch onto shortcuts. The σ-trap is the stable equilibrium where this occurs. NTK and capacity-bounds frameworks do not predict OOD failure. Spectral bias, functional LTH, and information bottleneck provide partial support.

**Cross-reference:** See `theoretical-frameworks.md` §1.

### Claim 5: Representation interventions can partly resolve the σ-trap — Confidence: MEDIUM

**Evidence:** Homomorphism Error regularization, LeAR, and relative positional encodings show significant gains on COGS and SCAN (effect sizes: +62.7pts for LeAR on COGS structural, +35–46pts for relative positional encodings). But studies are small, narrow in benchmark coverage, and not meta-analyzed.

**Cross-reference:** See `interventions.md` §1–§8.

---

## 2. What Is Unknown

| Unknown | Why it matters | Current state |
|---|---|---|
| **Prevalence**: What fraction of training runs produce σ-traps? | Determines whether the σ-trap is a rare pathology or a systemic failure mode | No prevalence study exists |
| **Causality**: Is σ a cause or a correlate of generalization failure? | Determines whether interventions targeting σ address the root cause or a symptom | Correlational evidence only; no causal manipulation study |
| **LLM-scale generalizability**: Do σ-traps occur in models >1B params? | Determines relevance to deployed production systems (GPT-4, Claude, etc.) | Press et al. 2023 shows compositionality gap persists at scale; no direct σ measurement in LLMs |
| **Real-world deployment impact**: Do σ-traps manifest in deployed systems beyond synthetic benchmarks? | Determines practical significance vs. academic curiosity | No study examines real-world deployment; all evidence from controlled benchmarks |
| **Temporal dynamics**: How quickly does σ collapse during training? | Informs early-warning detection and intervention timing | Phase analysis in Σ-Model paper; no independent replication |

---

## 3. What Is Contested

| Contested question | Positions | Current evidence |
|---|---|---|
| **Which theory best explains the σ-trap?** | NTK theory (infinite-width limit) vs. simplicity bias (SGD preference) vs. spectral bias (frequency principle) | NTK does not predict OOD failure; simplicity bias is strongest match but no decisive test distinguishes it from spectral bias |
| **Is the σ-trap distinct from shortcut learning?** | **Distinct** (optimization-dynamical construct that occurs even on balanced datasets) vs. **Not distinct** (shortcut learning is the same phenomenon under a different name) | `sigma-trap-boundary.md` taxonomic disambiguation distinguishes them on 5 dimensions; but the empirical tests distinguishing them have not been conducted |
| **Do SAM/SWAD work via σ or other mechanisms?** | SAM targets sharpness → σ (the σ-trap mechanism) vs. SAM works via implicit regularization or flat minima → robustness | No study has measured σ before/after SAM to test the mechanism |
| **Is the ID-OOD gap the same construct across benchmarks?** | Yes (generalization failure is a unified phenomenon) vs. No (compositional, covariate, and adversarial shifts are mechanistically different) | No systematic comparison across shift types; existing benchmarks confound shift type with difficulty |

---

## 4. Evidence Gap: Meta-Analysis Feasibility

**From `meta-analysis-feasibility.md`:**

- Only **11 studies** with extractable ID-OOD numerics
- Missing benchmarks: COFE, MathQA, QED, NACS, SQuAD compositional, GeoQuery baselines — these require Phase 2 search
- **Feasibility verdict:** LOR meta-analysis possible with ≥10 studies; pooled ΔAcc not possible
- High heterogeneity expected (I² > 75%); subgroup analysis mandatory
- Three-level RVE with benchmark-as-random-effect is the primary pooling strategy
- If <10 studies after full-text screening → abandon meta-analysis; deliver structured narrative synthesis

**Gap:** The current evidence base is on the boundary of meta-analytic feasibility. The systematic review must expand the search to reach the ≥10-study threshold.

---

## 5. Methodological Gap

**From `review-methodology.md`:**

| Gap | Evidence | Impact |
|---|---|---|
| **Missing variance reporting** | >80% of studies do not report per-seed SD or CIs | Conventional meta-analysis impossible; must re-derive from confusion matrices or impute |
| **No external validation** | <1% of ML studies report external validation | Optimism bias undetectable; c-statistic drops of 0.85→0.72 are typical |
| **No reporting standards** | No study follows TRIPOD+AI, REFORMS, or PROBAST+AI | ROB assessment requires manual adaptation of checklist items |
| **Benchmark heterogeneity** | Each study uses different benchmarks, OOD splits, and evaluation protocols | Direct ΔAcc pooling meaningless; must use relative measures (LOR) |
| **Selective benchmark reporting** | Pervasive; no off-the-shelf test detects it | Benchmark-selectivity audit required as part of publication bias assessment |
| **Code sharing** | <20% of studies share code; <2% share training data | Reproducibility checks impossible for most studies |

**Gap:** Existing studies do not use appropriate measures, controls, or reporting standards. The systematic review must adapt tools from `review-methodology.md` (PROBAST+AI + REFORMS) and implement the effect-size recovery plan (4-tier approach).

---

## 6. Conceptual Gap: The Safety Bridge

**From `safety-connection.md`:**

The most consequential gap for the broader thesis is the **absence of any paper explicitly connecting compositional generalization failure to alignment failure**. The σ-trap framing predicts that:

1. Compositional generalization failure is a *symptom* of the same low-coherence attractor that produces goal misgeneralization
2. Models with low σ are more likely to exhibit specification gaming, reward hacking, and deceptive behavior under distribution shift
3. Representation-level interventions that raise σ would simultaneously improve generalization AND safety

**Evidence level:** This is currently **speculative / unaddressed** in the literature. No direct evidence supports or refutes this prediction. The systematic review would provide the first quantitative evidence base for this bridge.

---

## 7. Why Filling These Gaps Matters for the Thesis

### The unification thesis

> **Compositional generalization failure and AI alignment failure are the same phenomenon — a bifurcation in the agent's internal schema coherence — and solving one solves the other.**

This thesis (from `narrative.md` and `Σ-Align/09-sigma-model-connection.md`) depends on the systematic review because:

1. **Paper 03 (Conceptual Framework)** requires a quantitative evidence base for the σ-trap construct — the systematic review provides this
2. **Paper 07 (Mesa-Optimization via Schema Coherence)** formalizes the σ-trap→alignment mapping; the systematic review establishes that the σ-trap is empirically grounded, not just theoretically motivated
3. **Paper 09 (Final Scoping Review on CEV)** depends on the claim that schema-coherent training is the optimal path to safe AGI; the systematic review provides the intervention-effectiveness data

### The safety bridge

If the systematic review demonstrates that:
- The σ-trap is a **prevalent** failure mode (not just a pathology on synthetic benchmarks)
- Representation-level interventions **effectively** resolve the σ-trap
- The σ-trap is **distinct** from shortcut learning (not relabeling)

Then the bridge to safety becomes empirically grounded rather than speculative. The systematic review is the evidence base that transforms a theoretical claim (σ-trap = alignment failure precursor) into a testable hypothesis with quantitative support.

### Timeline coherence

```
Paper 02 (Systematic Review) ──→ Paper 03 (Conceptual) ──→ Paper 07 (Mesa-Opt)
    M1–9                              M13–16                    M19–25

The systematic review is the FIRST empirical foundation in the thesis arc.
All subsequent papers depend on its findings.
```

---

## 8. Summary: The Six Gaps

| # | Gap type | Description | Severity | Systematic review contribution |
|---|---|---|---|---|
| 1 | **Evidence** | Only 11 studies with extractable ID-OOD numerics; meta-analysis on boundary of feasibility | High | Expanded search (Phase 2) + protocol-driven inclusion |
| 2 | **Methodological** | >80% missing variance; no external validation; no reporting standards | High | PROBAST+AI + REFORMS assessment; 4-tier effect-size recovery |
| 3 | **Conceptual (theory)** | Contested: which theory explains the σ-trap? Is it distinct from shortcut learning? | Medium | Systematic comparison of theoretical predictions across studies |
| 4 | **Conceptual (safety)** | No paper connects compositional gen failure → alignment failure | High | Establishes quantitative evidence base for the bridge |
| 5 | **Methodological (meta-analysis)** | No pooled ID-OOD gaps or intervention effect sizes exist | High | LOR meta-analysis with RVE; subgroup and sensitivity analyses |
| 6 | **Prevalence** | No prevalence study; unknown if σ-trap is systemic or rare | Medium | Narrative synthesis of prevalence-adjacent evidence; identifies prevalence as critical future direction |

---

## References

See individual research documents for full reference lists. Key sources:
- `empirical-evidence.md` (11 studies with ID-OOD numerics)
- `existing-reviews.md` (14 reviews, no meta-analysis)
- `review-methodology.md` (methodological guidance)
- `meta-analysis-feasibility.md` (SAP and feasibility verdict)
- `safety-connection.md` (safety bridge and mapping table)
- `interventions.md` (24 interventions, 6 negative results)
- `theoretical-frameworks.md` (7 frameworks)
- `sigma-trap-boundary.md` (formal definition and taxonomy)
