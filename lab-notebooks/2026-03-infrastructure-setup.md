# Lab Notebook: Phase 0 Infrastructure Setup

**Date:** 2026-03-30  
**Author:** Infrastructure Setup  
**Status:** Complete

## Objective

Initialize a maintainable monorepo structure for the Σ-Model Model V3.0+ project, with strict separation between paper source, modular code, configuration, documentation, and artifacts.

## Findings

### Notebook Bugs Discovered

1. **`SIGMA_CRITICAL` inconsistency**: Cell 4 uses 0.15 (actual training threshold), Cells 7/9/11 use 0.25 (diagnostic plots). Cell 11 comment says "must match Cell 4" but value is 0.25.
2. **`COUPLING_MULTIPLICATIVE` mismatch**: Cell 4 uses 0.20, Cell 10 diagnostic uses 0.30.

Both fixed in `configs/base.yaml` (canonical values: 0.15, 0.20).

### Structure Created

```
/code/sigma/          – 8 modules (ode, models, benchmarks, config, utils)
/experiments/configs/ – 6 YAML files (base + 5 benchmarks)
/paper/              – Makefile, pandoc template, figures/
/docs/adrs/          – 4 ADRs (monorepo, pandoc, claims-tracking, config-driven)
/artifacts/          – Model cards, datasheets
/scripts/            – monitor-pub.py
/docs/claims-registry.md – 20 claim entries mapped to paper lines
```

### Pending

- Kaggle results (post-June 1 2026) to populate claims C-009 through C-020
- Human baseline data collection (N=200 Prolific)
