# 7. Paper Type Evaluation

## 7.1 Context

With the research direction finalized (AGI Safety → Long-Term Agency → CEV), the next question is: what type of paper should be the first output of the Σ-Align project? Three candidates were evaluated using a 7-criteria MCDA framework following the same mathematical rigor as the domain selection.

## 7.2 Evaluation Framework

### Criteria and Weights

| # | Criterion | Weight | Rationale |
|:--|:----------|:------:|:----------|
| 1 | Scientific novelty | 20% | Does it produce new knowledge? |
| 2 | Time-to-submission | 15% | Can it be drafted and submitted quickly? |
| 3 | Career leverage | 15% | Does it strengthen research position / lab applications? |
| 4 | Venue prestige ceiling | 15% | Can it reach a top-tier venue? |
| 5 | Alignment with CEV direction | 15% | Does it feed directly into the terminal specialization? |
| 6 | Risk of rejection (inverse) | 10% | Probability of desk reject or major revisions |
| 7 | Reuse of Σ-Model assets | 10% | How much existing work carries forward |

### Candidates

| Option | Description | Est. Timeline |
|:------|:------------|:-------------:|
| **A: Sequel** | Extend ODE to model mesa-optimization and goal preservation explicitly. Show $\sigma$-trap equivalence to deceptive alignment emergence. | 4-6 months |
| **B: Position** | Argue that the $\sigma$-trap unifies compositional generalization and alignment failure. Synthesize existing literature with the Σ-Model as the bridge. | 1-3 months |
| **C: Formal Results** | Prove new theorems connecting the $\sigma$-trap, bifurcation theory, and formal alignment guarantees. Pure mathematical contribution. | 8-18 months |

## 7.3 Scoring

### Option A: Sequel Paper

| # | Criterion | Weight | Score | Weighted |
|:--|:----------|:------:|:----:|:--------:|
| 1 | Scientific novelty | 0.20 | 0.85 | 0.170 |
| 2 | Time-to-submission | 0.15 | 0.70 | 0.105 |
| 3 | Career leverage | 0.15 | 0.90 | 0.135 |
| 4 | Venue prestige ceiling | 0.15 | 0.85 | 0.128 |
| 5 | Alignment with CEV | 0.15 | 0.80 | 0.120 |
| 6 | Risk of rejection (inverse) | 0.10 | 0.80 | 0.080 |
| 7 | Reuse of Σ-Model assets | 0.10 | 0.95 | 0.095 |
| | **Total** | **1.00** | | **0.833** |

**Rationale:** Extends existing framework with new variables (mesa-optimization dynamics). Novel but bounded by existing paradigm. 95% reuse of Σ-Model ODE apparatus. Positions author as actively extending a published framework. Could target JAIR (continuation) or TMLR.

### Option B: Position Paper

| # | Criterion | Weight | Score | Weighted |
|:--|:----------|:------:|:----:|:--------:|
| 1 | Scientific novelty | 0.20 | 0.60 | 0.120 |
| 2 | Time-to-submission | 0.15 | 0.95 | 0.143 |
| 3 | Career leverage | 0.15 | 0.70 | 0.105 |
| 4 | Venue prestige ceiling | 0.15 | 0.70 | 0.105 |
| 5 | Alignment with CEV | 0.15 | 0.60 | 0.090 |
| 6 | Risk of rejection (inverse) | 0.10 | 0.90 | 0.090 |
| 7 | Reuse of Σ-Model assets | 0.10 | 0.80 | 0.080 |
| | **Total** | **1.00** | | **0.733** |

**Rationale:** Synthesizing existing work into a new framing is valuable but produces less new knowledge. Fastest timeline but weakest novelty and career leverage. Position papers are read widely but cited less. Moderate venue ceiling (CACM, AI & Society).

### Option C: Formal Results Paper

| # | Criterion | Weight | Score | Weighted |
|:--|:----------|:------:|:----:|:--------:|
| 1 | Scientific novelty | 0.20 | 0.95 | 0.190 |
| 2 | Time-to-submission | 0.15 | 0.30 | 0.045 |
| 3 | Career leverage | 0.15 | 0.95 | 0.143 |
| 4 | Venue prestige ceiling | 0.15 | 1.00 | 0.150 |
| 5 | Alignment with CEV | 0.15 | 0.90 | 0.135 |
| 6 | Risk of rejection (inverse) | 0.10 | 0.50 | 0.050 |
| 7 | Reuse of Σ-Model assets | 0.10 | 0.60 | 0.060 |
| | **Total** | **1.00** | | **0.773** |

**Rationale:** Highest novelty and prestige ceiling (Quantum, JACM, Nature). A formal theorem connecting $\sigma$-trap to alignment is career-defining. But timeline is long (8-18 months) and rejection risk is high — theorems must be completely correct.

## 7.4 Ranking

| Rank | Option | Score |
|:----:|:-------|:-----:|
| **1** | **A: Sequel Paper** | **0.833** |
| 2 | C: Formal Results Paper | 0.773 |
| 3 | B: Position Paper | 0.733 |

## 7.5 Recommended Strategy: A → C Pipeline

A (Sequel) and C (Formal Results) are not mutually exclusive. The optimal strategy is sequential:

1. **Publish A (Sequel)** first — 4-6 months, 95% reuse, establishes the mesa-optimization connection
2. **Publish C (Formal Results)** second — 8-12 months after A, deepest results, highest prestige

**Combined timeline:** ~12-18 months for two publications.

**Combined career leverage > either individually:** Shows sustained trajectory from a published framework through to deep theoretical results.

**Pipeline narrative:**
- Paper A: "The $\sigma$-trap as a formal model of mesa-optimization in deep learning"
- Paper C: "Threshold theorems for alignment: bifurcation analysis of goal preservation in recursively self-improving systems"

## 7.6 Target Venues

| Paper | Primary Venue | Secondary Venue |
|:------|:-------------|:----------------|
| A (Sequel) | JAIR (continuation), TMLR | NeurIPS, ICML |
| C (Formal Results) | *Quantum*, *Journal of the ACM* | *Nature Machine Intelligence* |
