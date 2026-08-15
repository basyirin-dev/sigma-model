# DEEP AGENT SCORING — ISSUE #10

**Issue:** The empirical prediction requires matching agents on δ_A while varying σ_A but does not specify a protocol to independently increase schema coherence without increasing depth.

---

## SCORING MATRIX

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | Composite | Flag |
|---------|----|----|----|----|----|----|-----------|------|
| A | 10 | 10 | 9 | 10 | 5 | 6 | 8.3 | — |
| B | 8 | 9 | 7 | 9 | 3 | 7 | 7.2 | — |
| C | 10 | 10 | 8 | 10 | 8 | 7 | 8.8 | [HACKATHON PRIORITY] |
| D | 10 | 10 | 7 | 10 | 5 | 6 | 8.0 | — |
| E | 9 | 9 | 8 | 9 | 10 | 8 | 8.8 | [HACKATHON PRIORITY] |

**Suppression threshold:** Composite < 6.0 → No variants suppressed.

---

## DETAILED SCORING

### VARIANT A (Local prose fix in §9)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No ODEs touched. Purely additive prose protocol. Zero risk to equation closure. |
| C2 — Novelty Defence | 10 | No variable definitions modified. Uniqueness table untouched. |
| C3 — Falsifiability | 9 | Directly adds a testing protocol with exact stopping criteria, matching procedure, and statistical thresholds (Cohen's d > 0.5, p < 0.01). Makes Prediction 1 testable. Does not add observable proxy. |
| C4 — Scope Discipline | 10 | All three boundaries clean. No psychological language. No version bleed. Single-agent scope preserved. |
| C5 — Hackathon Relevance | 5 | Protocol is adaptable to hackathon but does not directly produce a Kaggle benchmark design. Tangentially related. |
| C6 — Version Integration | 6 | Version-neutral. Does not improve or degrade version coherence. |
| **Composite** | **8.3** | |

---

### VARIANT B (Structural equation fix in §3.1.3 + §5)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 8 | Adds three new equations (3c, 3d, 16b). The decomposed growth ODEs (3c, 3d) introduce a parallel pathway to Equation 28, which creates a potential inconsistency: the paper must clarify whether Eq. 28 is the full dynamics or the sum of 3c/3d plus AI bypass terms. The σ_A-only discovery term (16b) is consistent with the multiplicative Ψ_A architecture. Minor risk: the covariance independence condition is an assumption, not a derivation. |
| C2 — Novelty Defence | 9 | New equations use existing variable names. Growth-pathway independence strengthens σ_A distinctness from δ_A by formalizing their separability. No conflation introduced. |
| C3 — Falsifiability | 7 | Equations provide a formal basis for the protocol but do not themselves add a testable prediction. The independence condition (Cov = 0) is an assumption that would need empirical verification. Partially improves falsifiability. |
| C4 — Scope Discipline | 9 | Single-agent boundary clean. No psychological language. Version boundary: new equations are version-neutral but could complicate V1.0/V2.0 layering if σ_A now has both a full ODE (Eq. 28) and decomposed ODEs (3c/3d). Minor version boundary concern. |
| C5 — Hackathon Relevance | 3 | Equations provide theoretical grounding but do not directly produce a Kaggle protocol. Tangentially related to hackathon tracks. |
| C6 — Version Integration | 7 | Growth-pathway independence could improve cross-version understanding, but the parallel ODE structure (Eq. 28 vs. 3c/3d) creates a version seam. Moderate integration improvement. |
| **Composite** | **7.2** | |

---

### VARIANT C (Systemic reframe — new §10.3)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No ODEs touched. Protocol section is purely procedural. Zero risk to equation closure. |
| C2 — Novelty Defence | 10 | No variable definitions modified. Protocols reference existing variables without redefining them. |
| C3 — Falsifiability | 8 | Three explicit protocols (P1/P2/P3) provide systematic methodology for testing predictions. P1 directly specifies how to increase σ_A at fixed δ_A. Does not add observable proxy but makes the manipulation methodology explicit. |
| C4 — Scope Discipline | 10 | All three boundaries clean. No psychological language. No version bleed. Single-agent scope preserved. Protocols are entirely within the formal agent-training framework. |
| C5 — Hackathon Relevance | 8 | Directly specifies implementable protocols for SCAN/COGS benchmarks. Hackathon implementation paragraph explicitly connects P1/P2 to the five hackathon tracks. |
| C6 — Version Integration | 7 | Section placement in §10 (Limitations) is version-neutral. Does not actively integrate across version boundaries but does not create new seams. |
| **Composite** | **8.8** | **[HACKATHON PRIORITY]** (C5 = 8) |

---

### VARIANT D (Local prose fix in §8)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No ODEs touched. Experimental design is purely procedural. Zero risk to equation closure. |
| C2 — Novelty Defence | 10 | No variable definitions modified. Protocol references existing benchmark families. |
| C3 — Falsifiability | 7 | Four-step protocol provides implementation details but is less systematic than Variant C's three-protocol structure. Does not add observable proxy. Adequate but not comprehensive. |
| C4 — Scope Discipline | 10 | All three boundaries clean. No psychological language. No version bleed. Single-agent scope preserved. |
| C5 — Hackathon Relevance | 5 | References SCAN/COGS/PCFG-SET splits but does not connect to hackathon tracks or produce a Kaggle design. Tangentially related. |
| C6 — Version Integration | 6 | Version-neutral. Placed in §8 which spans all versions. Does not improve or degrade integration. |
| **Composite** | **8.0** | |

---

### VARIANT E (Structural equation fix in §9 + Hackathon tracks)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 9 | Does not modify ODEs directly. The Kaggle protocol references Tier 1 proxy (Eq. 3d) which must exist in the paper — currently Eq. 3d is from Issue #2 (resolved). Minor dependency on resolved equations. |
| C2 — Novelty Defence | 9 | Protocol uses existing variable names (σ̃_A, δ_A). Does not introduce conflation. The Spearman evaluation metric is standard and does not redefine variables. |
| C3 — Falsifiability | 8 | Kaggle protocol provides exact features, targets, and evaluation metric. Makes Prediction 1 testable via a concrete benchmark design. Does not add new observable proxy beyond what already exists. |
| C4 — Scope Discipline | 9 | Single-agent boundary clean. No psychological language. Version boundary: the protocol spans V1.0 (δ_A) and V2.0 (σ̃_A) variables, but this is intentional for the prediction. Minor version-seam exposure. |
| C5 — Hackathon Relevance | 10 | Directly produces a Kaggle benchmark design with dataset specification, features, targets, and evaluation metric. Updates hackathon/track_learning.md with implementable benchmark. Maximum hackathon relevance. |
| C6 — Version Integration | 8 | The Kaggle protocol explicitly bridges V1.0 (δ_A) and V2.0 (σ̃_A) variables, which improves cross-version understanding. Updates to hackathon tracks ensure version-coherent documentation. |
| **Composite** | **8.8** | **[HACKATHON PRIORITY]** (C5 = 10) |

---

## TOP 2 VARIANTS

### #1: VARIANT C — Composite 8.8 [HACKATHON PRIORITY]

The systemic reframe adding §10.3 (Training Protocols for Independent Variable Manipulation) scores highest on balance. It provides the most systematic and comprehensive treatment of the protocol gap while maintaining perfect ODE coherence and scope discipline. The three-protocol structure (P1/P2/P3) covers all manipulation combinations needed by §9 predictions, and the hackathon implementation paragraph directly connects protocols to track designs.

**Strengths:**
- Most comprehensive protocol treatment (P1/P2/P3 covers all cases)
- Cleanest separation of concerns (protocols in §10, predictions in §9)
- Direct hackathon linkage

**Weaknesses:**
- Does not directly produce a Kaggle benchmark design (needs Variant E's contribution)
- New section adds structural weight to the paper

---

### #2: VARIANT E — Composite 8.8 [HACKATHON PRIORITY]

The structural equation fix producing a Kaggle benchmark design scores equally on composite but differs in profile. It has the highest C5 score (10) of any variant, directly producing an implementable hackathon protocol with exact features, targets, and evaluation metrics. The update to hackathon/track_learning.md ensures the protocol is discoverable.

**Strengths:**
- Highest hackathon relevance (C5 = 10) — directly produces Kaggle design
- Best version integration (C6 = 8) — bridges V1.0/V2.0 explicitly
- Most actionable for hackathon participants

**Weaknesses:**
- Minor dependency on Eq. 3d from Issue #2 (resolved but creates coupling)
- Slightly lower scope discipline (version boundary exposure)

---

## SUPPRESSED VARIANTS

**None suppressed.** All variants score ≥ 6.0 composite.

### VARIANT B — Composite 7.2

Suppressed from top 2 because:
- Lowest C5 score (3) — no hackathon relevance
- Introduces parallel ODE structure that creates a version seam
- The independence condition (Cov = 0) is an assumption, not a derivation
- Most complex intervention with least direct payoff

---

## NEGATIVE LOG ENTRIES

| Entry | Reason |
|-------|--------|
| Issue #10, Variant B: | Introduces parallel ODE structure (3c/3d alongside Eq. 28) creating version seam; lowest hackathon relevance (C5=3); independence condition is assumed not derived. |
| Issue #10, Variant A: | Adequate but superseded by Variant C (more systematic) and Variant E (higher hackathon relevance). |
| Issue #10, Variant D: | Adequate but superseded by Variant C (more comprehensive protocol structure). |
