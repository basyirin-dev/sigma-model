# Issue #22 — Variant Proposals (MODE 1: FAST AGENT)

## Issue Summary

**Issue #:** 22
**Tag:** Tier 1A [HACKATHON PRIORITY]
**Description:** The benchmark reliability function can theoretically return negative values when the coefficient of variation exceeds one, violating the requirement for bounded validity.

**Core problem:** Equation 48 defines:
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

This is $1 - CV^2$ where $CV = \sigma/\mu$ is the coefficient of variation. When $CV > 1$ (i.e., $\text{Var}_k > E[\text{score}]^2$), the reliability $R_A$ becomes negative. This violates the requirement that $R_A \in [0,1]$, as it enters Equation 49 as a multiplicative factor:

$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \cdot R_A(B,f,t) \tag{49}$$

A negative $R_A$ would flip the sign of the validity function — a nonsensical result for a validity metric. Section 6.2 also prescribes $R_A > 0.75$ as a minimum threshold, implying bounded non-negativity. The Appendix (A.13) provides a minimum reliability threshold formula that also assumes $R_A \in [0,1]$.

---

### VARIANT A
**Issue #:** 22
**Tag:** Tier 1A
**Section targeted:** §6.1.1 (Equation 48)
**Scope:** local

**DIAGNOSIS:** The reliability function $R_A = 1 - \text{Var}/E[\text{score}]^2$ is mathematically unbounded below — it can take arbitrarily negative values when the coefficient of variation exceeds 1. This occurs when score variance exceeds the squared mean, which is common for low-mean/high-variance scoring distributions (e.g., binary tasks with ~50% accuracy and high variance across repetitions). The function needs a floor at zero to preserve its role as a validity multiplier.

**PROPOSED FIX:**

*Old Equation 48:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

*New Equation 48:*
$$R_A(B,f,t) = \max\left(0, \; 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2}\right) \tag{48}$$

*Add prose after Equation 48:* "The $\max(0, \cdot)$ floor ensures $R_A \geq 0$. Benchmarks where coefficient of variation exceeds 1 receive $R_A = 0$, indicating unreliability sufficient to invalidate the benchmark regardless of other validity components. This is consistent with the minimum threshold $R_A > 0.75$ in §6.2: benchmarks with $CV > 0.5$ already fail the reliability criterion."

**JUSTIFICATION:** This is the minimal fix that resolves the boundedness violation without changing the functional form of the reliability measure. The coefficient-of-variance-based definition is preserved; only its domain is clipped. Benchmarks with $CV > 1$ receive zero reliability, which is the correct behaviour: such extreme variance indicates the benchmark is producing essentially random scores, and $V_A = 0$ is the appropriate validity assignment. The minimum threshold table in §6.2 remains unchanged since $R_A > 0.75$ already requires $CV < 0.5$.

**SAFETY NOTE:** This fix deliberately does NOT change Equation 49, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5 phase triggers, or the Burnell et al. citation. It modifies only Equation 48 by adding a non-negativity floor. The noise reduction protocol (§6.1.3) and minimum validity thresholds (§6.2) are unaffected.

---

### VARIANT B
**Issue #:** 22
**Tag:** Tier 1A
**Section targeted:** §6.1.1 (Equation 48) — replace with bounded functional form
**Scope:** structural

**DIAGNOSIS:** The CV-based definition $R_A = 1 - CV^2$ is unbounded below because the subtraction from 1 has no floor. An alternative bounded form that preserves the core intuition (high variance → low reliability) is the inverse-variance weighting form: $R_A = \frac{1}{1 + CV^2}$. This is always in $(0,1]$ — strictly positive, bounded above by 1, and smoothly penalises increasing variance without ever becoming negative or zero.

**PROPOSED FIX:**

*Old Equation 48:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

*New Equation 48:*
$$R_A(B,f,t) = \frac{1}{1 + \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2}} = \frac{E[\text{score}_A(B)]^2}{E[\text{score}_A(B)]^2 + \text{Var}_k(\text{score}_A^k(B))} \tag{48}$$

*Add prose:* "This form is the precision-weighted reliability: $R_A$ is the ratio of squared mean to squared mean plus variance. When variance is zero (perfectly consistent scores), $R_A = 1$. When variance equals the squared mean ($CV = 1$), $R_A = 0.5$. As variance grows, $R_A \to 0$ asymptotically — high-variance benchmarks are penalised smoothly without crossing into negative values. The form is equivalent to $R_A = 1/(1 + CV^2)$."

**JUSTIFICATION:** The inverse form $\frac{1}{1 + CV^2}$ is a standard bounded reliability measure in psychometrics (related to signal-to-noise ratio). It preserves the core property: $R_A$ decreases monotonically with increasing variance. It improves on the original in three ways: (1) $R_A \in (0,1]$ always — no negative values possible; (2) smooth asymptotic approach to zero rather than hard crossing; (3) symmetric interpretation: $R_A = 0.5$ at $CV = 1$ (equal signal and noise). The minimum threshold $R_A > 0.75$ in §6.2 now corresponds to $CV^2 < 1/3$, i.e., $CV < 0.577$, which is close to the original threshold.

