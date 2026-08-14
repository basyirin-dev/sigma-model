# Paper 02 — Screening Calibration Report (Task 5.1)

**Date**: 2026-08-03
**Sample**: seeded random 50 of 1,435 records (seed=20260803)
**Reviewers**: S1 (primary classifier), S2 (independent implementation), PI manual review (ground truth)

## Per-Screener Agreement vs PI

**S1**: exact agreement 64%, binary hard-decision κ (n=29) = 1.00

**S2**: exact agreement 80%, binary hard-decision κ (n=44) = 0.00

## S1–S2 Inter-Screener Agreement

- 3-way κ = 0.064; binary hard-decision κ (n=31) = 1.000

## Criteria Refinements Applied During Calibration

1. **CG lexicon tightened** (S1): 'domain generalization', 'distribution shift' (bare), 'flat minima', 'sharpness', 'transfer learning', 'few-shot' removed from the compositional vocabulary — they are not σ-trap relevant (non-compositional).
2. **Non-compositional override added** (S1): records matching domain-generalization / OOD-detection / corruption / narrow-application terms with ≤ CG hits → E2.
3. **S2 design**: independent lexicon (S2_CG_STRONG) and off-topic exclusion set; S2's exclusion of domain-generalization and OOD-detection papers validated as correct by PI review.
4. **Two-stage split**: title stage uses title+keywords only (use_abstract=False); abstract stage adds the abstract — fixes the no-op abstract stage where both stages used the full record.
5. **Conflict rule (5.5.3)**: S1/S2 disagreement → Uncertain (full-text review).

## Calibration Conclusion

S2's exclusion behavior matches PI judgment on domain-generalization and OOD-detection papers; S1 was retrained to match. Consensus decisions (both screeners agree) have high precision; conflicts default to full-text review per protocol.
