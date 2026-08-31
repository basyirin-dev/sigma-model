# ADR-008: Diagnostic Toolchain & Analysis Engines Specification

## 1. Context & Status
- **Status:** **APPROVED**
- **Date:** 2026-08-25
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Phase 04 (Multi-Benchmark Experimental Design & Protocol Specification)
- **Framework:** RPF v2.0.0 — Task 4.2
- **Prerequisites:**
  - `paper02/decisions/ADR-007_multi_benchmark_experimental_matrix.md`
  - `paper02/planning/phases/P04_experimental_design.md`

---

## 2. Decision: Toolchain Architecture & Mathematical Formulations

To measure the internal representations and dynamical trajectories of models undergoing the transcritical bifurcation, we specify five dedicated analysis engines:

### 2.1 Continuous Dynamics & Bifurcation Engine (`continuous/`)
- **Stiff Integration:** Uses adaptive Dormand-Prince / Radau / Tsit5 integrators with strict convergence tolerances (`atol=1e-8`, `rtol=1e-8`).
- **Transverse Jacobian Eigenvalue:** Computes:
  $$\mu_\perp(\lambda) = \left. \frac{\partial \dot{v}}{\partial v} \right|_{v=0} = \lambda a_C - b_C$$
  verifying $\mu_\perp < 0$ (subcritical stability of $E_S$) and $\mu_\perp > 0$ (supercritical destabilization).
- **Lyapunov Exponent Estimation:** Computes the maximal Lyapunov exponent $\Lambda = \lim_{t \to \infty} \frac{1}{t} \ln \frac{\|\delta(t)\|}{\|\delta(0)\|}$ along continuous trajectories.

### 2.2 Representation Geometry & Homomorphism Engine (`analysis/geometry.py`)
- **Centered Kernel Alignment (CKA):**
  $$\text{CKA}(K, L) = \frac{\text{HSIC}(K, L)}{\sqrt{\text{HSIC}(K, K) \text{HSIC}(L, L)}}$$
  where $\text{HSIC}(K, L) = \frac{1}{(n-1)^2} \text{Tr}(K H L H)$ with centering matrix $H = I - \frac{1}{n} \mathbf{1}\mathbf{1}^\top$.
- **Representational Homomorphism Error (HE per An & Du 2026):**
  For a grammar rule $r = (a, b) \to y$ and hidden representation function $\phi(x)$, HE measures:
  $$\text{HE} = \frac{1}{|\mathcal{R}|} \sum_{(a, b, y) \in \mathcal{R}} \frac{\|\phi(y) - \mathcal{T}(\phi(a), \phi(b))\|^2}{\|\phi(y)\|^2}$$
  where $\mathcal{T}$ is the learned bilinear or linear composition operator.
- **Two-Subspace Principal Angles $\theta(\mathcal{U}_S, \mathcal{V}_C)$ (Uselis et al. 2026):**
  Measures the canonical correlation between the shortcut subspace basis $U \in \mathbb{R}^{D \times d_S}$ and schema subspace basis $V \in \mathbb{R}^{D \times d_C}$:
  $$\cos \theta_k = \max_{u_k \perp \{u_i\}_{i<k}} \max_{v_k \perp \{v_i\}_{i<k}} \frac{u_k^\top U^\top V v_k}{\|U u_k\| \|V v_k\|}$$

### 2.3 Loss Landscape Curvature & Sharpness (`analysis/hessian.py`)
- **Top Hessian Eigenvalue ($\lambda_{\max}(H)$):**
  Computed via matrix-free Hessian-Vector Products (HVP) using power iteration:
  $$v_{k+1} = \frac{H v_k}{\|H v_k\|}, \quad H v = \left. \frac{\partial}{\partial \epsilon} \nabla \mathcal{L}(w + \epsilon v) \right|_{\epsilon=0}$$
  Tracking proximity to the Edge-of-Stability threshold $\lambda_{\max}(H) \approx \frac{2}{\eta}$.
- **Hutchinson Stochastic Trace Estimator:**
  $$\text{Tr}(H) \approx \frac{1}{M} \sum_{m=1}^M z_m^\top (H z_m), \quad z_m \sim \mathcal{N}(0, I)$$

### 2.4 Mechanistic Circuit Diagnostics (`analysis/circuits.py`)
- **Residual Stream Subspace Projection:**
  Decomposes hidden state $h_l(x) \in \mathbb{R}^D$ at layer $l$ into orthogonal projections:
  $$h_l(x) = \Pi_S h_l(x) + \Pi_C h_l(x) + h_l^\perp(x)$$
  where $\Pi_S = U (U^\top U)^{-1} U^\top$ and $\Pi_C = V (V^\top V)^{-1} V^\top$.
- **Attention Head Specialization Score:**
  $$S_{\text{head}}(l, h) = \frac{\|\Pi_C \text{Output}_{l, h}\|}{\|\Pi_S \text{Output}_{l, h}\| + \epsilon}$$

---

## 3. Consequences & Governance
- All diagnostic modules must be self-contained, typed with Python 3.14 hints, vectorized with NumPy/PyTorch, and verified against analytical solutions in unit tests.
- Fulfills Task 4.2 of Phase 04.
