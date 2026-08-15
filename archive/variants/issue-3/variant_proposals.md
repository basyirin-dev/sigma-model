# VARIANT PROPOSALS — ISSUE #3

**Issue #3 (Tier 1B):** The distinctions provided in the Excess column of the σA mapping table are based on temporal dynamics rather than a categorical difference in representational content.

**Related sections:** §3.1.3 (Schema Coherence σ_A uniqueness table), §3.1.3 prose definition.

**Negative log check:** Issues #1 and #2 (resolved) addressed σA definition grounding (issue #1) and computational proxy architecture (issue #2). Issue #1 variants introduced MDL framing, axiomatization, and proxy identification — none of which addressed the categorical-vs-temporal distinction problem in the uniqueness table. Issue #2 variants introduced training-time proxies without modifying the table structure. No rejected approaches from related issues overlap with the current issue.

---

### VARIANT A

**Issue #:** 3
**Tag:** schema-coherence-distinction
**Section targeted:** §3.1.3 — uniqueness table, additional rows
**Scope:** Local prose fix
**DIAGNOSIS:** The current uniqueness table distinguishes σA from Structured Repr., Disentangled Repr., Causal Repr., and Cognitive Schema using seven rows that are all temporal-dynamic properties: "Continuous scalar ODE," "Frontier-relative normalisation," "Multiplicative ΨA coupling," etc. These are properties of how σA *behaves* over time, not properties of what σA *is* as a representational construct. A reviewer can argue that the table demonstrates σA has different dynamics but does not demonstrate σA occupies a categorically different position in the space of representational constructs. The fix is to add rows that capture categorical properties — properties of representational content rather than temporal evolution.

**PROPOSED FIX:**

*After the existing seven rows in the uniqueness table (§3.1.3), add three new rows:*

> | Property                                 | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | ---------------------------------------- | --- | ---------------- | ------------------ | ------------ | ---------------- |
> | Continuous scalar ODE                    | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Frontier-relative normalisation          | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Evaluative function (AI error detection) | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Multiplicative Ψ_A coupling              | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Decay coupling (slows λ_c)               | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | AI bypass risk Ω_AI suppression          | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Cross-modal transfer Θ_A                 | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | **Encodes composition recombination capacity** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | **Normalised against domain frontier** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | **Evaluative (detects AI-derived surface shortcuts)** | **✓** | **✗** | **✗** | **✗** | **✗** |

*Immediately before the table, add:*

> **Categorical properties distinguishing σ_A.** The following table contrasts σ_A with four adjacent representational constructs on two categories of properties: (1) *categorical* properties that describe what the construct encodes (rows 8–10), and (2) *temporal-dynamic* properties that describe how the construct evolves and couples to other variables (rows 1–7). The categorical properties establish σ_A as occupying a distinct region of the representational-construct space; the temporal-dynamic properties establish its behavioural signature within the H-Bar ODE system.

**JUSTIFICATION:** This fix adds three categorical-property rows that answer "what is σA?" rather than "how does σA behave?" The three new rows assert that σA uniquely: (a) encodes the agent's capacity for compositional recombination of primitives (not merely statistical structure, causal structure, or disentanglement), (b) is normalised against the domain frontier Δ(d,t) (not a raw magnitude or bounded property of a single representation), and (c) has an evaluative function that detects when surface shortcuts from AI bypass are being used (not merely a descriptive property of representations). These are categorical claims about representational *content*, not temporal dynamics. The fix adds text only; no equations, ODEs, or coupling terms are modified. The existing seven rows are preserved, and the added introductory prose explicitly distinguishes the two categories.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds three rows and one paragraph of prose to the uniqueness table in §3.1.3. The temporal-dynamic rows are preserved — the fix supplements rather than replaces.

---

### VARIANT B

**Issue #:** 3
**Tag:** schema-coherence-distinction
**Section targeted:** §3.1.3 — uniqueness table structure
**Scope:** Structural reframe
**DIAGNOSIS:** The deeper problem is not merely that the table lacks categorical rows — it is that the table conflates two logically distinct comparison tasks. The table is simultaneously trying to: (1) distinguish σA from other representational constructs (a categorical comparison), and (2) demonstrate that σA has unique formal properties within the H-Bar framework (a structural comparison). These require different rows and different column interpretations. A structural fix separates the table into two sub-tables: one for categorical distinction and one for formal-structural distinction.

**PROPOSED FIX:**

