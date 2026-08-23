# ADR-005: Mechanism-Gate Experimental Protocol & Design Specification

**Date:** 2026-08-23  
**Status:** Approved  
**Phase:** P03  
**Deciders:** Principal Investigator & AI Agent  

---

## 1. Context & Problem Statement
In Phase 02 (ADR-001, ADR-003), we mathematically derived the critical compositional pressure law $\lambda_{\text{crit}} = b_C / a_C$ and scored the risk that deep Transformer generalization might follow a smooth dose-response curve ($H_{\text{null}}$) rather than a sharp supercritical separatrix ($H_0$) as the highest-risk theoretical assumption (Risk Score = 15).

To satisfy the core non-negotiable governance rule (*evidence gates ambition*), Phase 03 is designated as the **Mechanism Gate**. Before any manuscript writing or large-scale multi-benchmark sweep commences, we must execute a rigorous, high-throughput empirical test designed to validate or falsify the presence of the supercritical separatrix and late-onset destabilization.

---

## 2. Decision Drivers
- **Driver 1 (Statistical Power & Rigor):** The experiment must employ an ensemble size ($n = 30$ independent seeds per condition) sufficient to distinguish a sharp step function ($k \ge 15.0$) from a smooth sigmoid with statistical confidence ($p < 0.01$).
- **Driver 2 (Exact Reproducibility):** Zero data leakage between training and OOD test distributions, deterministic seed pinning (`seed = run_id * 42 + 7`), and declarative YAML configuration.
- **Driver 3 (Computational Feasibility):** The minimal gate suite (450 total runs) must complete within a reasonable compute budget (~3.5 hours on standard GPU hardware) using a lean 2-layer seq2seq Transformer architecture.

---

## 3. Minimal Gate Experimental Specifications

### 3.1 Model Architecture: 2-Layer Seq2Seq Transformer
- **Embedding Dimension ($d_{\text{model}}$):** 128
- **Attention Heads ($n_{\text{heads}}$):** 4 (head dimension = 32)
- **Feedforward Dimension ($d_{\text{ff}}$):** 512
- **Encoder Layers ($n_{\text{layers}}$):** 2
- **Decoder Layers ($n_{\text{layers}}$):** 2
- **Dropout:** 0.1
- **Positional Encoding:** Sinusoidal with learnable projection
- **Representation Hook:** Mean-pooled encoder representations extracted via `model.encode(src)` for downstream CKA geometry monitoring.
- **Total Parameters:** $\approx 9.3 \times 10^5$ parameters (934K trainable parameters).

### 3.2 Benchmark Specification: H-Bar Zero-Leakage Compositional Suite
The H-Bar suite generates compositional action sequences composed of primitive tokens, directional modifiers, and conjunctions.
- **Training Set ($\mathcal{D}_{\text{train}}$):** $N_{\text{train}} = 10,000$ examples drawn from single primitives and basic linear modifiers (e.g. `walk left`, `twice jump`).
- **In-Distribution Test ($\mathcal{D}_{\text{ID}}$):** $N_{\text{ID}} = 2,000$ examples with identical length distribution and seen primitive pairings.
- **Out-of-Distribution Test ($\mathcal{D}_{\text{OOD}}$):** $N_{\text{OOD}} = 2,000$ examples containing strictly unseen composite structures (e.g. `twice jump left`, `opposite jump right`, conjunctions, triple compositions).
- **Substitution Equivalence Probe Set ($\mathcal{D}_{\text{comp}}$):** $N_{\text{comp}} = 2,000$ pairs generated under primitive substitution for computing equivalence loss $\mathcal{L}_{\text{comp}}$.
- **Zero-Leakage Invariant:** Explicit hash-set verification confirms $\mathcal{D}_{\text{train}} \cap \mathcal{D}_{\text{OOD}} = \emptyset$.

