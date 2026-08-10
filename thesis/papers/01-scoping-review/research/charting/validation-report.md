# Extraction validation report — Paper 01 Phase 7 (CC.1.6)

- Sample: **254** papers (20%, seed=20260901)
- Extractor 1: scripted heuristic (`heuristic.py`)
- Extractor 2: independent implementation (`extractor2.py`)
- External-AI pass on the sample: user-run (see README); AI revisions
  already merged into `charted-data.csv` via `merge_ai.py` are included
  in extractor-1 values where applied.
- ICC mode `--ai`: `relevance_sigma_trap` compared as heuristic seed
  vs post-AI value over the sample (extractor2 charts no continuous
  field; rater pair seed->AI per Task 7.3.3).

## Categorical fields (Cohen's kappa)

| Field | n | Raw agreement | Cohen's kappa |
|---|---|---|---|
| publication_type | 254 | 0.614 | 0.444 |
| methodology | 254 | 0.728 | 0.417 |
| discusses_internal_representations | 254 | 0.898 | 0.558 |
| discusses_schema_coherence | 254 | 0.984 | 0.742 |
| limitations_stated | 254 | 0.783 | 0.520 |
| subdomains::capabilities | 254 | 0.906 | 0.790 |
| subdomains::ethics | 254 | 0.890 | 0.780 |
| subdomains::governance | 254 | 0.894 | 0.704 |
| subdomains::interpretability | 254 | 0.906 | 0.719 |
| subdomains::mesa-optimization | 254 | 0.972 | 0.815 |
| subdomains::other | 254 | 0.965 | 0.000 |
| subdomains::robustness | 254 | 0.740 | 0.477 |
| subdomains::value alignment | 254 | 0.799 | 0.338 |
| formal_framework::decision theory | 254 | 0.953 | 0.602 |
| formal_framework::dynamical systems | 254 | 0.992 | 0.497 |
| formal_framework::game theory | 254 | 0.992 | 0.497 |
| formal_framework::information theory | 254 | 0.961 | 0.669 |
| formal_framework::none | 254 | 0.776 | 0.485 |
| formal_framework::other | 254 | 0.807 | 0.376 |
| mathematical_formalism::ODEs | 254 | 0.811 | 0.063 |
| mathematical_formalism::logic | 254 | 0.823 | 0.485 |
| mathematical_formalism::none | 254 | 0.835 | 0.658 |
| mathematical_formalism::optimization | 254 | 0.846 | 0.686 |
| mathematical_formalism::probability | 254 | 0.902 | 0.760 |

## Continuous fields (ICC(2,1))

| Field | n | ICC |
|---|---|---|
| relevance_sigma_trap | 254 | 0.930 | (seed vs post-AI; 25 sample revisions)

## Disagreement examples (first 8 per field, for reconciliation)

