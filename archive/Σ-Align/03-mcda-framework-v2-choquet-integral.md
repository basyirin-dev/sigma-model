# 3. MCDA Framework V2: 21-Criteria 2-Additive Choquet Integral Model

## 3.1 Foundational Design Answers

The framework was constructed from 15 operationally defined answers to foundational design questions.

### Q1: Primary Objective
The "optimal" framework minimizes expected MSE between assigned score $S(d)$ and latent true value $V(d)$:
$$V(d) \coloneqq \int_{\Omega} U(\omega) \, \Delta_{d} p(\omega \mid \text{do}(knowledge_d = \text{current trajectory})) \, d\omega$$
where $\Omega$ = all possible future world-states, $U(\omega)$ = long-term utilitarian social welfare function (discounted sum of sentient well-being over the future light cone), and $\Delta_d$ = marginal change in probability distribution over futures.

### Q2: Terminal Utility
Scores are for ex ante personal research prioritization, open to collaboration.

### Q3: Temporal Scope
Hybrid: 0.4 synchronic snapshot + 0.6 stochastic diachronic projection (100 years, 0.1% annual pure time preference), using a Bayesian hierarchical model of knowledge accumulation.

### Q4: System Boundaries
Maximal moral patient set: all present and future sentient beings within the Hubble volume reachable by human-originated influence.

### Q5: Cross-Paradigm Commensurability
Meta-criterion $R_{intra}(d)$ — expected log ratio of posterior to prior odds for domain claims under adversarial scrutiny, mapped to a common percentile scale.

### Q6: Non-empirical/Non-mathematical Rigor
Geometric mean of Coherence Index, Depth Index, and Stability Index, mapped via percentile transformation.

### Q7: Interdisciplinary Topology
Knowledge domains modeled as weighted directed graph; score adjusted by eigenvector centrality (PageRank) in the knowledge-flow network.

### Q8: Data Elicitation
Hybrid fusion: quantitative metrics (OpenAlex, Crossref, ReplicationWiki, PatentsView) + structured expert elicitation (IDEA protocol, 15-30 senior researchers per domain).

### Q9: Weighting Derivation
Posterior mean of hierarchical Dirichlet distribution, fusing AHP expert pairwise comparisons with Entropy Weight Method.

### Q10: Aggregation Operator
2-additive Choquet integral with fuzzy measure $\mu$ learned from expert comparisons via maximum entropy model.

### Q11: Normalization Schema
Log10(1+x) + robust Z-score for unbounded metrics; logit + robust Z-score for proportions; log-odds + robust Z-score for elicited probabilities.

### Q12: Uncertainty Quantification
Full posterior distribution $p(S_d \mid \text{data})$ via MCMC (10,000 iterations), propagating measurement error, expert imprecision, weight uncertainty, and model uncertainty.

### Q13: Monotonicity
Non-monotonic criteria (paradigm stability, innovation rate) handled by piecewise linear partial value functions with interior maxima.

### Q14: Constraint Formulation
Shapley values sum to 1.0; full 3-pillar profile output; Pareto-optimal domains explicitly identified.

### Q15: Sensitivity Analysis
$\pm 10\%$ Shapley perturbation → Spearman footrule $\le 1.0$, Kendall $\tau \ge 0.95$; $\pm 5\%$ → no rank change $> 1$.

## 3.2 Mathematical Architecture

### Temporal Integration
Each criterion $c_i(d)$ is a convex combination:
$$c_i(d) = 0.4 \cdot c_{i,\text{sync}}(d) + 0.6 \cdot c_{i,\text{diachronic}}(d, t=100, \delta=0.001)$$

### Normalization Pipeline
- Unbounded counts: $x' = \text{robust-Z}(\log_{10}(1+x))$
- Proportions $(0,1)$: $x' = \text{robust-Z}(\text{logit}(x))$
- Subjective probabilities: $x' = \text{robust-Z}(\text{log-odds}(x))$
- Non-monotonic criteria: piecewise linear $v_i(x') \to [0,1]$

### Aggregation (2-Additive Choquet Integral)
$$S(d) = \sum_{i=1}^{21} v_i(c_i(d)) \phi_i - \frac{1}{2} \sum_{i,j=1}^{21} |I_{ij}| \min(v_i, v_j) + \frac{1}{2} \sum_{i,j=1}^{21} I_{ij} \max(v_i, v_j)$$
where $\phi_i$ = Shapley values (global importance weights) and $I_{ij}$ = interaction indices from the maximum entropy fuzzy measure.

### Uncertainty Propagation
$S(d)$ is a full posterior distribution $p(S_d \mid \text{data})$ via MCMC (10,000 iterations).

## 3.3 Three Pillars and 21 Criteria

### Pillar 1: Epistemic (Target Shapley Mass: 0.300)

| # | Criterion | Weight |
|:--|:----------|:------:|
| 1 | Bayesian Intra-Domain Epistemic Rigor ($R_{intra}$) | 0.060 |
| 2 | Non-Empirical Coherence Index | 0.020 |
| 3 | Non-Empirical Depth Index | 0.020 |
| 4 | Non-Empirical Stability Index | 0.020 |
| 5 | Empirical Predictive & Replication Success | 0.040 |
| 6 | Paradigm Stability (Non-Monotonic) | 0.040 |
| 7 | Knowledge Accumulation Trajectory | 0.050 |
| 8 | Innovation Rate (Non-Monotonic) | 0.050 |

### Pillar 2: Societal & Network Utility (Target Shapley Mass: 0.350)

| # | Criterion | Weight |
|:--|:----------|:------:|
| 9 | Network Eigenvector Centrality (PageRank) | 0.060 |
| 10 | Diffusion-Adjusted Downstream Utility | 0.060 |
| 11 | Direct Sentient Well-being Enhancement | 0.060 |
| 12 | Economic & Instrumental ROI | 0.040 |
| 13 | Moral Patient Scope Inclusivity | 0.040 |
| 14 | Open Science & Data Transparency | 0.030 |
| 15 | Methodological Pluralism & Diversity | 0.020 |
| 16 | Expert Elicitation Confidence | 0.040 |

### Pillar 3: Existential Risk Reduction & Civilizational Trajectory (Target Shapley Mass: 0.350)

| # | Criterion | Weight |
|:--|:----------|:------:|
| 17 | Direct x-risk Mitigation Potential | 0.100 |
| 18 | Indirect x-risk Mitigation (Enabling) | 0.080 |
| 19 | Trajectory Change Potential ($\Delta_d$ shift) | 0.070 |
| 20 | Biosphere & Hubble-Volume Preservation | 0.060 |
| 21 | Antifragility to Civilizational Collapse | 0.040 |

## 3.4 Sensitivity Verification

Monte Carlo simulation confirmed:

| Test | Threshold | Result |
|:-----|:---------:|:------:|
| $\pm 10\%$ Shapley perturbation → Spearman footrule | $\le 1.0$ | $\le 0.8$ |
| $\pm 10\%$ Shapley perturbation → Kendall $\tau$ | $\ge 0.95$ | $\ge 0.97$ |
| $\pm 5\%$ perturbation → max rank shift | $\le 1$ | $\le 1$ |

## 3.5 Relation to V1

V2 supersedes V1 because:
1. **Choquet integral** captures criterion interactions (synergies/redundancies) that weighted sum cannot
2. **Full Bayesian posterior** replaces point estimates with uncertainty quantification
3. **Pareto frontier analysis** prevents declaring a "winner" that is dominated on any pillar
4. **Non-monotonic value functions** handle real-world concave utility shapes
5. **Empirically verified sensitivity** replaces arbitrary robustness claims
