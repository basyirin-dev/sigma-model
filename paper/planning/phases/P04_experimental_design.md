# Phase 04 — Experimental Design & Multi-Benchmark Protocol Specification

**RPF v2.0:** Git tag `p04-protocol` · Duration 2–3d · GPU 0 · RACI: Agent **R** / PI **A** (approve protocol; halt fallback) · Abort: P03 not PASSED → this phase does not start · Acceptance: protocol with ≥2 baselines, ≥3 ablations, ≥5 sensitivity parameters, hidden test set · *Pending (locked by P03 gate).*

**Phase ID:** P04  
**Phase Title:** Multi-Benchmark Experimental Design, Protocol Specification, Toolchain Mapping, and Zero-Leakage Audit  
**Status:** Pending  
**Duration:** 2 Days  
**Dependencies:** P03 (PROCEED Gate Directive required)  
**Executor:** Agent (85%) / Human-Gate (15%)  
**Deliverables:** `paper/planning/phases/P04_experimental_design.md` (fully specified), updated `paper/planning/ledger.md`, `paper/decisions/ADR-006_experimental_protocol.md`

---

## 1. Purpose & Scope
Translate the gate-validated Two-Subspace Critical Pressure Law into an exhaustive, multi-benchmark experimental matrix. Formalize data generation protocols across 4 major compositional benchmarks (H-Bar, SCAN, COGS, PCFG-SET), map analysis toolchains (Diffrax, PyHessian, Geomstats, TransformerLens), conduct zero-leakage data audits, and pre-register statistical power calculations.

---

## 2. Exhaustive Tasks & Subtasks

