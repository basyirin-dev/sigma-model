# Reviewer Response — P11.5 (Eight External Assessments → Dispositions)

**Manuscript**: *The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation*
**Target venue**: TMLR (also arXiv preprint)
**Date**: P11.5, 2026-08-16 (post Phase 11 verification, commit `4a41a04`)
**Inputs**: four peer-review-style assessments (A5–A8) + four strategic responses (S9–S12), provided externally
**Status**: All text-level findings actioned; experiment-requiring findings deferred with rationale; predictive-validation probe run under a pre-committed rule (decision record in §6)

---

## 1. Verdict Spread Across the Eight Assessments

| Assessment | Verdict / Stance | Core message |
|---|---|---|
| A5 (review) | **Accept** (descriptive-framework paper) | Honesty and Table 3 are strengths; "So what?" is the residual risk |
| A6 (review) | **Major revision** | Replicate on a real benchmark; fix the proxy; clarify R₀ mapping; otherwise strong |
| A7 (review) | **Accept / strong revision** | Refine GCA; micro-foundations; benchmark breadth; solid as descriptive framework |
| A8 (review) | **Narrow and strengthen** (scorecard: conceptual 8/10, validation 5–6/10) | Make descriptive-vs-mechanistic the organising principle; equivalence wording; model comparison |
| S9 (strategy) | Defer experiments; **elevate predictive validation to mandatory** (Pivots A/B/C) | The probe is the only shield against Occam's-razor reviewers |
| S10 (strategy) | Defer; **skip the probe** | Identifiability risk; claim-lock scope creep; time vs reward |
| S11 (strategy) | Defer; **skip the probe**; precise text prescriptions (A/B/C) | "Statistically indistinguishable", not "matches"; logistic-defense; proxy as key finding |
| S12 (strategy) | Defer; **skip probe by default** (conditional if quick); insists on "no detectable difference" | Claim hierarchy; soften novelty; sharpen conclusion |

**Consensus across all eight**: (i) keep the descriptive claim level; (ii) do not add benchmark/architecture replications before submission; (iii) fix the p = 0.99 "matches/equivalent" language; (iv) soften the §2 "None models…" novelty claim. **Split**: whether to run cross-condition predictive validation (S9 yes/mandatory; S10/S11 no; S12 conditional).

---

## 2. Consolidated Findings → Dispositions

### A. Equivalence language for p = 0.99 — **ACTIONED**
- **Sources**: A8 Priority 5, S11-A, S12 (insists), A5/A6/A7 (indirectly).
- **Finding**: "matches/equivalent" implies formal equivalence; p = 0.99 is a failure to detect a difference, not proof of equality.
- **Fix applied**: abstract, Contribution 2, §7 headline, and Table 3 row 5 now read "no detectable difference" with the exact statistics (Δ = −0.01 pp, Welch t(24.5) = 0.01, p = 0.99, d = −0.00) and an explicit clause "we do not claim formal equivalence: no equivalence test was pre-registered."

### B. Novelty overclaim in §2 — **ACTIONED**
- **Sources**: A8 §13, S12 (Edit 3).
- **Finding**: "None models schema coherence as a dynamical variable…" is a very strong literature claim.
- **Fix applied**: both occurrences now read "To our knowledge, none models…" / "to our knowledge, none models…".

### C. Stage-1 proxy degeneracy — **ACTIONED (two passes)**
- **Sources**: A6, A7, A8 §7, S9 Pivot B, S11-C, S12 §6.
- **Finding**: GCA ≈ 0.95 at random init makes the crossing-time test degenerate and the fused proxy invalid as a leading indicator; the proxy is a measurement limitation, not a theory falsification; RGA tracks exposure; a working training-time proxy is an open instrumentation challenge.
- **Fix applied (Phase 11 + P11.5)**: §7 already reported the degeneracy honestly and explained why GCA is trivially high at init; the new §7 "Proxy status" paragraph explicitly states the fused proxy is *not a valid leading indicator in its current form*, frames it as a sensitivity failure rather than model falsification, elevates RGA as an *exposure tracker*, and states the open instrumentation challenge. Construct-vs-proxy separation made explicit in §3.1.2 (σ_A construct / σ̃_A estimate / σ̂_A diagnostic).

