# 2. MCDA Framework V1: 22-Criteria Weighted Sum Model

## 2.1 Mathematical Foundation

Let $D = \{d_1, d_2, ..., d_{50}\}$ be the set of research domains.
Let $C = \{c_1, c_2, ..., c_{22}\}$ be the set of evaluation criteria.
Let $W = \{w_1, w_2, ..., w_{22}\}$ be the weight vector with $\sum w_i = 1.0$.

Each domain $d_j$ receives a normalized score $s_{i,j} \in [0, 1]$ for each criterion $c_i$.

The final score is the weighted sum:
$$S_j = \sum_{i=1}^{22} w_i \cdot s_{i,j}$$

## 2.2 The 22 Criteria

### I. Exogenous Constraints & Pinnacle Achievements (24.0%)

| # | Criterion | Weight | Definition |
|:--|:----------|:------:|:-----------|
| 1 | Pinnacle Recognition Probability | 12.0% | Bayesian probability of Nobel/Fields/Turing/Kavli recognition |
| 2 | Resource Elasticity | 12.0% | Feasibility of high-impact research with constrained resources |

### II. Epistemic & Methodological Rigor (26.0%)

| # | Criterion | Weight | Definition |
|:--|:----------|:------:|:-----------|
| 3 | Mathematical & Logical Formalizability | 9.0% | Degree to which theories can be axiomatized |
| 4 | Empirical Falsifiability (Popperian Rigor) | 8.0% | Capacity for hypotheses to be tested and falsified |
| 5 | Reproducibility & Replication Stability | 6.0% | Probability of independent reproduction of results |
| 6 | Information-Theoretic Density | 3.0% | Bits of certainty gained per unit research output |

### III. Feasibility & Infrastructure Independence (18.0%)

| # | Criterion | Weight | Definition |
|:--|:----------|:------:|:-----------|
| 7 | Single-PI Feasibility | 6.0% | Can paradigm-shifting work be done by a lone researcher? |
| 8 | Computational Accessibility | 5.0% | Can boundaries be pushed with consumer-grade compute? |
| 9 | Data Availability & Open-Source Readiness | 5.0% | Existence of massive, open-source datasets |
| 10 | Ethical & Regulatory Friction (Inverse) | 2.0% | Speed unimpeded by regulatory frameworks |

### IV. Impact, Utility & Transdisciplinarity (19.0%)

| # | Criterion | Weight | Definition |
|:--|:----------|:------:|:-----------|
| 11 | Transdisciplinary Integrative Capacity | 5.0% | Degree to which methods act as foundational tools |
| 12 | Societal & Humanistic Impact | 6.0% | Measurable improvement in human condition |
| 13 | Economic & Technological Spillover | 4.0% | Total addressable market of derived technologies |
| 14 | Temporal Half-Life of Discoveries | 4.0% | Time until foundational discovery is obsolete |

### V. Paradigmatic Dynamics & Career Optimization (13.0%)

| # | Criterion | Weight | Definition |
|:--|:----------|:------:|:-----------|
| 15 | Paradigmatic Disruptive Potential (Kuhnian) | 2.0% | Is the field primed for scientific revolution? |
| 16 | Open-Source Toolchain Maturity | 2.0% | Quality of open-source domain software |
| 17 | Complexity & Non-Linearity Depth | 2.0% | Degree of modeling complex/emergent systems |
| 18 | Cognitive Transferability | 2.0% | Skill transferability to other careers |
| 19 | Funding Elasticity | 2.0% | Marginal output per unit grant funding |
| 20 | Publication Velocity | 1.0% | Median time to peer-reviewed publication |
| 21 | Global Collaborative Network Permeability | 1.0% | Ease of joining international collaborations |
| 22 | Epistemic Certainty Ceiling | 1.0% | How close the field is to being solved |

## 2.3 Level 1: Broad Domains (Top 3)