*Replace the existing uniqueness table in §3.1.3 with two sub-tables:*

> **Table 3.1a — Categorical Distinction (What σ_A encodes)**
>
> | Property | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | --- | --- | --- | --- | --- | --- |
> | Measures compositional recombination capacity | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Normalised against domain frontier (bounded relative to Δ(d,t)) | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Distinguishes principled encoding from surface-statistical encoding | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Carries evaluative function (detects AI-derived shortcuts) | ✓ | ✗ | ✗ | ✗ | ✗ |
>
> **Table 3.1b — Formal-Structural Distinction (How σ_A behaves within H-Bar)**
>
> | Property | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | --- | --- | --- | --- | --- | --- |
> | Continuous scalar ODE | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Multiplicative Ψ_A coupling | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Decay coupling (slows λ_c) | ✓ | ✗ | ✗ | ✗ | ✗ |
> | AI bypass risk Ω_AI suppression | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Cross-modal transfer Θ_A | ✓ | ✗ | ✗ | ✗ | ✗ |

*Add before Table 3.1a:*

> **Two-category distinction.** σ_A is distinguished from adjacent representational constructs on two logically independent axes. Table 3.1a lists *categorical* properties — what σ_A encodes as a representational quantity. Table 3.1b lists *formal-structural* properties — how σ_A behaves as a state variable within the H-Bar dynamical system. A construct could in principle satisfy the formal-structural properties without satisfying the categorical properties (e.g., any scalar with an ODE, coupling terms, and suppression channels); it is the conjunction of both tables that establishes σ_A as a novel quantity.

**JUSTIFICATION:** This fix restructures the table into two sub-tables that explicitly separate categorical from temporal-dynamic distinctions. The added prose makes this separation visible to the reviewer and explains why both categories are needed. The new Table 3.1a contains four rows asserting what σA *is* as a representational quantity. Table 3.1b retains five of the original seven rows (removing "Frontier-relative normalisation" and "Evaluative function" which are better classified as categorical properties, moved to Table 3.1a). The fix modifies table structure and adds prose; no equations are changed.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It restructures the uniqueness table into two sub-tables and adds linking prose. The content of the distinction is preserved — the fix reorganises for clarity.

---

### VARIANT C

**Issue #:** 3
**Tag:** schema-coherence-distinction
**Section targeted:** §3.1.3 — entire uniqueness table subsection
**Scope:** Systemic reframe
**DIAGNOSIS:** The issue reveals a deeper problem: the uniqueness table is performing the wrong kind of comparison. It compares σA against generic representational-construction types (Structured, Disentangled, Causal, Cognitive Schema), but these are not the actual competitors for the "σA is novel" claim. The real competitors are: (a) in-distribution accuracy as a proxy for generalisation, (b) parametric depth δA as a sufficient statistic for capability, and (c) loss-function value as a training-state summary. A systemic reframe replaces the table with a comparison against these actual competitors, grounding the distinction in the specific claims the paper makes.

**PROPOSED FIX:**

*Replace the entire uniqueness table and its introduction with:*

> **Why σ_A is not redundant with existing quantities.**
>
> The novelty claim for σ_A is not that it differs from "structured representations" in general — that is trivially true for any quantity with an ODE. The claim is that σ_A captures a training-state property that is not captured by any of the quantities currently used to evaluate agent capability. The following table compares σ_A against four quantities a reviewer might propose as substitutes:

| Property | σ_A | In-distribution accuracy (Acc_In) | Parametric depth (δ_A) | Training loss (ℒ) | OOD accuracy (Acc_OOD) |
| --- | --- | --- | --- | --- | --- |
| Predicts compositional recombination failure when Acc_In is high | ✓ | ✗ | ✗ | ✗ | ✓ (but is the target, not a predictor) |
| Evolves under a dedicated ODE with growth/suppression terms | ✓ | ✗ | ✓ | ✗ | ✗ |
| Gates decay rate of another variable (slows λ_c) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Multiplicatively gates intersection discovery (Ψ_A) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Normalised against the domain frontier Δ(d,t) | ✓ | ✗ | Partially (via δ_A^relative) | ✗ | ✗ |
| Detects AI bypass suppression (Ω_AI sensitivity) | ✓ | ✗ | ✗ | ✗ | ✗ |
| Supports cross-modal transfer (Θ_A) | ✓ | ✗ | ✗ | ✗ | ✗ |