**SAFETY NOTE:** This fix does NOT change Equation 49, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It replaces Equation 48 with a bounded functional form. The minimum thresholds in §6.2 require minor reinterpretation (the $CV$ boundary shifts slightly) but the qualitative prescription is unchanged.

---

### VARIANT C
**Issue #:** 22
**Tag:** Tier 1A
**Section targeted:** §6.1.1 (Equation 48) — replace with test-retest correlation
**Scope:** structural

**DIAGNOSIS:** The CV-based reliability measure conflates two distinct psychometric concepts: (1) absolute reliability (consistency of raw scores) and (2) relative reliability (rank-order consistency across repetitions). The CV form measures absolute reliability but is unbounded. Test-retest Pearson correlation — the standard psychometric reliability measure — is naturally bounded in $[-1, 1]$ and, for valid benchmarks, in $[0, 1]$. Replacing the CV form with test-retest correlation resolves the boundedness issue while adopting the field-standard reliability definition.

**PROPOSED FIX:**

*Old Equation 48:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

*New Equation 48:*
$$R_A(B,f,t) = \text{Corr}\left(\text{score}_A^{k}(B), \; \text{score}_A^{k'}(B)\right) \tag{48}$$

where $k$ and $k'$ are distinct repetition indices, and the correlation is computed across all benchmark items. For $k=5$ repetitions, compute the average pairwise Pearson correlation across the $\binom{5}{2} = 10$ repetition pairs.

*Add prose:* "Test-retest reliability measures rank-order consistency: do items that score high on one repetition also score high on another? This is the standard psychometric definition (Nunnally & Bernstein, 1994). The Pearson correlation is bounded in $[-1, 1]$; for a valid benchmark, $R_A \in [0, 1]$ with $R_A = 1$ indicating perfect consistency and $R_A = 0$ indicating no consistency. Negative values indicate systematic reversal, which would invalidate the benchmark."

**JUSTIFICATION:** Test-retest correlation is the field-standard reliability measure in psychometrics, with established interpretive benchmarks ($R > 0.7$ = acceptable, $R > 0.8$ = good, $R > 0.9$ = excellent). Adopting this form resolves the boundedness issue by construction and aligns the H-Bar reliability definition with established measurement theory. The minimum threshold $R_A > 0.75$ in §6.2 corresponds to "acceptable-to-good" reliability in standard psychometric interpretation. The noise reduction protocol (§6.1.3) remains applicable: majority voting and temperature=0 reduce item-level variance, which increases test-retest correlation.

**SAFETY NOTE:** This fix does NOT change Equation 49, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It replaces Equation 48 with the psychometrically standard reliability definition. The minimum threshold $R_A > 0.75$ in §6.2 is preserved with a cleaner interpretation.

---

### VARIANT D
**Issue #:** 22
**Tag:** Tier 1A
**Section targeted:** §6.1.1 + §6.1.2 + §6.2 (reliability definition + validity integration + thresholds)
**Scope:** systemic

**DIAGNOSIS:** The reliability boundedness problem is a symptom of a deeper issue: the current $R_A$ definition conflates absolute and relative reliability, and the validity function (Equation 49) uses $R_A$ as a multiplicative factor without accounting for the interaction between reliability and other validity components. A systemic fix redefines reliability as a properly bounded quantity and adjusts the validity integration to handle edge cases (zero reliability, zero mean scores) explicitly.

**PROPOSED FIX:**

**Part 1 — §6.1.1, new Equation 48:**

*Old:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

*New:*
$$R_A(B,f,t) = \begin{cases} \displaystyle\frac{1}{1 + \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2}} & \text{if } E[\text{score}_A(B)] > 0 \\[8pt] 0 & \text{if } E[\text{score}_A(B)] = 0 \end{cases} \tag{48}$$

*Add prose:* "Reliability is the precision-weighted ratio $R_A = 1/(1 + CV^2)$, bounded in $(0, 1]$ for positive-mean scores. The edge case $E[\text{score}] = 0$ (benchmark where all scores are zero) is assigned $R_A = 0$, indicating complete unreliability. This form is equivalent to $R_A = \mu^2/(\mu^2 + \sigma^2)$ — the signal-to-noise ratio in the variance decomposition."

**Part 2 — §6.1.2, update Equation 49 with edge-case handling:**

*Old:*
$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \cdot R_A(B,f,t) \tag{49}$$

*New:*
$$V_A(B,f,t) = CI(B,f) \cdot FD(B) \cdot DG(B) \cdot R_A(B,f,t) \tag{49}$$

*Add prose:* "Since $R_A \in [0, 1]$ by construction (Equation 48), and $CI, FD, DG \in [0, 1]$ by their respective definitions, the validity function $V_A \in [0, 1]$. A benchmark with $R_A = 0$ has $V_A = 0$ regardless of other components — reliability is a necessary condition for validity."

**Part 3 — §6.2, update threshold table:**

| Component | Minimum | Rationale |
|-----------|---------|-----------|
| $CI(B,f)$ | > 0.60 | Target faculty must be dominant predictor |
| $FD(B)$ | > 0.55 | No single format may dominate |
| $DG(B)$ | > 0.40 | Must span multiple difficulty levels |
| $R_A(B,f,t)$ | > 0.75 | Precision-weighted reliability; corresponds to $CV < 0.577$ |
| **$V_A(B,f,t)$** | **> 0.20** | **Combined minimum** |

*Add prose:* "The $R_A > 0.75$ threshold corresponds to $CV^2 < 1/3$, i.e., $CV < 0.577$. This ensures the benchmark's score variance is less than 57.7% of the mean — a conservative reliability requirement consistent with psychometric standards for experimental instruments."

**JUSTIFICATION:** This systemic fix addresses the boundedness issue, the edge case (zero mean), and the integration with the validity function in a single coherent revision. The precision-weighted form $1/(1 + CV^2)$ is bounded by construction, monotonically penalising variance, and interpretable as signal-to-noise ratio. The edge-case handling prevents division-by-zero errors in downstream computations. The threshold table is updated with an explicit $CV$ interpretation. The validity function (Equation 49) is unchanged but now has a formal guarantee that $V_A \in [0,1]$ from the boundedness of all four factors.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It modifies Equations 48 and 49 (adding boundedness guarantee), updates §6.2 threshold table with $CV$ interpretation, and adds edge-case handling. The noise reduction protocol (§6.1.3) is unaffected.

---

### VARIANT E
**Issue #:** 22
**Tag:** Tier 1A
**Section targeted:** §6.1.1 + §12 (Appendix A.8) — add boundedness proof and conditional definition
**Scope:** local

**DIAGNOSIS:** The current reliability definition lacks a formal boundedness proof. The Appendix (A.13) provides a minimum reliability threshold but does not prove that $R_A$ is bounded. A minimal fix adds a boundedness proof to the Appendix and restates Equation 48 with an explicit domain condition that prevents negative values from arising in well-defined cases.

**PROPOSED FIX:**

**Part 1 — §6.1.1, update Equation 48 with domain condition:**

*Old:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \tag{48}$$

*New:*
$$R_A(B,f,t) = 1 - \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \quad \text{for} \quad \frac{\text{Var}_k(\text{score}_A^k(B))}{E[\text{score}_A(B)]^2} \leq 1 \tag{48}$$

*Add prose:* "The reliability function is defined when the coefficient of variation satisfies $CV \leq 1$. Benchmarks where $CV > 1$ are assigned $R_A = 0$ by convention — such extreme variance indicates the benchmark is producing essentially random scores. See Appendix A.8 for the boundedness argument and the relationship between $R_A$ and the minimum reliability threshold."

**Part 2 — Appendix A.8 (after existing content), add boundedness argument:**

```
### A.8a Reliability Boundedness

**Claim:** For benchmarks satisfying $CV \leq 1$, $R_A(B,f,t) \in [0, 1]$.

**Proof:** By definition, $R_A = 1 - CV^2$ where $CV = \sigma/\mu$.
When $CV \leq 1$: $CV^2 \leq 1$, so $R_A = 1 - CV^2 \geq 0$.
When $CV = 0$: $R_A = 1$ (perfect reliability).
When $CV = 1$: $R_A = 0$ (unreliable).

For $CV > 1$: $R_A < 0$, which violates the validity requirement.
By convention, benchmarks with $CV > 1$ are assigned $R_A = 0$.

**Relationship to minimum threshold:** The requirement $R_A > 0.75$
(§6.2) implies $CV^2 < 0.25$, i.e., $CV < 0.5$. This ensures
score variance is less than 25% of the squared mean — a
conservative reliability floor.

**Edge case:** When $E[\text{score}] = 0$, the CV is undefined.
Assign $R_A = 0$ by convention (zero-mean benchmarks are unreliable).
```

**JUSTIFICATION:** This fix preserves the original functional form ($R_A = 1 - CV^2$) while adding the formal boundedness argument that was missing. The domain condition ($CV \leq 1$) is stated explicitly in Equation 48, and the Appendix provides the proof. Benchmarks with $CV > 1$ are handled by convention assignment ($R_A = 0$), which is the correct behaviour: such benchmarks are unreliable. This is the minimal fix that adds formal rigour without changing the mathematical structure.

**SAFETY NOTE:** This fix does NOT change Equation 49, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It modifies Equation 48 (adding domain condition) and adds Appendix A.8a (boundedness proof). The functional form $R_A = 1 - CV^2$ is preserved; only its domain is explicitly bounded.
