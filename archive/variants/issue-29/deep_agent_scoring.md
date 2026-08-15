# Deep Agent Scoring — Issue #29

**Issue:** The framework must engage with the finding from Lake & Baroni (2023) that meta-learning improves lexical compositionality while structural gaps persist.
**Tag:** [N]

---

## Variant A — Gap Statement Prose Addition

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No equations modified. Pure prose addition in §2.2. |
| C2 — Novelty Defence | 8 | Positions H-Bar as predicting the Lake & Baroni dissociation rather than restating it. Forward reference to Prediction 6b strengthens argumentative chain. |
| C3 — Falsifiability | 5 | Indirect improvement via forward reference to Prediction 6b. No new testable protocol added. |
| C4 — Scope Discipline | 10 | Contained within §2.2. Single-agent boundary, cognitive bridge boundary, version boundary all clean. |
| C5 — Hackathon Relevance | 3 | No direct benchmark or protocol improvement. Tangentially related to Learning track. |
| C6 — Version Integration | 6 | Forward reference to V3.0+ prediction. Version-neutral prose. |
| **Composite** | **7.00** | |

---

## Variant B — Formal Boundary Criterion (Corollary)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No equations modified. Corollary added to existing theorem. All referenced terms already defined. |
| C2 — Novelty Defence | 9 | Adds formal boundary criterion (c ∈ T_train vs. c' ∉ T_train) that directly distinguishes σA from meta-learned compositionality. Operationalises via three-condition battery. Sharpest differentiation argument among all variants. |
| C3 — Falsifiability | 8 | Operationalises the distinction via Acc_OOD-struct/Acc_ID ratio, directly measurable from the three-condition battery. Connects to Prediction 6b. |
| C4 — Scope Discipline | 10 | Contained within §3.1.3. All three boundaries clean. |
| C5 — Hackathon Relevance | 5 | Formal boundary criterion could improve Learning track benchmark design by clarifying what OOD-struct items should test. |
| C6 — Version Integration | 6 | Corollary to V1.0 theorem. Neutral version integration. |
| **Composite** | **8.00** | |

---

## Variant C — Systemic Reframe

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No equations modified. Gap statement rewrite only. |
| C2 — Novelty Defence | 8 | Synthesises multiple [N]-tagged objections into coherent challenge. Positions σA as formal response. Strong but risks over-complication if reviewer disputes any cited paper. |
| C3 — Falsifiability | 5 | Forward reference to Prediction 6b. No new testable protocol. |
| C4 — Scope Discipline | 9 | Contained within §2.2. Minor risk: references papers beyond Lake & Baroni (2023), slightly broader scope than issue requires. |
| C5 — Hackathon Relevance | 5 | Systemic framing could inform multiple track protocols indirectly. |
| C6 — Version Integration | 7 | Synthesises across V1.0–V3.0+ predictions. |
| **Composite** | **7.33** | |

---

## Variant D — Prediction 6b Enhancement

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No equations modified. Addition within existing prediction. |
| C2 — Novelty Defence | 8 | Adds specific MAML numbers and mechanistic explanation. Strengthens prediction as novelty defence. |
| C3 — Falsifiability | 9 | Adds concrete experimental evidence (59.4% vs. 16.2% lexical; 8.1% vs. 1.2% structural) and explains mechanism through σA ODE. Strongest falsifiability improvement. |
| C4 — Scope Discipline | 10 | Contained within Prediction 6b. Clean scope. |
| C5 — Hackathon Relevance | 7 | Directly operationalises Prediction 6b as a Learning track benchmark protocol. |
| C6 — Version Integration | 7 | Sharpens V3.0+ prediction. |
| **Composite** | **8.50** | |

---

## Variant E — Table + Prose Addition

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 — ODE System Coherence | 10 | No equations modified. Prose and table updates only. |
| C2 — Novelty Defence | 7 | Adds Lake & Baroni (2023) to two locations. Moderate differentiation. Less formal than Variant B. |
| C3 — Falsifiability | 5 | Indirect improvement via forward reference to Prediction 6b. |
| C4 — Scope Discipline | 10 | Contained within §2.2 and §2.6. Clean scope. |
| C5 — Hackathon Relevance | 3 | No direct protocol improvement. |
| C6 — Version Integration | 5 | Adds to V1.0 table and gap statement. Version-neutral. |
| **Composite** | **6.67** | |

---

## Scoring Summary

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | Composite | Flags |
|---------|----|----|----|----|----|----|-----------|-------|
| **B** | 10 | 9 | 8 | 10 | 5 | 6 | **8.00** | |
| **D** | 10 | 8 | 9 | 10 | 7 | 7 | **8.50** | [HACKATHON PRIORITY] |
| C | 10 | 8 | 5 | 9 | 5 | 7 | 7.33 | |
| A | 10 | 8 | 5 | 10 | 3 | 6 | 7.00 | |
| E | 10 | 7 | 5 | 10 | 3 | 5 | 6.67 | |

All variants score ≥ 6.0 — none suppressed.

---

## Top 2 Variants

### #1: VARIANT D (Composite: 8.50) [HACKATHON PRIORITY]

**C5 = 7** triggers [HACKATHON PRIORITY] — directly operationalises Prediction 6b as a Learning track benchmark protocol.

VARIANT D strengthens the Lake & Baroni (2023) engagement by adding specific empirical numbers and a mechanistic explanation to Prediction 6b. This makes the prediction immediately actionable as a benchmark design: experimenters can replicate the MAML-on-SCAN protocol and measure the σA/δA dissociation directly. The addition does not modify any equations and is contained within the existing prediction.

### #2: VARIANT B (Composite: 8.00)

VARIANT B adds a formal boundary criterion (c ∈ T_train vs. c' ∉ T_train) that directly distinguishes σA from meta-learned compositionality. This is the strongest differentiation argument and operationalises via the three-condition battery. It provides the formal grounding that a reviewer would need to accept the σA/meta-learning distinction.

---

## HACKATHON UPDATE

**VARIANT D (Top 1):**
Update `/hackathon/track_learning.md` to add the MAML-on-SCAN protocol as a concrete benchmark implementation for Prediction 6b. Specifically: run MAML (5-shot) on SCAN, measure Acc_ID and Acc_OOD-struct before and after meta-learning, compute σA proxy = Acc_OOD-struct/Acc_ID. If ΔAcc_ID >> ΔAcc_OOD-struct, the σA/δA dissociation is confirmed. This directly implements one of the Learning track benchmark families.

**VARIANT B (Top 2):**
No direct hackathon update. The boundary criterion improves benchmark design theory but does not produce a concrete protocol change.

---

## INTEGRATION UPDATE

**For both Top 1 and Top 2 variants:**
Update `integration_map.md` row for Issue #29:
- Consistency Verified: change NO → YES
- Add note: "Lake & Baroni (2023) engaged via [variant location]. Prediction 6b connected to §2.2 gap statement."

---

## NEGATIVE LOG

- **Variant A:** Prose-only gap statement addition is necessary but weaker than Variant D's Prediction 6b enhancement (C3: 5 vs. 9) and Variant B's formal boundary criterion (C2: 8 vs. 9).
- **Variant C:** Systemic reframe is comprehensive but addresses more than Issue #29 requires (Issues #30–#36), creating scope risk and no direct falsifiability improvement.
- **Variant E:** Table + prose addition is the most minimal intervention but provides the weakest novelty defence (C2: 7) and no falsifiability improvement (C3: 5).

---

## CHECKPOINT RECOMMENDATION

Not yet at Checkpoint threshold (current edit count: 12 approved edits, Checkpoint A threshold: 9, Checkpoint B already passed). No additional checkpoint needed at this time.
