# ADR-007: Multi-Benchmark Experimental Matrix & Architecture Specification

## 1. Context & Status
- **Status:** **APPROVED**
- **Date:** 2026-08-25
- **Deciders:** Principal Investigator, Lead Research Agent
- **Phase:** Phase 04 (Multi-Benchmark Experimental Design & Protocol Specification)
- **Framework:** RPF v2.0.0 — Task 4.1
- **Prerequisites:** 
  - `paper/decisions/ADR-006_gate_verdict_and_threshold_reconciliation.md` (Gate passed, $\hat{\lambda}_{\text{crit}} = 0.025 \pm 0.005$)
  - `paper/planning/preregistration.md`
  - `paper/planning/phases/P04_experimental_design.md`

---

## 2. Decision: Factorial Multi-Benchmark Matrix Design

To rigorously evaluate the universality of the Two-Subspace Critical Pressure Law ($\lambda_{\text{crit}} = b_C / a_C \iff R_0 = 1$) and prove that the transcritical bifurcation is an intrinsic property of gradient-optimized compositional representations rather than an artifact of a single benchmark or architecture, we establish a full factorial experimental matrix across:

1. **4 Compositional Benchmark Suites**
2. **3 Distinct Architecture Classes**
3. **2 Supervision Regimes (Dense Pressure Sweep + Late-Onset Destabilization)**

---

## 3. Benchmark Suite Formalization

### 3.1 Suite 1: $\hbar$ (H-Bar Canonical Homomorphic Benchmark)
- **Domain:** Homomorphic command execution into atomic action sequences $\llbracket \cdot \rrbracket: \mathcal{L}(\mathcal{G}_{\hbar}) \to \mathcal{A}^*$.
- **Primitives:** 27 closed vocabulary tokens (verbs, adverbs, directional operators) with hash-seeded cryptographic alias generators ensuring zero web pretraining leakage.
- **Split Taxonomy (Decoupled 3-Way Protocol per Ahuja & Mansouri 2024):**
  - **Split A (Pure Recombination):** Fixed length ($L = 4$), evaluating novel Cartesian combinations of seen primitives.
  - **Split B (Structural Recursion Depth):** Training on depth $d \le 2$; testing on depth $d \in \{3, 4, 5\}$.
  - **Split C (Length Extrapolation Control):** Training on length $L \le 6$; testing on length $L \in [7, 16]$ with identical token frequencies to isolate positional encoding mechanics.

### 3.2 Suite 2: SCAN (Lake & Baroni 2018)
- **Domain:** Synthetic spatial navigation commands.
- **Evaluated Splits:**
  - `add_primitive` (Jump Split): Zero-shot compositional synthesis of `jump` in complex frames (`jump twice`, `jump after walk around left`).
  - `length_split`: Training on lengths $\le 22$; testing on lengths $23 \dots 48$.

### 3.3 Suite 3: COGS / ReCOGS (Kim & Linzen 2020; Wu et al. 2023)
- **Domain:** Semantic parsing and role assignment.
- **Evaluated Splits:**
  - Structural generalization: Active $\leftrightarrow$ passive voice transformation.
  - Novel argument assignment: Common nouns trained only in object position tested in subject position.
  - **Target Formatting:** Minimal denotational semantic forms per Wu et al. (2023) to eliminate incidental logical-form parsing artifacts.

### 3.4 Suite 4: PCFG-SET (Hupkes et al. 2020)
- **Domain:** Probabilistic context-free grammar evaluation across 5 canonical axes: systematicity, productivity, substitutivity, localism, and overgeneralization.

---

## 4. Architecture Class Variations

| Architecture ID | Architecture Family | Hidden Dim ($d_{\text{model}}$) | Layers | Attention Heads | Param Count | Research Objective |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| **Arch A** | Standard Transformer (Baseline) | 128 | 2 | 4 | ~0.93M | Canonical baseline for mechanism validation. |
| **Arch B** | Scaled Transformer (Deep Capacity) | 256 | 4 | 8 | ~3.8M | Tests capacity scaling: does higher capacity alter $b_C/a_C$ or accelerate $\hat{\tau}$? |
| **Arch C** | Gated Recurrent Seq2Seq (GRU) | 128 | 2 | N/A | ~0.41M | Tests cross-architecture universality beyond attention mechanisms (ADR-012). |