> **Reading the table.** In-distribution accuracy (column 2) fails the recombination-prediction test — the entire SCAN/COGS literature demonstrates that high Acc_In does not predict OOD success. Parametric depth (column 3) has an ODE and partial frontier normalisation, but does not predict recombination failure at matched depth (the High-δ/Low-σ cell in §8.2) and does not gate decay or intersection discovery. Training loss (column 4) captures none of the properties. OOD accuracy (column 5) predicts recombination failure but is itself the quantity being predicted — using Acc_OOD as a proxy for σ_A is circular. σ_A uniquely combines: (a) predictive content not captured by any existing quantity, (b) formal integration into the ODE system, and (c) evaluative function against AI bypass. This establishes categorical novelty, not merely temporal-dynamic novelty.

**JUSTIFICATION:** This systemic reframe replaces the generic comparison against "Structured Repr., Disentangled Repr., etc." with a comparison against the quantities a reviewer would actually propose as substitutes for σ_A. Each column represents a quantity that already exists in the machine-learning evaluation toolkit; the table demonstrates that σ_A captures something none of them capture. The categorical property "predicts compositional recombination failure when Acc_In is high" is the core novelty claim, and the table shows it is unique to σ_A (and trivially to Acc_OOD, which is circular). This grounds the distinction in the paper's specific argument rather than in abstract category labels. The fix replaces the entire table subsection; no equations are changed.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It replaces the uniqueness table and its introductory prose. The comparison targets are changed from generic representational-construct types to the specific quantities a reviewer would propose as substitutes.

---

### VARIANT D

**Issue #:** 3
**Tag:** schema-coherence-distinction
**Section targeted:** §3.1.3 — prose definition + uniqueness table
**Scope:** Local prose fix
**DIAGNOSIS:** The uniqueness table lacks a formal criterion for what counts as a "categorical distinction." Each row asserts a property without explaining why that property constitutes a categorical (as opposed to merely formal) distinction. The fix introduces an explicit definition of "categorical distinction" and then verifies that σA satisfies it, before presenting the table.

**PROPOSED FIX:**

*Insert the following immediately before the uniqueness table in §3.1.3:*

> **Criterion for categorical distinction.** A representational construct C is categorically distinct from construct C' if and only if there exists at least one property P such that:
>
> 1. P is a property of *what the construct encodes* (representational content), not merely *how the construct behaves* (temporal dynamics).
> 2. P is satisfied by C and not by C'.
> 3. P is not an artefact of the formalism (i.e., P would hold under any reasonable mathematical encoding of C, not only the specific ODE formulation used here).
>
> A table that lists only temporal-dynamic properties satisfies condition (2) but not condition (1) — it distinguishes σA by its formal behaviour without establishing that σA encodes something categorically different from adjacent constructs.

*Immediately after this criterion, add two new rows to the existing table:*

> | Property | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | --- | --- | --- | --- | --- | --- |
> | ... (existing 7 rows) | | | | | |
> | **Encodes capacity for zero-shot primitive recombination** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | **Defined as ratio of OOD to ID performance** | **✓** | **✗** | **✗** | **✗** | **✗** |

*Add after the table:*

> **Verification against criterion.** The two categorical rows satisfy all three conditions: (1) they describe what σA encodes (recombination capacity, performance ratio) rather than how it evolves; (2) they are true of σA and false of all four comparator constructs; (3) they hold under any mathematical encoding that defines σA as a recombination-capacity measure — the specific ODE formulation is not the source of the distinction.

**JUSTIFICATION:** This fix makes the distinction criterion explicit, exposing the logical gap in the current table (temporal-dynamic rows violate condition 1) and filling it with two categorical rows that satisfy all three conditions. The verification paragraph closes the argument by confirming the new rows meet the criterion. The fix adds text only; no equations or coupling terms are modified. The existing seven rows are preserved as temporal-dynamic distinctions, which remain valid on condition (2) alone.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds a criterion definition, two table rows, and a verification paragraph to §3.1.3.

---

### VARIANT E

