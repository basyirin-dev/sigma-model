# Supplementary code & data — "The σ-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation"

This archive supports the reproducibility of the mechanism-gate experiment
(Sections 6–7 of the manuscript). All files are anonymized for double-blind review.

## Contents

```
configs/
  gate.yaml                     # gate experiment configuration (all hyperparameters, arms, seeds)
code/
  hbar_data.py                  # H-Bar benchmark generator (SCAN-style grammar)
  hbar_model.py                 # 2-layer, 4-head Transformer used in the gate
  hbar_train.py                 # training harness: baseline / fixed-weight / additive / multiplicative arms,
                                # Stage-1 proxy (GCA+RGA) recording every 25 steps
data/
  gate-results/                 # raw per-run results, one pickle per run (60 runs, 4 arms x 15 seeds)
    <arm>_run<N>.pkl            # metrics: step/loss/acc_id/acc_ood/sigma_tilde/gca/rga/sigma_sched/phase/lr_eff/param_norm/final
    all_results.pkl             # aggregated result container
```

## Reading the data

Each `<arm>_run<N>.pkl` contains a dict with `metrics` (per-25-step lists over 2000
steps: `step`, `loss`, `acc_id`, `acc_ood`, `sigma_tilde`, `gca`, `rga`,
`sigma_sched`, `phase`, `lr_eff`, `param_norm`, `final`) and `config` (`condition`,
`run_id`, `n_timesteps`).

## Notes

- Seed discipline: `seed = run_id * 42 + 7`, deterministic cuDNN flags.
- The full analysis scripts and per-seed tables are described in the companion
  technical report (uploaded separately as supplementary material).
- Licensing: code is released under the same terms as the manuscript (CC BY 4.0).
