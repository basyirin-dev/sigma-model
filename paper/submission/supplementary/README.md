# Supplementary Material: Code, Data, and Companion Technical Report

**Manuscript:** *Compositional Generalization as a Threshold Phase Transition: Why Adaptive Curricula are Unnecessary for Asymptotic Recovery*  
**Review Mode:** Double-Blind Submission (Anonymized)

---

## 1. Overview and Contents

This supplementary package provides full documentation, self-contained standalone source code, configuration files, and raw multi-seed experimental data to reproduce all empirical and theoretical findings reported in the main manuscript:

```
├── companion.pdf              # 24-page anonymized companion technical report (extended framework & data)
├── README.md                  # Comprehensive reproduction and schema documentation (this file)
├── configs/
│   └── gate.yaml              # Complete experiment configuration (all hyperparameters, seeds, conditions)
├── code/
│   ├── __init__.py
│   ├── hbar_data.py           # Self-contained H-Bar benchmark generator (SCAN-style grammar)
│   ├── hbar_model.py          # 2-layer, 4-head sequence-to-sequence Transformer architecture
│   ├── hbar_proxy.py          # Stage-1 online proxy estimation (GCA and RGA algorithms)
│   └── hbar_train.py          # Standalone training harness (baseline, fixed-weight, additive, multiplicative)
└── data/
    ├── gate-results/          # 60 per-run pickle files (4 experimental arms × 15 independent seeds)
    │   ├── baseline_run0.pkl ... baseline_run14.pkl
    │   ├── fixed_weight_run0.pkl ... fixed_weight_run14.pkl
    │   ├── additive_run0.pkl ... additive_run14.pkl
    │   └── multiplicative_run0.pkl ... multiplicative_run14.pkl
    ├── all_results.pkl        # Consolidated dictionary containing all 60 trajectory records
    ├── trajectories.csv       # Flattened step-by-step metric logs across all runs
    ├── summary.json           # Aggregated statistical metrics, effect sizes, and TOST bounds
    └── gate_summary.png       # Consolidated trajectory comparison plot
```

---

## 2. Environment Setup and Dependencies

The codebase requires Python 3.10+ and standard PyTorch ecosystem libraries. No proprietary or specialized hardware packages are needed.

### Prerequisites
```bash
pip install torch numpy scipy pandas pyyaml tqdm matplotlib
```

### Hardware Requirements
- **Compute:** CPU-compatible for inspection/evaluation; standard GPU (e.g., NVIDIA RTX 3090/4090 or T4/V100/A100) recommended for rapid multi-seed training sweeps.
- **Precision:** Automatic Mixed Precision (`torch.amp`) enabled by default on CUDA devices.

---

## 3. Instructions for Reproducing Experiments

All experimental conditions, hyperparameters, and seeds are managed through `configs/gate.yaml` (ADR-0004 standard).

### A. Running a Single Training Seed
To execute an individual run (e.g., the discriminating static `fixed_weight` condition with seed 0):
```bash
python -m code.hbar_train --config configs/gate.yaml --condition fixed_weight --run-id 0
```

### B. Running Experimental Conditions
To train specific experimental arms:
- **Baseline ERM (Standard Training):**
  ```bash
  python -m code.hbar_train --config configs/gate.yaml --condition baseline --run-id 0
  ```
- **Fixed-Weight Compositional Loss ($\lambda=1.0$, Constant):**
  ```bash
  python -m code.hbar_train --config configs/gate.yaml --condition fixed_weight --run-id 0
  ```
- **Additive $\sigma$-Modulated Curriculum:**
  ```bash
  python -m code.hbar_train --config configs/gate.yaml --condition additive --run-id 0
  ```
- **Multiplicative $\sigma$-Modulated Curriculum:**
  ```bash
  python -m code.hbar_train --config configs/gate.yaml --condition multiplicative --run-id 0
  ```

### C. Extended-Horizon Grokking Controls
To evaluate the 20,000-step extended training duration ($10\times$ standard horizon):
```bash
python -m code.hbar_train --config configs/gate.yaml --condition baseline --timesteps 20000 --run-id 0
```