- `P003` **publication_type**: ex1=`position` ex2=`other` — Architecturally Aligned Trustworthy AI: Substrate and System Design St
- `P007` **publication_type**: ex1=`position` ex2=`other` — Relative Principals, Pluralistic Alignment, and the Structural Value A
- `P012` **publication_type**: ex1=`review` ex2=`other` — Teach AI What It Doesn’t Know
- `P048` **publication_type**: ex1=`theoretical` ex2=`empirical` — Could We Control Superintelligent AI?
- `P080` **publication_type**: ex1=`empirical` ex2=`other` — A data-driven generative strategy to avoid reward hacking in multi-obj
- `P098` **publication_type**: ex1=`position` ex2=`other` — Moral disagreement and the limits of AI value alignment: a dual challe
- `P1036` **publication_type**: ex1=`theoretical` ex2=`other` — Limitations on formal verification for AI safety
- `P108` **publication_type**: ex1=`theoretical` ex2=`other` — Survival egoism: we are, they will be
- `P016` **methodology**: ex1=`experiment` ex2=`simulation` — Belief-Driven Value Alignment for Human-Robot Collaboration
- `P068` **methodology**: ex1=`experiment` ex2=`analysis` — LLM ethics benchmark: a three-dimensional assessment system for evalua
- `P105` **methodology**: ex1=`experiment` ex2=`simulation` — Moral Anchor System: A Predictive Framework for AI Value Alignment and
- `P1072` **methodology**: ex1=`experiment` ex2=`simulation` — Reward hacking in reinforcement learning
- `P1107` **methodology**: ex1=`experiment` ex2=`not_applicable` — Social value alignment in large language models
- `P117` **methodology**: ex1=`experiment` ex2=`not_applicable` — Investigating Temperature and Reasoning Effort in AI Alignment with Hu
- `P1188` **methodology**: ex1=`experiment` ex2=`not_applicable` — On the interplay of human-AI alignment, fairness, and performance trad
- `P1207` **methodology**: ex1=`experiment` ex2=`not_applicable` — Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for L
- `P003` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Architecturally Aligned Trustworthy AI: Substrate and System Design St
- `P012` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Teach AI What It Doesn’t Know
- `P1036` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Limitations on formal verification for AI safety
- `P1108` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Bias‑mitigation techniques in AI are methods applied at the data, mode
- `P118` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Coadaptive Value Alignment Blue Sky Ideas Track
- `P1188` **discusses_internal_representations**: ex1=`yes` ex2=`no` — On the interplay of human-AI alignment, fairness, and performance trad
- `P1204` **discusses_internal_representations**: ex1=`yes` ex2=`implicitly` — Minding Motivation: The Effect of Intrinsic Motivation on Agent Behavi
- `P1207` **discusses_internal_representations**: ex1=`yes` ex2=`no` — Regularized Best-of-N Sampling with Minimum Bayes Risk Objective for L
- `P161` **discusses_schema_coherence**: ex1=`related concept` ex2=`no` — VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large Lang
- `P213` **discusses_schema_coherence**: ex1=`related concept` ex2=`no` — BEE: Belief-Value-Aligned, Explainable, and Extensible Cognitive Frame
- `P277` **discusses_schema_coherence**: ex1=`related concept` ex2=`no` — Choice Vectors: Streamlining Personal AI Alignment Through Binary Sele
- `P384` **discusses_schema_coherence**: ex1=`related concept` ex2=`no` — From Pursuit of the Universal AGI Architecture to Systematic Approach 
- `P026` **limitations_stated**: ex1=`no` ex2=`yes` — Value Function Shaping-Based Backdoor Attacks on Deep Reinforcement Le
- `P036` **limitations_stated**: ex1=`yes` ex2=`no` — Secure and trustworthy energy systems: A four-layer threat model and d
- `P080` **limitations_stated**: ex1=`yes` ex2=`no` — A data-driven generative strategy to avoid reward hacking in multi-obj
- `P1072` **limitations_stated**: ex1=`yes` ex2=`no` — Reward hacking in reinforcement learning
- `P1107` **limitations_stated**: ex1=`yes` ex2=`no` — Social value alignment in large language models
- `P1203` **limitations_stated**: ex1=`yes` ex2=`no` — Incomplete Contracting and Al Alignment
- `P1257` **limitations_stated**: ex1=`partially` ex2=`yes` — Synthesis and Properties of Optimally Value-Aligned Normative Systems
- `P133` **limitations_stated**: ex1=`yes` ex2=`no` — Optimising multi-value alignment: a multi-objective evolutionary strat
- `P003` **subdomains**: ex1=`value alignment; interpretability; robustness; mesa-optimization; governance; ethics; capabilities` ex2=`value alignment; interpretability; mesa-optimization; governance; ethics; capabilities` — Architecturally Aligned Trustworthy AI: Substrate and System Design St
- `P012` **subdomains**: ex1=`robustness; interpretability` ex2=`value alignment; interpretability; robustness; capabilities` — Teach AI What It Doesn’t Know
- `P026` **subdomains**: ex1=`value alignment; robustness; governance; ethics; capabilities` ex2=`value alignment; robustness; ethics; capabilities` — Value Function Shaping-Based Backdoor Attacks on Deep Reinforcement Le
- `P036` **subdomains**: ex1=`value alignment; robustness; mesa-optimization; governance; ethics; capabilities` ex2=`value alignment; robustness; mesa-optimization; governance; capabilities` — Secure and trustworthy energy systems: A four-layer threat model and d
- `P068` **subdomains**: ex1=`value alignment; interpretability; robustness; governance; ethics; capabilities` ex2=`value alignment; interpretability; robustness; ethics; capabilities` — LLM ethics benchmark: a three-dimensional assessment system for evalua
- `P069` **subdomains**: ex1=`value alignment; interpretability; robustness; ethics; capabilities` ex2=`value alignment; ethics` — MIRA: An LLM-Driven Dual-Loop Architecture for Metacognitive Reward De
- `P080` **subdomains**: ex1=`value alignment; capabilities` ex2=`value alignment` — A data-driven generative strategy to avoid reward hacking in multi-obj
- `P1001` **subdomains**: ex1=`value alignment` ex2=`` — Normative conflicts and shallow ai alignment: R. millière
- `P007` **formal_framework**: ex1=`game theory` ex2=`none` — Relative Principals, Pluralistic Alignment, and the Structural Value A
- `P044` **formal_framework**: ex1=`dynamical systems` ex2=`none` — Parallel Diffusion Solver via Residual Dirichlet Policy Optimization
- `P048` **formal_framework**: ex1=`other` ex2=`none` — Could We Control Superintelligent AI?
- `P069` **formal_framework**: ex1=`other` ex2=`none` — MIRA: An LLM-Driven Dual-Loop Architecture for Metacognitive Reward De
- `P080` **formal_framework**: ex1=`other` ex2=`none` — A data-driven generative strategy to avoid reward hacking in multi-obj
- `P1036` **formal_framework**: ex1=`none` ex2=`other` — Limitations on formal verification for AI safety
- `P105` **formal_framework**: ex1=`other` ex2=`none` — Moral Anchor System: A Predictive Framework for AI Value Alignment and
- `P1162` **formal_framework**: ex1=`decision theory` ex2=`none` — AI Alignment Problem: "Human Values" Idea is Built Upon Many Assumptio
- `P003` **mathematical_formalism**: ex1=`optimization` ex2=`ODEs; logic; optimization` — Architecturally Aligned Trustworthy AI: Substrate and System Design St
- `P007` **mathematical_formalism**: ex1=`probability; optimization` ex2=`logic; optimization` — Relative Principals, Pluralistic Alignment, and the Structural Value A
- `P012` **mathematical_formalism**: ex1=`probability; optimization` ex2=`ODEs; probability; logic; optimization` — Teach AI What It Doesn’t Know
- `P043` **mathematical_formalism**: ex1=`none` ex2=`optimization` — Human-Machine Moral Divergence
- `P045` **mathematical_formalism**: ex1=`none` ex2=`ODEs` — The Power of Stories: Narrative Priming in Networked Multi-Agent LLM I
- `P048` **mathematical_formalism**: ex1=`logic` ex2=`optimization` — Could We Control Superintelligent AI?
- `P069` **mathematical_formalism**: ex1=`probability; logic; optimization` ex2=`ODEs; probability; logic; optimization` — MIRA: An LLM-Driven Dual-Loop Architecture for Metacognitive Reward De
- `P080` **mathematical_formalism**: ex1=`probability; optimization` ex2=`optimization` — A data-driven generative strategy to avoid reward hacking in multi-obj
