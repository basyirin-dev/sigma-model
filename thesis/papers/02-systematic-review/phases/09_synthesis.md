# Phase 9 — Thematic Synthesis & Meta-Analysis

**Duration**: 4 weeks (Month 4–5)
**Deadline**: 2026-12-04
**Dependencies**: Phase 7 (extracted data), Phase 8 (RoB assessments)
**Output**: Completed synthesis — narrative themes and/or meta-analysis results: `research/analysis/analysis-data.csv`, `research/synthesis-log.md`, SoF table, `research/analysis/figures/`

---

### Operationalizations (Phase A)

Locked before analysis; governs the whole phase.

- **Primary-effect amendment (supersedes 9.4.3 as stated)**: the corpus contains exactly **one** σ-training intervention study (S046; `train_regime_sigma` = other_sigma; 280/286 not_applicable; Phase 8 D3 N/A for 224). The ``overall effect of interventions on OOD accuracy vs baseline`` meta-analysis is therefore **infeasible (k = 1)** and is conducted as narrative synthesis only, with a harvest plot (9.3.4). The **primary meta-analysis is the pooled ID--OOD gap** (Theme 1, σ-trap prevalence): 71 studies have both accuracies (64 LOR-computable), k = 27--31 in the pre-specified S3/S4/S5 strata. This amends `meta-analysis-feasibility.md` SAP-1 (whose primary LOR is an intervention contrast) per its own fallback path; amendment logged in `research/synthesis-log.md`.
- **Effect-size definitions (9.1.3)**: primary = ID--OOD gap (`id_ood_gap_raw`); LOR computed from `id_acc_mean`/`ood_acc_mean` with 0.5/n continuity correction; Cohen's d only where SDs exist (32 ID-SD, 60 OOD-SD). Missing gap variance: derived from binomial SE of the accuracies where gap SE absent (14/71 have `id_ood_gap_se`); studies without any variance basis are pooled with imputed mean variance (documented) or excluded from pooling but kept in narrative.
- **Outliers (9.1.4)**: |z| > 3 on the gap flagged (1 study: S0 gap mean 0.21, sd 0.31, min -1.158); sensitivity with/without outliers.
- **Heterogeneity (9.3.3)**: per `meta-analysis-feasibility.md` SAP-3, I² > 75% triggers subgroup/meta-regression exploration, not abandonment. Expect I² ≈ 100% across benchmark families.
- **Subgroups (9.4.4, adapted)**: benchmark family (custom vs compositional CFQ/SCAN/COGS/gSCAN/GeoQuery, k = 22; per-family k ≤ 6 below the ≥5 pooling threshold → narrative for individual families), architecture family (transformer k = 30), scale (small k = 11; unspecified 53 → excluded from scale subgroup). Meta-regression on year/scale only where k ≥ 10.
- **GRADE (9.6)**: pre-specified to rate **Very Low for most outcomes** (96.2% studies HIGH RoB → risk-of-bias downgrade; indirectness; imprecision). SoF table is a transparency exercise.
- **CC numbering (Paper-02 convention)**: CC.1.9 = narrative synthesis complete even if meta-analysis infeasible; CC.1.10 = publication-bias assessment; CC.4.5 = analysis scripts in `research/analysis/`; CC.4.6 = scripts version-controlled and documented; CC.5.3 = phase committed. (Differs from global `cross-cutting.md` numbering; Paper-02 meanings used here.)
- **Named outputs**: `research/analysis/analysis-data.csv`, `research/synthesis-log.md`, SoF table (in log + appendix of manuscript), `research/analysis/figures/` (forest, harvest, funnel).

---

### Task 9.1: Prepare Synthesis Dataset

- [x] 9.1.1: Load `research/charted-data.csv` into analysis environment (R or Python)
- [x] 9.1.2: Merge RoB data from `research/risk-of-bias.csv`
- [x] 9.1.3: Compute derived variables:
  - ID-OOD gap = ID accuracy − OOD accuracy
  - Log odds ratio = ln((ID_acc/(1-ID_acc)) / (OOD_acc/(1-OOD_acc)))
  - Cohen's d = (mean_ID − mean_OOD) / pooled_SD (if SD available)
  - Effect size from intervention vs baseline = Δ_intervention − Δ_baseline
- [x] 9.1.4: Check distributional assumptions — normality of effects, outliers (±3 SD)
- [x] 9.1.5: Create analysis-ready dataset `research/analysis/analysis-data.csv`

### Task 9.2: Narrative Thematic Synthesis

- [x] 9.2.1: Organize extracted data into thematic categories:
  - **Theme 1: σ-trap prevalence** — across benchmarks, architectures, and training regimes, how common is the high-ID / low-OOD pattern?
  - **Theme 2: σ-trap detection** — what proxy measures have been used to detect low σ_A? Which ones correlate with OOD performance?
  - **Theme 3: Intervention effectiveness** — which interventions systematically reduce the ID-OOD gap? By how much? Are some interventions more effective for certain architectures or benchmarks?
  - **Theme 4: Architecture effects** — do some architectures inherently resist the σ-trap?
  - **Theme 5: Scale effects** — does increasing model size, data size, or compute resolve the σ-trap?
  - **Theme 6: Safety connection** — what evidence links σ-trap to alignment failure modes?
