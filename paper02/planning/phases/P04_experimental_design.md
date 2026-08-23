# Phase 04 — Experimental Design & Multi-Benchmark Protocol Specification

**RPF v2.0:** Git tag `p04-protocol` · Duration 2–3d · GPU 0 · RACI: Agent **R** / PI **A** (approve protocol; halt fallback) · Abort: P03 not PASSED → this phase does not start · Acceptance: protocol with ≥2 baselines, ≥3 ablations, ≥5 sensitivity parameters, hidden test set · *Pending (locked by P03 gate).*

**Phase ID:** P04  
**Phase Title:** Multi-Benchmark Experimental Design, Protocol Specification, Toolchain Mapping, and Zero-Leakage Audit  
**Status:** Pending  
**Duration:** 2 Days  
**Dependencies:** P03 (PROCEED Gate Directive required)  
**Executor:** Agent (85%) / Human-Gate (15%)  
**Deliverables:** `paper02/planning/phases/P04_experimental_design.md` (fully specified), updated `paper02/planning/ledger.md`, `paper02/decisions/ADR-006_experimental_protocol.md`

---

## 1. Purpose & Scope
Translate the gate-validated Two-Subspace Critical Pressure Law into an exhaustive, multi-benchmark experimental matrix. Formalize data generation protocols across 4 major compositional benchmarks (H-Bar, SCAN, COGS, PCFG-SET), map analysis toolchains (Diffrax, PyHessian, Geomstats, TransformerLens), conduct zero-leakage data audits, and pre-register statistical power calculations.

---

## 2. Exhaustive Tasks & Subtasks

### Task 4.1: Full Experimental Matrix Specification
1. **Benchmark Suite Specifications:**
   - **Suite 1 — H-Bar (Syntactic & Lexical Recombination):**
     - Primitives: 27 tokens (verbs, adverbs, directional operators).
     - Split structure: In-distribution length $\le 3$; Out-of-distribution length $\ge 4$ multi-combinator frames.
   - **Suite 2 — SCAN Benchmark (Lake & Baroni 2018):**
     - `add_primitive` (jump split): zero-shot compositional extrapolation of primitive `jump` in novel syntactic contexts (`jump twice`, `jump after walk around left`).
     - `length_split`: training on commands of length $\le 22$; testing on length $23 \dots 48$.
   - **Suite 3 — COGS Benchmark (Kim & Linzen 2020):**
     - Structural recursion and novel syntactic role mappings (e.g., passive to active voice, novel noun phrases in subject vs object position).
   - **Suite 4 — PCFG-SET Benchmark (Hupkes et al. 2020):**
     - Context-free grammar evaluation testing systematic recombination depth.
2. **Model Architecture Variations:**
   - Architecture A: 2-layer standard seq2seq Transformer (baseline capacity).
   - Architecture B: 4-layer Transformer ($d_{\text{model}} = 256, n_{\text{heads}} = 8$) to evaluate capacity scaling on $\lambda_{\text{crit}}$.
   - Architecture C: Recurrent / State-Space Model (Mamba / GRU baseline) to evaluate cross-architecture universality.

### Task 4.2: Toolchain & Engine Mapping
1. **Continuous Dynamics Engine:**
   - Use **Diffrax** (JAX) with `Tsit5` / `Kvaerno5` stiff ODE integrators (`atol=1e-8`, `rtol=1e-8`) to simulate the continuous two-subspace system and compute exact theoretical phase boundaries.
2. **Bifurcation & Stability Tracking:**
   - Use **SciPy / DifferentialEquations.jl** to track the Jacobian transverse eigenvalue $\mu_\perp(\lambda)$ and compute numerical Lyapunov exponents.
3. **Loss Landscape & Sharpness Tracking:**
   - Use **PyHessian / Curvlinops** to compute the top eigenvalue $\lambda_{\text{max}}(H)$ via 50 Lanczos iterations at each checkpoint.
4. **Representation Geometry & Manifold Analysis:**
   - Use **Geomstats** and linear/RBF **Centered Kernel Alignment (CKA)** to compute internal representational dissimilarity matrices against causal task graphs.
5. **Mechanistic Circuit Diagnostics:**
   - Use **TransformerLens / residual stream extraction** to isolate whether attention heads specialize in shortcut vs. schema extraction.

### Task 4.3: Zero-Leakage & Data-Card Audit (CC.4.2)
1. Write formal mathematical proof demonstrating support disjointness:
   $$\text{supp}(\mathcal{D}_{\text{train}}) \cap \text{supp}(\mathcal{D}_{\text{OOD}}) = \emptyset$$
   $$\text{supp}(\mathcal{D}_{\text{comp}}) \cap \text{supp}(\mathcal{D}_{\text{OOD}}) = \emptyset$$
2. Emit data card documenting grammar generation rules, token frequencies, and test set isolation guarantees.

### Task 4.4: Statistical Power Analysis & Pre-Registered Protocol
1. Perform power analysis: For $n = 30$ seeds per cell, the minimal detectable effect size (MDES) at $\alpha = 0.05, 1 - \beta = 0.90$ is Cohen's $d \approx 0.58$ (medium effect size).
2. Pre-register statistical pipeline:
   - Welch's two-sample $t$-test for pairwise differences.
   - TOST two-one-sided test with equivalence bound $\delta = \pm 2.5\%$.
   - Granger causality test for CKA lead-lag: $\text{CKA}_{t-1} \to \text{OOD}_t$ controlling for $\text{OOD}_{t-1}, \text{Loss}_t, \|\theta\|_t$.
   - Non-parametric bootstrap (10,000 resamples) for 95% confidence intervals on $\hat{\lambda}_{\text{crit}}$.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reviews and signs off on the multi-benchmark matrix, toolchain selections, and zero-leakage data card.

---

## 4. Machine-Checkable Exit Criteria
- [ ] Multi-benchmark matrix specified across all 4 benchmark suites.
- [ ] Toolchain mapping defined for Diffrax, PyHessian, Geomstats, and TransformerLens.
- [ ] Formal zero-leakage proof committed.
- [ ] `paper02/decisions/ADR-006_experimental_protocol.md` committed.
- [ ] `[HUMAN-GATE]` Protocol approved.

---

## 5. Deliverables & Artifacts
- Protocol document: `paper02/planning/phases/P04_experimental_design.md`
- Decision record: `paper02/decisions/ADR-006_experimental_protocol.md`
- Updated ledger: `paper02/planning/ledger.md`
