# Phase 04 — Mechanism-Gate Experiment

**Duration**: 5–7 days (compute on Kaggle T4 ~4–5 h)
**Deadline**: TBD (user-scheduled Kaggle run)
**Dependencies**: Phases 01, 03 (novelty audit)
**Output**: `paper/planning/gate-result.md` + committed configs/scripts; claim level locked
**Executor**: Agent (port, notebook prep, analysis) + **user** (Kaggle GPU run)
**Status**: 🔶 In progress — harness ported to `code/sigma_align` + smoke-verified (4 arms, CPU); Kaggle notebook ready; awaiting the user's T4 gate run

## Purpose

Produce the discriminating evidence that determines the paper's claim level, per the
consultations' decision rule:

- **σ̃_A (measured) precedes OOD improvement AND fixed-weight does not match ODE-guided**
  → **mechanistic** framing ("σ-trap as a dynamical mechanism")
- **OOD improves but measured σ does not precede it**
  → **phenomenological/descriptive** framing ("dynamical model of σ-trap behaviour")
- **Neither survives** → stop; rework the model before any rewrite

**Calibration facts (already measured, 2026-08-16):** this CPU-only box runs the pilot at
~1.3 s/step → the full gate (4 arms × n=15 × 2000 steps ≈ 60 runs) would take ≈ 43 h here.
The original pilot ran on a Kaggle T4 at ≈ 5 min/run → ≈ 4–5 h. **Decision (user): run on
Kaggle GPU; agent prepares the notebook and analyses the results.**

**Archived-data finding (zero compute, already measured):** the pilot's *scheduled* σ knob
does **not** lead OOD — σ-leads-fraction = 0.00 across all conditions (σ crosses 0.15 at
step 200–500, after OOD rose at step 50–100; σ_t→OOD_{t+1} partial correlations negative).
Consequence: the leading-indicator test must use a **measured** Stage-1 proxy, not the
scheduled knob. **Decision (agent, per user's 'choose the best strategy'): implement a
minimal measured Stage-1 proxy (GCA + RGA) and include the σ-before-OOD test in the gate.**

## Tasks & subtasks

1. **Port the pilot harness to `code/sigma_align`**
   - Convert `archive/experiments/h-bar-experiment.ipynb` (13 cells) to
     `code/experiments/run_pilot.py`; fix `from sigma.…` → `from sigma_align.…`
   - Parameterize via argparse + YAML (`code/experiments/configs/gate.yaml`, ADR-0004):
     `--condition {baseline,fixed_weight,additive,multiplicative}`, `--n-runs`,
     `--n-timesteps`, `--eval-every`, `--seed`, `--outdir`
   - Keep the pilot's benchmark generator, `HBarTransformer` (add `encode()` for probing),
     training loop, and per-run pkl schema (`metrics.step/acc_id/acc_ood/sigma_tilde/phase/…`)
   - Seed discipline: `torch.manual_seed(run_id * 42 + 7)`; deterministic flags (CC.2.1)
2. **Implement the Stage-1 proxy (measured σ̃_A)** — `code/sigma_align/monitoring/proxy.py`
   - GCA — gradient-composition alignment: cosine between main-task loss gradient and
     compositional-probe loss gradient over a fixed parameter slice (output_proj + first
     encoder layer + embedding), mapped to [0,1]
   - RGA — representational-geometry alignment: mean same-operator cosine similarity minus
     random-pair cosine similarity over mean-pooled encoder states (operator labels from
     target action tokens: X2/X3/OPPOSITE/AFTER/AND/AROUND)
   - Fused `sigma_tilde = 0.5*(GCA + RGA)`; per-run min-max normalisation applied in analysis
   - Full GCA/RGA/AC + two-stage calibration (Props 3.6–3.7) stays in the companion (P10)
3. **Add the `fixed_weight` arm** (the discriminating control)
   - Constant-weight compositional loss (`total += λ · L_comp` every `comp_every` steps),
     NO σ modulation, NO phase-gated curriculum; σ tracked as diagnostic only
   - Design note: fixed-weight gets maximal comp exposure (from step 0) — a deliberately
     strong plain-compositional-loss baseline; record this in gate-result.md
4. **Kaggle notebook** — `code/experiments/kaggle-gate.ipynb` (mirrors the archived notebook
   structure: /kaggle/working paths, output persistence, 4 arms × n=15 × 2000 steps,
   `eval_every=25` for finer early resolution of the leading test; saves `all_results.pkl`
   + `summary.json` + per-run proxy trajectories)
   - Include a short README/instructions block: how to import, expected runtime (~4–5 h T4),
     what to download back
5. **Reproduction sanity check** (before the user commits 4–5 GPU hours)
   - Short CPU smoke (1 run × ~150–300 steps per arm) to verify the port runs all 4 arms
     without error and produces sensible trajectories; compare early shape against the
     archived `all_results.pkl`
   - Optionally a 1-run full-length CPU run for exact parity (≈ 45 min) — only if needed
6. **User runs the full gate on Kaggle** (T4): download `all_results.pkl` + `summary.json`
   back into `archive/gate-results/` (gitignored)
7. **Analysis** — `code/experiments/analyze_gate.py` producing `paper/planning/gate-result.md`:
   - Fixed-weight vs ODE-guided: per-seed OOD trajectories, CIs, Welch t-tests,
     per-benchmark (per-split) effect sizes; report raw distributions (no pooled d alone)
   - Leading-indicator: measured σ̃_A crossing time vs OOD-rise time; partial correlation
     σ̃_A,t → OOD_{t+1} controlling OOD_t, training loss, and parameter norm
   - Competing-variable check: does measured σ̃_A predict final OOD beyond loss/norm/ID
   - Apply the decision rule (above); write the verdict + evidence into gate-result.md
8. **Commit** configs, scripts, analysis, and gate-result.md (raw results stay out of git)
   — `[I][C][Δ]` / `[V][C][Δ]` as appropriate

## Expected outputs

- `code/experiments/run_pilot.py`, `code/experiments/configs/gate.yaml`,
  `code/experiments/kaggle-gate.ipynb`, `code/experiments/analyze_gate.py`
- `code/sigma_align/monitoring/proxy.py`
- `paper/planning/gate-result.md` (verdict + evidence tables)
- `archive/gate-results/` (raw, gitignored)

## Decisions (forks that gate this phase)

1. Compute allocation — **user: Kaggle GPU** (agent preps notebook, analyses results)
2. Leading-indicator scope — **agent: implement minimal GCA+RGA proxy**, include the test
3. If the gate comes back negative (neither discriminator survives): **halt the rewrite**,
   report to the user, rework the model before P06

## Exit criteria

- Gate notebook runs end-to-end on Kaggle; `gate-result.md` records the decision-rule verdict
- Claim level (mechanistic / phenomenological / stop) locked and reflected in P05's blueprint
