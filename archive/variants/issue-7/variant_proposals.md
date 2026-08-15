# Variant Proposals — Issue #7

**Issue #:** 7
**Tag:** [P] (Phase transition)
**Status:** OPEN
**Description:** The Phase 2 transition is triggered by an unobservable latent variable and lacks a formalised differential proxy signal for external verification.

---

### VARIANT A
**Issue #:** 7
**Tag:** [P]
**Section targeted:** §7.2 Phase 2 — Depth Acceleration and Schema Crystallisation
**Scope:** local
**DIAGNOSIS:** The Phase 2 trigger statement (`σ_A(d,t) > σ_critical`) uses a latent variable that cannot be directly observed by external evaluators. While §3.1.3 provides a two-tier proxy architecture (Tier 1 training-time probes, Tier 2 evaluation-time SGG), §7.2 does not reference these proxies in the transition trigger. An external observer reading only the phase structure has no way to verify when Phase 2 has begun. The fix must bridge the proxy architecture from §3.1.3 into the phase transition specification.

**PROPOSED FIX:**
*Old text (§7.2, currently):*
> **Trigger:** σ_A(d,t) > σ_critical for at least one mastery candidate.

*New text:*
> **Trigger:** σ̂_A(d,t) > σ_critical for at least one mastery candidate, where σ̂_A is the training-time proxy from §3.1.3 (causal intervention probe, Eq. 3c, or augmentation consistency, Eq. 3d). External verification uses the evaluation-time SGG proxy (Eq. 3b) at the nearest checkpoint. The differential signal indicating imminent Phase 2 entry is dσ̂_A/dt > 0 sustained over at least two consecutive probe intervals Δt_probe, observable as a narrowing OOD gap in the training-time proxy trajectory.

**JUSTIFICATION:** This fix connects the existing proxy architecture (§3.1.3) to the phase transition specification without introducing new equations or variables. The proxy definitions (Eqs. 3b, 3c, 3d) are already formally specified and validated at Checkpoints A and B. Adding the differential criterion `dσ̂_A/dt > 0` provides a concrete observable signal for external verification. No other section is affected — the proxy definitions remain unchanged, and the σ_critical derivation (Eq. 51) is untouched.

**SAFETY NOTE:** This fix does NOT modify Equation 51 (σ_critical derivation), Equation 28 (σ_A ODE), or any V2.0/V3.0 ODE. It adds a prose bridge between existing proxy definitions and the phase trigger statement. Protected elements (Eq. 28, Table 1, §7.1–7.5 trigger statements) are not altered in substance — only annotated with proxy references.

---

### VARIANT B
**Issue #:** 7
**Tag:** [P]
**Section targeted:** §7.2 + Appendix A (new equation A.16)
**Scope:** structural
**DIAGNOSIS:** The Phase 2 transition lacks a formalised differential criterion. The current trigger is a point condition (`σ_A > σ_critical`) rather than a trajectory condition. External verification requires detecting *when* the threshold is crossed, not merely that it has been crossed. A derivative-based entry test would provide the differential signal missing from the current specification.

**PROPOSED FIX:**
*Add to §7.2 after the trigger statement:*
> **Phase 2 Entry Test (external verification).** Define the Phase 2 entry signal as the inflection point in the schema coherence proxy trajectory:
> $$\frac{d\hat{\sigma}_A(d,t)}{dt} \bigg|_{t^*} > 0 \quad \text{AND} \quad \frac{d^2\hat{\sigma}_A(d,t)}{dt^2} \bigg|_{t^*} > 0 \tag{51a}$$
> where t* is the candidate transition time. The first condition confirms σ_A is increasing; the second confirms the rate of increase is accelerating (schema crystallisation is self-reinforcing). Both are computable from the Tier 1 proxy time series at probe intervals.

*Add to Appendix A as Equation A.16:*
> $$\Phi_{\text{Phase2}}(d,t) = \mathbb{1}\left[\frac{d\hat{\sigma}_A}{dt} > \delta_{\text{min}} \quad \text{AND} \quad \frac{d^2\hat{\sigma}_A}{dt^2} > 0\right] \tag{A.16}$$
> where δ_min is a minimum rate threshold (calibration parameter, recommended value: 0.02 per probe interval). Φ_Phase2 = 1 indicates Phase 2 entry has been detected.