- [x] 9.2.2: For each theme, synthesize across studies — identify consistent findings, contradictions, and gaps
- [x] 9.2.3: Create summary of findings table (SoF table) per GRADE approach
- [x] 9.2.4: Satisfy CC.1.9 — narrative synthesis complete even if meta-analysis infeasible

### Task 9.3: Meta-Analysis Feasibility Check

- [x] 9.3.1: Assess number of studies with extractable effect sizes per comparison type
- [x] 9.3.2: Minimum threshold: ≥5 studies per meta-analysis (random-effects model)
- [x] 9.3.3: Check heterogeneity across studies (I² statistic, τ²)
- [x] 9.3.4: If meta-analysis not feasible (too few studies, too heterogeneous, incomparable outcomes):
  - Document explicit reasons
  - Proceed with narrative synthesis only
  - Generate harvest plot as alternative to forest plot
- [x] 9.3.5: If meta-analysis feasible, proceed to Task 9.4
- [x] 9.3.6: Satisfy CC.1.9 — feasibility assessment documented

### Task 9.4: Meta-Analysis Execution (Conditional — feasible only if ≥5 comparable studies)

- [x] 9.4.1: Choose effect size measure based on outcome type:
  - Accuracy data: log odds ratio or Cohen's d
  - Continuous metrics: standardized mean difference (Hedges' g)
- [x] 9.4.2: Fit random-effects model (DerSimonian-Laird or REML estimator)
- [x] 9.4.3: Primary meta-analysis: overall effect of interventions on OOD accuracy vs baseline
- [x] 9.4.4: Subgroup analyses (pre-specified in Phase 1):
  - By intervention type (curriculum vs augmentation vs regularization vs σ-coupling vs architectural)
  - By architecture (RNN vs Transformer vs CNN)
  - By benchmark (SCAN vs COGS vs CFQ vs PCFG-SET)
  - By model scale (small < 10M params vs medium 10M–100M vs large > 100M)
- [x] 9.4.5: Meta-regression (if ≥10 studies): explore moderators — year, dataset size, architecture depth
- [x] 9.4.6: Generate forest plots for each analysis — store in `research/analysis/figures/`
- [x] 9.4.7: Perform sensitivity analyses as pre-specified in Phase 8 (excluding high RoB, excluding preprints, etc.)
- [x] 9.4.8: Satisfy CC.4.5 — all analysis scripts stored in `research/analysis/`

### Task 9.5: Publication Bias Assessment (if ≥10 studies in meta-analysis)

- [x] 9.5.1: Generate funnel plot — effect size vs standard error
- [x] 9.5.2: Egger's regression test for funnel plot asymmetry
- [x] 9.5.3: Trim-and-fill analysis to estimate adjusted effect size
- [x] 9.5.4: If publication bias detected, discuss implications and report adjusted estimates
- [x] 9.5.5: Satisfy CC.1.10 — publication bias assessment completed

### Task 9.6: Confidence in Evidence (GRADE)

- [x] 9.6.1: Apply GRADE framework to rate confidence in the body of evidence:
  - **Risk of bias**: from Phase 8
  - **Inconsistency**: heterogeneity across studies (I²)
  - **Indirectness**: do studies directly address the PICO question?
  - **Imprecision**: width of confidence intervals, optimal information size
  - **Publication bias**: from Task 9.5
- [x] 9.6.2: Assign overall GRADE rating: High / Moderate / Low / Very Low
- [x] 9.6.3: Generate GRADE summary of findings (SoF) table

### Task 9.7: Synthesis Documentation

- [x] 9.7.1: Document all synthesis decisions and their rationale in `research/synthesis-log.md`
- [x] 9.7.2: Archive all analysis scripts in `research/analysis/` with documentation
- [x] 9.7.3: Archive all figures in `research/analysis/figures/`
- [x] 9.7.4: Satisfy CC.4.6 — all analysis scripts version-controlled and documented

---

**Phase 9 Exit Criteria**:
- [x] Synthesis dataset prepared with derived variables
- [x] Narrative thematic synthesis complete (all 6 themes)
- [x] Meta-analysis feasibility documented (whether feasible or not) — incl. k = 1 intervention finding
- [x] If meta-analysis conducted: forest plots, subgroup analyses, sensitivity analyses completed (primary = ID--OOD gap per amendment)
- [x] If meta-analysis conducted: publication bias assessment completed
- [x] GRADE assessment completed (pre-specified Very Low for most outcomes)
- [x] SoF table generated
- [x] All analysis scripts and figures archived
- [x] CC.1.9, CC.1.10, CC.4.5, CC.4.6 (Paper-02 meanings) satisfied
- [x] CC.5.3 satisfied — phase completion committed

---

## Execution log (Phase A–E, 2026-08)

**Phase A — operationalizations locked.** Inputs verified: 71 studies with both ID+OOD accuracies (64 LOR-computable), 71 with gap (14 charted SEs), 1 outlier; exactly 1 σ-intervention study (S046) — interventions k = 1; scenario gap pools S3 k = 31 / S4 27 / S5 30 (pooling k 27/23/27 once variance required). Phase doc patched: primary-effect amendment (ID–OOD gap prevalence; intervention narrative-only + harvest plot; SAP-1 amendment), effect-size definitions (LOR with continuity correction, Cohen's d where SDs), missing-variance handling, outlier rule, heterogeneity rule (I² > 75% → subgroup, not abort), adapted subgroups, GRADE pre-spec (Very Low), Paper-02 CC annotations, named outputs.

**Task 9.1.** `analysis/prepare_analysis_data.py` → `analysis/analysis-data.csv` (286×34): derived gap/LOR/Cohen's d/gap SE, outlier flag (1), scenario flags S0–S5, subgroup keys; distribution checks in `analysis-data-report.md` (gap skew −0.47, LOR skew 0.81).

**Task 9.2.** Narrative thematic synthesis of the 6 themes → `research/synthesis-themes.md`: Theme 1 prevalence (61/71 = 86% gap > 0; median 0.125; compositional benchmarks largest), Theme 2 detection (21 measured; proxies rare; corr gap↔σ-rel 0.126), Theme 3 interventions (k = 1), Theme 4 architecture (transformer 0.285 k = 30), Theme 5 scale (untestable), Theme 6 safety connection (192/286 σ-relevant vs 271/286 low alignment-relevance); SoF skeleton → completed table (§7). CC.1.9 satisfied.

**Task 9.3.** `analysis/feasibility-report.md`: intervention meta-analysis **NOT feasible** (k = 1, documented reasons, harvest plot in place of forest plot); ID–OOD gap meta-analysis **FEASIBLE** (k = 23–64 ≥ 5, ≥ 10 for meta-regression); heterogeneity I² 55–91% handled per SAP-3. CC.1.9 satisfied.

**Task 9.4 (adapted).** `analysis/run_meta_analysis.py` (DL random-effects via pre-existing `meta_analysis.py`): pooled gap S0 0.220 [0.176, 0.264] k = 64; S3 0.258 [0.153, 0.362] k = 27; S4 0.321 [0.221, 0.421] k = 23; S5 0.306 [0.233, 0.379] k = 27 (all p < 0.001); subgroups (S3): compositional benchmarks 0.699 [0.598, 0.799] k = 5 vs custom 0.186 k = 19; transformer 0.266 k = 10; small 0.446 k = 4 vs medium/large 0.076 k = 4; meta-regression on year slope −0.051/yr (p = 0.001, k = 64) **with benchmark-mix confound caveat**; outlier sensitivity (no change — outlier lacked variance); forest plots + harvest plot in `analysis/figures/` (PNG/PDF/SVG). CC.4.5 satisfied.

**Task 9.5.** `analysis/pub_bias.py`: funnel plots (S3, S5), Egger's regression (intercept p = 0.219 / 0.274 — no significant asymmetry), trim-and-fill (10 / 4 trimmed; adjusted gap 0.075 / 0.059, still positive); caveats documented (underpowered Egger, crude trim-fill CIs, heterogeneity confound). CC.1.10 satisfied.

**Task 9.6.** GRADE rated **Very Low** for every outcome with explicit per-domain reasons (RoB 96.2% HIGH, indirectness, I² 55–91%, imprecision); SoF table populated in `synthesis-themes.md` §7.

**Task 9.7.** `research/synthesis-log.md` — decision log D1–D9 with rationale, Anti-JAIR interpretation statement (one claim: high-ID/low-OOD gap is modal and significant; largest on compositional benchmarks; no intervention estimate exists), archive inventory. Scripts documented + version-controlled (CC.4.6).

**Verification.** Independent recomputation of S3 pooled gap matched meta-results.md exactly (k = 27, 0.258 [0.153, 0.362], I² 91%); ruff clean on all three analysis scripts; figures archived.

**Exit criteria (CC.5.3 — phase completion committed):**
- [x] Synthesis dataset prepared with derived variables
- [x] Narrative thematic synthesis complete (all 6 themes)
- [x] Meta-analysis feasibility documented (incl. k = 1 intervention finding)
- [x] Meta-analysis conducted: forest plots, subgroup analyses, sensitivity (primary = ID–OOD gap per amendment)
- [x] Publication bias assessment completed
- [x] GRADE assessment completed (Very Low, pre-specified)
- [x] SoF table generated
- [x] All analysis scripts and figures archived
- [x] CC.1.9, CC.1.10, CC.4.5, CC.4.6 (Paper-02 meanings) satisfied
- [x] CC.5.3 (phase completion committed) satisfied
