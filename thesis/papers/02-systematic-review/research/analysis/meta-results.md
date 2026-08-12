# Meta-analysis results — Paper 02 Phase 9 (9.4)

Random-effects (DerSimonian-Laird) pooling of the ID-OOD gap. Variance from charted gap SE or binomial SE.

## Strata

| Stratum | k | pooled gap | 95% CI | I² | τ² | p |
|---|---|---|---|---|---|---|
| S0 (all) | 64 | 0.220 | [0.176, 0.264] | 71% | 0.0268 | 0.000 |
| S3 (peer-reviewed) | 27 | 0.258 | [0.153, 0.362] | 91% | 0.0711 | 0.000 |
| S4 (code) | 23 | 0.321 | [0.221, 0.421] | 91% | 0.0558 | 0.000 |
| S5 (seeds>=3) | 27 | 0.306 | [0.233, 0.379] | 55% | 0.0268 | 0.000 |

## Sensitivity (outlier excluded)

- S0 (all) (no outlier): 64 studies, pooled 0.220 [0.176, 0.264]
- S3 (peer-reviewed) (no outlier): 27 studies, pooled 0.258 [0.153, 0.362]
- S4 (code) (no outlier): 23 studies, pooled 0.321 [0.221, 0.421]
- S5 (seeds>=3) (no outlier): 27 studies, pooled 0.306 [0.233, 0.379]

## Subgroups (S3 stratum)

- compositional benchmarks: k=5, pooled 0.699 [0.598, 0.799], I²=22%
- custom benchmarks: k=19, pooled 0.186 [0.145, 0.227], I²=58%
- transformer: k=10, pooled 0.266 [-0.039, 0.571], I²=96%
- non-transformer: k=17, pooled 0.257 [0.191, 0.323], I²=73%
- small scale: k=4, pooled 0.446 [0.160, 0.733], I²=90%
- medium/large scale: k=4, pooled 0.076 [-0.091, 0.244], I²=58%

## Meta-regression (year)

- k=64, slope -0.0514 per year (SE 0.0140, p=0.001)
