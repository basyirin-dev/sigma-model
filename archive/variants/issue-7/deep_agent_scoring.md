# Deep Agent Scoring — Issue #7

**Issue #:** 7
**Tag:** [P] (Phase transition)
**Description:** The Phase 2 transition is triggered by an unobservable latent variable and lacks a formalised differential proxy signal for external verification.

---

## Scoring Summary

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | Composite | Flag |
|---------|----|----|----|----|----|----|-----------|------|
| **A** | 9 | 8 | 7 | 10 | 5 | 7 | **7.67** | — |
| **B** | 8 | 8 | 8 | 10 | 6 | 8 | **8.00** | — |
| **C** | 9 | 8 | 10 | 10 | 8 | 7 | **8.67** | [HACKATHON PRIORITY] |
| **D** | 8 | 8 | 6 | 10 | 7 | 9 | **8.00** | [INTEGRATION PRIORITY] |
| **E** | 7 | 8 | 9 | 8 | 7 | 8 | **7.83** | — |

**Suppression threshold:** 6.0 — No variants suppressed.

**Top 2:** Variant C (8.67) and Variant B/D (tied at 8.00). Variant C selected as top; Variant D selected as second (higher C6 than B).

---

## Detailed Scoring

### VARIANT A — Local Prose Fix (Proxy Bridge)

**C1 — ODE System Coherence: 9/10**
Uses existing proxy definitions (Eqs. 3b, 3c, 3d) without modification. No new equations introduced. ODE system closure fully maintained. Minor deduction: the differential criterion `dσ̂_A/dt > 0` is stated in prose without a formal equation, leaving implementation details to the reader.

**C2 — Novelty Defence: 8/10**
No variable redefinition or boundary alteration. σ_A retains its categorical distinction from adjacent constructs. The fix is purely operationalisation — connecting existing definitions to existing phase triggers.

**C3 — Falsifiability: 7/10**
Makes Phase 2 detection more testable by connecting to observable proxies, but does not add a new §9 prediction. The differential criterion (`dσ̂_A/dt > 0 sustained over ≥2 probe intervals`) is testable in principle but lacks the formal falsification condition that §9 predictions require.

**C4 — Scope Discipline: 10/10**
Clean local prose fix. Single-agent boundary respected (no multi-agent language). Cognitive bridge boundary respected (no psychological vocabulary). Version boundary respected (no V2.0+ variables bleeding into V1.0 equations).

**C5 — Hackathon Relevance: 5/10**
Tangentially related. Better phase detection could inform training protocol design for hackathon tracks, but no direct benchmark improvement or Kaggle protocol enhancement. No §9 prediction operationalised.

**C6 — Version Integration Score: 7/10**
Connects V1.0 proxy architecture (§3.1.3) to V3.0+ phase structure (§7.2). This is a modest integration improvement — the proxy definitions were already present but not referenced in the phase trigger. The fix reduces the version seam by making the phase structure rely on definitions from the core framework.

**Composite: 7.67**

---

### VARIANT B — Structural Equation Fix (Derivative Entry Test)

**C1 — ODE System Coherence: 8/10**
Introduces new equation (51a) and Appendix equation (A.16), but both are derived from existing ODE dynamics. The second-derivative condition (`d²σ̂_A/dt² > 0`) is grounded in the self-reinforcing nature of the σ_A ODE (Eq. 28). Minor deduction: the second-derivative criterion assumes smooth proxy trajectories, which may not hold with noisy Tier 1 probe estimates.

**C2 — Novelty Defence: 8/10**
Does not affect variable distinctness. The new criterion is operationalisation-only — it does not redefine σ_A, α_A, or any other variable.

**C3 — Falsifiability: 8/10**
The second-derivative criterion provides a sharper testable condition than Variant A. The entry test (Eq. 51a) is formally computable from proxy time series. However, like Variant A, it does not add a new §9 prediction — it only improves the phase detection mechanism.

