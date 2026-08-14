# Synthesis Log — Paper 02 Phase 9 (Task 9.7.1)

All synthesis decisions and their rationale, for auditability (CC.4.6).

## Decision log

| # | Decision | Rationale | Where |
|---|---|---|---|
| D1 | Primary effect = **ID–OOD gap prevalence**; intervention effect narrative-only | k = 1 σ-intervention study (S046); 280/286 `train_regime_sigma` = not_applicable; Phase 8 D3 N/A for 224. Amends `meta-analysis-feasibility.md` SAP-1 per its fallback path. | `phases/09_synthesis.md` Operationalizations; `analysis/feasibility-report.md` |
| D2 | LOR with 0.5/n continuity correction; Cohen's d only where both SDs present | Standard practice; SDs sparse (32 ID / 60 OOD) | `analysis/prepare_analysis_data.py` |
| D3 | Gap variance: charted `id_ood_gap_se`, else binomial SE from accuracies; studies without any variance excluded from pooling, kept in narrative | 14/71 charted SEs; keeps pooling principled | `analysis/prepare_analysis_data.py`; `feasibility-report.md` §9.3.6 |
| D4 | Outlier rule |z| > 3 (1 flagged); sensitivity with/without | S0 gap sd 0.31, min −1.158 | `prepare_analysis_data.py`; `meta-results.md` |
| D5 | I² > 75% → subgroup/meta-regression exploration, not abandonment | SAP-3 of `meta-analysis-feasibility.md` | `meta-results.md` |
| D6 | Subgroups: benchmark family (custom vs compositional CFQ/SCAN/COGS/gSCAN/GeoQuery), architecture (transformer vs other), scale (small vs medium/large); individual families k ≤ 6 → narrative | ≥5 pooling threshold per family unmet; collinearity of arch × benchmark noted | `meta-results.md`; `synthesis-themes.md` Theme 4 |
| D7 | Meta-regression on year only (k = 64 ≥ 10); slope −0.051/yr (p = 0.001) reported **with confound caveat** (later years dominated by custom/vision benchmarks with smaller gaps; not evidence of σ-trap resolution) | Small k per other moderators; benchmark-mix confound | `meta-results.md` |
| D8 | Publication bias: Egger + trim-and-fill on S3/S5 only; reported with caveats (underpowered Egger; crude fixed-effect trim-fill CIs; heterogeneity confound) | k ≥ 10; honesty about instrument limits | `analysis/pub-bias-results.md` |
| D9 | GRADE = **Very Low** for every outcome; SoF is a transparency instrument | 96.2% HIGH RoB; indirectness (prevalence); high I²; sparse precision | `synthesis-themes.md` §7 |

## Interpretation statement (Anti-JAIR discipline)

The one claim this synthesis supports: **the high-ID/low-OOD gap is the modal,
statistically significant pattern in the σ-trap corpus (pooled gap 0.22–0.32, all
strata p < 0.001), is largest on compositional benchmarks (0.70), and no
intervention-effectiveness estimate exists (k = 1).** The synthesis does NOT claim:
that the σ-trap causes alignment failure (Theme 6 shows 271/286 studies low on
alignment relevance), that proxies detect σ_A (Theme 2: none validated), or that
scale resolves the gap (Theme 5: k too small; the year trend is confounded).

## Archive (CC.4.5/CC.4.6)

- Scripts (version-controlled in `research/analysis/`, docstrings + usage):
  `prepare_analysis_data.py`, `run_meta_analysis.py`, `pub_bias.py` (+ pre-existing
  `meta_analysis.py` pooling functions).
- Outputs: `analysis-data.csv` + `analysis-data-report.md`; `meta-results.md`;
  `pub-bias-results.md`; `feasibility-report.md`; `synthesis-themes.md` (narrative +
  SoF, CC.1.9).
- Figures (`research/analysis/figures/`, PNG/PDF/SVG): `forest-strata`,
  `forest-strata-nooutlier`, `forest-subgroups`, `harvest-interventions`,
  `funnel-S3`, `funnel-S5`.
