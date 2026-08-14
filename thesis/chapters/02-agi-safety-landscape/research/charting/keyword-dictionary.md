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
Studies with final rating ≥ 4 carry the signal (464 of 1,136; 40.8%); the working export file additionally holds AI-revised rows below 4. The rating
is seeded from a phrase scan and revised by the LLM-assisted pass with recorded
justification; the author-adjudicated reliability check (Round 2 of the
adjudication instruments, `research/charting/adjudication/`) reports the
human-vs-pipeline agreement on this high-inference variable.

## Synonym-sensitivity: author-proposed token additions (Round 4)

The author proposed additional tokens per theme (Goodhart, scheming, rlaif/kto,
dictionary learning, red-teaming, pluralism, combinatorial generalisation, OOD,
inductive bias). New studies these would add beyond the current rules
(n = 1,136; deltas are upper bounds, overlap not subtracted):

| Theme | Proposed tokens | New studies hit |
|---|---|---|
| Proxy reward & reward hacking | goodhart, underspecification, proxy overoptim | +8 |
| Deceptive alignment & sycophancy | scheming, treacherous turn, power-seeking | +3 |
| Preference & value learning | rlaif, kto, preference elicitation | +8 |
| Interpretability & mechanistic analysis | dictionary learning, activation patching, linear represent | +1 |
| Robustness, security & adversarial | red-teaming, red teaming, trojan | +1 |
| Ethics, fairness & human values | pluralism, moral disagreement | +18 |
| Compositional generalization & σ-trap | combinatorial general, out-of-distribution, ood, inductive bias | +46 |

**Decision (recorded)**: headline theme counts remain on the current rules; the
deltas are reported here as sensitivity evidence. Two proposed tokens were not
adopted: `ood` / `out-of-distribution` (broad — would pull in distribution-shift
robustness work unrelated to compositional generalisation, the same over-inclusion
class the Round-4 false-positive notes flag) and `pluralism` (similarly broad
across ethics). `Goodhart`, `scheming`, `rlaif`, `kto`, `red teaming`, and
`combinatorial general` are safe additions and are adopted for future
re-operationalisations.
