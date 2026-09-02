# 03 — Research Trajectories & 12-Month Execution Matrix

---

## 1. Portfolio Architecture (A $\to$ B $\to$ C Pipeline)

The research program is organized into three compounding trajectories.

```
┌───────────────────────────────────────┐
│ TRAJECTORY A (50% Effort):            │ ──> Theoretical Foundations & Phase-Boundary Laws
│ Critical Threshold Control Theory     │     (Proves and predicts when representations reorganize)
└──────────────────┬────────────────────┘
                   ▼
┌───────────────────────────────────────┐
│ TRAJECTORY B (30% Effort):            │ ──> Geometric Instrumentation & Order Parameters
│ Representation Geometry & Probing     │     (Measures and tracks schema emergence online)
└──────────────────┬────────────────────┘
                   ▼
┌───────────────────────────────────────┐
│ TRAJECTORY C (20% Effort):            │ ──> Architecture & Domain Application Engines
│ Verified Neuro-Symbolic Reasoning     │     (Scales to automated mathematics, physics & biology)
└───────────────────────────────────────┘
```

---

## 2. Detailed Trajectory Specifications

### Trajectory A: Critical Threshold Control Theory (Lead Program)
* **Core Thesis:** Compositional generalization is governed by a supercritical phase transition ($R_0 > 1$). Optimization dynamics near the boundary are low-dimensional and universal across architectures.
* **6–12 Month Milestones:**
  1. *Dense $\lambda$-Sweep:* Sweep $\lambda \in [0, 2.0]$ across 30 seeds to measure the empirical critical boundary $\hat{\lambda}_{\text{crit}}$ on H-Bar, SCAN, and COGS.
  2. *Late-Intervention Grid:* Initiate compositional loss at steps $t_{\text{int}} \in \{0, 100, 250, 500, 1000\}$ to empirically map the basin of attraction separatrix.
  3. *Two-Subspace Theorem:* Publish formal proof connecting gradient flow transverse eigenvalues to $\lambda_{\text{crit}}$.
* **3–5 Year Frontier:** A universal scaling law for structural intelligence that predicts $\lambda_{\text{crit}}$ for arbitrary deep architectures.
* **Fatal Failure Mode:** If the threshold $\lambda_{\text{crit}}$ fluctuates wildly and unpredictably across seeds and benchmark variants, indicating that the bifurcation is an artifact of synthetic toy grammars.

### Trajectory B: Geometric Order Parameters & Representation Probing
* **Core Thesis:** Global representation geometry (CKA, principal subspace angles) reliably predicts structural phase transitions, whereas local gradient alignment (GCA) is plagued by initialization artifacts.
* **6–12 Month Milestones:**
  1. *Layerwise CKA Battery:* Build an automated diagnostic suite measuring internal representational dissimilarity matrices against task grammar graphs.
  2. *Whitened / Projected GCA:* Formalize the mathematical correction to GCA (projecting out the shared input embedding subspace) to eliminate the step-0 $0.95$ artifact.
  3. *Lead-Lag Granger Causality:* Prove that $\Delta \text{RGA}_{t \to t+k}$ Granger-causes $\Delta \text{OOD}_{t+k \to t+2k}$.
* **3–5 Year Frontier:** Real-time closed-loop training controllers that modulate data sampling and auxiliary losses based on live representation geometry.
* **Fatal Failure Mode:** If representation geometry shifts only *after* behavioral accuracy changes, rendering RGA an epiphenomenon rather than a predictive order parameter.

### Trajectory C: Verified Neuro-Symbolic Schema Engines
* **Core Thesis:** General reasoning requires coupling differentiable neural pattern discovery with explicit symbolic verifier feedback loops.
* **6–12 Month Milestones:**
  1. *Grammar-Latent Transformer:* Build a seq2seq architecture with explicit latent operator-tree bottleneck variables.
  2. *Verifier-in-the-Loop:* Integrate formal checking (finite-state syntax validator, RDKit valence checker, or Lean 4 proof checker) into the reward loop.
  3. *Zero-Leakage Guarantee:* Mathematically audit and prove zero support overlap between training substitutions and OOD evaluation splits.
* **3–5 Year Frontier:** Autonomous theorem-proving and scientific hypothesis generation engines.
* **Fatal Failure Mode:** If discrete symbolic bottlenecks prevent gradient propagation, causing optimization to stall in non-differentiable plateaus.

---

## 3. 12-Month Resource & Execution Realism

### Compute Tiers
* **Tier 1 (Small Compute / Rapid Iteration):** 1–4 GPUs (Tesla T4 / RTX 3090). 
  - Used for: Dense $\lambda$-sweeps, late-intervention grids, toy dynamical simulations, CKA probing.
  - Budget: ~60–200 GPU hours.
* **Tier 2 (Medium Compute / Benchmark Verification):** 8–32 A100 GPU hours.
  - Used for: SCAN/COGS multi-seed replications, scaling to 100M parameter models.

### Day-One Experimental Protocol
```bash
# Protocol: Dense Phase Boundary Sweep + Late-Onset Intervention
# Grid: λ ∈ {0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0}
# Late-Onset: t_int ∈ {0, 100, 250, 500, 1000}
# Seeds: n = 30 per cell

python -m sigma_align.experiments.phase_sweep \
    --config code/experiments/phase_boundary_grid.yaml \
    --metrics ood_acc id_acc cka_rga param_norm \
    --output archive/phase_sweep_results/
```