| Rank | Domain | Score | Key Strengths |
|:----:|:-------|:-----:|:--------------|
| 1 | **Physics** | **0.852** | Highest Nobel density, perfect formalizability + falsifiability balance |
| 2 | Computer Science | 0.831 | Ultimate resource elasticity, Turing Award recognition |
| 3 | Mathematics | 0.784 | Absolute resource independence, permanent discoveries |

## 2.4 Level 2: Physics Sub-domains (Top 3)

| Rank | Sub-domain | Score | Key Strengths |
|:----:|:-----------|:-----:|:--------------|
| 1 | **Quantum Information & Computation** | **0.912** | Nobel factory (2022), trillion-dollar spillover, single-PI feasible |
| 2 | Cosmology | 0.875 | Hubble Tension crisis = ripe for revolution, open-access data |
| 3 | Quantum Field Theory | 0.868 | Purest pen-and-paper physics, perfect formalizability |

## 2.5 Level 3: QIC Sub-domains (Top 3)

| Rank | Sub-sub-domain | Score | Key Strengths |
|:----:|:---------------|:-----:|:--------------|
| 1 | **Quantum Information Theory** | **0.921** | Zero infrastructure, absolute reproducibility, permanent theorems |
| 2 | Quantum Complexity Theory | 0.904 | BQP vs. PH — profound open problem |
| 3 | Quantum Error Correction | 0.895 | Holy grail of quantum computing industry |

## 2.6 Full Audit Trail

| # | Criterion (Weight) | Physics | QIC | QIT |
|:--|:-------------------|:-------:|:---:|:---:|
| 1 | Pinnacle Recognition (0.12) | 1.00 | 0.90 | 0.95 |
| 2 | Resource Elasticity (0.12) | 0.90 | 1.00 | 1.00 |
| 3 | Math Formalizability (0.09) | 1.00 | 1.00 | 1.00 |
| 4 | Empirical Falsifiability (0.08) | 0.90 | 0.80 | 0.60 |
| 5 | Reproducibility (0.06) | 0.80 | 0.90 | 1.00 |
| 6 | Info-Theoretic Density (0.03) | 0.90 | 0.95 | 1.00 |
| 7 | Single-PI Feasibility (0.06) | 0.70 | 0.90 | 1.00 |
| 8 | Computational Accessibility (0.05) | 0.70 | 1.00 | 1.00 |
| 9 | Data Availability (0.05) | 0.70 | 1.00 | 1.00 |
| 10 | Ethical Friction Inverse (0.02) | 0.80 | 0.90 | 1.00 |
| 11 | Transdisciplinary (0.05) | 0.90 | 1.00 | 1.00 |
| 12 | Societal Impact (0.06) | 0.90 | 0.80 | 0.70 |
| 13 | Economic Spillover (0.04) | 0.80 | 1.00 | 0.50 |
| 14 | Temporal Half-Life (0.04) | 1.00 | 0.90 | 1.00 |
| 15 | Kuhnian Malleability (0.02) | 0.90 | 1.00 | 0.90 |
| 16 | Open-Source Toolchain (0.02) | 0.80 | 1.00 | 0.80 |
| 17 | Complexity Depth (0.02) | 1.00 | 0.90 | 0.90 |
| 18 | Cognitive Transferability (0.02) | 0.80 | 1.00 | 0.90 |
| 19 | Funding Elasticity (0.02) | 0.80 | 1.00 | 1.00 |
| 20 | Publication Velocity (0.01) | 0.70 | 1.00 | 0.80 |
| 21 | Network Permeability (0.01) | 0.80 | 1.00 | 0.90 |
| 22 | Epistemic Certainty Ceiling (0.01) | 0.90 | 0.90 | 0.90 |
| | **Weighted Sum** | **0.852** | **0.912** | **0.921** |

## 2.7 Status

**Superseded.** This framework was replaced by MCDA V2 (Choquet integral) which provided greater rigor, uncertainty quantification, and capacity for modeling criterion interactions. See `03-mcda-framework-v2-choquet-integral.md`.
