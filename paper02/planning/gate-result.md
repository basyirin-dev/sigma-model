# Phase 03 — Mechanism-Gate Result

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)  
**Date:** [Pending P03 Execution]  
**Verdict:** **[PENDING EVALUATION]**  
**Results Source:** `paper02/experiments/YYYY-MM-DD_gate/`  

---

## 1. Pre-Registered Decision Criteria

> Criteria quoted verbatim from the P02.5 pre-registration (`planning/preregistration.md` §1–2, which itself matches `phases/P03_GATE.md` Task 3.3). Evaluation is scored against the pre-registration only.

- **Criterion 1 — Sharp Step-Function Escape (primary):** escape := $\text{Acc}_{\text{OOD}} \ge 80\%$; fit $P(\text{escape} \mid \lambda) = \frac{1}{1 + \exp(-k(\lambda - \lambda_{\text{crit}}))}$. **PASS iff** $k \ge 15.0$ and $P(\text{escape} \mid \lambda \le 0.10) < 0.05$ and $P(\text{escape} \mid \lambda \ge 0.50) > 0.95$.  
  **Status:** [Pending]
- **Criterion 2 — Late-Onset Destabilization of $E_S$:** for $t_{\text{int}} = 1000$ runs (trapped at step 1000, $\text{Acc}_{\text{OOD}} \le 50\%$), switching on $\lambda = 1.0$ reaches final $\text{Acc}_{\text{OOD}} \ge 90\%$ in $\ge 90\%$ of seeds.  
  **Status:** [Pending]
- **Criterion 3 — Supercritical Asymptotic Equivalence:** pairwise TOST equivalence among $\lambda \in \{0.5, 0.75, 1.0, 1.5, 2.0\}$ within margin $\pm 2.5\%$ ($p < 0.05$, Bonferroni across 10 pairs).  
  **Status:** [Pending]

---

## 2. Quantitative Summary Table (n = 30 seeds per cell)

| Condition (λ) | Mean OOD ± Std | Median | 95% CI | Escape Fraction | Inflection τ (steps) |
|---|---|---|---|:---:|:---:|
| λ = 0.00 (Baseline) | — | — | — | — | — |
| λ = 0.05 | — | — | — | — | — |
| λ = 0.10 | — | — | — | — | — |
| λ = 0.20 | — | — | — | — | — |
| λ = 0.30 | — | — | — | — | — |
| λ = 0.50 | — | — | — | — | — |
| λ = 0.75 | — | — | — | — | — |
| λ = 1.00 | — | — | — | — | — |
| λ = 1.50 | — | — | — | — | — |
| λ = 2.00 | — | — | — | — | — |

---

## 3. Binding Downstream Constraints
*(To be populated upon gate evaluation)*
