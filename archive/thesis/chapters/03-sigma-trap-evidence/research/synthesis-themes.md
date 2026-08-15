# Narrative Thematic Synthesis — Paper 02 Phase 9 (Task 9.2)

**Inputs**: `research/analysis/analysis-data.csv` (286 studies; 71 with ID–OOD gap),
`research/risk-of-bias.csv` (Phase 8), `research/charted-data-main.csv`,
`research/gap-analysis.md` (Paper 01) · **Method**: six pre-specified themes (9.2.1),
synthesised across studies with consistent findings, contradictions, and gaps (9.2.2);
SoF skeleton in §7 (9.2.3); CC.1.9 satisfied — narrative synthesis complete regardless
of meta-analysis feasibility.

---

## Theme 1 — σ-trap prevalence (high-ID / low-OOD pattern)

**Evidence.** Of the 71 studies with both ID and OOD accuracy, **61 (86%) exhibit a
positive ID–OOD gap** (gap > 0.1 in 39 studies; median gap 0.125, IQR 0.036–0.369;
outlier 1). The pattern is consistent across benchmark families, architectures, and
training regimes: compositional benchmarks show the largest mean gaps (CFQ 0.488,
COGS 0.467, gSCAN 0.280, GeoQuery 0.282, SCAN 0.221; custom 0.153); by architecture,
transformers (k = 30, mean 0.285) and MLPs (0.282) lead, while ViTs (0.089) and GNNs
(0.109) are smallest.

**Synthesis.** The high-ID/low-OOD pattern is the modal outcome of the empirical
σ-trap corpus: roughly six of seven studies with comparable accuracies report a
non-trivial gap. The pattern holds across the three axes the theme asked about
(benchmarks, architectures, regimes). Contradictions: 10/71 studies (14%) show no
gap or a negative gap, concentrated in vision/shift benchmarks (Waterbirds,
ColoredMNIST, Camelyon17 — mean gaps ≤ 0.06) and in the scale tail.

**Gap.** The corpus is dominated by a single "custom" benchmark family (43/71), and
71/286 studies (25%) report both accuracies at all — prevalence is estimated from a
credibility-limited subset.

## Theme 2 — σ-trap detection (proxy measures)

**Evidence.** Only 21/286 studies (7.3%) report measuring schema coherence directly
(`schema_coherence_measured` = TRUE); 5 report an intervention value. Representation
analysis is present in 88 studies (attention patterns 18, probing 9, PCA 4, clustering
3, activation max 1, other 53), and explicit coherence proxies are rare (linear probe
accuracy 4, compositionality score 3, mutual information 2, effective rank 2).
Correlation between the charted σ-trap relevance rating and the measured gap is weak
(r = 0.126, n = 71).

**Synthesis.** There is no established proxy for low σ_A in the corpus: measurement is
sporadic, heterogeneous, and unvalidated. The strongest statement the evidence
supports is negative — no proxy correlates with OOD performance in a replicated way.

**Gap.** This is the single largest methodological hole and the direct target of the
thesis's measurement programme (Paper 03).

## Theme 3 — Intervention effectiveness

**Evidence.** Exactly **one** study (S046, E2A/SAM on graph generalization) applies a
σ-targeting intervention (`train_regime_sigma` = other_sigma) with a standard-Adam
baseline; it reports no charted ID/OOD accuracies. A further 62 studies chart a
baseline regime, but none applies a σ-coupled training intervention.

**Synthesis.** No meta-analysis of intervention effectiveness is possible (k = 1);
effect sizes for interventions cannot be estimated. The literature simply has not
run controlled σ-intervention-vs-baseline comparisons at scale.

**Gap.** This is the empirical vacuum that Papers 04/07 (σ-coupling interventions)
and the pilot study are designed to fill.

## Theme 4 — Architecture effects

**Evidence.** With gap data: transformers k = 30 (mean gap 0.285), neurosymbolic 10
(0.185), RNN 6 (0.206), MLP 5 (0.282), GNN 5 (0.109), CNN 4 (0.165), ViT 4 (0.089).

**Synthesis.** Transformer-based and MLP models dominate the largest gaps; GNN and
ViT families show smaller gaps on their (mostly vision/custom) benchmarks. Whether
architectures "resist" the σ-trap cannot be separated from benchmark confounds in
this corpus: architecture and benchmark family are collinear.

**Gap.** No study varies architecture while holding benchmark and training regime
fixed.

## Theme 5 — Scale effects

**Evidence.** With gap data: small (k = 11, mean 0.143), medium (k = 4, 0.251), large
(k = 3, 0.000; median −0.035), unspecified (k = 53, 0.232). k is tiny in every
scale class and model scale is unspecified for 74% of gap-bearing studies.

**Synthesis.** No credible scale trend can be estimated. The suggestive pattern
(large models show no gap) rests on three studies and is confounded by benchmark.

**Gap.** Scale-resolution of the σ-trap is untested; the corpus cannot adjudicate the
"capabilities outpace alignment" claim (Paper 01 G5a).

## Theme 6 — Safety connection

**Evidence.** 192/286 studies (67.1%) are charted σ-trap-relevant (relevance ≥ 4), but
**271/286 (94.8%) are rated low on alignment relevance** (relevance 1–2). The σ-trap
and alignment signals are charted independently and barely overlap.

**Synthesis.** The corpus is σ-trap-relevant by construction (it is the systematic
review's inclusion criterion), yet almost none of it connects the σ-trap to alignment
failure modes. The alignment connection exists in the charted annotations, not in the
papers' own claims.

**Gap.** Consistent with Paper 01 G2: the compositional-generalisation↔alignment
bridge is absent from the literature itself.

---

## 7. Summary of findings (SoF) table — GRADE

| Outcome | k | Pooled ID–OOD gap (95% CI) | I² | Risk of bias | GRADE | Reasons |
|---|---|---|---|---|---|---|
| σ-trap prevalence (S0 all) | 64 | 0.220 [0.176, 0.264] | 71% | High | Very Low | RoB (96.2% HIGH), indirectness, heterogeneity |
| σ-trap prevalence (S3 peer-reviewed) | 27 | 0.258 [0.153, 0.362] | 91% | High | Very Low | RoB, heterogeneity |
| σ-trap prevalence (S5 seeds≥3) | 27 | 0.306 [0.233, 0.379] | 55% | High | Very Low | RoB, indirectness |
| Compositional benchmarks (S3) | 5 | 0.699 [0.598, 0.799] | 22% | High | Very Low | RoB, small k |
| Proxy detection validity | 21 | n/a (narrative) | n/a | High | Very Low | no validated proxy |
| Intervention effectiveness | 1 | n/a (k = 1, harvest plot) | n/a | High | Very Low | k = 1, no effect size |

GRADE ratings are **Very Low** for every outcome: 96.2% of studies are high RoB
(Phase 8) → downgrade 2 levels; the primary effect is indirect (prevalence, not an
intervention contrast); heterogeneity is high (I² 55–91%); precision is limited by
sparse variance data (14/71 charted SEs) and the trim-and-fill shrinkage. The SoF
table is a transparency instrument: it reports the direction (positive pooled gap)
while flagging that the confidence band around the magnitude is wide and the
credibility of the underlying studies is low.
