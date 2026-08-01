# Paper 02 — Inter-Rater Agreement (Task 5.4)

**Date**: 2026-08-01
**Screeners**: S1 (primary classifier) vs S2 (independent implementation), both run over all 1,435 records at title stage

## Title Screening

- 3-way Cohen's kappa: **0.138**
- Binary hard-decision kappa (n=869): **0.738**

## Abstract Screening

- 3-way Cohen's kappa: **0.446**
- Binary hard-decision kappa (n=437): **0.725**

## Interpretation

κ < 0.80 at title stage triggered criteria refinement (5.4.3): CG lexicon tightened to compositional-only terms, non-compositional override added (domain generalization, OOD detection, corruption, flat minima), spurious Uncertain paths converted to Exclude. Remaining disagreements are genuine borderline cases (robotics manipulation, OOD-with-application), resolved per 5.5.3 by default to full-text review.
