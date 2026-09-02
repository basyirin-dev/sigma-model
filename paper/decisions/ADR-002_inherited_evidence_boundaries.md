# ADR-002: Inherited Evidence Scope & Epistemic Boundaries

**Date:** 2026-08-23  
**Status:** Approved  
**Phase:** P0.5 / P01  
**Deciders:** Principal Investigator & AI Agent  

---

## 1. Context & Problem Statement
Paper 01 v2 successfully established the macro-dynamical framework of the $\sigma$-trap and demonstrated that static fixed-weight compositional loss achieves asymptotic parity with adaptive curricula ($p = 0.9899$, TOST $\pm 2.5\%$). However, rigorous peer-review assessments (Tanaka & Chen, Vasquez, Williams) identified three crucial limitations:
1. The mapping between loss gradients and the bifurcation threshold ($R_0 > 1$) was posited rather than mathematically derived.
2. The empirical proxy (Gradient Cosine Alignment, GCA) suffered a step-0 $0.95$ initialization artifact due to shared embeddings.
3. The geometric representation manifold lacked a formal coordinate decomposition.

Paper 02 must clearly demarcate what empirical findings are inherited as established premises versus what novel theoretical and empirical contributions must be proven.

---

## 2. Decision Drivers
- **Driver 1 (Epistemic Cleanliness):** Do not re-litigate established findings (e.g., fixed-weight parity, ERM failure gap); focus all empirical compute and mathematical proofs on the unproven phase separatrix.
- **Driver 2 (Reviewer Responsiveness):** Directly resolve the microscopic derivation critique (Vasquez) and bifurcation mechanics critique (Tanaka & Chen).
- **Driver 3 (Measurement Integrity):** Retire the degraded GCA proxy and elevate Centered Kernel Alignment (CKA) and Whitened GCA.

---

## 3. Considered Options
- **Option 1 (Full Re-execution from Scratch):** Re-run all Paper 01 curriculum sweeps across all hyperparameter grids. *(Rejected: Wasteful compute; does not address the theoretical gap).*
- **Option 2 (Pure Theoretical Extension):** Write a purely mathematical paper without new neural network simulations. *(Rejected: Fails the empirical rigor standard of top-tier ML conferences).*
- **Option 3 (Grounded Two-Tier Architecture):** Ingest Paper 01 quantitative baselines as premises, derive $\lambda_{\text{crit}} = b_C / a_C$ from continuous gradient flow, and execute targeted separatrix validation sweeps on deep Transformers. *(Chosen)*

---

## 4. Decision Outcome & Inherited Evidence Boundaries

### 4.1. Inherited Empirical Premises & Grounding:
1. **ERM Generalization Deficit:** Standard empirical risk minimization converges to a stable low-coherence equilibrium $E_S$ with a $44.3\text{ pp}$ deficit ($\text{Acc}_{\text{ID}} = 90.2\%$, $\text{Acc}_{\text{OOD}} = 45.9\%$).
2. **Fixed-Weight Parity:** A static structural penalty ($\lambda = 1.0$) matches adaptive curricula ($t(24.5)=0.013, p=0.9899$, TOST equivalent within $\pm 2.5\%$).
3. **Latency Monotonicity:** Transition latency is strictly ordered by initial pressure ($\hat{\tau}_{\text{fixed}} \approx 148 < \hat{\tau}_{\text{mult}} \approx 340 < \hat{\tau}_{\text{add}} \approx 542$ steps).
4. **CKA Predictive Correlation:** Representational Geometry Alignment (RGA via CKA) significantly correlates with OOD generalization ($r = +0.125, p = 0.005$).
5. **GCA Failure Dynamics:** Uncentered GCA exhibits $g_A(t=0) \approx 0.95$ due to shared input embedding dominance on intermediate parameters $\mathbf{w}_{\text{int}}$ prior to feature specialization, making prospective crossing-time tests degenerate.
6. **Arm-Dependent Trajectory Geometry:** S-curve trajectories follow asymmetric Gompertz curves under fixed weight ($\Delta\text{AIC} \approx 50$) and symmetric Logistic curves under curricula ($\Delta\text{AIC} \approx 20$), proving that the $\Sigma$-Model ODE unifies cross-regime behavior under a single phase-space geometry.

### 4.2. Novel Scope & Commitments for Paper 02:
1. **Analytical Derivation:** Prove that continuous gradient flow over orthogonal shortcut and schema subspaces yields a transcritical bifurcation at $\lambda_{\text{crit}} = b_C / a_C$ (Theorem 1).
2. **Separatrix Gate:** Empirically demonstrate a sharp phase boundary $\hat{\lambda}_{\text{crit}}$ in deep Transformer escape probabilities during Phase 03.
3. **Whitened Instrumentation:** Validate Whitened Gradient-Cosine Alignment (WGCA) and CKA as uncorrupted training-time order parameters.

### 4.3. Explicitly Deferred Open Questions (Paper 03/04):
1. **Time-Dependent Domain Expansion (OQ-01 / CLM-010):** Global existence proofs under general non-autonomous moving frontiers $\dot{\Delta}(t) \ge f_{\text{learn}}\eta(1)T_A - \mu_c^{\text{eff}}\Delta(t)$.
2. **Nonlinear Timescale Bounds (OQ-02 / CLM-011):** Analytical stiffness bounds for IMEX-RK integrators as $\sigma_A \to 1$.
3. **Phase-Space Model Discrimination Framework (OQ-03 / CLM-012):** Developing non-isomorphic statistical tests to discriminate multidimensional phase-space bifurcation geometry from 1D empirical curve fits.

---

## 5. Compliance & Traceability
- **Ledger Impact:** Anchors claims **CLM-001** through **CLM-007** as active and **CLM-008** through **CLM-012** as deferred in `paper/planning/ledger.md`.
- **Standards Cross-Reference:** Complies with **CC.1.1** (provenance), **CC.2.1** (solver tolerances), and **CC.3.3** (tripartite claim separation).