---

## 5. Authorized Tiered Phase 06 Production Scope (Amendment 2026-08-27)

To satisfy compute budget constraints ($\le 20\text{ GPU hours}$ per Phase 06 allocation) while ensuring rigorous statistical power for primary hypotheses, the experimental matrix is formally tiered:

### 5.1 Tier 1: Primary Change-Point Falsification Matrix (Primary Evidence)
- **Objective:** Primary falsification of sharp phase boundary, critical threshold estimation $\hat{\lambda}_{\text{crit}} \in [0.020, 0.030]$, and cross-benchmark universality.
- **Benchmarks:** 4 Suites ($\hbar$, SCAN `add_primitive_jump`, COGS, PCFG-SET).
- **Architecture:** Arch A (Transformer 2-Layer Baseline).
- **$\lambda$ Grid (6 levels):** $\{0.000\text{ (subcritical reference)}, 0.015\text{ (boundary approach)}, 0.020\text{ (boundary entry)}, 0.025\text{ (locked critical estimate)}, 0.030\text{ (boundary exit)}, 0.500\text{ (supercritical reference)}\}$.
- **Sample Size:** $n = 30$ independent random seeds/cell.
- **Run Count:** $4 \times 1 \times 6 \times 30 = \mathbf{720\text{ runs}}$ ($\approx 15.4\text{ GPU hours}$ at $77.07\text{ s/run}$).

### 5.2 Tier 2: Exploratory Architecture Universality Matrix (Exploratory Evidence)
- **Objective:** Exploratory screening of capacity scaling (Arch B) and recurrent universality (Arch C).
- **Benchmarks:** 4 Suites ($\hbar$, SCAN, COGS, PCFG-SET).
- **Architectures:** Arch B (Transformer 4-Layer) and Arch C (GRU Recurrent).
- **$\lambda$ Grid (3 levels):** $\{0.000\text{ (subcritical)}, 0.025\text{ (boundary)}, 0.500\text{ (supercritical)}\}$.
- **Sample Size:** $n = 10$ seeds/cell.
- **Run Count:** $4 \times 2 \times 3 \times 10 = \mathbf{240\text{ runs}}$ ($\approx 5.1\text{ GPU hours}$).

### 5.3 Total Production Scope & Aspirational Reference Design
- **Authorized Phase 06 Production Runs:** $720\text{ (Tier 1)} + 240\text{ (Tier 2)} = \mathbf{960\text{ runs}}$ (Hard GPU cap: 20 GPU-hours).
- **Aspirational Reference Matrix:** The full 6,120-run factorial design (Arm A dense sweep + Arm B late intervention across all architectures) remains documented as an asymptotic reference design.

---

## 6. Hardware & Compute Budget Discipline

- **Per-Run Runtime:** ~60–80 seconds on Tesla T4 / A100 GPU (with PyTorch AMP FP16).
- **Total Compute Budget:**
  - Arm A: 11 $\lambda$ levels $\times$ 30 seeds = 330 runs per benchmark $\times$ architecture.
  - Arm B: 6 $t_{\text{int}}$ levels $\times$ 30 seeds = 180 runs per benchmark $\times$ architecture.
  - Total runs per cell = 510 runs (~8.5 GPU hours per cell).
- **Deterministic Checkpoint Hashing:** Every manifest generates a SHA-256 seed signature ensuring zero run collision and strict reproducibility.

---

## 7. Consequences & Downstream Directives
1. **Implementation:** Codify declarative matrix configuration in `paper/experiments/configs/matrix_p04.yaml` and manifest generator in `paper/src/config/matrix.py`.
2. **Verification:** Add unit tests validating parameter coverage and seed uniqueness in `paper/tests/test_matrix.py`.
3. **Phase Progression:** Fulfills Task 4.1 of Phase 04.