**Issue #:** 3
**Tag:** schema-coherence-distinction
**Section targeted:** §3.1.3 uniqueness table + §3.1.3 prose definition + §3.4.3 (schema coherence ODE intro)
**Scope:** Structural equation fix
**DIAGNOSIS:** The uniqueness table's reliance on temporal-dynamic properties is a symptom of a deeper structural gap: the paper never provides a *pointwise characterisation* of σA — a definition of what σA is at a single instant in time, independent of its temporal evolution. The ODE (Eq. 28) specifies dσA/dt; the proxy identification (Eq. 3b) specifies a measurement procedure; but neither specifies the *kind* of quantity σA is at a point. Without a pointwise characterisation, the only way to distinguish σA from other constructs is by its dynamics (ODE, coupling terms, etc.) — which is exactly what the table does. The fix introduces an explicit pointwise characterisation axiom and derives the table's categorical rows from it.

**PROPOSED FIX:**

*Insert the following axiom immediately after Equation 3 in §3.1.3, before the proxy identification:*

> **Pointwise Characterisation Axiom.** At any instant t, σ_A(d,t) is uniquely characterised by the following three-point specification:
>
> **(PC1) Representational content.** σ_A(d,t) is a scalar measure of the degree to which the agent's current representation of domain d supports compositional recombination of independently trained primitives. Formally: if the agent's representation enables zero-shot recombination of primitives p_1, ..., p_k into novel compositions not seen during training, then σ_A(d,t) > 0; if the representation supports only interpolations within the training distribution, then σ_A(d,t) ≈ 0.
>
> **(PC2) Normalisation basis.** σ_A(d,t) is normalised against the domain frontier Δ(d,t), not against an absolute scale. This means σ_A measures recombination capacity *relative to the maximum possible recombination capacity in domain d at time t*. As Δ(d,t) advances, σ_A can decrease without any change in the agent's absolute recombination capacity.
>
> **(PC3) Evaluative function.** σ_A(d,t) has a signature property absent from all four comparator constructs: it detects when AI-derived outputs bypass the agent's own compositional encoding. Formally, σ_A enters the Ω_AI suppression term (Eq. 28) as the variable that is suppressed — it is the quantity that AI bypass erodes. No other representational construct in the table has this evaluative function.
>
> **Theorem (Categorical Distinction).** The conjunction of (PC1)–(PC3) is not satisfied by any of: Structured Representations, Disentangled Representations, Causal Representations, or Cognitive Schemas.
>
> *Proof sketch.* (PC1) fails for Structured and Disentangled Representations because these measure geometric properties of the representation space (cluster structure, factor independence) rather than recombination capacity. It fails for Causal Representations because causal structure enables interventional queries, not necessarily compositional recombination. It fails for Cognitive Schemas because schemas are qualitative knowledge organisations, not scalar recombination-capacity measures. (PC2) fails for all four because none is normalised against a time-varying domain frontier. (PC3) fails for all four because none has an evaluative function against AI bypass — this is a property specific to the H-Bar ODE architecture. □

*Update the uniqueness table to reference the axiom:*

> | Property | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | --- | --- | --- | --- | --- | --- |
> | **PC1: Encodes compositional recombination capacity** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | **PC2: Normalised against domain frontier Δ(d,t)** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | **PC3: Evaluative function (AI bypass detection)** | **✓** | **✗** | **✗** | **✗** | **✗** |
> | Continuous scalar ODE | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Multiplicative Ψ_A coupling | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Decay coupling (slows λ_c) | ✓ | ✗ | ✗ | ✗ | ✗ |
> | AI bypass risk Ω_AI suppression | ✓ | ✗ | ✗ | ✗ | ✗ |
> | Cross-modal transfer Θ_A | ✓ | ✗ | ✗ | ✗ | ✗ |

*Replace "Frontier-relative normalisation" and "Evaluative function (AI error detection)" rows with the PC2 and PC3 rows (these are the categorical formulations of the same properties).*

**JUSTIFICATION:** This fix introduces a pointwise characterisation axiom (PC1–PC3) that defines what σA is at a single instant, independent of its temporal evolution. The theorem with proof sketch establishes categorical distinction formally. The table is reordered to place the three categorical rows (PC1–PC3) first, with the five temporal-dynamic rows below — making the categorical foundation explicit. The fix adds an axiom, a theorem, a proof sketch, and reorganises the table; no ODEs or coupling terms are modified. The two rows removed ("Frontier-relative normalisation," "Evaluative function") are subsumed by PC2 and PC3 in their categorical formulations.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs (the pointwise axiom complements the ODE, which specifies temporal evolution), (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds an axiom, theorem, and proof sketch to §3.1.3 and reorganises the uniqueness table. The ODE (Eq. 28) is unaffected because the axiom defines σA at a point in time and the ODE defines its rate of change — these are complementary.