**C4 — Scope Discipline: 10/10**
Structural fix but stays within all three boundaries. No psychological language, no multi-agent extension, no version boundary violation.

**C5 — Hackathon Relevance: 6/10**
Slightly more actionable than Variant A — the formal entry test (Eq. 51a, A.16) could be implemented as a training-monitoring function in hackathon protocols. But no direct benchmark improvement.

**C6 — Version Integration Score: 8/10**
Adds a new equation to Appendix A (A.16) that bridges the phase structure (§7, V1.0/V3.0+) with the proxy architecture (§3.1.3, V1.0). Better integration than Variant A because the connection is formalised in equation form.

**Composite: 8.00**

---

### VARIANT C — Local Fix + Falsifiable Prediction (OOD Acceleration)

**C1 — ODE System Coherence: 9/10**
No new equations introduced. Uses existing OOD accuracy concept (§3.1.3, Eq. 3b) and connects it to the phase structure via a prose definition of the acceleration signature. The theoretical basis is sound: σ_A > σ_critical → α_A·P_A coupling dominates → faster σ_A growth → narrowing OOD gap. This is a direct consequence of Eq. 28.

**C2 — Novelty Defence: 8/10**
Does not affect variable distinctness. The acceleration signature is an observable consequence of existing dynamics, not a redefinition of any variable.

**C3 — Falsifiability: 10/10**
Adds Prediction 9 to §9 with explicit claim, measurement protocol, and falsification condition. This is the strongest score possible — the fix directly extends the falsifiable prediction set with a testable empirical claim about Phase 2 entry.

**C4 — Scope Discipline: 10/10**
Local fix. No boundary violations. The prediction uses only measurable quantities (Acc_OOD, dAcc_OOD/dt, σ̂_A) without importing psychological language or extending to multi-agent scope.

**C5 — Hackathon Relevance: 8/10**
Prediction 9 is directly operationalisable for hackathon training protocols. The OOD acceleration signature can be monitored during training to detect Phase 2 entry, informing when to shift from depth-accumulation prescriptions (Phase 1) to schema-crystallisation prescriptions (Phase 2). This is actionable for the Learning track (SCAN/COGS benchmarks).

**C6 — Version Integration Score: 7/10**
Links phase structure (§7, V1.0/V3.0+) to falsifiable predictions (§9, V3.0+). Modest integration improvement — the phase structure and prediction set were previously unconnected. The fix creates a formal bridge between them.

**Composite: 8.67** — **[HACKATHON PRIORITY]**

---

### VARIANT D — Structural Fix (Reliability Inflection)

**C1 — ODE System Coherence: 8/10**
Uses existing R_A function (Eq. 48) without modification. Adds a cross-reference between §6.1 and §7.2. The theoretical chain (higher σ_A → more stable Acc_OOD → lower variance → higher R_A) is sound but relies on an indirect causal link that is not formally derived in the ODE system.

**C2 — Novelty Defence: 8/10**
Does not affect variable distinctness. The reliability inflection is an observable consequence of schema crystallisation, not a redefinition.

**C3 — Falsifiability: 6/10**
The reliability inflection (`dR_A/dt > 0`) is a weaker testable signal than SGG acceleration. Reliability depends on score variance, which is a second-order effect of schema coherence. The signal is noisier and harder to detect than direct OOD accuracy changes.

**C4 — Scope Discipline: 10/10**
Structural fix but within all boundaries. No violations.

**C5 — Hackathon Relevance: 7/10**
Reliability (R_A) is directly relevant to benchmark design — it is part of the V3.0+ validity function (Eq. 49). Connecting R_A to phase detection could inform when to switch benchmark protocols during training. Directly improves benchmark quality assessment.

**C6 — Version Integration Score: 9/10**
This is the strongest integration score. The fix bridges V3.0+ reliability extension (§6.1) with V1.0 phase structure (§7.2). This is a meaningful cross-version integration — R_A was introduced in V3.0+ but had no connection to the core phase structure. The fix creates a formal link.

