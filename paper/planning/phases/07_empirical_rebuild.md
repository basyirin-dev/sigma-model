# Phase 07 — Empirical Sections Rebuild

**Duration**: 3–4 days
**Deadline**: after P06
**Dependencies**: P04 gate results, P06 front half
**Output**: complete narrow-manuscript draft (§§10–13)
**Executor**: Agent

## Purpose

Rebuild the empirical story around the gate results with transparent reporting, the
claim-status table, and a proof-of-concept (not confirmation) framing.

## Tasks & subtasks

1. **§10 Empirical Grounding (≈1 pp)** — candid framing: "these experiments test whether
   the model's qualitative predictions are observable in a controlled setting; they do not
   validate generality." State the synthetic-benchmark scope and the n = 15 pilot status
   (with power note: d ≈ 7+ ⇒ >99.9% power for the primary comparisons, reported per-benchmark)
2. **§11 Empirical Validation (≈3–4 pp)** — rebuilt on the P04 3-arm (+fixed-weight) results:
   - Per-seed OOD trajectories, confidence intervals, per-condition and per-split effect
     sizes (no pooled giant d)
   - The fixed-weight comparison as the mechanism evidence (or, if the gate came back
     descriptive: the σ-trap trajectory characterisation instead)
   - Phase-transition timing: predicted vs observed inflection (Prediction 9), segmented
     regression with CI on the breakpoint
   - Competing-variable analysis: measured σ̃_A predicts final OOD beyond loss/norm/ID
     (and beyond sharpness/LLC-style probes where available) — the "not just X" defence
   - Transparency block: seeds, hyperparameters, compute budget, data/code availability
3. **§12 Scope & Open Questions (≈1–1.5 pp)**
   - **Claim-status table**: low-σ equilibrium exists (proven in model) · stability (proven
     under assumptions) · bifurcation (proven under assumptions) · σ predicts OOD
     (empirically supported in pilot) · SGD necessarily produces the σ-trap (not
     established) · σ is a unique construct (open) · generalises across architectures (open)
   - Circularity statement (post-hoc σ̂_A diagnostic); 2–3 open mathematical questions
     (global existence, timescale bounds, stability landscape)
   - Cut: adoption guide, expanded failure modes (companion)
4. **§13 Conclusion (≈0.5 pp)** — no "origin" language; three next steps (pre-registered
   N=500 protocol, direct proxy validation, SGD↔ODE derivation)
5. **Ledger re-check** — every result in the draft maps to a ledger disposition; nothing
   reintroduced from the cut list

## Expected outputs

- §§10–13 rewritten in `paper/manuscript.tex`; full draft assembled

## Decisions

- Claim-level wording everywhere consistent with the P04 gate verdict (no backsliding)
- If the gate failed to discriminate: §11 reports the descriptive account; the paper is
   still written but with the weaker claim — this is a P04 decision already made

## Exit criteria

- Full draft assembled; ledger re-checked (CC.3.7); abstract still pending (P08)
