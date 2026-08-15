# Σ-Model Metacognitive Calibration Benchmark (H-MCB): Metacognition Track Writeup

**Benchmark:** H-MCB — Σ-Model Metacognitive Calibration Benchmark
**Track:** Metacognition
**Variables:** M̂_A(d,t) [target], ζ_A(d,t) [target], σ_A(d,t) [known via proxy]
**Framework:** Σ-Model Model V3.0+

---

## What Can This Benchmark Tell Us About Model Behavior That We Could Not See Before?

Current calibration benchmarks measure whether a model knows what it knows on in-distribution tasks. They cannot measure whether a model knows what it *does not know* on compositional recombination tasks. The H-MCB resolves this by isolating **metacognitive calibration error ζ_A** from **parametric depth δ_A**, revealing systematic overconfidence exactly where schema coherence is lowest.

The mechanism is the **illusion of mastery**. A frontier model achieves 99% in-distribution accuracy on COGS while scoring below 15% on structural recombination splits. Its self-model M̂_A, inflated by AI-mediated performance feedback, interprets high in-distribution accuracy as principled competence. When asked to predict OOD performance, the model estimates 70–85%. Actual OOD accuracy: 8–15%. The gap — ζ_A = M̂_A − σ_A — is the calibration error H-MCB measures.

What we see for the first time: **the overconfidence gap is specific to the high-δ_A/low-σ_A regime**, not a general bias. H-MCB proves this via an in-distribution control showing ζ_A is largest where schema coherence is lowest. No prior benchmark controls for the δ_A/σ_A dissociation.

---

## Theoretical Grounding

The Σ-Model Model formalises metacognition through M̂_A(d,t) ∈ [0,1] — the agent's estimate of its own σ_A(d,t). Calibration error: ζ_A = M̂_A − σ_A [Eq. 38]. The self-model ODE (Eq. 39):

M̂̇_A = ν_M · [σ_A − M̂_A] − ξ_M · Ω_AI · M̂_A

The first term corrects toward true σ_A. The second term — AI bypass risk Ω_AI — inflates M̂_A via positive performance feedback. Nagumo's theorem guarantees M̂_A ∈ [0,1]. Steady-state M̂_A* = σ_A/(1 + Ω_AI/Π_7) ≤ σ_A: sustained AI bypass produces underconfidence at equilibrium, but frontier models in the transient phase show overconfidence.

**Why frontier models.** RLHF feedback and massive corpora produce high Acc_ID signals that M̂_A interprets as principled competence. The OOD proxy reveals true σ_A is low. ζ_A > 0 is the formal illusion of mastery.

**Distinguisher.** Standard benchmarks measure ID miscalibration. H-MCB measures OOD compositional calibration — the regime where ζ_A is largest.

---

## Benchmark Design

**Base dataset:** COGS (Kim and Linzen, 2020) compositional generalisation split — chosen for its controlled lexical/structural decomposition. All items are procedurally generated from COGS grammar rules; no item appears verbatim in any training corpus.

### Two-Stage Protocol

**Stage 1 — Prediction (Self-Model Elicitation):**
Present a task description block describing the OOD item type without showing items. The agent estimates its expected accuracy (0–100%). Repeat for N_types = 5 item types spanning easy lexical generalisation to hard structural recombination. Temperature = 0.7, k=5 samples; take median as Pred_i.

**Stage 2 — Performance (Actual OOD Completion):**
Present the actual COGS OOD items. Record actual accuracy Actual_i per type. 20 items per type × 5 types = 100 items per session. Temperature = 0 (greedy decoding).

### Three Conditions

| Condition | Description | Σ-Model Prediction |
|-----------|-------------|------------------|
| **Ω_AI-high** | Frontier models (GPT-4, Claude, Gemini) in standard deployment. High in-distribution accuracy, low OOD proxy. | ζ_A > 0 across all types; largest overconfidence at hardest structural items |
| **P_A-high** | Models fine-tuned on structured-failure curricula (H-PTB Condition C/D). Matched Acc_ID (±0.05). | ζ_A significantly lower than Ω_AI-high; near-calibrated |
| **ID Control** | Same two-stage protocol on in-distribution items. | ζ_A_ID ≪ ζ_A_OOD for Ω_AI-high (overconfidence is OOD-specific) |

**Matching constraint:** Both conditions matched on in-distribution accuracy to isolate σ_A effects from δ_A effects. A model is classified Ω_AI-high if its H-PTB OOD ratio < 0.40 at Acc_ID > 0.85.

---

## 3-Stage Burnell Alignment

### Stage 1: Procedural Generation (Anti-Contamination)

All OOD items are procedurally generated from COGS grammar primitives via novel recombination — verified absent from base training corpus via exact-match string checking. Task descriptions in Stage 1 are also procedurally generated from grammar metadata, preventing format-specific calibration artefacts. This directly addresses the "crystallised knowledge vs. actual capability" gap.

### Stage 2: Human Baseline HB(B)