**Composite: 8.00** — **[INTEGRATION PRIORITY]**

---

### VARIANT E — Systemic Reframe (Compound Observable Trigger)

**C1 — ODE System Coherence: 7/10**
Introduces a compound observable trigger (Eq. 51c) that replaces the latent-variable trigger. While the compound trigger is designed to detect the same latent threshold, having two different criteria (theoretical: σ_A > σ_critical vs. operational: Eq. 51c) could create confusion about which is the "real" trigger. The calibration procedure (mapping σ̂_critical to σ_critical) adds a dependency on calibration accuracy that could fail if proxy quality degrades.

**C2 — Novelty Defence: 8/10**
Does not affect variable distinctness. The compound trigger uses existing proxy quantities.

**C3 — Falsifiability: 9/10**
The compound observable trigger (Eq. 51c) is highly testable — all three conditions are computable from observable data. The three-condition conjunction provides robustness against noise. Stronger than Variants A and B, slightly weaker than Variant C (which adds a formal §9 prediction).

**C4 — Scope Discipline: 8/10**
Systemic scope — reframes the trigger entirely. Stays within single-agent boundary and version boundary. Minor concern: the calibration procedure adds complexity that could be seen as exceeding the original phase structure scope.

**C5 — Hackathon Relevance: 7/10**
The compound trigger is directly implementable in training-monitoring code. Hackathon protocols could use Eq. 51c as a concrete Phase 2 detection function.

**C6 — Version Integration Score: 8/10**
Integrates proxy architecture (§3.1.3, V1.0) with phase structure (§7.2, V1.0/V3.0+) more deeply than Variants A/B by adding calibration guidance. The calibration procedure creates a formal dependency between the two sections.

**Composite: 7.83**

---

## NEGATIVE LOG (for future reference)

**Variant A:** Not recommended — weakest on Hackathon Relevance (C5=5) and Falsifiability (C3=7); superseded by Variant C on both dimensions.

**Variant B:** Tied for second; not selected as primary recommendation because Variant C scores higher on Falsifiability (10 vs. 8) and Hackathon Relevance (8 vs. 6).

**Variant E:** Not recommended — lowest ODE System Coherence (C1=7) due to dual-trigger confusion risk and calibration dependency; Scope Discipline (C4=8) also lowest among variants.

---

## HACKATHON UPDATE:

**Variant C (TOP):**
- **track_learning.md:** Add monitoring protocol for Prediction 9 — track Acc_OOD trajectory and detect acceleration inflection (dAcc_OOD/dt exceeding Phase 1 baseline by ≥2σ for ≥3 consecutive checkpoints) as Phase 2 entry signal for SCAN/COGS training.
- **track_metacognition.md:** Phase 2 entry detection informs when to shift calibration protocols — ζ_A monitoring becomes more critical post-Phase 2 entry.

**Variant D (SECOND):**
- **track_learning.md:** Add R_A tracking to benchmark quality assessment — reliability inflection (dR_A/dt > 0) serves as secondary Phase 2 confirmation signal.

---

## INTEGRATION UPDATE:

**Variant C:**
- No integration_map.md updates required — the fix adds content to §7.2 and §9 but does not change existing integration relationships.

**Variant D:**
- integration_map.md: Update row for §6.1 (Reliability) — add cross-reference to §7.2 Phase Structure. New dependency: "Phase detection signal (dR_A/dt > 0)".

---

## CHECKPOINT RECOMMENDATION:

Not yet at Checkpoint threshold. This is the 10th approved edit (Issues #1–#6, #10, #22, #23, and now #7 pending). After this edit is approved, recommend mini re-diagnosis at Checkpoint A for §7.2 (Phase 2 trigger statement) to verify no new inconsistencies introduced.
