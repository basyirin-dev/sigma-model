# Lab Notebook: Pre-Submission Audit & Accessibility Fixes

**Date:** 2026-06-10  
**Author:** Sigma Model V3.0+  
**Status:** Complete

## Objective

Perform pre-submission codebase audit: verify experimental reproducibility, fix figure accessibility (colourblind-safe, greyscale, alt-text), clarify manuscript prose, document failed experiments, and clean up stale artifacts.

## Findings

### 1. Reproducibility Verification

| Check | Result |
|-------|--------|
| `verify_table5.py` | 15/15 PASS — all values match manuscript |
| `verify_empirical_claims.py` | All claims PASS — body text, statistical tests, sigma trajectories |
| `generate_figures.py` | 3 figures regenerated from canonical pkl |
| `make pdf` | 37 pages, 2.1 MB, 0 errors |

### 2. Pilot Bug Discovered: `batch_first=True`

**What happened:** The `kaggle-pilot-optimised.ipynb` notebook was missing `batch_first=True` in `nn.Transformer` (Cell 2). The model received inputs shaped `(B, S, d)` but without `batch_first=True`, PyTorch's Transformer expected `(S, B, d)`.

**Impact:** Systematic OOD accuracy drop of ~7pp (87.4% vs manuscript 94.1%). Deterministic re-runs (`cudnn.benchmark=False`) confirmed the drift was not cuDNN noise but the `batch_first` bug.

**Resolution:** Abandoned pilot notebook. Canonical source is `experiments/h-bar-experiment.ipynb`, which reproduces manuscript values exactly. Pilot notebook marked as DEPRECATED with full failure mode documentation.

### 3. Figure Accessibility Fixes

- Added `\Description{...}` alt-text to all 7 figure environments in `manuscript.tex`
- Embedded EXIF metadata (Description field) in all 3 PNG figures via `generate_figures.py`
- Figure 2: Changed `alpha_A` curve from `dotted` to `densely dashed` for greyscale distinguishability
- Figure 4: Added black `north east lines` pattern to green target quadrant; red quadrant pattern color changed to black

### 4. Manuscript Prose Enhancements

Approximately 200 lines edited across all sections:
- **Signpost injection:** Every section now opens with a "why this matters" sentence
- **Active voice conversion:** ~30 passive constructions replaced (e.g., "It was observed that..." → "We observe that...")
- **Dense math intuition:** Added plain-English analogies (cyclist for Fenichel timescale separation, calculator for shortcut learning, epidemic R_0 for schema growth ratio)
- **Weak transitions strengthened:** Between §2→§3, §3.1→§3.2, §3→§4, §4→§5

### 5. Failed Experiment Documentation

4 artifacts tagged with explicit failure modes (see `archive/FAILURE_MANIFEST.md`):
- `kaggle-pilot-optimised.ipynb` — batch_first bug
- `benchmark_pilot.py` — hardware incompatibility
- `new_results_b64` — systematic drift (same batch_first bug)
- `results_smoke` — underpowered

### 6. Cleanup Actions

- **Deleted:** Root LaTeX build artifacts (`.aux`, `.bbl`, `.blg`, `.fdb_latexmk`, `.fls`, `.log`, `.out`)
- **Deleted:** `opencode.json.bak`, `opencode.json.bak2`
- **Deleted:** Empty scaffolding directories (`experiments/output/checkpoints/`, `logs/`, `models/`, `results/`)
- **Deleted:** `.DS_Store` from SCAN dataset
- **Archived:** `new_results_b64/` → `archive/new_results_b64.tar.gz`
- **Archived:** `experiments/output/results_smoke/` → `archive/results_smoke.tar.gz`
- **Added to `.gitignore`:** `*.synctex.gz`, `*.toc`, `*.lof`, `*.lot`

### 7. Hyperparameters (Canonical Experiment)

| Parameter | Value |
|-----------|-------|
| Architecture | Transformer (2 layers, 4 heads, d_model=128) |
| Training steps | 2000 |
| Batch size | 64 |
| Learning rate | 0.001 |
| Max sequence length | 50 |
| Gradient clip norm | 1.0 |
| AMP | True |
| Global seed | 2024 |
| cuDNN benchmark | False |
| cuDNN deterministic | True |
| Conditions | 3 (baseline, additive, multiplicative) |
| Runs per condition | 15 |
| Evaluation interval | Every 10 steps |
| GPU | NVIDIA Tesla T4 (via Kaggle) |

## Pending

- Full `N=500` protocol execution (pilot at `N=15` complete)
- Docstrings for remaining `code/sigma/` functions (core 5 completed today)
