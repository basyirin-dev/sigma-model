# 01 — Theoretical Foundations & The Two-Subspace Minimal Model

## 1. Problem Formulation: The $\Sigma$-Trap

In empirical risk minimization (ERM), neural networks optimize parameters $w \in \mathbb{R}^D$ on in-distribution dataset $\mathcal{D}_{\text{train}}$:
$$\mathcal{L}_{\text{task}}(w) = \mathbb{E}_{(x, y) \sim \mathcal{D}_{\text{train}}} [\ell(f_w(x), y)]$$

When the task permits shortcut solutions (surface statistical heuristics correlated with labels in-distribution but uninformative out-of-distribution), the optimization landscape exhibits multiple basins of attraction with identical or near-identical empirical risk but radically divergent generalization geometries.

The $\Sigma$-Model decomposes representation state into two macroscopic coordinates:
1. **Parametric Depth ($\delta_A \in [0, 1]$):** Specialization to task surface statistics.
2. **Schema Coherence ($\sigma_A \in [0, 1]$):** Internal representational reorganization around invariant compositional operators.

Standard ERM drives the system to the **shortcut equilibrium**:
$$E_S = (\delta_A^*, 0)$$
where $\delta_A \approx 1$ and $\sigma_A \approx 0$, yielding high in-distribution accuracy ($\ge 90\%$) but near-complete compositional failure ($45.9\%$ OOD on H-Bar).

---

## 2. Derivation of the Two-Subspace Minimal Model

To bridge the gap between phenomenological ODEs and microscopic gradient flow (closing Conjecture 1 of the manuscript), we construct a minimal two-subspace linear model.

### 2.1 Parameter and Feature Decomposition
Let the input space decompose into two orthogonal subspaces:
$$x = (s, c) \in \mathbb{R}^{d_S} \times \mathbb{R}^{d_C}$$
where:
- $s$ represents task-shortcut features (sufficient to solve $\mathcal{D}_{\text{ID}}$).
- $c$ represents compositional/schema features (necessary to solve $\mathcal{D}_{\text{OOD}}$).

Let the linear student network have parameter $w = (u, v) \in \mathbb{R}^{d_S} \times \mathbb{R}^{d_C}$:
$$f_w(x) = u^\top s + v^\top c$$

### 2.2 Objective Functions
1. **Task Loss (ERM):**
   $$\mathcal{L}_{\text{task}}(u, v) = \frac{1}{2} \mathbb{E}_{(s, c, y) \sim \mathcal{D}_{\text{ID}}} \left[ (u^\top s + v^\top c - y)^2 \right]$$
   Because in-distribution labels are strongly correlated with $s$, the gradient along $u$ dominates:
   $$\nabla_u \mathcal{L}_{\text{task}} \approx a_S (u - \theta_S), \quad \nabla_v \mathcal{L}_{\text{task}} \approx b_C v + \mathcal{O}(v^2)$$
   where $b_C > 0$ represents the shortcut-pressure erosion that decays schema alignment in the absence of explicit structural supervision ($\Omega_{SL}$).

2. **Compositional Supervision Loss:**
   $$\mathcal{L}_{\text{comp}}(u, v) = \frac{1}{2} \mathbb{E}_{(x, x') \sim \mathcal{D}_{\text{equiv}}} \left[ (f_w(x) - f_w(x'))^2 \right]$$
   where $\mathcal{D}_{\text{equiv}}$ applies primitive substitutions that preserve invariant semantics. Under substitution transformations, shortcut features vary while schema features are invariant, generating gradient pressure exclusively along the schema subspace:
   $$\nabla_u \mathcal{L}_{\text{comp}} \approx b_S u, \quad \nabla_v \mathcal{L}_{\text{comp}} \approx -a_C v + \kappa v^2$$

### 2.3 Continuous Gradient Flow
Under total loss $\mathcal{L}_{\text{total}} = \mathcal{L}_{\text{task}} + \lambda \mathcal{L}_{\text{comp}}$, the projected gradient flow dynamics are:
$$\dot{u} = -\nabla_u \mathcal{L}_{\text{total}} = a_S (\theta_S - u) - \lambda b_S u$$
$$\dot{v} = -\nabla_v \mathcal{L}_{\text{total}} = v (\lambda a_C - b_C) - \kappa v^2$$

---

## 3. The Transcritical Bifurcation & Critical Threshold

### 3.1 Transverse Stability at $E_S$
The shortcut equilibrium is given by:
$$E_S = \left( \frac{a_S \theta_S}{a_S + \lambda b_S}, \, 0 \right)$$
Evaluating the Jacobian transverse eigenvalue along the schema direction $v$ at $E_S$:
$$\mu_\perp = \left. \frac{\partial \dot{v}}{\partial v} \right|_{v=0} = \lambda a_C - b_C$$

### 3.2 Stability Criterion
- **Subcritical Regime ($\lambda < \lambda_{\text{crit}} = \frac{b_C}{a_C}$):**
  $$\mu_\perp < 0 \implies E_S \text{ is locally asymptotically stable.}$$
  Any small schema perturbation decays exponentially to zero. The network is trapped in the low-coherence shortcut state.

- **Supercritical Regime ($\lambda > \lambda_{\text{crit}} = \frac{b_C}{a_C}$):**
  $$\mu_\perp > 0 \implies E_S \text{ undergoes a transcritical bifurcation and becomes unstable.}$$
  The non-trivial coherent equilibrium emerges in the positive state space:
  $$v^* = \frac{\lambda a_C - b_C}{\kappa} > 0$$
  and is locally asymptotically stable ($E_C$).

### 3.3 Identification with the Macroscopic Reproductive Ratio $R_0$
In the macroscopic $\Sigma$-Model, the reproductive ratio is defined as:
$$R_0 = \frac{\rho P_A \alpha_A}{\epsilon_\sigma \Omega_{SL}}$$
Under the two-subspace correspondence:
$$\rho P_A \alpha_A \longleftrightarrow \lambda a_C, \qquad \epsilon_\sigma \Omega_{SL} \longleftrightarrow b_C$$
Thus:
$$R_0 = \frac{\lambda a_C}{b_C} = \frac{\lambda}{\lambda_{\text{crit}}}$$
$$R_0 > 1 \iff \lambda > \lambda_{\text{crit}}$$

---

## 4. Instrumentation: GCA Failure vs. RGA Geometric Invariance

A critical insight from Paper 06 v2 is the fundamental divergence between **local gradient observables** and **global representation geometry**:

```
                 LOCAL GRADIENTS (GCA) vs GLOBAL GEOMETRY (RGA)
                 
  Gradient Cosine Alignment (GCA):                 Representational Geometry (RGA / CKA):
  • Measured via ∇_θ L_comp · ∇_θ L_task           • Measured via CKA of internal activations
  • Step 0 value: ≈ 0.95 (Artifact)                • Step 0 value: ≈ 0.0 (Unstructured)
  • Dominated by shared input embeddings           • Invariant to parameter orthogonalization
  • FAILS as online leading indicator             • RELIABLY tracks structural exposure (p=0.005)
```

### The Methodological Principle
> **Reasoning phase transitions are governed by global metric geometry (representation space), not by local differential vectors (gradient space).**

To build reliable observers for internal neural phase transitions, diagnostics must monitor **Centered Kernel Alignment (CKA)**, manifold curvature, and subspace principal angles rather than raw gradient inner products.
