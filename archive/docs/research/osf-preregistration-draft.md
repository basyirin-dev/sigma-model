# OSF Pre-Registration Draft — σ-A Model Brittle Domain Experiment

> **Source**: Adapted from DeepSearch AI research output (Jun 2026); analysis design informed by `docs/research/power-analysis.md`
> **Purpose**: Ready-to-copy-paste into OSF Preregistration template before Phase 03 data collection
> **Data version**: Pfam 38.2

---

# Study Information

**Title**
The Effect of Architecture Variance (σ_A) on Out-of-Distribution Generalization in Transformer Language Models Trained on Pfam Domain Architectures

**Authors**
[Enter Author Names / ORCIDs here]

**Description**
This pre-registration outlines a computational experiment investigating how the variance of domain architectures (σ_A) impacts the out-of-distribution (OOD) generalization capabilities of transformer language models. We will train N=500 models on Pfam 38.2 domain architecture sequences across three compositionality conditions. We hypothesize that models exposed to higher σ_A will demonstrate significantly better OOD accuracy on domain architecture prediction compared to those with lower σ_A.

**Hypotheses**
1. **Primary Hypothesis:** Higher σ_A runs will yield significantly higher OOD accuracy, measured as a positive slope in the continuous regression of OOD accuracy on σ_A.
2. **Secondary Hypothesis 1:** High σ_A runs will exhibit a smaller compositional gap (ΔCG) than low σ_A runs.
3. **Secondary Hypothesis 2:** The effect of σ_A on OOD accuracy will be modulated by the architectural condition (familiar, new combinations, cross-clan).
4. **Exploratory Hypothesis:** OOD generalization will exhibit phase-transition dynamics during training, which will correlate with σ_A trajectories.

---

# Design Plan

**Study Type**
Computational Experiment (Machine Learning)

**Blinding**
There is no blinding in this computational study, as data generation and evaluation are fully automated and deterministic based on pre-specified random seeds.

**Study Design**
The study employs a between-runs experimental design with N=500 independent training runs. Runs are stratified across 3 independent conditions:
1. **Familiar combinations (Type A):** Training and testing on standard combinations of Pfam families.
2. **New combinations of familiar families (Type B):** Testing on novel recombinations of families seen during training.
3. **Cross-clan combinations (Type C):** Testing on combinations requiring generalization across distinct Pfam clans.

The primary independent variable is the architecture variance (σ_A), which will be operationalised as a **continuous predictor in the primary analysis** and as a **dichotomous grouping variable (median split)** in the secondary analysis.

**Randomization**
Run configurations are deterministically assigned using the seed formula: `seed = run_id * 42 + 7`. Randomization of data shuffling and model weight initialisation is governed entirely by this deterministic seed sequence.

---

# Sampling Plan

**Existing Data**
No prior data has been collected or analysed for this specific study. The data provenance is the Pfam 38.2 database.

**Sample Size, Power, and Backing**
The target sample size is N=500 valid runs (approximately 167 per condition). Power analysis was conducted for two scenarios:

- **Pooled across conditions** (all 500 runs enter the primary regression): power > 99.9% for detecting Cohen's d ≥ 0.5 at α = 0.00625.
- **Per-condition subset** (≈167 runs): power ≈ 68% at the same α and effect size.

The primary analysis uses a continuous regression model that pools across conditions (via the Condition × σ_A interaction term), making the pooled power figure applicable. The per-condition caveat is documented for transparency; if per-condition comparisons are of primary interest, N should be increased to ≈618. See `docs/research/power-analysis.md` for full details.

**Stopping Rule**
Data collection (model training and evaluation) will cease once 500 *valid* runs have been successfully completed and recorded. Runs that meet the exclusion criteria (see Analysis Plan) will be considered invalid and will not count toward the N=500 target. Invalid runs will be replaced by new runs with sequentially incremented `run_id`s until N=500 is reached.

---

# Variables

**Manipulated Variables**
- **Condition:** Categorical variable with 3 levels (Familiar / Type A, New Combinations / Type B, Cross-Clan / Type C).
- **Architecture Variance (σ_A):** The degree of variance in domain architectures presented during training. Used as a **continuous predictor** in the primary analysis and **dichotomised at the median** (High σ_A vs Low σ_A) in the secondary analysis.

