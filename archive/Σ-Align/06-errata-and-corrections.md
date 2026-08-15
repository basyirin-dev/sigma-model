# 6. Errata and Corrections

This document records all identified errata, biases, and corrections across both MCDA frameworks.

## 6.1 MCDA V1 (Weighted Sum) Errata

### E1: Criterion 22 Name Inconsistency
- **Issue:** Criterion 22 was named "Epistemic Certainty Ceiling" in the definition block but "Epistemic Ceiling" in the section header.
- **Correction:** Standardized to "Epistemic Certainty Ceiling" throughout.

### E2: Score Transparency
- **Issue:** Physics' 0.852 score was asserted without the full matrix — only 5 of 22 scores were shown, accounting for 0.430 of the total. The remaining 0.422 from 12 unstated criteria at 55% weight was unverifiable.
- **Correction:** Full 22×3 audit trail was published, allowing independent verification.

### E3: Structural Tautology
- **Issue:** The 24% weight on user-defined criteria (Pinnacle + Resource Elasticity) already encodes a preference for theoretical/low-resource fields. The remaining 76% doubly reinforces this (Mathematical Formalizability 9%, Single-PI Feasibility 6%, Reproducibility 6%). The framework is structurally guaranteed to rank theoretical physics at the top.
- **Assessment:** This is not an error — it is honest engineering of the objective function. The weights *are* the decision. The MCDA does not "discover" the best field; it formalizes the optimization parameters.

### E4: Information-Theoretic Circularity
- **Issue:** Criterion 6 (Information-Theoretic Density, 3%) measures "bits of certainty gained per unit of research output" — an information-theoretic metric applied to "Quantum Information Theory" (the Level 3 winner).
- **Assessment:** An inherent feature of applying information-theoretic metrics to a field defined by information theory. The criterion measures Shannon entropy reduction of the natural world, which is universally applicable but semantically resonates most strongly with QIT.

### E5: Hierarchy Monotonicity
- **Issue:** QIT (0.921) > QIC (0.912) > Physics (0.852) appears to violate monotonicity (sub-field scoring higher than parent).
- **Clarification:** This is a **filtering effect**, not an error. Broad domains include sub-fields with poor resource elasticity (Particle Physics, Medical Physics) that drag down the parent's average. Level 2 and 3 filter out infrastructure-heavy sub-fields, isolating local maxima. Scores increase as we narrow because we filter out low-scoring sub-fields.

### E6: Physics Description Inconsistency
- **Issue:** Level 1 winner's description was shortened from "Physics (Classical, Quantum, Relativistic, Condensed Matter, Particle, and Plasma)" to "Physics (Classical, Quantum, Relativistic, etc.)" in the final confirmation.
- **Correction:** Full original description restored.

## 6.2 MCDA V2 (Choquet Integral) Notes

### N1: Framework Complexity vs. Operationalizability
- MCDA V2 introduces significantly greater complexity (MCMC, Choquet integral, IDEA protocol elicitation, hierarchical Dirichlet weights) than V1.
- This complexity is justified by the higher stakes of the decision (civilizational utility) but creates a higher barrier to independent replication.

### N2: Dirichlet Weight Prior Subjectivity
- The hierarchical Dirichlet prior fuses AHP expert judgments with entropy-based variance. The AHP panel composition (20 science policy experts + philosophers of science) introduces a framing effect: different panel compositions would yield different posterior weights. This is transparently modeled via the posterior distribution but remains a structural source of uncertainty.

### N3: Diachronic Projection Model Risk
- The 100-year Bayesian hierarchical projection assumes knowledge accumulation follows a smooth parametric form. Black swan events (e.g., an unaligned AGI appearing within 5 years, or a breakthrough in nuclear fusion rendering energy science obsolete) are captured only through the MCMC uncertainty bands, not through explicit regime-change modeling.

## 6.3 Corrections Applied

| Erratum | Severity | Status |
|:--------|:--------:|:-------|
| E1: Naming inconsistency | Cosmetic | Corrected |
| E2: Score opacity | Moderate | Corrected (full audit trail published) |
| E3: Structural tautology | Observation | Acknowledged, not corrected (by design) |
| E4: Circularity | Observation | Acknowledged, not corrected (inherent) |
| E5: Monotonicity confusion | Clarification | Documented |
| E6: Description inconsistency | Cosmetic | Corrected |
