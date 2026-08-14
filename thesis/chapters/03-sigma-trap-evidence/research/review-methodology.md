# Review Methodology for Systematic Reviews of ML Experimental Papers

**Document type:** Reference — informs Phase 2 search, Phase 8 risk of bias, Phase 9 meta-analysis
**Purpose:** Methodological guidance for conducting systematic reviews and meta-analyses of ML performance experiments
**Status:** Draft

---

## 1. Unique Challenges of Reviewing ML Papers vs. Medical Trials

ML experimental papers differ from randomized clinical trials in ways that materially affect every stage of a systematic review:

1. **Absence of standardized intervention definitions** — each paper typically proposes a bespoke architecture/hyperparameter configuration; the "intervention" is not replicable across studies
2. **Performance metrics reported as point estimates without CIs** — the majority of ML papers omit confidence intervals, seeds, or variance reporting, making conventional inverse-variance pooling impossible
3. **Benchmarks rather than patient populations define the "units" of evidence** — the same model evaluated on different benchmarks yields non-independent effects
4. **Data leakage and test-set contamination** — pervasive and frequently undetectable from the manuscript alone; Kapoor and Narayanan documented 329 affected papers across 17 fields
5. **Reproducibility crisis** — code, weights, and training data shared in fewer than ~20% of healthcare ML studies and ~2% share training data
6. **Pace of publication** — arXiv preprints and conference proceedings outstrip peer-review cycles
7. **Optimism bias from selective benchmark reporting** — structurally analogous to publication bias but harder to detect because the unit of suppression is the benchmark, not the study

A recent methodological synthesis in *Frontiers in AI* concludes that "current systematic review methodologies are poorly suited to ML evidence, contributing to optimism bias, limited external validation, and non-comparable performance estimates."

---

## 2. Handling Papers That Do Not Report Effect Sizes or Confidence Intervals

This is the norm rather than the exception in ML. A defensible analytic plan proceeds in four tiers.

### Tier 1 — Re-derivation from reported counts

When a study reports a confusion matrix (TP, FP, TN, FN) and the test-set size *n*, the variance of accuracy, sensitivity, specificity, and F1 can be re-derived analytically:

- **Proportion** *p* = *k/n*: SE(*p*) = √(*p*(1−*p*)/*n*)
- **AUC**: Hanley–McNeil estimator:

  SE(AUC) = √[(AUC(1−AUC) + (n₊−1)(Q₁−AUC²) + (n₋−1)(Q₂−AUC²))/(n₊n₋)]

  where Q₁ = AUC/(2−AUC) and Q₂ = 2AUC²/(1+AUC)

### Tier 2 — Imputation from test-set size

When only the metric and *n* are reported, the binomial SE provides a conservative variance bound; multiple imputation of missing variances using a gamma mixed model on reported variances from comparable studies propagates imputation uncertainty into the pooled estimate, as formalized by Weir and colleagues. The Cochrane Handbook and CEBM guidance provide conversion formulae from SE, CI, IQR, or range to SD when at least one dispersion measure is reported.

### Tier 3 — Narrative synthesis with vote-counting

When neither counts nor dispersion are recoverable, quantitative pooling is precluded; the *Frontiers in AI* framework recommends narrative synthesis describing the range of reported metrics, stratified by validation design, with explicit flagging of optimism bias.

### Tier 4 — Author contact and code re-execution

Contacting corresponding authors and re-running released code on the reported benchmark to recover seed-level variance is the gold-standard recovery path; if code is available, bootstrap or k-fold resampling can supply the missing dispersion. Studies that cannot be placed in Tiers 1–2 should be excluded from the meta-analysis and retained only in sensitivity analyses.

---

## 3. Risk of Bias in ML Experiments

### Available tools

| Tool | Scope | Status | Reference |
|---|---|---|---|
| **PROBAST+AI** | ROB + applicability for ML prediction models | Final (BMJ 2025) | Moons et al. |
| **QUADAS-AI** | ROB for AI diagnostic-accuracy studies | Under development | EQUATOR Network |
| **RoB 2** | ROB for randomized trials (incl. ML RCTs) | Cochrane-recommended | Sterne et al. |
| **REFORMS** | 32-item checklist for ML-based science | Science Advances 2024 | Kapoor et al. |

### Known ML-specific sources of bias

| Source | Description | Targeted by tool |
|---|---|---|
| (a) **Data leakage** | Train/test contamination, feature selection on full data, temporal leakage | PROBAST+AI, REFORMS |
| (b) **Hyperparameter tuning on test set** | Tuning without nested cross-validation | PROBAST+AI |
| (c) **Test-set reuse** | Systematic accuracy inflation on reused benchmarks | REFORMS |
| (d) **Selective benchmark reporting** | Choosing favorable benchmarks post-hoc | REFORMS |
| (e) **Seed cherry-picking** | Reporting best of multiple seeds without disclosing variance | REFORMS |
| (f) **Distribution shift** | Case-mix, temporal, geographic mismatch between development and deployment | PROBAST+AI |
| (g) **Class imbalance** | Prevalence dependence of accuracy/F1 | — |
| (h) **No external validation** | <1% of ML studies report external validation; c-statistic drops of 0.85→0.72 are typical | PROBAST+AI |
| (i) **Algorithmic bias** | Performance disparities across demographic subgroups | — |
| (j) **Inadequate EPV** | Insufficient events-per-variable ratio | PROBAST+AI |
| (k) **Model updating without re-validation** | Deployment drift without re-assessment | PROBAST+AI |

**Action:** Apply PROBAST+AI to every included study; supplement with REFORMS items on leakage and code availability; rate each study low/some-concerns/high; exclude high-ROB from primary pooling.

---

## 4. Handling arXiv Preprints

The methodological consensus, reinforced during COVID-19 evidence synthesis, is that preprints *should* be included in ML systematic reviews. Recommended practice:

1. **Search arXiv, bioRxiv, OpenReview explicitly** and record preprint DOI/version alongside any published version
2. **Deduplicate preprint–publication pairs** and prefer the peer-reviewed version when both exist, extracting any updated metrics
3. **Mark preprint status as a study-level covariate** and conduct a pre-specified subgroup analysis comparing pooled estimates from preprints versus peer-reviewed studies
4. **Apply the same ROB tool** (PROBAST+AI / REFORMS) to preprints, since ROB is orthogonal to peer-review status
5. **Down-weight or sensitivity-test** preprints in the meta-analysis — either by assigning them larger variance (e.g., inflation factor on SE) or by excluding them in a leave-one-out sensitivity analysis
6. **Track preprint-to-publication status** for living-systematic-review updates — automated frameworks such as AutoConfidence predict preprint publication probability

Note: as of 2025 arXiv's CS section now requires review articles and position papers to be peer-reviewed before submission, reflecting community concern about preprint quality control. The PRISMA-S extension requires transparent reporting of grey-literature and preprint searches.

---

## 5. Meta-Analytic Methods Appropriate for ML Performance Metrics

### For proportions (accuracy, sensitivity, specificity)

Raw pooling is inadmissible because the variance of a proportion depends on its mean. Apply a variance-stabilizing transformation:

- **Logit transform** (preferred for proportions 0.2–0.8)
- **Freeman–Tukey double-arcsine transform** (preferred when proportions approach 0 or 1 or when sample sizes are small)

Pool on the transformed scale with a random-effects model (DerSimonian–Laird or Hartung–Knapp–Sidik–Jonkman adjustment) and back-transform with the delta method.

### For AUC

The Hanley–McNeil or Obuchowski variance estimator supplies within-study SE. AUC values can be pooled directly via inverse-variance random-effects models, or converted to log-odds for combination with discrimination-oriented syntheses (R packages: `mada`, `meta`).

### For F1 and other ratio metrics

No closed-form variance exists; use the delta method on precision and recall, or bootstrap.

### Heterogeneity

Quantify with *I*² and τ²; explore via pre-specified subgroup meta-regression (model family, dataset, validation design).

### Dependent effect sizes (multiple seeds, benchmarks, or metrics per study)

Use a **three-level meta-analysis** (effect sizes nested within studies) or **robust variance estimation (RVE)** with correlated-effects structures to avoid pseudoreplication and inflated Type-I error.

### Alternative: rank-based comparison

The Friedman test with Nemenyi post-hoc (Demšar 2006, JMLR) ranks classifiers across datasets and is appropriate when the goal is rank-based comparison rather than effect-size pooling.

### Publication / small-study bias

Assess with contour-enhanced funnel plots, Egger's regression, and trim-and-fill, with the caveat that benchmark-selective reporting produces bias patterns distinct from classic publication bias.

---

## 6. Existing Guidelines

| Guideline | Scope | Status | Reference |
|---|---|---|---|
| **PRISMA 2020** | General SR & meta-analysis reporting | Final, widely adopted | Page et al., BMJ 2021 |
| **PRISMA-AI** | Extension for SRs of AI/ML in healthcare | In development (EQUATOR); interim Nat Med 2023 | — |
| **PRISMA-trAIce** | Transparent reporting of AI *use within* SRs | Published JMIR AI 2025 | — |
| **PRISMA-S** | Reporting of literature searches | Final 2021 | — |
| **CONSORT-AI / SPIRIT-AI** | Clinical trials / protocols of AI interventions | Final BMJ 2020; 14 new items | — |
| **TRIPOD+AI** | Reporting prediction-model studies (regression or ML) | Final BMJ 2024 | — |
| **PROBAST+AI** | ROB + applicability for ML prediction models | Final BMJ 2025 | — |
| **QUADAS-AI** | ROB for AI diagnostic-accuracy studies | Under development | — |
| **σ-ROB** | 6-domain RoB tool for σ-trap ML experiments | Custom (see `quality-criteria.md`) | Adapted from QUADAS-2 + ROBINS-I + PROBAST+AI |
| **RoB 2** | ROB for randomized trials (incl. ML RCTs) | Cochrane-recommended | — |
| **REFORMS** | 32-item checklist for ML-based science | Science Advances 2024 | — |
| **CLAIM / CLAIM-AI** | Reporting medical AI imaging studies | Published; AI extension evolving | — |

**Critical caveat:** PRISMA-AI remains under development, and the published 2023 *Nature Medicine* item is an interim statement, not a final checklist. TRIPOD+AI and PROBAST+AI are the most mature ML-specific instruments but are oriented toward clinical prediction models; their direct applicability to general ML benchmarks (e.g., OOD-generalization or compositional-generalization benchmarks) is partial and requires reviewer adaptation. REFORMS is the most cross-domain instrument and the only one co-developed by computer scientists for ML-based science broadly.

**Recommendation:** Combine PRISMA 2020 with the most relevant AI extensions. Use REFORMS for cross-domain ROB items and PROBAST+AI for structured risk-of-bias signaling questions.

---

## 7. Handling Studies Comparing Multiple Interventions on Different Benchmarks

This is the single most distinctive analytic problem in ML systematic reviews and one of the hardest.

### Three architectures (in increasing order of sophistication)

**(a) Three-level / multilevel meta-analysis.** Treat each (intervention × benchmark) cell as an effect size nested within study, with random effects at both the study level and the effect-size level; this models the covariance among effects from the same study and among effects on the same benchmark, and is the recommended default when the same benchmarks recur across studies.

**(b) Network meta-analysis (NMA).** When interventions form a connected network via shared comparators (e.g., multiple methods all evaluated against a common baseline on overlapping benchmark sets), NMA synthesizes direct and indirect evidence and produces a ranking of interventions. NMA in the ML context is feasible — Gao et al. (2024) demonstrated it for sepsis-prediction algorithms — but its validity rests on the **transitivity assumption** (the set of studies comparing any pair of interventions must be similar in all effect modifiers). A 2025 scoping review of 28 NMAs of prediction models found that transitivity and consistency were "often underreported or inadequately assessed."

**(c) Hierarchical / multivariate meta-regression with benchmark-level covariates.** When benchmarks differ systematically in difficulty, sample size, or shift type, include benchmark characteristics as moderators; this disentangles intervention effects from benchmark difficulty and is the natural framework for σ-trap-mechanism reviews.

### Practical 6-step workflow

1. Construct the (study × intervention × benchmark) effect-size matrix
2. Account for sparsity and disconnected networks — restrict to largest connected component or use multi-arm correction
3. Fit a three-level random-effects model with RVE as the primary analysis
4. Run an NMA on the connected sub-network as a secondary analysis if transitivity holds
5. Report rankograms and SUCRA scores for intervention ranking
6. Conduct a **component-network meta-analysis** if interventions are themselves combinations of components (e.g., data augmentation + architecture + loss function), decomposing the intervention into additive component effects

---

## 8. Actionable Recommendations Summary

| Domain | Recommendation | Tool/Reference |
|---|---|---|
| **Protocol** | Register on PROSPERO; pre-specify PICO-style eligibility with benchmark as the "population" analog; follow PRISMA 2020 with PRISMA-S for search reporting | PRISMA 2020, PRISMA-S |
| **Search** | IEEE Xplore, ACM DL, Scopus, Web of Science, PubMed, arXiv, OpenReview; record preprint DOIs and versions | — |
| **ROB** | Apply PROBAST+AI to every included study; supplement with REFORMS items on leakage and code availability; rate each study low/some-concerns/high; exclude high-ROB from primary pooling | PROBAST+AI, REFORMS |
| **Effect-size recovery** | Re-derive from confusion matrices where possible; otherwise impute variances with uncertainty propagation; contact authors and re-run code as a last resort | Hanley–McNeil, Cochrane Handbook |
| **Meta-analysis** | Use logit/Freeman–Tukey transforms for proportions, Hanley–McNeil for AUC; default to three-level random-effects with RVE for dependent effects; consider NMA only when transitivity is defensible | R packages: `metafor`, `meta`, `mada` |
| **Preprints** | Include with a preprint covariate; sensitivity-test by exclusion; track publication status for living updates | AutoConfidence |
| **Reporting** | Use PRISMA-AI (interim) plus TRIPOD+AI items for primary-study appraisal; publish code and extraction spreadsheets | PRISMA-AI, TRIPOD+AI |
| **Heterogeneity & bias** | Quantify *I*²/τ²; funnel plots + Egger; stratify by external-validation status, model family, and benchmark | — |
| **Living review** | Given ML's pace, structure the review for periodic update via automated literature monitoring | Frontiers AI framework |

**Caveat:** The AI-specific guideline ecosystem (PRISMA-AI, QUADAS-AI) is still maturing in 2026; reviewers should monitor the EQUATOR Network and the Latitudes Network for finalized checklists and update their protocol accordingly before submission.

---

## References

- Demšar, J. (2006). Statistical Comparisons of Classifiers over Multiple Data Sets. *JMLR*, 7, 1–30.
- Kapoor, S., & Narayanan, A. (2023). Leakage and the Reproducibility Crisis in ML-based Science. *Patterns*, 4(9).
- Kapoor, S., et al. (2024). REFORMS: A 32-item consensus checklist for ML-based science. *Science Advances*.
- Page, M. J., et al. (2021). The PRISMA 2020 statement. *BMJ*, 372:n71.
- Sterne, J. A. C., et al. (2019). RoB 2: A revised tool for assessing risk of bias in randomised trials. *BMJ*, 366:l4898.
- Weir, C. J., et al. (2018). Multiple imputation of missing variances in meta-analysis. *BMC Medical Research Methodology*.