### D. Occam's-razor / curve-fitting objection — **ACTIONED (prose) + PROBE (record)**
- **Sources**: A8 §11 (phase-2 needs evidence), S9 Pivot C, S11-B.
- **Finding**: on a single trajectory the OOD signature may look logistic; the model must state why the ODE is more than a curve fit.
- **Fix applied**: new §3.4 "Against a purely logistic reading" — the model's content is phase-space geometry (stable E_S trap with σ̇_A < 0, E_C attractor, stability exchange at R₀ = 1), which a fitted sigmoid cannot represent; formal model selection listed as new Open Question 4 in §8.3.
- **Probe**: see §6 — the empirical check was run; the outcome does not enter the paper (pre-committed rule).

### E. "So what?" / moot-curriculum critique — **ACTIONED (framing)**
- **Sources**: A5, A6, A7, S9 Pivot A.
- **Finding**: if a plain fixed-weight loss matches the σ-modulated curriculum, the scheduling has no algorithmic utility.
- **Fix applied**: §7 now frames the σ-scheduling as a *causal probe* ("tests whether dynamic coupling between the loss and the coherence state is necessary to escape the trap… the answer is no") and adds the mechanism sentence (compositional-loss exposure lowers Ω_SL, pushing R₀ above 1, Proposition 4) — answering A6's "why does comp loss work within the model" and converting the negative result into a contribution.

### F. H-Bar benchmark transparency — **ACTIONED**
- **Sources**: A8 §12 (why H-Bar, difference from SCAN, generation, splits, availability), A6.
- **Fix applied**: §6 now states why H-Bar (SCAN-like but enumerable recombination grammar; OOD compositional by construction), programmatic generation from the gate config, committed generator/splits/scripts, raw tables in the companion.

### G. Per-seed trajectories — **ACTIONED**
- **Sources**: A8 §10, A7.
- **Finding**: aggregate endpoints are insufficient for a dynamics paper; per-seed trajectories should be available.
- **Fix applied**: Table 1 caption corrected to point to full per-seed trajectories in the companion (the mean±CI figure was previously mis-cited as per-seed).

### H. Construct validity of σ — **PARTIALLY ACTIONED; remainder OPEN (by design)**
- **Sources**: A8 §6, S12 §7.
- **Finding**: what observable uniquely corresponds to σ? Latent-variable problem; uniqueness vs grokking/SLT open.
- **Fix applied**: §3.1.2 measurement sketch (P11) + explicit construct/estimate separation (P11.5).
- **Not actioned (deliberately)**: construct uniqueness remains "open" in Table 3 — the assessments agree this is the correct status; resolving it needs the proxy-validation programme (P13), not a rhetorical fix.

### I. RQ2 — model comparison against competing dynamical descriptions — **DEFERRED + Open Question**
- **Sources**: A8 §10, S12 §9.
- **Finding**: the paper has not shown the ODE describes trajectories better than plausible alternatives.
- **Disposition**: added as Open Question 4 (§8.3). The P11.5 probe (§6) demonstrates why formal discrimination is genuinely hard: the σ_A dynamics are logistic-family in projection, so curve-shape AIC comparison cannot separate the model from an S-curve — consistent with the "phenomenological description" claim. Full model comparison is a P13 follow-up item, not a submission blocker.

### J. Benchmark/architecture replication (SCAN/COGS; larger models) — **DEFERRED**
- **Sources**: A6, A7, A8 §23.
- **Disposition**: the paper explicitly marks generality as "open" (Table 3, §6 proof-of-concept scope) and sequences the N = 500 protocol across SCAN/COGS/PCFG-SET as next step (i) in the Conclusion. Running it pre-submission would change the paper's scope and claim level; all eight assessments support deferral.

