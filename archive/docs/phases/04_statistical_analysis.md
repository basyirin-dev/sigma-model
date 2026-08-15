# Phase 04 — Statistical Analysis & H1 Testing

**Deadline**: 10 Jan 2027
**Dependencies**: Phase 03 (N=500 aggregated results)
**Output**: H1 test results, ΔCG analysis, σ_A trajectory figures, ICML go/no-go decision

---

### Task 4.1: Primary H1 hypothesis test

- [ ] 4.1.1: Load aggregated results from Phase 03: `results/pfam-brittle/aggregated_results.parquet`
- [ ] 4.1.2: Split runs into high/low σ_A groups using median split of `sigma_proxy` (across all conditions)
  - Document the threshold value θ_σ chosen
  - Verify group sizes are balanced (target: n ≥ 64 per group per condition)
- [ ] 4.1.3: Implement Welch's t-test for each condition (familiar_combos, new_families, cross_fold):
  - H0: μ(Acc_OOD | σ_A > θ_σ) — μ(Acc_OOD | σ_A < θ_σ) = 0
  - H1: μ(Acc_OOD | σ_A > θ_σ) — μ(Acc_OOD | σ_A < θ_σ) > 0
  - Compute: t-statistic, degrees of freedom (Welch-Satterthwaite), p-value, Cohen's d, 95% CI
- [ ] 4.1.4: Apply Bonferroni correction: α = 0.05 / 8 comparisons = 0.00625
  - 8 comparisons: 3 conditions × (Acc_OOD + ΔCG) + 2 secondary (overall + cross-condition)
- [ ] 4.1.5: Sensitivity analysis — repeat with:
  - σ_A threshold at quartiles (Q1, Q3) instead of median
  - Continuous regression (σ_A as predictor, not dichotomised)
  - Excluding top/bottom 5% of σ_A values
- [ ] 4.1.6: Secondary: Bayesian estimation with `scipy.stats.bayes_mvs` or PyMC:
  - Report posterior distribution of group difference
  - Report probability of positive effect: P(d > 0 | data)
- [ ] 4.1.7: Output: `results/pfam-brittle/h1-test-results.json` with all statistics

### Task 4.2: Compositional gap analysis

- [ ] 4.2.1: Compute ΔCG per run: `deltaCG = acc_id - acc_ood`
- [ ] 4.2.2: Per-condition ΔCG statistics: mean, std, effect size (Cohen's d between conditions)
- [ ] 4.2.3: Test gradient: ΔCG(familiar_combos) < ΔCG(new_families) < ΔCG(cross_fold)
  - If violated, investigate: are the splits invalid or is there a ceiling effect?
- [ ] 4.2.4: Correlation analysis: Pearson r between σ_A proxy and ΔCG for each condition
- [ ] 4.2.5: Partial correlation: σ_A vs ΔCG controlling for confounds (architecture length, family count, sequence diversity)
- [ ] 4.2.6: Output: `results/pfam-brittle/deltaCG-analysis.json`

### Task 4.3: σ_A trajectory analysis

- [ ] 4.3.1: Load σ_A proxy trajectories across training steps from Phase 03 checkpoints
- [ ] 4.3.2: Cluster trajectories using k-means (k=3: high/medium/low terminal σ_A)
- [ ] 4.3.3: Phase transition detection:
  - For each run, identify the training step where σ_A proxy crosses `sigma_critical` (0.15 from config)
  - Count runs that cross vs. don't cross, per condition
  - Does crossing σ_critical predict higher OOD accuracy? (t-test)
- [ ] 4.3.4: Plot: σ_A trajectory curves (mean ± std per condition), with phase transition bands
- [ ] 4.3.5: Output: trajectory figures saved to `paper-neurips/figures/` placeholder

### Task 4.4: Construct isolation validation

- [ ] 4.4.1: Compute `compute_construct_isolation()` for the σ_A proxy:
  - Target: OOD accuracy
  - Proxy: σ_A (fused)
  - Confounds: architecture length, number of unique families in architecture, taxonomic diversity, sequence conservation score
- [ ] 4.4.2: Report CI score for each confound
- [ ] 4.4.3: If CI < 0.60 (validity threshold from Codex C-007), investigate whether σ_A is measuring something distinct from confounds

### Task 4.5: Figure generation

- [ ] 4.5.1: Generate Figure 1 (protein domain architecture concept):
  - Panel A: Pfam domain architecture examples (graphical representation)
  - Panel B: Comparison table (synthetic SCAN/COGS vs. protein domain data)
- [ ] 4.5.2: Generate Figure 2 (σ-trap on protein data):
  - Scatter plot: σ_A proxy vs OOD accuracy per condition (167 points × 3 colours)
  - Regression lines per condition with shaded 95% CI
  - Inset: Cohen's d bar chart (high vs low σ_A for each condition)
- [ ] 4.5.3: Generate Figure 3 (ΔCG across conditions):
  - Box plot: ΔCG distributions per condition, split by high/low σ_A
  - Pairwise significance annotations (Bonferroni-corrected)
- [ ] 4.5.4: Register alt-text for all new figures in `docs/figure-alt-text.md`
- [ ] 4.5.5: Save all figures as PDF + PNG (300 DPI) to `paper-neurips/figures/`

### Task 4.6: ICML go/no-go decision

- [ ] 4.6.1: Assess whether Phase 05 (Grammar Induction) analysis is sufficiently mature
- [ ] 4.6.2: Criteria for ICML submission (Jan 2027 deadline):
  - **GO**: H1 significant (p < 0.00625) in at least 2 of 3 conditions, d ≥ 0.5, ΔCG gradient confirmed, Phase 05 initial probe results available
  - **NO-GO**: H1 null across all conditions, or Phase 05 not complete enough for a coherent paper
- [ ] 4.6.3: Document decision in `docs/lab-notebooks/2027-01-icml-decision.md`

---

**Phase 04 Exit Criteria**:
- [ ] H1 tested and documented (significant or null, either is publishable)
- [ ] ΔCG gradient confirmed (familiar < new < cross-fold)
- [ ] σ_A trajectory analysis complete with phase transition detection
- [ ] Construct isolation CI ≥ 0.60 or documented limitation
- [ ] Figures 1–3 generated and saved to `paper-neurips/figures/`
- [ ] ICML go/no-go decision documented
- [ ] Claim C-039 (H1 result) updated to status based on outcome