### Task 4.1: Full Experimental Matrix Specification — ✅ COMPLETED
- **Governance Record:** [`ADR-007: Multi-Benchmark Experimental Matrix & Architecture Specification`](file:///home/bigbasy/Documents/sigma-model/paper/decisions/ADR-007_multi_benchmark_experimental_matrix.md)
- **Declarative Config:** [`paper/experiments/configs/matrix_p04.yaml`](file:///home/bigbasy/Documents/sigma-model/paper/experiments/configs/matrix_p04.yaml)
- **Manifest Engine:** [`paper/src/config/matrix.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/config/matrix.py) (validation, filtering, budget calculation)
- **Verification Tests:** [`paper/tests/test_matrix.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_matrix.py) (8 unit tests, 100% pass)

1. **Benchmark Suite Specifications:**
   - **Suite 1 — H-Bar (Syntactic & Lexical Recombination):**
     - Primitives: 27 tokens (verbs, adverbs, directional operators).
     - Split structure: In-distribution length $\le 3$; Out-of-distribution length $\ge 4$ multi-combinator frames.
   - **Suite 2 — SCAN Benchmark (Lake & Baroni 2018):**
     - `add_primitive` (jump split): zero-shot compositional extrapolation of primitive `jump` in novel syntactic contexts (`jump twice`, `jump after walk around left`).
     - `length_split`: training on commands of length $\le 22$; testing on length $23 \dots 48$.
   - **Suite 3 — COGS Benchmark (Kim & Linzen 2020):**
     - Structural recursion and novel syntactic role mappings (e.g., passive to active voice, novel noun phrases in subject vs object position with ReCOGS minimal logical form targets).
   - **Suite 4 — PCFG-SET Benchmark (Hupkes et al. 2020):**
     - Context-free grammar evaluation testing systematic recombination depth.
2. **Model Architecture Variations:**
   - Architecture A: 2-layer standard seq2seq Transformer (baseline capacity: $d_{\text{model}} = 128, n_{\text{heads}} = 4$).
   - Architecture B: 4-layer Transformer ($d_{\text{model}} = 256, n_{\text{heads}} = 8$) to evaluate capacity scaling on $\lambda_{\text{crit}}$.
   - Architecture C: Recurrent / State-Space Model (Mamba / GRU baseline: $d_{\text{model}} = 128, d_{\text{state}} = 16$) to evaluate cross-architecture universality.

### Task 4.2: Toolchain & Engine Mapping — ✅ COMPLETED
- **Governance Record:** [`ADR-008: Diagnostic Toolchain & Analysis Engines Specification`](file:///home/bigbasy/Documents/sigma-model/paper/decisions/ADR-008_diagnostic_toolchain_and_analysis_engines.md)
- **Geometry & Homomorphism Engine:** [`paper/src/analysis/geometry.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/analysis/geometry.py) (Linear & RBF CKA, Homomorphism Error, Principal Subspace Angles)
- **Hessian & Curvature Engine:** [`paper/src/analysis/hessian.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/analysis/hessian.py) (HVP Power Iteration $\lambda_{\max}(H)$, Hutchinson Trace Estimator)
- **Circuit & Attribution Engine:** [`paper/src/analysis/circuits.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/analysis/circuits.py) (Residual Stream Decomposition, Head Specialization $S_{\text{head}}$)
- **Verification Tests:** [`test_geometry.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_geometry.py), [`test_hessian.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_hessian.py), [`test_circuits.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_circuits.py) (14 unit tests, 100% pass)

1. **Continuous Dynamics Engine:**
   - Unified stiff ODE/SDE solvers (`atol=1e-8`, `rtol=1e-8`) in `paper/src/continuous/` simulating the two-subspace system and computing exact theoretical phase boundaries.
2. **Bifurcation & Stability Tracking:**
   - Analytical & numerical Jacobian transverse eigenvalue $\mu_\perp(\lambda) = \lambda a_C - b_C$ tracking and maximum Lyapunov exponents $\Lambda$.
3. **Loss Landscape & Sharpness Tracking:**
   - Matrix-free Hessian-Vector Product power iteration computing $\lambda_{\text{max}}(H)$ (Edge-of-Stability proximity) and stochastic Hutchinson trace $\text{Tr}(H)$.
4. **Representation Geometry & Manifold Analysis:**
   - Centered Kernel Alignment (CKA), Homomorphism Error (HE per An & Du 2026), and two-subspace principal angles $\theta(\mathcal{U}_S, \mathcal{V}_C)$ (Uselis et al. 2026).
5. **Mechanistic Circuit Diagnostics:**
   - Residual stream orthogonal projection isolating shortcut ($u \in \mathbb{R}^{d_S}$) vs schema ($v \in \mathbb{R}^{d_C}$) components and per-head specialization scoring.

### Task 4.3: Axiomatic Formalization, Grammar Specification, and Multi-Axis Diagnostic Suite for the $\hbar$ (H-Bar) Benchmark — ✅ COMPLETED
- **Governance & Datacard:** [`paper/docs/datacards/hbar_benchmark.md`](file:///home/bigbasy/Documents/sigma-model/paper/docs/datacards/hbar_benchmark.md) (Gebru et al. 2021)
- **Grammar & Semantics:** [`paper/src/data/hbar/grammar.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/data/hbar/grammar.py)
- **3-Way Decoupled Generator:** [`paper/src/data/hbar/generator.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/data/hbar/generator.py) (Split A: Recombination, Split B: Depth, Split C: Length)
- **Zero-Leakage Auditor:** [`paper/src/data/audit_leakage.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/data/audit_leakage.py)
- **Verification Tests:** [`test_hbar_benchmark.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_hbar_benchmark.py), [`test_audit_leakage.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_audit_leakage.py) (10 unit tests, 100% pass)

1. **Artifact-Free Minimal Denotational Grammar (Addressing Wu et al. 2023 - ReCOGS):**
   - **Root Cause Eliminated:** ReCOGS showed that COGS logical form parsing introduces syntax artifacts (variable naming, redundant symbols) that cause false 0% scores.
   - **$\hbar$ Solution:** Defined an artifact-free Chomsky grammar $\mathcal{G}_{\hbar} = (\mathcal{V}_N, \mathcal{V}_T, \mathcal{P}, \mathcal{S})$ with an exact homomorphic denotational semantics $\llbracket \cdot \rrbracket: \mathcal{L}(\mathcal{G}_{\hbar}) \to \mathcal{A}^*$ mapping directly into canonical atomic execution traces without intermediate parsing boilerplate.
   - **Algebraic Invariance:** Verified algebraic commutativity and distributivity (e.g., $\llbracket \text{opposite} \circ \text{left} \rrbracket = \text{RTURN}$, $\llbracket \text{twice}(\text{jump left}) \rrbracket = \text{JUMP LTURN JUMP LTURN}$).

2. **Orthogonal Factorized Split Taxonomy (Addressing Ahuja & Mansouri 2024; Hupkes et al. 2019):**
   - **Root Cause Eliminated:** Existing benchmarks conflate sequence length extrapolation with compositional novelty.
   - **$\hbar$ Solution (3-Way Decoupled Evaluator):**
     - **Split A (Pure Fixed-Length Compositional Recombination):** Sequence length held strictly constant ($L = 4$); test inputs drawn from the held-out Cartesian product support $\mathcal{Q} \setminus \text{supp}(\mathcal{D}_{\text{train}})$.
     - **Split B (Structural Depth Extrapolation / Hierarchical Recursion):** Fixed token vocabulary; train on recursion depth $d \le 2$; test on depth $d \in \{3, 4, 5\}$ (Kohli et al. 2026).
     - **Split C (Pure Length Generalization Control):** Test on sequence length $L \in [7, 16]$ under the *identical* token distribution $P_{\text{train}}$ to isolate positional encoding artifacts from semantic compositionality (Kazemnejad et al. 2023).

3. **Cryptographic Lexical Exposure Control (Addressing Kim et al. 2022):**
   - **Root Cause Eliminated:** Pretrained models encounter benchmark tokens during pretraining, inflating generalization scores from 6% to 83%.
   - **$\hbar$ Solution:** Synthetic isolated lexicons with pseudoword token aliases and hash-seeded vocabulary generators guaranteeing zero overlap with web-crawled pretraining corpora.
   - **Strict Support Disjointness Invariant:**
     $$\text{supp}(\mathcal{D}_{\text{train}}) \cap \text{supp}(\mathcal{D}_{\text{ID}}) \cap \text{supp}(\mathcal{D}_{\text{OOD\_A}}) \cap \text{supp}(\mathcal{D}_{\text{OOD\_B}}) \cap \text{supp}(\mathcal{D}_{\text{OOD\_C}}) = \emptyset$$

4. **Mechanistic Representation Geometry & Homomorphism Probes (Addressing An & Du 2026; Uselis et al. 2026; Raju 2026):**
   - **Homomorphism Error (HE) Tracker:** Compute consistency between symbolic production rules and hidden-state combination matrices ($R^2 = 0.73$ predictive of OOD transfer; An & Du 2026).
   - **Subspace Orthogonality Probe:** Measure linear factorization and angle between the shortcut subspace $\mathcal{U}_S$ and schema subspace $\mathcal{V}_C$ (Uselis et al. 2026).

5. **Stratified Error Taxonomy & Standardized Datasheet (Gebru et al. 2021):**
   - Stratified decomposition: $\text{Acc}_{\text{prim}}$, $\text{Acc}_{\text{mod}}$, $\text{Acc}_{\text{order}}$, $\text{Acc}_{\text{depth}}$.
   - Formal Dataset Card emitted in `paper/docs/datacards/hbar_benchmark.md`.
   - Standalone modular library in `paper/src/data/hbar/` with PyTorch & JAX DataLoaders.

### Task 4.4: Statistical Power Analysis & Pre-Registered Protocol — ✅ COMPLETED
- **Governance Record:** [`ADR-009: Statistical Power Analysis & Multi-Benchmark Pre-Registered Protocol`](file:///home/bigbasy/Documents/sigma-model/paper/decisions/ADR-009_statistical_power_and_protocol.md)
- **PI Human Gate Directive:** [`paper/decisions/human-gates/P04_protocol_directive.md`](file:///home/bigbasy/Documents/sigma-model/paper/decisions/human-gates/P04_protocol_directive.md)
- **Power & Diagnostic Engine:** [`paper/src/analysis/power.py`](file:///home/bigbasy/Documents/sigma-model/paper/src/analysis/power.py)
- **Verification Tests:** [`test_power.py`](file:///home/bigbasy/Documents/sigma-model/paper/tests/test_power.py) (5 unit tests, 100% pass)

1. Perform power analysis: For $n = 30$ seeds per cell, the minimal detectable effect size (MDES) at $\alpha = 0.05, 1 - \beta = 0.90$ is Cohen's $d \approx 0.58$ (medium effect size).
2. Pre-register statistical pipeline:
   - Welch's two-sample $t$-test for pairwise differences.
   - TOST two-one-sided test with equivalence bound $\delta = \pm 2.5\%$.
   - Granger causality test for CKA lead-lag: $\text{CKA}_{t-1} \to \text{OOD}_t$ controlling for $\text{OOD}_{t-1}, \text{Loss}_t, \|\theta\|_t$.
   - Non-parametric bootstrap (10,000 resamples) for 95% confidence intervals on $\hat{\lambda}_{\text{crit}}$.

---

## 3. Human Gates
- [x] `[HUMAN-GATE]` Principal Investigator reviewed and signed off on the multi-benchmark matrix, toolchain selections, and zero-leakage data card in [`P04_protocol_directive.md`](file:///home/bigbasy/Documents/sigma-model/paper/decisions/human-gates/P04_protocol_directive.md).

---

## 4. Machine-Checkable Exit Criteria
- [x] Multi-benchmark matrix specified across all 4 benchmark suites (H-Bar, SCAN, COGS, PCFG-SET) in `ADR-007` & `matrix_p04.yaml`.
- [x] Toolchain mapping defined for Diffrax, PyHessian, Geomstats, and Circuit Diagnostics in `ADR-008`.
- [x] Axiomatic $\mathcal{G}_{\hbar}$ formal grammar, algebraic semantics, and multi-axis split taxonomy committed.
- [x] Automated zero-leakage audit suite committed with cryptographic support disjointness verified (`audit_leakage.py`).
- [x] Formal Dataset Card (`paper/docs/datacards/hbar_benchmark.md`) emitted per Gebru et al. standards.
- [x] Protocol decision records committed (`ADR-007`, `ADR-008`, `ADR-009`).
- [x] `[HUMAN-GATE]` Protocol approved by Principal Investigator (`P04_protocol_directive.md`).

---

## 5. Deliverables & Artifacts
- Protocol document: `paper/planning/phases/P04_experimental_design.md` (Resolved)
- Decision records: `ADR-007`, `ADR-008`, `ADR-009`
- Modular H-Bar package: `paper/src/data/hbar/`
- Zero-leakage audit tool: `paper/src/data/audit_leakage.py`
- Formal Dataset Card: `paper/docs/datacards/hbar_benchmark.md`
- Directive: `paper/decisions/human-gates/P04_protocol_directive.md`
