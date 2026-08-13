# Adjudication instruments — Paper 01 major-revision round

You (the author) are the human second reviewer. These three forms inject your
own judgment into the decision chain and become the paper's only "validation"
numbers. Everything else in the pipeline is renamed to **consistency checks**.

**Before you start**: set aside ~2 hours. Do the three rounds in order. Do NOT
look up the original decisions while working. Fill the blank column in each CSV.

---

## Round 1 — Screening adjudication (screening-100.csv, ~40 min)

100 records, randomly seeded: 50 were included in the review, 50 excluded (27
not-structural, 17 no-subdomain, 4 date, 2 language). You see only id, title,
authors, year, abstract, source.

**Task**: for each row, decide **include** or **exclude** using the eligibility
rule as you would apply it fresh:

> "the research object is concerned with risks, control, alignment,
> generalisation, robustness, interpretability, evaluation, or governance of
> highly generalised, autonomous, or potentially self-improving systems,
> published 2015–2026 in English, peer-reviewed or grey."

Fill `user_decision` with `include` or `exclude`. If genuinely undecidable from
the abstract, write `uncertain`.

## Round 2 — σ-trap relevance adjudication (relevance-30.csv, ~40 min)

30 studies: 15 carried the heuristic schema-coherence/σ-trap relevance signal
(final rating ≥ 4 on a 1–5 scale), 15 did not. The original rating is hidden.
You see paper_id, title, year, and the charted relevance justification.

**Task**: rate each study's relevance to the schema-coherence/σ-trap question
**as a reviewer-defined heuristic** — "does this study engage with safety-
relevant internal structure, compositional generalisation, or the σ-trap
construct?" — on the same 1–5 scale (5 = directly engages the construct).
Fill `user_rating_1_5` with an integer 1–5.

## Round 3 — Borderline eligibility (borderline-15.csv, ~30 min)

15 records that the original screen flagged **Uncertain** (carried to full text,
then resolved). These are the boundary cases the reviewer's Concern 7 asks about
(reward-hacking RL not AGI-framed, general ML robustness, etc.).

**Task**: for each, decide **include** or **exclude**, and in one short line
state the deciding consideration (e.g., "not AGI-framed — exclude"; "explicit
safety motivation — include"). Fill `user_decision` and `user_justification`
(create the column if absent).

## After the rounds

1. Save the three filled CSVs back into this folder.
2. I will compute: Round 1 agreement + Cohen's κ vs the original screening;
   Round 2 agreement + κ (and per-rating distribution); Round 3 agreement on the
   uncertain set. Disagreements are logged, not resolved silently — the report
   will list every disagreement and you will make the final call on each.

## What I will NOT do

- I will not re-run, tune, or "fix" your decisions.
- I will not hide disagreements from the report.

## Keywords dictionary (for your review — Round 4, optional but recommended)

Theme membership (13 themes) is keyword-rule based over the charted text fields
(`key_contribution`, `relevance_justification`, `open_questions`), from
`charting/phase9_themes.py`:

| Theme | Rule tokens (any-hit; single words are token-prefix, phrases substring) |
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

**σ-trap relevance signal** (`charting/sigma_signal.py`): final rating 1–5 per
study on the reviewer-defined scale; studies with final ≥ 4 carry the signal
(534 of 1,136; 47.0%). The rating is seeded from a phrase scan and revised by
the LLM-assisted pass with justification text; the human adjudication (Round 2)
is the accuracy check on this variable.

**Eligibility rule** (the operational rule you apply in Rounds 1 and 3): see the
manuscript §3.2; exclusion reasons R-STRUCT (858), R-SUBJ (547), R-DATE (141),
R-LANG (43) across 1,589 excluded records.

If any rule token looks wrong to you (too broad, missing a synonym), note it in
the `user_notes` column of relevance-30 or on the dictionary page — synonym
sensitivity is a planned Phase D analysis and your edits to this dictionary are
the ground truth for it.
