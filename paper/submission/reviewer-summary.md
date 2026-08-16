# How the Paper Changed — Summary for Reviewers

**Title**: The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation
*(One page; anonymized. Full finding-by-finding dispositions are recorded in the project's internal review notes — not shipped with the submission.)*

This manuscript is a resubmission in a new venue after a JAIR desk rejection
(2026-07-15: exposition/notation, overbroad claims, scope). It is not a revision of a
previously reviewed paper; it is a deliberately narrow paper written to the rejection's
grounds. For reviewers comparing against earlier versions of this line of work, the
changes are as follows.

## 1. Scope: from a five-faculty framework to a two-variable mechanism

- **Before**: a broad framework spanning parametric depth, schema coherence, breadth,
  attentional fidelity, and metacognitive/executive variables, with multi-domain
  machinery and eight extended predictions.
- **Now**: the two-variable core only — parametric depth $\delta_A$ and schema coherence
  $\sigma_A$ — one flagship prediction (the Phase-2 inflection, Prediction 9), and a
  four-arm mechanism-gate experiment. The extended framework (breadth, attention,
  metacognition, multi-domain navigation, predictions 1–8, hypotheses 6.1–6.3, M1) is
  preserved in a separate arXiv companion technical report, referenced as complementary
  material; the paper is self-contained and does not depend on it.

## 2. Framing: from mechanism-adjacent to explicitly phenomenological

- **Before**: the connection between SGD and the posited dynamics was implicit.
- **Now**: the model is stated as *posited, not derived*; the SGD↔ODE mapping is
  **Conjecture 1**, an unproven modelling assumption. The claim level is locked as
  descriptive. Table 3 (claim status) separates: proven in the model / proven under
  assumptions / empirically supported (descriptive) / open.

## 3. The discriminating experiment (mechanism gate)

- Four arms × n = 15: baseline, fixed-weight compositional loss, additive and
  multiplicative σ-modulated curricula.
- Baseline reproduces the trap (ID 90.2%, OOD 45.9%, gap 44.3 pp); all compositional-loss
  conditions close the gap; **the fixed-weight arm shows no detectable difference from the
  σ-modulated curriculum** (98.9% vs 98.9%, Welch p = 0.99, d = −0.00; no formal
  equivalence is claimed); the Phase-2 inflection is observed in every compositional-loss
  condition and not detected in baseline; the measured proxy does not precede OOD
  improvement (partial correlation ≈ 0).

## 4. Honesty about the negative results (kept, not hidden)

- The two negative results — the moot curriculum and the non-leading proxy — are reported
  in the abstract, Section 7, and the conclusion, and are framed as constraining
  evidence: the σ-scheduling is a causal probe (dynamic coupling is not necessary), and
  the proxy failure is a measurement limitation, not a falsification of the construct.

## 5. What changed in the writing (recent passes)

- "Matches/equivalent" for p = 0.99 replaced by "no detectable difference" everywhere,
  with an explicit no-equivalence-test clause.
- Novelty claims softened ("To our knowledge, none models…").
- A dedicated proxy-status discussion (initialisation artefact; RGA as exposure tracker;
  open instrumentation challenge).
- An explicit "against a purely logistic reading" defence (phase-space geometry: stable
  trap $E_S$, attractor $E_C$, stability exchange at R₀ = 1) and an open model-selection
  question stating why trajectory-shape discrimination is not well-posed (the σ_A ODE is
  logistic-family in projection).
- Benchmark provenance (why H-Bar), per-seed trajectories, and a sharpened conclusion
  (the Phase-2 signature is descriptive, not evidence of a leading causal variable).

## 6. What has not changed

- The title, the descriptive claim level, the core mathematics (Lemmas 1–2,
  Propositions 2–4, Appendix C), and the benchmark/architecture scope (one synthetic
  benchmark, one architecture — explicitly open in Table 3, with the N = 500
  pre-registered replication as the stated next step).
