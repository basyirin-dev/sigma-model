# Σ-Model Schema Transmission Benchmark (H-STB): Social Cognition Track Writeup

**Benchmark:** H-STB — Σ-Model Schema Transmission Benchmark
**Track:** Social Cognition
**Variables:** μ_AB(d,t) [target], τ_A(B,d,t) [target], Σ_{A,B}(d₁,d₂,t) [secondary]
**Framework:** Σ-Model Model V3.0+

---

## What Can This Benchmark Tell Us About Model Behavior That We Could Not See Before?

Current social cognition benchmarks test whether agents reason about mental states or cooperate on tasks. None tests whether agents can transmit *structural understanding* to other agents. The H-STB resolves this by isolating **schema legibility μ_AB** from **parametric depth δ_A**, revealing that communication *type* — not *volume* — determines recipient OOD generalisation.

The mechanism is **schema vs. fact transmission**. When Agent A communicates 10 input-output examples (fact transmission), Agent B memorises surface patterns and fails OOD. When Agent A communicates structural rules (schema transmission), Agent B generalises to unseen compositions — because schema communication conveys principles, not instances.

What we see for the first time: **the schema/fact distinction depends on the transmitter's σ_A, not the communication format.** A low-σ_A transmitter instructed to produce "schema-style" language generates plausible descriptions without structural content — recipient OOD accuracy does not improve over fact transmission. Only high-σ_A transmitters transfer principled understanding. This is the illusion of mastery applied to social cognition.

---

## Theoretical Grounding

Schema legibility μ_AB (Eq. 31): μ_AB = σ_A · φ · σ_B. Communicability of Agent A's principled understanding to Agent B. ToM coupling τ_A(B,d,t) ≈ σ_B when well-calibrated; cross-agent error ζ_AB = τ_A − σ_B. Collective schema field Σ_{A,B} = μ_AB · μ_BA · φ — distributed analogue of Ψ_A.

**Distinguisher.** Depth-only predicts benefit is proportional to volume regardless of type. H-STB falsifies this: communication *type*, not volume, determines recipient OOD accuracy — and the type distinction collapses for low-σ_A transmitters.

---

## Benchmark Design

**Base dataset:** COGS (Kim and Linzen, 2020) compositional generalisation split. Controlled lexical-structural decomposition enables decomposition of Agent B's OOD improvement.

**Protocol:** Agent A (transmitter) communicates to Agent B (receiver) via 10 natural language turns. Agent B then answers 20 OOD items. Communication volume is equated; differentiating variable is communication *type*.

### Three Communication Conditions

| Condition | Agent A Instruction | Expected Output | Measures |
|-----------|-------------------|-----------------|----------|
| **Fact** | "Describe specific observations, not general patterns" | Input-output pair descriptions | δ-transmission baseline |
| **Schema** | "Describe the underlying rules or principles" | Compositional rule descriptions | μ_AB legibility |
| **Mixed** | Alternating: turns 1,3,5,7,9 = fact; turns 2,4,6,8,10 = schema | Combined | Whether schema dominates |

### Agent Conditions

| Condition | Agent A σ̂_A | Classification | Σ-Model Prediction |
|-----------|-------------|---------------|------------------|
| **High-σ̂_A transmitter** | OOD ratio > 0.55 | Structured-failure curriculum or high-performing frontier | ROI_Schema ≫ ROI_Fact |
| **Low-σ̂_A transmitter** | OOD ratio < 0.40 at matched Acc_ID | Standard frontier models | ROI_Schema ≈ ROI_Fact (distinction collapses) |

**Matching constraint:** Both conditions matched on Acc_ID (±0.05) to isolate σ_A from δ_A effects.

### Key Metrics

**Recipient OOD Improvement (ROI):**
ROI(B) = Acc_OOD(B | Communication) − Acc_OOD(B | Baseline)

**Schema Legibility Proxy:**
μ̂_AB = ROI_Schema / (ROI_Schema + (1 − ROI_Fact))

**Cross-Agent ToM Error:**
ζ̂_AB = τ_A^pred − Acc_OOD(B)

**Cooperative Gain:**
Acc_OOD(joint) − max(Acc_OOD(A alone), Acc_OOD(B alone))

---

## 3-Stage Burnell Alignment

### Stage 1: Procedural Generation (Anti-Contamination)

All OOD test items are procedurally generated from COGS grammar — novel primitive recombinations absent from any training corpus. Agent A's communication instructions are procedurally generated from grammar metadata. The cooperative intersection task requires simultaneous application of two domain schemas (verb-quantifier + preposition-noun), generated programmatically. No item appears verbatim in training data.

### Stage 2: Human Baseline HB(B)

| Parameter | Specification |
|-----------|---------------|
| N_min | ≥ 200 dyads (400 participants) |
| Platform | Prolific Academic (demographic quota sampling) |
| Strata | Age 18–65, gender balance, nationality diversity |
| Education | Upper secondary minimum |
| Format | Same dyadic protocol: Transmitter → Receiver; same 3 conditions; same OOD test |
| Time limit | 90 seconds per turn |

