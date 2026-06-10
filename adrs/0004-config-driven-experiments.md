# ADR 0004: Config-Driven Experiments

**Date:** 2026-03-30  
**Status:** Accepted  
**Author:** Infrastructure Setup (Phase 0)

## Context

Both experiment notebooks contained hardcoded parameters (learning rates, batch sizes, threshold values). This caused bugs — `SIGMA_CRITICAL` was 0.15 in Cell 4 (training logic) but 0.25 in Cells 7/9/11 (diagnostic plots). Parameter changes required editing notebook cells directly, with no version history or audit trail.

## Decision

1. All experiment parameters are defined in YAML files under `/experiments/configs/`
2. `configs/base.yaml` contains shared parameters (ODE thresholds, model architecture, training loop)
3. Each benchmark (`h-ptb.yaml`, `h-afb.yaml`, etc.) has its own config with benchmark-specific params
4. Notebooks load configs via `sigma.config.load_config()` at startup
5. A `merge_configs()` function allows benchmark configs to override base values

## Consequences

- The `SIGMA_CRITICAL` inconsistency is fixed (canonical value: 0.15, documented in `base.yaml`)
- `COUPLING_MULTIPLICATIVE` is 0.20 (matching Cell 4 training logic), not 0.30
- Parameter changes are tracked in Git as YAML diffs
- Reproducing an experiment requires only the config file, commit hash, and seed
- Notebooks become thin orchestration; all domain logic lives in `code/sigma/`