### K. Predictive validation (fit on one condition, predict another) — **PROBE RUN, RULE APPLIED**
- **Sources**: A8 §22 (the single experiment they'd add), S9 (mandatory), S10/S11 (skip), S12 (conditional).
- **Disposition**: run as a time-boxed internal probe with a pre-committed entry rule; see §6 for the decision record.

### L. Formal criterion for "phase-2 acceleration" — **PRE-ADDRESSED (verified)**
- **Sources**: A8 §11.
- **Finding**: "phase" must not be metaphorical; need a formal criterion.
- **Status**: §5.1 pre-registers segmented regression with Δβ = 0.02 and reports per-arm breakpoints with CIs (§7); phases are defined by the bifurcation structure (§4), not retrospectively. No change needed; the probe re-verified the breakpoints from raw data (§6).

### M. Descriptive-vs-mechanistic claim hierarchy — **PRE-ADDRESSED + sharpened**
- **Sources**: A8 §§3, 20; S12.
- **Status**: Conjecture 1, Table 3, and §8 already separate model-proven / assumption-proven / empirically-supported / open. The Conclusion was additionally sharpened (P11.5): "The observed Phase~2 signature is therefore a *descriptive* property of the model's phase structure, not evidence that σ_A is a leading causal variable."

### N. Conclusion sharpening around the negative result — **ACTIONED**
- **Sources**: S12 Edit 6.
- **Fix applied**: see M — the descriptive-signature sentence now leads the conclusion's status paragraph.

---

## 3. Review-A8 Scorecard → Action Mapping

| A8 dimension | Score (A8) | Action / disposition |
|---|---|---|
| Problem importance | 8.5/10 | No change needed |
| Conceptual originality | 8/10 | No change needed |
| Theoretical ambition | 9/10 | No change needed |
| Theoretical validation | 5.5/10 | **Raised by**: Pivot C defense (phase-space content made explicit), Open Question 4, probe record; not raised to "mechanistic" (claim lock) |
| Experimental design | 6.5/10 | **Raised by**: H-Bar provenance, per-seed pointer, causal-probe framing of the gate |
| Statistical support | 6/10 | **Raised by**: "no detectable difference" precision, no-equivalence clause, per-comparison stats already present |
| Construct validity of σ | 5/10 | **Partially raised**: measurement sketch + construct/estimate separation; uniqueness remains open (correct status) |
| Writing | 8/10 | Slight improvement via tightened wording |
| Narrative coherence | 7.5/10 | **Raised**: causal-probe narrative makes the negative results cohere as a contribution |
| Publication potential | 8/10 | Deferred items (replication, model comparison, proxy validation) sequenced to P13 |

---

## 4. What Was Changed (P11.5, `paper/manuscript.tex`)

1. §2: novelty claims softened ("To our knowledge…") — two spots.
2. Abstract, Contribution 2, §7, Table 3: "no detectable difference" + no-equivalence clause for p = 0.99.
3. §7: σ-scheduling framed as a causal probe; Ω_SL/R₀ mechanism sentence.
4. §7: new "Proxy status" paragraph (proxy invalid as leading indicator; RGA exposure tracker; open instrumentation challenge).
5. §3.4: new "Against a purely logistic reading" paragraph.
6. §8.3: new Open Question 4 (model selection).
7. §6: H-Bar provenance and SCAN-relation notes.
8. Table 1 caption: per-seed trajectories correctly located in the companion.
9. §3.1.2: construct (σ_A) vs estimates (σ̃_A, σ̂_A) separation.
10. Conclusion: Phase-2 signature explicitly descriptive, not causal.

---

## 5. Deferred Items (with rationale) — P13 follow-up roadmap

| Item | Source | Why deferred |
|---|---|---|
| N = 500 replication across SCAN/COGS/PCFG-SET | A6, A7, A8 | New empirical objective; would change paper scope and claim level; already next step (i) |
| Formal RQ2 model comparison | A8, S12 | Probe shows trajectory-shape discrimination is impossible by construction (σ dynamics are logistic-family in projection); a P13 methodological problem, listed as Open Question 4 |
| Proxy redesign / construct validation | A6, A7, A8, S11 | Requires new instrumentation research; uniqueness stays "open" in Table 3 |
| Microscopic SGD→ODE derivation | A7, A8 | Unproven Conjecture 1 by design; closing it is a research programme, not a revision |
| Predictive-validation as a paper claim | A8, S9 | Probe run internally; entry rule not satisfied (see §6); the rate-ordering evidence is recorded for the companion |

---

## 6. Predictive-Validation Probe — Decision Record

**Pre-committed entry rule** (before the run): the probe's result enters the paper only if (i) the reduced model fits in-sample at least as well as logistic/Gompertz, (ii) it predicts a held-out arm's breakpoint τ within its CI, and (iii) parameters are identifiable.

**Method** (scratch, gitignored `output/p11probe/`, run 2026-08-16 on `archive/gate-results`, 60 runs): per-run segmented regression over the eval grid (the paper's procedure); logistic and Gompertz fits with AIC on per-arm mean trajectories; per-seed bootstrap on the logistic rate k; rate-ordering test.

**Results**:
- **Q1 (verification)**: breakpoints reproduce the paper's numbers — fixed 148.3 (paper 148, CI [125,175]), mult 340.0 (340, [300,408]), add 541.7 (542, [493,591]); baseline ill-determined (median 50, CI [34,1139]). ✅
- **Q2 (identifiability)**: AIC is arm-dependent — Gompertz beats logistic on fixed-weight (ΔAIC ≈ 50), logistic beats Gompertz on additive/multiplicative (ΔAIC ≈ 19–22), tie on baseline. No single S-curve family dominates; because the model's σ_A dynamics are logistic-family in projection, ODE-vs-logistic *shape* discrimination is impossible by construction.
- **Q3 (ordering)**: logistic rate k is exactly monotone in effective compositional pressure — fixed 0.0210 > mult 0.0115 > add 0.0067 — matching τ_fixed < τ_mult < τ_add. The model's structural (cross-condition) ordering prediction holds.
- **Q4 (identifiability of the projected rate)**: per-seed k CIs are tight and disjoint across arms (fixed [0.0173, 0.0266], mult [0.0101, 0.0132], add [0.0063, 0.0074]).

**Rule application**: condition (i) is not met (no clean ODE-vs-logistic discrimination — by construction, not by failure); condition (ii) is not met (a full fit-on-A-predict-B τ test requires a schedule→parameter map the paper never quantified, and deriving one now would be a new modeling claim). **Outcome: the probe does not enter the manuscript.** Private value: (a) the paper's headline numbers are re-verified; (b) the rate-ordering result is genuine structural evidence for the descriptive model and is recorded for the companion/P13; (c) the arm-dependent S-curve winner (Gompertz on fixed-weight) is a small empirical counter to a blanket "just a logistic" reading, worth noting in rebuttal if it arises; (d) the identifiability finding confirms that Open Question 4 and the Pivot C framing are the correct public posture.

**Cost**: < 1 day, zero GPU.

---

## 7. Residual Submission Risks (unchanged by this pass)

1. A reviewer reading the ODEs as unfalsifiable curve-fitting (mitigated by Pivot C + Open Question 4; probe shows the objection cannot be fully refuted at the trajectory level).
2. Single-benchmark, single-architecture scope (explicitly "open"; pre-registered N = 500 as next step).
3. Proxy degeneracy (now stated as an open instrumentation challenge; RGA as the constructive component).
4. Reviewer-assignment luck on the "So what?" question (mitigated by the causal-probe framing).

No changes were made to the locked claim level; the title and the descriptive framing are unchanged.

---

*End of P11.5 reviewer-response document.*
