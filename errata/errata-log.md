# Errata Log

| Date | ID | File | Error | Fix | Status |
|------|----|------|-------|-----|--------|
| 2026-03-30 | E-001 | `experiments/sigma-experiment.ipynb`, Cells 7, 9, 11 | `SIGMA_CRITICAL` set to 0.25 in diagnostic plots; actual training threshold in Cell 4 is 0.15 | Canonical value set to 0.15 in `experiments/configs/base.yaml`. Plots now reference config. | FIXED |
| 2026-03-30 | E-002 | `experiments/sigma-experiment.ipynb`, Cell 10 | `COUPLING_MULTIPLICATIVE` set to 0.30 in loss modulation diagnostic; actual Cell 4 training value is 0.20. Cell 4 comment also incorrectly says "30% peak effect" for multiplicative. | Canonical value set to 0.20 in `experiments/configs/base.yaml`. Comment corrected. | FIXED |