---

## 4. 60-Run Raw Data Schema and Structure

The `data/` directory contains complete per-seed trajectories for all $N=60$ runs ($4 \text{ conditions} \times 15 \text{ seeds}$, evaluated every 25 steps across 2,000 steps).

### Per-Run File Format (`<arm>_run<N>.pkl`)
Each `.pkl` file contains a Python dictionary with two top-level keys:
1. `config`: Dictionary of run hyperparameters (`condition`, `run_id`, `n_timesteps`, `seed = run_id * 42 + 7`).
2. `metrics`: Dictionary mapping metric names to time-series lists (evaluated every 25 steps):
   - `step`: Integer training step ($0, 25, 50, \dots, 2000$).
   - `loss`: Cross-entropy task training loss.
   - `acc_id`: In-distribution (ID) test sequence accuracy $\in [0, 1]$.
   - `acc_ood`: Out-of-distribution (OOD) zero-shot compositional sequence accuracy $\in [0, 1]$.
   - `sigma_tilde`: Measured Stage-1 fused proxy ($\tilde{\sigma}_A = 0.5 \cdot \text{GCA} + 0.5 \cdot \text{RGA}$).
   - `gca`: Gradient-Composition Alignment score $\in [0, 1]$.
   - `rga`: Representational-Geometry Alignment score via CKA $\in [0, 1]$.
   - `sigma_sched`: Scheduled heuristic curriculum value (for additive/multiplicative comparisons).
   - `phase`: Discrete curriculum state indicator (0: Pre-domain, 1: Depth accumulation, 2: Coherent recovery).
   - `lr_eff`: Effective learning rate at the evaluation step.
   - `param_norm`: $\ell_2$ Frobenious norm of model parameter weights.
   - `final`: Final evaluation dictionary containing terminal test accuracies.

### Reading Data Example in Python
```python
import pickle

with open("data/gate-results/fixed_weight_run0.pkl", "rb") as f:
    run_data = pickle.load(f)

print("Condition:", run_data["config"]["condition"])
print("Final OOD Accuracy:", run_data["metrics"]["acc_ood"][-1])
print("Measured Proxy:", run_data["metrics"]["sigma_tilde"][-1])
```

---

## 5. Companion Technical Report (`companion.pdf`)

The included 24-page document `companion.pdf` provides complementary theoretical analyses and framework extensions:
1. **The Full Two-Tier Proxy Architecture:** GCA, RGA, and AC mathematical definitions, estimation bounds, and Stage-2 calibration theorems.
2. **Cognitive-Dimension Extensions:** Attentional fidelity ($\alpha_A$), executive control ($\Xi_A$), metacognitive self-modelling, and collective schema fields.
3. **Multimodal Machinery:** Domain $\times$ modality product spaces and cross-modal schema transfer formulations.
4. **Extended Mechanism-Gate Data:** Per-seed trajectory logs, individual metric breakdowns, and detailed diagnostic correlations.

---

## 6. Expected Results and Statistical Interpretation

- **Equivalence of Static vs. Dynamic Supervision:** Terminal OOD accuracy for `fixed_weight` ($98.9 \pm 3.6\%$) matches adaptive curricula ($98.9 \pm 2.4\%$), yielding Welch $p = 0.99$ and passing Two-One-Sided Tests (TOST) within $\pm 2.5\%$.
- **Absence of Spontaneous Grokking:** Extended 20,000-step baseline ERM saturates at $98.7\%$ ID accuracy but remains arrested at $34.7\%$ OOD accuracy.
- **Latency Ordering:** Segmented regression inflection points follow the ODE-predicted ordering: $\hat{\tau}_{\text{fixed}} \approx 148 < \hat{\tau}_{\text{mult}} \approx 340 < \hat{\tau}_{\text{add}} \approx 542$ steps.

---

## 7. License

- **Code:** Open source under the MIT License / Apache-2.0.
- **Data & Documentation:** Licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
