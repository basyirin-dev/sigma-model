# Phase 04 — Mechanism-Gate Result

**Date**: 2026-08-16
**Verdict**: **PHENOMENOLOGICAL** — OOD improves but measured σ̃_A does not precede OOD (dynamic partial-corr test) and fixed-weight matches (or beats) ODE-guided OOD — the dynamical σ-model describes the observed behaviour but is not needed to explain it.

**Results source**: `archive/gate-results` (raw, gitignored)

## 1. Decision-rule evidence

- OOD improves (best ODE-guided arm ≥ 50%): **True**
- σ̃_A (measured) precedes OOD (dynamic partial-corr test, pooled ODE n=30, one-sided t): **False**
- fixed_weight does not match ODE-guided (significantly worse): **False**
- crossing-time test degenerate (σ̃_A starts at its normalized max): 100% of ODE-guided runs

Decision rule applied (phases/04_mechanism_gate.md): OOD improves but measured σ̃_A does not precede OOD (dynamic partial-corr test) and fixed-weight matches (or beats) ODE-guided OOD — the dynamical σ-model describes the observed behaviour but is not needed to explain it.

## 2. Experiment summary

| Arm | n runs | steps/run | eval_every |
|-----|--------|-----------|------------|
| baseline | 15 | 2000 | 25 |
| fixed_weight | 15 | 2000 | 25 |
| additive | 15 | 2000 | 25 |
| multiplicative | 15 | 2000 | 25 |

GPU: Tesla T4 | AMP: True | global_seed: 2024

## 3. Final accuracy (raw per-seed distributions, 95% CI)

### OOD

| Condition | mean±std | median | 95% CI | raw per-seed |
|-----------|----------|--------|--------|--------------|
| baseline | 45.9±4.8 | 45.3 | [43.2, 48.5] | 51.5, 46.6, 37.5, 45.3, 43.6, 49.4, 51.4, 43.6, 40.6, 40.8, 42.8, 46.6, 55.3, 44.1, 48.9 |
| fixed_weight | 98.9±3.6 | 100.0 | [97.0, 100.9] | 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 98.1, 100.0, 100.0, 100.0, 100.0, 86.1, 100.0 |
| additive | 98.9±2.4 | 100.0 | [97.6, 100.3] | 100.0, 100.0, 100.0, 98.7, 100.0, 100.0, 98.9, 100.0, 100.0, 92.0, 100.0, 100.0, 100.0, 94.4, 100.0 |
| multiplicative | 94.0±8.9 | 100.0 | [89.0, 98.9] | 90.8, 97.5, 73.7, 100.0, 100.0, 100.0, 79.0, 100.0, 100.0, 100.0, 89.1, 100.0, 82.8, 100.0, 96.7 |

### ID

| Condition | mean±std | median | 95% CI | raw per-seed |
|-----------|----------|--------|--------|--------------|
| baseline | 90.2±2.2 | 89.7 | [89.0, 91.4] | 94.7, 88.3, 88.4, 91.8, 89.7, 92.7, 91.6, 88.2, 88.4, 89.9, 88.2, 90.2, 93.3, 87.6, 89.5 |
| fixed_weight | 98.1±1.7 | 98.5 | [97.2, 99.0] | 98.2, 99.5, 98.7, 98.9, 99.1, 100.0, 98.5, 96.3, 97.2, 96.6, 99.1, 98.2, 98.3, 93.3, 99.6 |
| additive | 97.8±1.9 | 97.8 | [96.8, 98.8] | 98.6, 100.0, 97.7, 97.8, 99.1, 99.6, 96.8, 97.2, 99.1, 93.0, 97.2, 100.0, 95.5, 96.8, 98.7 |
| multiplicative | 97.3±2.3 | 97.2 | [96.0, 98.5] | 94.9, 96.9, 91.3, 100.0, 99.0, 98.2, 96.4, 97.2, 97.2, 98.2, 96.3, 100.0, 96.0, 100.0, 97.2 |

## 4. Discriminator A — fixed_weight vs ODE-guided (Welch t, per-split)

**Design note**: `fixed_weight` applies a constant-weight compositional loss (`total += λ·L_comp` every `comp_every` steps) with **no σ modulation and no phase-gated curriculum** — maximal comp exposure from step 0. It is a deliberately strong plain-compositional-loss baseline; if it matches the ODE-guided arms, the σ-scheduling adds nothing beyond plain comp loss.

