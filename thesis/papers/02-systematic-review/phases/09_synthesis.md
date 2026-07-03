# Phase 9 — Thematic Synthesis & Meta-Analysis

**Duration**: 4 weeks (Month 4–5)
**Deadline**: 2026-12-04
**Dependencies**: Phase 7 (extracted data), Phase 8 (RoB assessments)
**Output**: Completed synthesis — narrative themes and/or meta-analysis results

---

### Task 9.1: Prepare Synthesis Dataset

- [ ] 9.1.1: Load `research/charted-data.csv` into analysis environment (R or Python)
- [ ] 9.1.2: Merge RoB data from `research/risk-of-bias.csv`
- [ ] 9.1.3: Compute derived variables:
  - ID-OOD gap = ID accuracy − OOD accuracy
  - Log odds ratio = ln((ID_acc/(1-ID_acc)) / (OOD_acc/(1-OOD_acc)))
  - Cohen's d = (mean_ID − mean_OOD) / pooled_SD (if SD available)
  - Effect size from intervention vs baseline = Δ_intervention − Δ_baseline
- [ ] 9.1.4: Check distributional assumptions — normality of effects, outliers (±3 SD)
- [ ] 9.1.5: Create analysis-ready dataset `research/analysis/analysis-data.csv`

### Task 9.2: Narrative Thematic Synthesis

- [ ] 9.2.1: Organize extracted data into thematic categories:
  - **Theme 1: σ-trap prevalence** — across benchmarks, architectures, and training regimes, how common is the high-ID / low-OOD pattern?
  - **Theme 2: σ-trap detection** — what proxy measures have been used to detect low σ_A? Which ones correlate with OOD performance?
  - **Theme 3: Intervention effectiveness** — which interventions systematically reduce the ID-OOD gap? By how much? Are some interventions more effective for certain architectures or benchmarks?
  - **Theme 4: Architecture effects** — do some architectures inherently resist the σ-trap?
  - **Theme 5: Scale effects** — does increasing model size, data size, or compute resolve the σ-trap?
  - **Theme 6: Safety connection** — what evidence links σ-trap to alignment failure modes?
- [ ] 9.2.2: For each theme, synthesize across studies — identify consistent findings, contradictions, and gaps
- [ ] 9.2.3: Create summary of findings table (SoF table) per GRADE approach
- [ ] 9.2.4: Satisfy CC.1.9 — narrative synthesis complete even if meta-analysis infeasible

### Task 9.3: Meta-Analysis Feasibility Check

- [ ] 9.3.1: Assess number of studies with extractable effect sizes per comparison type
- [ ] 9.3.2: Minimum threshold: ≥5 studies per meta-analysis (random-effects model)
- [ ] 9.3.3: Check heterogeneity across studies (I² statistic, τ²)
- [ ] 9.3.4: If meta-analysis not feasible (too few studies, too heterogeneous, incomparable outcomes):
  - Document explicit reasons
  - Proceed with narrative synthesis only
  - Generate harvest plot as alternative to forest plot
- [ ] 9.3.5: If meta-analysis feasible, proceed to Task 9.4
- [ ] 9.3.6: Satisfy CC.1.9 — feasibility assessment documented

### Task 9.4: Meta-Analysis Execution (Conditional — feasible only if ≥5 comparable studies)

- [ ] 9.4.1: Choose effect size measure based on outcome type:
  - Accuracy data: log odds ratio or Cohen's d
  - Continuous metrics: standardized mean difference (Hedges' g)
- [ ] 9.4.2: Fit random-effects model (DerSimonian-Laird or REML estimator)
- [ ] 9.4.3: Primary meta-analysis: overall effect of interventions on OOD accuracy vs baseline
- [ ] 9.4.4: Subgroup analyses (pre-specified in Phase 1):
  - By intervention type (curriculum vs augmentation vs regularization vs σ-coupling vs architectural)
  - By architecture (RNN vs Transformer vs CNN)
  - By benchmark (SCAN vs COGS vs CFQ vs PCFG-SET)
  - By model scale (small < 10M params vs medium 10M–100M vs large > 100M)
- [ ] 9.4.5: Meta-regression (if ≥10 studies): explore moderators — year, dataset size, architecture depth
- [ ] 9.4.6: Generate forest plots for each analysis — store in `research/analysis/figures/`
- [ ] 9.4.7: Perform sensitivity analyses as pre-specified in Phase 8 (excluding high RoB, excluding preprints, etc.)
- [ ] 9.4.8: Satisfy CC.4.5 — all analysis scripts stored in `research/analysis/`

### Task 9.5: Publication Bias Assessment (if ≥10 studies in meta-analysis)

- [ ] 9.5.1: Generate funnel plot — effect size vs standard error
- [ ] 9.5.2: Egger's regression test for funnel plot asymmetry
- [ ] 9.5.3: Trim-and-fill analysis to estimate adjusted effect size
- [ ] 9.5.4: If publication bias detected, discuss implications and report adjusted estimates
- [ ] 9.5.5: Satisfy CC.1.10 — publication bias assessment completed

### Task 9.6: Confidence in Evidence (GRADE)

- [ ] 9.6.1: Apply GRADE framework to rate confidence in the body of evidence:
  - **Risk of bias**: from Phase 8
  - **Inconsistency**: heterogeneity across studies (I²)
  - **Indirectness**: do studies directly address the PICO question?
  - **Imprecision**: width of confidence intervals, optimal information size
  - **Publication bias**: from Task 9.5
- [ ] 9.6.2: Assign overall GRADE rating: High / Moderate / Low / Very Low
- [ ] 9.6.3: Generate GRADE summary of findings (SoF) table

### Task 9.7: Synthesis Documentation

- [ ] 9.7.1: Document all synthesis decisions and their rationale in `research/synthesis-log.md`
- [ ] 9.7.2: Archive all analysis scripts in `research/analysis/` with documentation
- [ ] 9.7.3: Archive all figures in `research/analysis/figures/`
- [ ] 9.7.4: Satisfy CC.4.6 — all analysis scripts version-controlled and documented

---

**Phase 9 Exit Criteria**:
- [ ] Synthesis dataset prepared with derived variables
- [ ] Narrative thematic synthesis complete (all 6 themes)
- [ ] Meta-analysis feasibility documented (whether feasible or not)
- [ ] If meta-analysis conducted: forest plots, subgroup analyses, sensitivity analyses completed
- [ ] If meta-analysis conducted: publication bias assessment completed
- [ ] GRADE assessment completed
- [ ] SoF table generated
- [ ] All analysis scripts and figures archived
- [ ] CC.1.9, CC.1.10, CC.4.5, CC.4.6 satisfied
- [ ] CC.5.3 satisfied — phase completion committed