**Measured Variables**
- **Primary Outcome:** OOD accuracy on domain architecture prediction (continuous, bounded [0, 1]).
- **Secondary Outcomes:**
  - Compositional Gap (ΔCG): Difference between in-distribution (ID) accuracy and OOD accuracy (ID_acc − OOD_acc).
  - σ_A trajectories: Continuous measurement of σ_A over training epochs.
  - Phase transition markers: Epoch/time step where the second derivative of OOD accuracy crosses zero (indicating a sudden shift in generalisation capability).

**Indices**
- ΔCG is computed per run as the arithmetic difference between the final ID accuracy and the final OOD accuracy.

---

# Analysis Plan

**Statistical Models & Hypothesis Tests**

- **Primary Analysis:**
  To test the primary hypothesis, we will fit a linear regression model predicting OOD accuracy from the continuous architecture variance (σ_A), the experimental Condition (3 levels), and their interaction:
  `OOD_accuracy ~ σ_A + Condition + σ_A : Condition`
  - The primary coefficient of interest is the main effect of continuous σ_A.
  - **Significance Threshold:** α = 0.00625 (Bonferroni-corrected for a family of 8 pre-registered comparisons: the σ_A main effect, 3 condition contrasts, 3 σ_A:Condition interaction terms, and the overall model F-test).
  - **Effect Size:** Standardised regression coefficient (β) with 95% confidence intervals.

- **Secondary / Robustness Analyses:**
  1. **Dichotomised Welch's t-test:** To maintain comparability with prior literature utilising binary thresholds, we will perform a median split on σ_A and conduct an independent two-sided Welch's t-test comparing High vs Low σ_A groups on OOD accuracy. Cohen's d with 95% CIs will be reported.
  2. **Non-parametric:** Mann–Whitney U test on the median-split groups.
  3. **Permutation Test:** 100,000 permutations of group labels to empirically derive the p-value for the t-test.
  4. **Outlier Sensitivity:** Re-running the primary regression after excluding the top and bottom 1% of OOD accuracy runs.

- **Secondary Bayesian Analysis:**
  We will employ the BEST (Bayesian Estimation Supersedes the t-test) framework using a Student-t likelihood with separate variances for each σ_A group.
  - Priors: Broad normal priors on means, half-Cauchy on standard deviations, Gamma(2, 0.1) on degrees of freedom.
  - Inference: 4 chains, 4,000 iterations (Stan/PyMC). We will report the 95% Highest Density Interval (HDI) for the standardised difference in means.
  - Decision Rule: A meaningful effect is declared if the 95% HDI completely excludes the Region of Practical Equivalence (ROPE), defined as [−0.1, 0.1].

- **Secondary Outcome Analysis:**
  1. **ΔCG:** Welch's t-test comparing High vs Low σ_A groups on ΔCG.
  2. **Phase Transition Detection:** We will plot the derivative of OOD accuracy over training steps. The presence of a phase transition will be formally tested using piecewise regression (segmented) with a pre-specified breakpoint search window.

**Data Exclusion Rules**
Runs will be excluded and replaced if they meet any of the following criteria:
1. **NaN Loss:** Training logs record NaN for the loss function at any point.
2. **Failed Training:** The training script crashes, times out, or fails to write the final checkpoint/evaluation logs.
3. **Floor Performance:** The final in-distribution (ID) accuracy is < 10%, indicating the model failed to learn the base task entirely.

**Transformations**
If OOD accuracy values exhibit severe ceiling effects (e.g., a cluster of runs exactly at 1.0 or 0.0), we will apply a logit transformation to the accuracy scores prior to the regression analysis. If values are exactly 0 or 1, they will be compressed to 0.001 and 0.999 respectively before transformation. A decision to apply this transformation will be made prior to data unblinding/analysis by inspecting the marginal distribution of OOD accuracy.

---

# Other

**Data Provenance & Availability**
- All training and evaluation data are derived from the **Pfam 38.2** database.
- Random seeds for all stochastic processes (initialisation, batching, dropout) are strictly governed by the formula: `seed = run_id * 42 + 7`.
- Upon completion of the study, all training scripts, evaluation code, configuration files, and raw run logs will be deposited in a public GitHub repository and archived on Zenodo. A direct link will be provided in the final manuscript.

**Conflict of Interest**
[Insert standard COI statement or state "The authors declare no conflicts of interest."]