| Pair (OOD) | Δ mean (pp) | t | p | Cohen's d | raw OOD means |
|------------|-------------|-----|-------|-----------|---------------|
| fixed_weight vs additive | -0.01 | 0.013 | 0.9899 | -0.005 | 98.9 vs 98.9 |
| fixed_weight vs multiplicative | -4.98 | 2.011 | 0.0592 | -0.760 | 98.9 vs 94.0 |
| additive vs multiplicative | -4.96 | 2.087 | 0.0532 | -0.789 | 98.9 vs 94.0 |

## 5. Discriminator B — does measured σ̃_A precede OOD?

Two tests. **(a) Crossing-time test** (spec): σ̃_A crossing time = first step where min-max-normalized σ̃_A ≥ 0.5; OOD-rise time = first step where OOD ≥ 0.5 × final OOD. **(b) Dynamic test**: partial correlation σ̃_A,t → OOD_{t+1} controlling OOD_t, loss_t, param_norm_t. The crossing-time test is **degenerate** here: σ̃_A starts at its normalized maximum (GCA ≈ 0.95 on a random-initialised model — the untrained output projection makes any two loss gradients nearly parallel), so the crossing time is 0 by construction. The dynamic test is decisive.

### (a) Crossing-time test

| Condition | σ-leads fraction | % crossing-degenerate | median σ cross | median OOD rise |
|-----------|------------------|-----------------------|----------------|-----------------|
| baseline | 0.67 | 100% | 0 | 25 |
| fixed_weight | 1.00 | 100% | 0 | 50 |
| additive | 1.00 | 100% | 0 | 325 |
| multiplicative | 1.00 | 100% | 0 | 175 |

### (b) Dynamic test (partial correlation) — decisive

| Condition | mean partial corr | fraction runs PC>0 | RGA-only mean PC (one-sided t p) |
|-----------|-------------------|--------------------|---------------------------------|
| baseline | +0.004 | 0.33 | -0.086 (p=0.897) |
| fixed_weight | +0.023 | 0.60 | +0.129 (p=0.000) |
| additive | +0.033 | 0.60 | +0.149 (p=0.000) |
| multiplicative | +0.002 | 0.53 | +0.101 (p=0.011) |

Pooled ODE-guided (n=30): fused σ̃_A partial corr = 0.018 (one-sided t p = 0.236) — **no dynamic leading evidence for the measured σ̃_A**. In contrast, the RGA-only partial corr is +0.125 (mean one-sided p = 0.005): the geometry component significantly predicts OOD_{t+1} **but only in the arms with compositional-loss exposure (including `fixed_weight`, which has no σ dynamics)** — it tracks comp-loss exposure, not the σ-scheduling. GCA is init-dominated (≈ 0.95 at step 0, decaying) and masks this signal in the fused proxy. Model-rework lead for the companion: fix GCA (per-layer normalisation / reweighted fusion) before any mechanistic claim.

RGA normalized half-rise (crossing-time diagnostic): baseline=125, fixed_weight=100, additive=150, multiplicative=125 vs OOD-rise medians above — RGA nominally precedes in the comp-exposure arms, consistent with its positive dynamic test.

Scheduled knob diagnostic (same test on `sigma_sched`, archived finding: leads-fraction = 0.00):

- `baseline`: σ_sched leads fraction = 0.00
- `fixed_weight`: σ_sched leads fraction = 0.00
- `additive`: σ_sched leads fraction = 0.00
- `multiplicative`: σ_sched leads fraction = 0.00

## 6. Competing-variable check — does σ̃_A predict final OOD beyond loss/norm/ID?

Standardized OLS betas of final OOD on [σ̃_A_final, loss_final, param_norm_final, acc_id_final]; Spearman ρ for σ̃_A. n=15 per arm — interpret with caution.

| Condition | β(σ̃_A) | β(loss) | β(param_norm) | β(ID) | ρ(σ̃_A, OOD) | p |
|-----------|---------|---------|---------------|-------|--------------|-----|
| baseline | -0.35 | -0.38 | +0.01 | +0.64 | -0.62 | 0.013 |
| fixed_weight | +0.04 | -0.95 | +0.00 | +0.10 | +0.13 | 0.637 |
| additive | -0.12 | -0.84 | -0.17 | -0.16 | +0.06 | 0.820 |
| multiplicative | -0.06 | -0.26 | -0.25 | +0.43 | +0.15 | 0.591 |

## 7. Next step

Claim level: **phenomenological/descriptive** — proceed to P05 with the σ-trap framed as a dynamical model of behaviour, not a mechanism.