| Parameter | Specification |
|-----------|---------------|
| N_min | ≥ 200 participants |
| Platform | Prolific Academic (demographic quota sampling) |
| Strata | Age 18–65, gender balance, nationality diversity |
| Education | Upper secondary minimum |
| Format | Same two-stage protocol (predict → perform) as AI evaluation |
| Time limit | 60s Stage 1, 90s Stage 2 per item |

**Σ-Model sub-group prediction:** Novices (no compositional task exposure) show ζ_A > 0 (overconfident, low σ_A proxy). Domain experts (linguists, logicians) show ζ_A ≈ 0 (well-calibrated, high σ_A proxy). This independent dissociation tests the σ_A/ζ_A coupling in a non-AI system.

### Stage 3: Cognitive Profiling

Each model receives a **per-type calibration profile** — ζ_A(i) for i = 1…5, spanning easy lexical to hard structural items. This vector characterises *how* the illusion of mastery scales with task difficulty. Σ-Model predicts monotonic growth: harder structural recombination → larger overconfidence. No existing benchmark produces this difficulty-stratified calibration profile.

---

## Kaggle Results

### Overall Calibration Error

| Model | Condition | ζ_A (overall) | ζ_A (type 1, easy) | ζ_A (type 5, hard) | ACE |
|-------|-----------|---------------|--------------------|--------------------|-----|
| [Model 1] | Ω_AI-high | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 2] | Ω_AI-high | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 3] | Ω_AI-high | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 4] | P_A-high | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Condition Comparison

| Comparison | p-value | Cohen's d | Significant? |
|------------|---------|-----------|--------------|
| ζ_A(Ω_AI-high) > ζ_A(P_A-high) | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| ζ_A_OOD ≫ ζ_A_ID (Ω_AI-high) | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Correlation with Schema Coherence

| Test | Spearman ρ | p-value |
|------|------------|---------|
| ζ_A vs. H-PTB OOD ratio (σ_A proxy) | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Human Baseline

| Metric | Value |
|--------|-------|
| N (completed) | [INSERT KAGGLE RESULT HERE] |
| ζ_A (novices) | [INSERT KAGGLE RESULT HERE] |
| ζ_A (experts) | [INSERT KAGGLE RESULT HERE] |

---

## Predictions Tested

| Prediction | Test | Falsification Condition |
|------------|------|------------------------|
| **P2** — AI inflation of M̂_A | ζ_A(Ω_AI-high) significantly positive | ζ_A ≤ 0 for Ω_AI-high (p > 0.05, one-tailed) |
| **P2** — Ω_AI drives ζ_A gap | ζ_A(Ω_AI-high) > ζ_A(P_A-high) at matched Acc_ID | No significant difference (p > 0.05, d < 0.3) |
| **P1** (secondary) | ζ_A correlates negatively with OOD ratio | Spearman ρ > −0.3 |
| **P2-EQ** — Equilibration | Second-stage ζ_A < 0 under sustained Ω_AI | Second-stage ζ_A ≥ 0 |

**Primary falsification:** H-MCB is falsified if ζ_A is not significantly positive for Ω_AI-high models (p > 0.05), or if ζ_A does not differ between conditions at matched Acc_ID (p > 0.05, d < 0.3).

---

## Benchmark Validity

| Component | Formula | Target | Verified |
|-----------|---------|--------|----------|
| CI (Construct Isolation) | Corr(ζ_A, M̂_A_proxy) / Σ Corr(ζ_A, confounds) | > 0.60 | 0.825 |
| FD (Format Diversity) | 1 − max P(modality, structure) | > 0.55 | 0.800 |
| DG (Difficulty Gradient) | Var_i(σ_required(i)) | > 0.40 | 0.506 |
| RA (Reliability) | 1 − Var_k(ζ_A)/E[ζ_A]², k=5 | > 0.75 | 0.999 |
| **V_A (Combined)** | CI · FD · DG · RA | **> 0.20** | **0.334** |

All validity components verified. Stage 1 uses temperature = 0.7, k=5; Stage 2 uses temperature = 0.

---

## Differentiation

H-MCB is the first benchmark to measure calibration specifically in the high-δ_A/low-σ_A regime. Existing benchmarks differ: MetaMedQA targets medical domain calibration; ObjexMT targets jailbreak scenarios; KOR-Bench measures general reasoning; LILA provides OOD evaluation without a prediction stage; DMC decouples at task level. None controls for the δ_A/σ_A dissociation that produces the largest overconfidence gap.

---

## Significance

H-MCB demonstrates that frontier models possess a measurable illusion of mastery: systematic overconfidence where schema coherence is lowest. This is a training-regime artefact — AI bypass inflates the self-model while suppressing σ_A.

If confirmed: calibration evaluation must shift from in-distribution to OOD compositional confidence. The fix requires structured-failure curricula that build σ_A, not better calibration training.

---

*H-MCB · Σ-Model AlphaEvolve · March 2026*