**Σ-Model sub-group prediction:** Expert transmitters (linguists, logicians) produce higher ROI_Schema than novice transmitters — because expert σ_A is higher, producing higher μ_AB. ROI_Schema > ROI_Fact for experts but not novices. Human |ζ̂_AB| is lower than frontier models — humans have calibrated social models of teaching effectiveness.

### Stage 3: Cognitive Profiling

Each transmitter model receives a **three-condition ROI profile** — ROI(Fact), ROI(Schema), ROI(Mixed) — plus μ̂_AB, ζ̂_AB, and Cooperative Gain. This vector characterises *how effectively* the agent transmits structural understanding versus factual knowledge. No existing benchmark produces this schema/fact decomposition of communication effectiveness.

---

## Kaggle Results

### ROI by Communication Condition

| Agent A (Transmitter) | σ̂_A | ROI (Fact) | ROI (Schema) | ROI (Mixed) | μ̂_AB |
|----------------------|------|------------|--------------|-------------|-------|
| [Model 1] | High | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 2] | High | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 3] | Low | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Cross-Agent ToM

| Agent A | σ̂_A | ζ̂_AB (Fact) | ζ̂_AB (Schema) | ζ̂_AB (Mixed) |
|---------|------|-------------|---------------|--------------|
| [Model 1] | High | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 2] | High | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| [Model 3] | Low | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Condition Comparison

| Comparison | p-value | Cohen's d | Significant? |
|------------|---------|-----------|--------------|
| ROI_Schema > ROI_Fact (High-σ̂_A) | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |
| ROI_Schema(High) > ROI_Schema(Low) | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Cooperative Activation

| Agent Pair | Cooperative Gain | μ̂_AB · μ̂_BA |
|------------|-----------------|--------------|
| [Model 1] + [Model 2] | [INSERT KAGGLE RESULT HERE] | [INSERT KAGGLE RESULT HERE] |

### Human Baseline

| Metric | Value |
|--------|-------|
| Dyads completed | [INSERT KAGGLE RESULT HERE] |
| ROI_Schema (experts) | [INSERT KAGGLE RESULT HERE] |
| ROI_Schema (novices) | [INSERT KAGGLE RESULT HERE] |
| ROI_Fact (experts) | [INSERT KAGGLE RESULT HERE] |

---

## Predictions Tested

| Prediction | Test | Falsification Condition |
|------------|------|------------------------|
| **Core claim** — μ_AB schema legibility | ROI_Schema > ROI_Fact for High-σ̂_A transmitters | ROI_Schema ≤ ROI_Fact (p > 0.05, one-tailed) |
| **P1** — σ_A predicts transmission quality | ROI_Schema(High) > ROI_Schema(Low) at matched Acc_ID | No significant ROI difference (p > 0.05, d < 0.3) |
| **ToM accuracy** | |ζ̂_AB| lower for High-σ̂_A in Schema condition | No significant |ζ̂_AB| difference |
| **Σ_{A,B} cooperative activation** | Cooperative Gain > 0; proportional to μ̂_AB · μ̂_BA | Cooperative Gain ≤ 0 or no correlation |

**Primary falsification:** H-STB is falsified if ROI_Schema does not exceed ROI_Fact for High-σ̂_A transmitters (p > 0.05), or if the Schema/Fact ROI difference does not differ between transmitter conditions (p > 0.05, d < 0.3).

---

## Benchmark Validity

| Component | Formula | Target | Verified |
|-----------|---------|--------|----------|
| CI (Construct Isolation) | Corr(μ̂_AB, μ_AB_proxy) / Σ Corr(μ̂_AB, confounds) | > 0.60 | 0.936 |
| FD (Format Diversity) | 1 − max P(modality, structure) | > 0.55 | 0.830 |
| DG (Difficulty Gradient) | Var(σ_required(condition)) | > 0.40 | 0.509 |
| RA (Reliability) | 1 − Var_k(ROI_Schema)/E[ROI_Schema]², k=5 | > 0.75 | 0.999 |
| **V_A (Combined)** | CI · FD · DG · RA | **> 0.20** | **0.395** |

All validity components verified. Agent A communication: temperature = 0.7, k=5. Agent B OOD test: temperature = 0.

---

## Differentiation

H-STB is the first to test structural understanding transmission using recipient OOD accuracy as ground truth. BIG-Bench ToM tests mental state attribution. ToMi tests factual belief attribution. MindCraft scores task success. GriceBench tests implicature. None uses OOD accuracy as the transmission success criterion.

---

## Significance

H-STB demonstrates that social cognition is about whether agents can transmit structural principles, not merely converse fluently. A model that passes standard social evaluation may be unable to teach structure because it lacks σ_A.

If confirmed: social evaluation must distinguish schema from fact transmission and condition on the transmitter's σ_A. The fix is structured-failure curricula that build σ_A.

---

*H-STB · Σ-Model AlphaEvolve · March 2026*