**JUSTIFICATION:** This fix introduces a formal differential criterion grounded in the mathematical structure of the σ_A ODE (Eq. 28). The second-derivative condition captures the self-reinforcing nature of schema crystallisation — when σ_A crosses σ_critical, the α_A·P_A coupling produces accelerating growth. This is a structural property of the ODE, not an arbitrary threshold. The fix is consistent with all existing equations: it uses σ̂_A (already defined), references the probe interval (already specified), and does not modify σ_critical derivation.

**SAFETY NOTE:** This fix does NOT modify Equation 51 (σ_critical), Equation 28 (σ_A ODE), or any protected element. It adds a new observable criterion (Eq. 51a and A.16) that is derived from but independent of the existing ODE system. The original trigger statement (`σ_A > σ_critical`) is preserved as the theoretical condition; the entry test is the external verification method.

---

### VARIANT C
**Issue #:** 7
**Tag:** [P]
**Section targeted:** §7.2 + §9 (Falsifiable Predictions)
**Scope:** local
**DIAGNOSIS:** The Phase 2 transition is not connected to any falsifiable prediction. If Phase 2 entry produces a qualitative shift in agent behaviour (as the phase structure claims), this shift should be detectable in benchmark performance trajectories. Adding a falsifiable prediction linking Phase 2 entry to a measurable performance inflection would provide both external verification and empirical testability.

**PROPOSED FIX:**
*Add to §7.2 after the "Characterisation" paragraph:*
> **Observable Phase 2 Signature.** Phase 2 entry produces a characteristic acceleration pattern in the OOD performance trajectory. Specifically, when σ_A crosses σ_critical, the systematic generalisation gap (SGG) begins narrowing at an accelerating rate:
> $$\frac{d}{dt}\left[\text{Acc}_{\text{OOD}}(d,t)\right] \bigg|_{t_{\text{Phase2}}} > \frac{d}{dt}\left[\text{Acc}_{\text{OOD}}(d,t)\right] \bigg|_{t_{\text{Phase1}}}$$
> This acceleration is externally verifiable from benchmark time series and serves as the differential proxy signal for Phase 2 entry.

*Add as Prediction 9 in §9:*
> ### Prediction 9 — Phase 2 Entry Inflection
> **Claim:** The transition from Phase 1 to Phase 2 produces a measurable inflection in the OOD accuracy trajectory, detectable as an acceleration in dAcc_OOD/dt that coincides with σ̂_A crossing σ_critical.
> **Measurement:** Track Acc_OOD over training checkpoints; compute dAcc_OOD/dt via finite differences. Phase 2 entry is detected when dAcc_OOD/dt exceeds its Phase 1 baseline by ≥ 2 standard deviations for ≥ 3 consecutive checkpoints.
> **Falsification:** No statistically significant acceleration in dAcc_OOD/dt is observed when σ̂_A crosses σ_critical (p > 0.05, change-point detection).

**JUSTIFICATION:** This fix links the phase transition to a concrete, falsifiable empirical claim. The OOD acceleration signature is a direct consequence of the σ_A ODE dynamics — when σ_A > σ_critical, the α_A·P_A coupling term dominates, producing faster σ_A growth, which narrows the OOD gap via the SGG proxy (Eq. 3b). Adding this as Prediction 9 makes Phase 2 entry empirically testable without modifying any existing equation.

**SAFETY NOTE:** This fix does NOT modify any existing equation. It adds a new observable signature (prose definition) to §7.2 and a new prediction (Prediction 9) to §9. Protected elements are untouched. The fix is additive — it extends the phase structure and prediction set without altering existing content.

---

### VARIANT D
**Issue #:** 7
**Tag:** [P]
**Section targeted:** §7.2 + §6.1 (Reliability)
**Scope:** structural
**DIAGNOSIS:** The reliability function R_A(B,f,t) in §6.1 provides a variance-based quality measure for benchmarks but is not connected to phase detection. If Phase 2 entry produces a qualitative shift in performance consistency (schema-coherent agents show more stable OOD performance), the reliability trajectory could serve as a secondary differential signal. This creates a bridge between the V3.0+ reliability extension and the phase structure.

**PROPOSED FIX:**
*Add to §7.2 after the trigger statement:*
> **Secondary Phase 2 Signal — Reliability Inflection.** Schema crystallisation stabilises OOD performance, producing a measurable increase in benchmark reliability R_A(B,f,t) (Eq. 48) when σ_A crosses σ_critical. The Phase 2 entry is secondarily confirmed by:
> $$\frac{dR_A(B,f,t)}{dt} \bigg|_{t^*} > 0 \quad \text{for OOD-targeting benchmarks} \tag{51b}$$
> This signal is weaker than the primary SGG acceleration (Eq. 51a) but provides independent corroboration via a different measurement channel. Recommended verification: both SGG acceleration (primary) and reliability increase (secondary) should be observed within the same checkpoint window.

