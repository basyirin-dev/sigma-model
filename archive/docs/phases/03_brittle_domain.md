# Phase 03 — Brittle Domain N=500 Experiment

**Deadline**: 13 Dec 2026
**Dependencies**: Phase 02 (model, training loop, metrics)
**Output**: N=500 runs × 3 conditions, raw result pickles, experiment monitoring dashboard

---

### Task 3.1: OSF pre-registration

- [ ] 3.1.1: Transfer pre-registration draft from Phase 00_5 to OSF
- [ ] 3.1.2: Register: study title, hypotheses (H1), sampling plan (N=500, 3 conditions), analysis plan (Welch's t-test, α=0.00625, Bonferroni), exclusion criteria, data provenance (Pfam 38.2)
- [ ] 3.1.3: Save OSF registration DOI in `docs/protein-data-registry.md`

### Task 3.2: Experiment configuration finalisation

- [ ] 3.2.1: Finalise `experiments/configs/pfam-brittle.yaml`:
  - `experiment.n_runs_per_condition: 167` (501 total ≈ N=500)
  - `experiment.conditions: ["familiar_combos", "new_families", "cross_fold"]`
  - `experiment.split_ratios: {train: 0.70, val: 0.15, test: 0.15}`
  - `experiment.ood_ratio: 0.30` (proportion of test that is OOD)
  - `experiment.batch_size: 32`
  - `experiment.accumulation_steps: 2` (effective batch 64)
  - `experiment.max_steps: 5000`
  - `experiment.eval_every: 100`
  - `experiment.checkpoint_every: 500`
- [ ] 3.2.2: Generate all three compositional splits from Pfam 38.2 using `make_compositional_splits()` — cache to `data/pfam/splits/brittle/`
- [ ] 3.2.3: Verify that each condition produces ~167 evaluations (train/val ID/OOD/comp loaders)
- [ ] 3.2.4: Document splits: architecture counts, unique families, average recombination distance

### Task 3.3: Kaggle notebook implementation

- [ ] 3.3.1: Create `experiments/pfam-brittle-domain.ipynb` following 13-cell canonical pattern (never reorder cells):
  - **Cell 0**: Imports, path setup (Kaggle detection → `/kaggle/working/` fallback to `./output/`), GPU detection, reproducibility (GLOBAL_SEED)
  - **Cell 1**: Pfam dataset loading from cached splits (detect if on Kaggle → download from Kaggle Dataset, else → local cache)
  - **Cell 2**: Model definition — `SmallProteinLM` + `OdeAwareProteinLM` with σ_A proxy hooks
  - **Cell 3**: Data loaders — train/val/OOD/comp for all 3 conditions, `num_workers=2`, `pin_memory=True`
  - **Cell 4**: Training function — `train_protein_model()` adapted for notebook context
  - **Cell 5**: Orchestrator — loop over conditions × runs, collect results
  - **Cell 6**: σ_A proxy computation per run (GCA, RGA, AC, fused)
  - **Cell 7**: Primary analysis — high/low σ_A groups, Welch's t-test, ΔCG visualisation
  - **Cell 8**: Secondary analysis — σ_A trajectories across training, phase transition detection
  - **Cell 9**: Figure generation — accuracy curves, σ_A vs OOD accuracy scatter, ΔCG bar plots
  - **Cell 10**: Export results — pickle results, generate summary table
  - **Cell 11**: Diagnostics — per-run loss curves, gradient norm monitoring, learning rate schedule
  - **Cell 12**: Optimisation summary — AMP usage, memory profiling, timing
- [ ] 3.3.2: Package notebook as Kaggle-compatible: add Kaggle Dataset mount for Pfam cache, add output directory for results
- [ ] 3.3.3: Upload notebook to Kaggle as private notebook

### Task 3.4: Pilot run (N=15)

- [ ] 3.4.1: Run N=5 per condition (15 total) — limited pilot to validate:
  - Training convergence across all 3 split types
  - σ_A proxy shows variation across runs (if all runs have identical σ_A, the experiment cannot split into high/low groups)
  - OOD accuracies are in measurable range (not floor/ceiling)
  - Wall time per run matches profile estimate
- [ ] 3.4.2: Check go/no-go criteria from Phase 00_5 pilot design:
  - **GO**: OOD accuracy ∈ [20%, 80%] for all conditions, σ_A proxy CV > 0.10 across runs, ΔCG ≥ 10pp in at least one condition
  - **NO-GO**: Debug and return to Phase 02 for fixes
- [ ] 3.4.3: Document pilot results in `docs/lab-notebooks/2026-08-pfam-pilot.md`
- [ ] 3.4.4: Adjust config if needed (LR, batch size, model size)

### Task 3.5: N=500 execution

- [ ] 3.5.1: Launch first batch: 50 runs per condition (150 total) — monitor for the first 24 hours
  - Check: loss convergence, NaN detection, GPU memory stability, Kaggle session timeout
  - If >10% of runs fail → pause, diagnose, fix
- [ ] 3.5.2: Scale to full N=500: launch remaining 117 runs per condition (351 total)
  - Strategy: 3–5 parallel Kaggle notebooks, each running 30–60 sequential runs
  - Use Kaggle Datasets to share Pfam cache and results across notebooks
  - Each notebook saves results to Kaggle Dataset output → all notebooks write to same Dataset
- [ ] 3.5.3: Implement run monitoring:
  - For each run: log start time, end time, exit status (success/fail/NaN), final metrics
  - Upload monitoring log to Kaggle Dataset after each notebook completes
  - Set up email alert for failures (or check daily)
- [ ] 3.5.4: Handle session timeouts:
  - Kaggle: 30-hour session limit
  - If a run takes >8 hours, checkpoint strategy: every 500 steps saves state → resume from checkpoint if interrupted
  - Split across sessions if necessary: Run 1–100 in Session 1, 101–200 in Session 2, etc.
- [ ] 3.5.5: Aggregate all results into a single collective:
  - One DataFrame with columns: run_id, condition, seed, acc_id, acc_ood, deltaCG, sigma_proxy, gca, rga, ac, exit_status, wall_time
  - Save to `results/pfam-brittle/aggregated_results.parquet`

### Task 3.6: Data quality checks

- [ ] 3.6.1: Check for failed runs: NaN in any metric → exclude from analysis
- [ ] 3.6.2: Check for outlier runs: accuracy > 3σ from condition mean → flag for review
- [ ] 3.6.3: Verify seed reproducibility: re-run 3 randomly selected runs with same seed, confirm metrics within numerical tolerance (1e-5)
- [ ] 3.6.4: Compute per-condition summary statistics: mean, std, min, max, quartiles for all metrics
- [ ] 3.6.5: Document exclusion decisions and final N count in `docs/lab-notebooks/2026-12-brittle-quality.md`

---

**Phase 03 Exit Criteria**:
- [ ] OSF pre-registration locked before any data collection
- [ ] Kaggle notebook implemented, tested with pilot, uploaded
- [ ] N=500 runs × 3 conditions completed (or max feasible, documented)
- [ ] Aggregated results saved to `results/pfam-brittle/aggregated_results.parquet`
- [ ] Data quality checks pass: <5% failure rate, no systematic biases detected
- [ ] Raw result pickles archived (gitignored, in results/ or Kaggle Dataset)
- [ ] All claims C-039, C-040 updated to COLLECTED status in `docs/claims-registry.md`
