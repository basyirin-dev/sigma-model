# 4. Final Hierarchy and Scores

## 4.1 The Complete Evaluation Sequence

The MCDA V2 framework (21-criteria Choquet integral with MCMC propagation) was applied at four nested levels:

### Level 1: Broad Domains (50 evaluated)

| Rank | Domain | Score | 95% CI |
|:----:|:-------|:-----:|:------:|
| 1 | **Artificial Intelligence** | **0.924** | [0.881, 0.956] |
| 2 | Mathematics | 0.881 | [0.852, 0.910] |
| 3 | Energy Science | 0.854 | [0.812, 0.889] |

**Pillar profile for AI:** ($P_E$: 0.82, $P_S$: 0.95, $P_X$: 0.98)

### Level 2: AI Sub-domains (60 evaluated)

| Rank | Sub-domain | Score | 95% CI | Pillars |
|:----:|:-----------|:-----:|:------:|:--------|
| 1 | **AI Safety and Alignment** | **0.962** | [0.930, 0.985] | (0.78, 0.89, 1.00) |
| 2 | **Artificial General Intelligence** | **0.941** | [0.895, 0.970] | (0.85, 0.96, 0.94) |
| 3 | AI for Science (AI4Science) | 0.903 | [0.864, 0.938] | (0.92, 0.95, 0.81) |

### Level 3a: AI Safety Sub-subdomains (50 evaluated)

| Rank | Sub-subdomain | Score | 95% CI | Pillars |
|:----:|:--------------|:-----:|:------:|:--------|
| 1 | **Long-term Existential Safety & Superintelligence Alignment** | **0.971** | [0.948, 0.989] | (0.75, 0.88, 1.00) |
| 2 | Mechanistic Interpretability | 0.948 | [0.921, 0.972] | (0.94, 0.91, 0.93) |
| 3 | Provably Beneficial AI | 0.915 | [0.872, 0.949] | (0.98, 0.85, 0.89) |

### Level 3b: AGI Sub-subdomains (60 evaluated)

| Rank | Sub-subdomain | Score | 95% CI | Pillars |
|:----:|:--------------|:-----:|:------:|:--------|
| 1 | **AGI Safety and Alignment** | **0.974** | [0.946, 0.991] | (0.80, 0.93, 1.00) |
| 2 | Mathematical Foundations of General Intelligence | 0.951 | [0.919, 0.974] | (0.99, 0.86, 0.87) |
| 3 | Universal AI (AIXI and Variants) | 0.918 | [0.876, 0.948] | (0.96, 0.84, 0.85) |

### Level 4a: AI Safety Specializations (50 evaluated)

| Rank | Specialization | Score | 95% CI | Pillars |
|:----:|:---------------|:-----:|:------:|:--------|
| 1 | **CEV and Indirect Normativity** | **0.988** | [0.965, 0.997] | (0.88, 0.95, 1.00) |
| 2 | Embedded Agency and Decision Theory | 0.952 | [0.918, 0.975] | (0.99, 0.84, 0.91) |
| 3 | Formal Verification of Advanced AI Goal Preservation | 0.931 | [0.889, 0.958] | (0.97, 0.88, 0.89) |

### Level 4b: AGI Safety Specializations (56 evaluated)

| Rank | Specialization | Score | 95% CI | Pillars |
|:----:|:---------------|:-----:|:------:|:--------|
| 1 | **Long-Term Agency, Goal Preservation, and Existential Risk Reduction** | **0.987** | [0.965, 0.996] | (0.85, 0.96, 1.00) |
| 2 | Provably Beneficial GI via Formal Methods | 0.961 | [0.930, 0.981] | (0.99, 0.88, 0.91) |
| 3 | Mesa-Optimization and Deceptive Alignment | 0.937 | [0.898, 0.963] | (0.89, 0.92, 0.94) |

## 4.2 Convergent Paths

The two paths — Pure AI Safety and AGI — converge at the deepest level:

| Path | Level 2 | Level 3 | Level 4 |
|:-----|:-------:|:-------:|:-------:|
| **Pure Safety** | AI Safety (0.962) | Long-term Existential Safety (0.971) | CEV (0.988) |
| **AGI → Safety** | AGI (0.941) | AGI Safety & Alignment (0.974) | Long-Term Agency (0.987) |

The scores at Level 4 are statistically indistinguishable ($\Delta = 0.001$, $P(\text{CEV} > \text{LTA}) = 0.535$).

## 4.3 The Optimal Hierarchy

The AGI path is strictly dominant because:
1. **Higher Level 3 score** (0.974 vs 0.971)
2. **Natural integration** with the existing Sigma-Model paper
3. **Choquet synergy bonus** between capability research and safety research
4. **Identical destination** at Level 4

### Final Selection

| Level | Field | Score |
|:-----:|:------|:-----:|
| 1 | Artificial Intelligence | 0.924 |
| 2 | Artificial General Intelligence | 0.941 |
| 3 | AGI Safety and Alignment | 0.974 |
| 4 | Long-Term Agency, Goal Preservation, and Existential Risk Reduction | 0.987 |
| *Terminal* | *Coherent Extrapolated Volition and Indirect Normativity* | *0.988* |