### 3.3 Training & Optimization Protocol
- **Optimizer:** Adam ($\eta = 10^{-3}, \beta_1 = 0.9, \beta_2 = 0.999, \epsilon = 10^{-8}$)
- **Gradient Clipping:** Max norm $1.0$
- **Batch Size:** 64
- **Total Steps:** 2,000 steps per run
- **Loss Function:** $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{task}} + \lambda \mathcal{L}_{\text{comp}}$
- **Metric Logging Frequency:** Every 25 steps (`step`, `loss_train`, `loss_comp`, `acc_id`, `acc_ood`, `cka_rga`, `param_norm`).

---

## 4. Experimental Arms & Grid Configuration

A total of **450 independent training runs** ($n = 30$ seeds per cell) are structured into two complementary arms:

```
                            ┌────────────────────────────────────────────────────────┐
                            │    Phase 03 Mechanism Gate Protocol (450 Runs)        │
                            └────────────────────────────────────────────────────────┘
                                         │                              │
                    ┌────────────────────┴───────────┐      ┌───────────┴────────────────────┐
                    ▼                                ▼      ▼                                ▼
┌─────────────────────────────────────────────────────────┐ ┌─────────────────────────────────────────────────────────┐
│ Arm A: Dense λ-Sweep (Step 0 Onset)                     │ │ Arm B: Late-Onset Intervention (λ = 1.0)                │
│ λ ∈ {0.00, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00,   │ │ t_int ∈ {0, 100, 250, 500, 1000 steps}                 │
│      1.50, 2.00}                                        │ │ Purpose: Tests dynamical destabilization of E_S after   │
│ Total: 10 levels × 30 seeds = 300 runs                  │ │          prolonged shortcut entrapment.                 │
│ Purpose: Tests Separatrix Step Sharpness (k ≥ 15.0)     │ │ Total: 5 levels × 30 seeds = 150 runs                   │
└─────────────────────────────────────────────────────────┘ └─────────────────────────────────────────────────────────┘
```

---

## 5. Pre-Registered Decision Criteria (Gate Exit Rules)

The Gate outcome is legally binding and evaluated against three quantitative criteria:

1. **Criterion 1 — Sharp Step-Function Separatrix ($P(\text{escape} \mid \lambda)$):**
   - Escape condition: Run achieves $\text{Acc}_{\text{OOD}} \ge 80\%$ at step 2,000.
   - Logistic change-point fit: $P(\text{escape} \mid \lambda) = \frac{1}{1 + \exp(-k(\lambda - \lambda_{\text{crit}}))}$.
   - **PASS Requirement:** Steepness $k \ge 15.0$ and clear threshold separation:
     $$P(\text{escape} \mid \lambda \le 0.10) < 0.05 \quad \text{and} \quad P(\text{escape} \mid \lambda \ge 0.50) > 0.95$$

2. **Criterion 2 — Late-Onset Destabilization of Trapped State $E_S$:**
   - In the $t_{\text{int}} = 1000$ arm (where models are fully trapped at $E_S$ with $\text{Acc}_{\text{OOD}} \le 50\%$), switching to $\lambda = 1.0$ must achieve final $\text{Acc}_{\text{OOD}} \ge 90\%$ in $\ge 90\%$ of seeds ($27/30$).

3. **Criterion 3 — Supercritical Asymptotic Equivalence:**
   - Pairwise two one-sided tests (TOST) between supercritical arms ($\lambda \in \{0.50, 0.75, 1.00, 1.50, 2.00\}$) must confirm asymptotic equivalence within margin $\pm 2.5\%$ ($p < 0.05$).

---

## 6. Consequences & Traceability
- **Traceability:** Governs empirical evaluation for claims `CLM-003` (Separatrix), `CLM-004` (Late-Onset Recovery), and `CLM-007` (Benchmark Invariance).
- **Binding Constraint:** If the gate passes, Phase 04 experimental design is unlocked. If the gate fails, downstream writing is prohibited.
