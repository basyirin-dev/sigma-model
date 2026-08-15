# integration_map.md

| Variable | Introduced | Interacts With | Coupling Mechanism | Equation | Consistency Verified |
|---|---|---|---|---|---|
| αA(d,t) | V2.0 | σA(d,t), R_A^{surface}(d,t) | Gates σA growth via multiplicative term in ODE 28; eroded by surface-reward pressure via ODE 29 | 28, 29, A.4 | YES |
| R_A^{surface}(d,t) | V2.0 | αA(d,t) | Surface-reward pressure — erodes attentional fidelity via $ζ_α · R_A^{surface} · α_A$ term in ODE 29. Formal definition: $1 - H(Y\|S)/H(Y)$ (Eq. 29a). Proxy: $1 - \hat{α}_A = 1 - \text{Acc}_{OOD\text{-struct}}/\text{Acc}_{ID}$ (Eq. 29b). Calibration procedure in Appendix A.4. | 29, 29a, 29b, A.4 | YES |
| ΞA^P(t) | V2.0 | δ_A^{relative}(d*,t) | Planning relaxes toward (1 − δ_A^{rel}); rigid when depth low, relaxed near frontier. Eq. 36a (bifurcation-aware step). | 36, 36a, A.6 | YES |
| ΞA^I(t) | V2.0 | σA(d*,t), σ_critical | Inhibition: 0.9 below σ_critical, 0.4 above. Step function at bifurcation connects V1.0 σ_critical to V2.0 executive control. Eq. 36b. | 36, 36b, A.6 | YES |
| ΞA^F(t) | V2.0 | |M_A(t)|, Ψ_A^{max}(t) | Flexibility: 0.3 when |M_A|<2 and Ψ=0; 0.9 otherwise. Grows with mastery and intersection activity. Eq. 36c. | 36, 36c, A.6 | YES |
| M̂A(d,t) | V2.0 | σA(d,t), Ω_AI | Self-model of schema coherence; ζA = M̂A - σA. Nagumo boundedness proven (§4.4.2). Steady-state: M̂A* = σA/(1 + Ω_AI/Π_7) ≤ σA (Eq. 39a). Overconfidence transient; underconfidence at equilibrium under sustained Ω_AI. | 39, 39a, A.5 | YES |
| ζA(d,t) | V2.0 | M̂A, σA, PA(d,t), αA, Ω_AI | Calibration error; distorts principled practice. Derived ODE (Eq. 38a): restoring force (−ν_M ζ_A) opposes overconfidence; AI bypass terms inflate ζ_A. Bounded in [−1,1] by Nagumo on M̂A. | 38, 38a, A.5a | YES |
| μAB(d,t) | V2.0 | σA, σB, ϕ | Schema legibility: A's σA readable by B | 31 | YES |
| τA(B,d,t) | V2.0 | σB(d,t) | A's model of B's schema; ζAB = τA - σB | 32, 33 | YES |
| ΣA,B(d1,d2,t) | V2.0 | μAB, μBA, ϕ | Collective schema field (cross-agent ΨA) | 34 | YES |
| ΘA(d,m1,m2,t) | V3.0 | σA(d,m,t), ω(m1,m2) | Cross-modal schema transfer | 42 | YES |
| ω(m1,m2) | V3.0 | ΘA | Modal structural similarity coefficient | 41 | YES |
| VA(B,f,t) | V3.0 | CI, FD, DG, RA | Benchmark validity composite | 47, 49 | YES |
| CI(B,f) | V3.0 | VA | Construct isolation score | 44 | YES |
| FD(B) | V3.0 | VA | Format diversity score | 45 | YES |
| DG(B) | V3.0 | VA | Difficulty gradient score | 46 | YES |
| RA(B,f,t) | V3.0+ | VA | Precision-weighted reliability: $R_A = 1/(1 + CV^2)$, bounded in $[0,1]$ by construction. Edge case: $E[\text{score}]=0 \implies R_A=0$. Validity guarantee: $R_A \in [0,1] \implies V_A \in [0,1]$. $CV$ interpretation: $R_A > 0.75 \iff CV < 0.577$. | 48, 49 | YES |
| HB(B) | V3.0+ | Submission protocol | Human baseline specification | 50 | YES |
| Prediction 6b (Issue #9) | V3.0+ | σA, δA, Eq. 3b, Appendix A.4 | σA/δA dissociation test under meta-learning; uses three-condition battery for falsification | 3b, A.4 | YES |
| λc eff = λc·(1−γσ·σA) | V1.0 (resolved Issue #4) | σA, λc, rA | Schema-mediated decay reduction; three-mechanism architecture (engagement/schema/frontier) | 7, 12, A.1 | YES |
| rA(d,t) | V1.0 | τA (elapsed time) | Engagement decay — purely temporal, no σA dependence | 8 | YES |
| σA(d,t) definition ↔ §8 Protocol | V1.0 (resolved Issue #1) | σA, SGG, Acc_OOD, Acc_In | Proxy identification (Eq. 3b) integrates §3.1.3 definition with §8/Appendix A.4 measurement protocol. σA = Acc_OOD/Acc_In operationalisation closes definitional gap. | 3, 3b, A.4 | YES |
| σA(d,t) training-time proxy (Issue #2) | V1.0 (resolved Issue #2) | σA, Eq. 3b, Eq. 3c, Eq. 3d | Two-tier proxy architecture: Tier 1 (training-time) = causal intervention probe (Eq. 3c) or augmentation consistency (Eq. 3d); Tier 2 (evaluation-time) = SGG (Eq. 3b). Operational convention: σ̃A used as operative value in ODE system; σ̂A used for validation at checkpoints. §10.1 updated with two-tier description. | 3, 3b, 3c, 3d, 10.1 | YES |
| §10.6 Training Protocols (Issue #10) | V3.0+ (resolved Issue #10) | σA, δA, αA, PA, hackathon tracks | Three-protocol structure for independent variable manipulation: P1 (σA↑ at fixed δA via structure-preserving augmentations), P2 (δA↑ at fixed σA via capacity increase), P3 (joint increase via standard training). Hackathon implementation links P1/P2 to all five tracks. Dependencies: §9 (uses protocols for predictions), §8 (references benchmark splits), Appendix A.4 (augmentation families). | 10.6, 9, 8, A.4 | YES |
| J (Jacobian dominance) | V3.0+ | δ_A, σ_A, α_A | Column norm of linearised coupled system; identifies growth-limiting variable via dominance criterion v† = argmax ‖J_{:,v}‖·(1−v*). Proposition: α_A binding in Phase 1 when σ_A ≈ 0. | A.16, A.17 | YES |
| Prediction 6c (Issue #28) | V3.0+ | σA, δA, Eq. 3b, Appendix A.4 | Distribution engineering dissociation test; uses three-condition battery for falsification of Patel et al. (2022) claim. Tests c ∈ T_train (trained-composition recall) vs. c ∉ T_train (structural recombination). | 3b, A.4 | YES |
| Lake & Baroni (2023) engagement (Issue #29) | V3.0+ (resolved Issue #29) | σA, δA, PA, Prediction 6b, §2.2 | Lake & Baroni (2023) meta-learning dissociation explicitly engaged via Prediction 6b enhancement: added "Existing evidence" section with MAML-on-SCAN numbers (59.4% lexical vs. 8.1% structural) and mechanistic explanation via σA ODE. Connected to §2.2 gap statement and hackathon track_learning.md (§5a MAML-on-SCAN protocol). | 6b, 3b, A.4 | YES |
| Multiplicative ΨA justification (Issue #11) | V3.0+ (resolved Issue #11) | ΨA, qA, Eq. 21, Prediction 6, non-compensation property | Added empirical justification paragraph in §3.5 grounding the multiplicative √(q₁·q₂) form in its falsifiable Prediction 6 and non-compensation property. Added justification paragraph in §9, Prediction 6, identifying non-compensation as the key structural property that makes the geometric mean the unique symmetric, bounded form. Cross-references between §3.5 and §9 strengthened. | 21, 6, 20 | YES |
| Prediction 6d (Issue #30) | V3.0+ (resolved Issue #30) | σA, δA, Eq. 3b, Appendix A.4 | Training regime optimisation dissociation test; uses three-condition battery for falsification of Han & Pad'o (2024) claim. Empirical evidence: 78.3% vs 62.1% on COGS systematic, structural gain only 3.3pp. Distinguishes from Predictions 6b (meta-learning) and 6c (distribution engineering). | 3b, A.4 | YES |
