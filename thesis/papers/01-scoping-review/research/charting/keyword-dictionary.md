# Keyword dictionary — Paper 01 supplementary material

Theme membership (13 axial themes) is keyword-rule based over the charted text
fields (`key_contribution`, `relevance_justification`, `open_questions`).
Rules are any-hit: single words are token-prefix matches, phrases are substring
matches. Source of truth: `research/charting/phase9_themes.py` (THEMES dict).

| Theme | Rule tokens |
|---|---|
| Proxy reward & reward hacking | reward hack(ing), specification gaming, proxy reward, reward model(s), proxy objective, reward overoptimization, reward misspecif |
| Deceptive alignment & sycophancy | deceptive alignment, decept(ion), sycophancy, machiavellian, betrayal, ulterior |
| Preference & value learning (RLHF/DPO) | rlhf, reinforcement learning from human feedback, preference learning/optimization/data, human feedback, dpo, constitutional ai |
| Evaluation, benchmarks & measurement | benchmark(s), evaluation, evaluat, metric(s), measurement, test item, test suite, assess |
| Interpretability & mechanistic analysis | interpretab, mechanistic, circuit, probing, monosemantic, feature attribution, sparse autoencoder, neuron |
| Internal representation structure & schema | internal representation, representation structure/engineering, schema, latent, world model, model internals, activation, representational |
| Robustness, security & adversarial | robust, adversarial, attack, defense/defence, jailbreak, poisoning, backdoor, prompt injection, security |
| Governance, incentives & sociotechnical | governance, regulation(ory), oversight, incentive, principal-agent, sociotechnical, audit, accountability, legislation |
| Ethics, fairness & human values | moral, ethic(s), fairness, bias, human values, rights, beneficence, responsibility, society |
| Capabilities, control & existential risk | control problem, existential risk, superintelligence, x-risk, catastrophic, misalignment, alignment problem, agi, corrigibility |
| Formal methods & mathematical theory | formal, theorem, proof, axiom(atic), bayesian, mathematical, probability, decision theory, game theory, dynamical systems, optimization theory |
| Human-AI interaction & collaborative alignment | human-ai, human-robot, human-machine, human in the loop, joint reasoning, collaboration, interactive |
| Compositional generalization & σ-trap | compositional generalization, sigma trap, σ-trap, compositional, systematic generalization, schema coherence |

## Synonym-sensitivity test (G2 robustness; §4.5 of the manuscript)

Counts over the same charted text fields (n = 1,136 unique studies):

| Term variant | Studies |
|---|---|
| compositional generali(z)ation | 44 |
| systematic generali(z)ation | 1 |
| generalisation failure | 0 |
| generalization failure | 7 |
| distribution shift | 7 |
| goal misgeneralization / misgeneralisation | 0 |
| schema coherence (literal) | 11 |
| latent structure | 0 |
| world model | 5 |
| internal representation (literal) | 14 |
| catastrophic forgetting | 0 |
| continual learning | 0 |

Interpretation: the vocabulary-absence findings (G2, G5) are robust to synonym
variants; they reflect vocabulary sparsity in the corpus, not a narrow rule.

## σ-trap relevance signal

Rating scale 1–5 (reviewer-defined heuristic; `research/charting/sigma_signal.py`).
Studies with final rating ≥ 4 carry the signal (534 of 1,136; 47.0%). The rating
is seeded from a phrase scan and revised by the LLM-assisted pass with recorded
justification; the author-adjudicated reliability check (Round 2 of the
adjudication instruments, `research/charting/adjudication/`) reports the
human-vs-pipeline agreement on this high-inference variable.