*Add a sentence to §6.1 after Eq. 48:*
> R_A also serves as a secondary phase detection signal: schema crystallisation (Phase 2 entry) produces reliability inflection in OOD-targeting benchmarks, detectable as dR_A/dt > 0 sustained over multiple scoring runs.

**JUSTIFICATION:** This fix connects two existing formal objects — the Phase 2 trigger and the reliability function — without introducing new variables. The theoretical basis is sound: schema-coherent representations produce more consistent OOD performance because principled encoding is less sensitive to surface-feature variation than statistical encoding. Higher σ_A → more stable Acc_OOD → lower score variance → higher R_A. This chain uses only existing definitions.

**SAFETY NOTE:** This fix does NOT modify Equation 48 (R_A definition), Equation 51 (σ_critical), or any ODE. It adds a secondary detection criterion (Eq. 51b) and a cross-reference sentence to §6.1. Protected elements are untouched. The fix is purely additive.

---

### VARIANT E
**Issue #:** 7
**Tag:** [P]
**Section targeted:** §7.2 + §3.1.3 (Proxy architecture)
**Scope:** systemic
**DIAGNOSIS:** The fundamental problem is that the Phase 2 trigger references a latent variable (σ_A) while the proxy architecture provides only indirect estimates. A systemic fix would replace the latent-variable trigger entirely with a compound observable trigger that uses only measurable quantities. This requires reframing the Phase 2 criterion as a conjunction of observable conditions rather than a single latent threshold.

**PROPOSED FIX:**
*Replace the Phase 2 trigger in §7.2:*
> **Trigger:** Phase 2 begins when the following compound observable condition is satisfied:
> $$\hat{\sigma}_A(d,t) > \hat{\sigma}_{\text{critical}} \quad \text{AND} \quad \frac{d\hat{\sigma}_A(d,t)}{dt} > 0 \quad \text{AND} \quad \text{Acc}_{\text{OOD}}(d,t) > \theta_{\text{OOD}} \tag{51c}$$
> where:
> - σ̂_A is the Tier 1 training-time proxy (Eq. 3c or 3d)
> - σ̂_critical is σ_critical calibrated against the proxy scale (see Appendix A.4 calibration procedure)
> - θ_OOD is the minimum OOD accuracy threshold indicating non-trivial compositional capacity (recommended: 0.15 for SCAN-class benchmarks)
>
> All three conditions are observable from training-time proxy data and benchmark results. No internal agent state is required.
>
> *Theoretical basis:* σ̂_A > σ̂_critical corresponds to σ_A > σ_critical (by proxy calibration). dσ̂_A/dt > 0 confirms schema coherence is actively increasing (not merely above threshold by measurement noise). Acc_OOD > θ_OOD confirms the agent has achieved non-trivial compositional capacity (σ_A > 0 is insufficient if absolute OOD performance is near-chance).

*Add to §3.1.3 after the operational convention paragraph:*
> **Phase transition calibration.** The proxy scale σ̂_A must be calibrated to the latent scale σ_A for phase detection. Calibration procedure: (1) compute σ̂_A at each evaluation checkpoint using Eq. 3c/3d; (2) compute σ_A using the SGG ground truth (Eq. 3b); (3) fit a monotonic mapping σ̂_critical = f(σ_critical) via regression over the calibration history. The mapping should be updated when proxy parameters change.

**JUSTIFICATION:** This systemic fix eliminates the dependence on latent variables for phase detection. The compound trigger (Eq. 51c) uses only quantities that are computable from training-time proxy data (σ̂_A, dσ̂_A/dt) and benchmark results (Acc_OOD). The three-condition conjunction provides robustness: any single condition could be satisfied by measurement noise, but all three simultaneously indicate genuine Phase 2 entry. The fix is consistent with existing ODE dynamics — the compound trigger is designed to detect the same latent threshold (σ_A > σ_critical) that the original trigger specifies.

**SAFETY NOTE:** This fix does NOT modify Equation 28 (σ_A ODE), Equation 51 (σ_critical derivation), or any protected element. It reframes the trigger as a compound observable condition (Eq. 51c) and adds calibration guidance to §3.1.3. The theoretical trigger (σ_A > σ_critical) is preserved in the σ_critical derivation; only the operationalisation in §7.2 is changed.
