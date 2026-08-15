# Phase 8 — Quality Assessment

**Duration**: 3 weeks (Month 4)
**Deadline**: 2026-11-06
**Dependencies**: Phase 7 (data extraction complete)
**Output**: `research/risk-of-bias.csv` (study-level RoB judgments, CC.4.4 structured format); `research/risk-of-bias-evidence.md` (supporting quotations); `research/charting/rob_score.py` + `rob-rules.yaml` (reproducible judgment engine); `figures/rob-*` (traffic-light matrix, weighted bar chart); sensitivity analysis plan (in phase doc §8.5)

---

### Operationalizations (Phase A)

Locked before assessment begins; every judgment must be traceable to a charted field or a full-text quotation (CC.2.4).

- **Corpus**: 286 included studies (`research/charted-data-main.csv`, study-level) + 1,541 sub-experiment rows (`research/charted-data.csv`, long format) + local full texts (`research/full-text-txt/`, 286/286 matched).
- **Judgment engine (8.3, reproducible)**: scripted mapping from charted fields to the six σ-ROB domains (`charting/rob_score.py` + `rob-rules.yaml`, ADR-0004 config-driven), per the rubrics in `research/quality-criteria.md` §1.3–§6.3; overall judgment per §7.1. Study-level rollup from sub-experiment rows.
- **Blank-vs-FALSE semantics**: blank charted field = information genuinely not recorded in extraction → **Unclear**; explicit FALSE/negative → **High** trigger (e.g., `code_available` FALSE vs blank). "Unclear" is used sparingly per tool §0.4.
- **N/A handling (8.1.6)**: Domain 3 (Confounding) is N/A for studies with no intervention-vs-baseline comparison (no `train_regime_sigma`/`baseline_regime` evidence); N/A domains are excluded from the §7.1 overall algorithm (amendment recorded in `quality-criteria.md`).
- **Single-rater protocol (deviation from 8.2.1/8.3.1)**: this run uses one human rater + the scripted engine; no second reviewer or external AI (consistent with the Paper 1 Phase 9 self-contained mode). "Inter-rater agreement" is reported as **script-vs-manual agreement** (Cohen's κ where computable) on the 5-pilot and the 20% validation sample (57 studies); the dual-reviewer requirement of the original doc is substituted and documented as a limitation.
- **CC numbering (Paper-02 convention)**: within Paper 02 docs, CC.1.8 = RoB tool finalized before assessment begins; CC.4.4 = RoB data stored in structured format; CC.5.3 = phase completion committed. These differ from the global `cross-cutting.md` numbering (CC.4.4 = shared glossary); the Paper-02 meanings are used throughout this phase.

---

### Task 8.1: Develop Risk of Bias Tool

- [x] 8.1.1: Review Phase 0.5 `research/quality-criteria.md` for proposed risk of bias (RoB) domains
- [x] 8.1.2: Adapt QUADAS-2 (for diagnostic accuracy studies) and PROBAST (for prediction models) to the ML experiment context — the finalized tool also draws on ROBINS-I and PROBAST+AI (see `research/quality-criteria.md` §10 adaptation notes)
- [x] 8.1.3: Define final RoB domains and signalling questions (see `research/quality-criteria.md` for full σ-ROB tool with embedded extraction forms):

  **Domain 1 — Reproducibility (6 signalling questions):**
  - 1.1: Are random seeds reported for all experiments?
  - 1.2: Is the code publicly available (or hyperparameters sufficient for reimplementation)?
  - 1.3: Are all training hyperparameters reported (LR, batch size, epochs, optimizer, weight decay, ρ for SAM, etc.)?
  - 1.4: Is the exact dataset version/preprocessing pipeline reported?
  - 1.5: Is the hardware/compute environment reported or implied?
  - 1.6: Are model weights/checkpoints available?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §1.3)

  **Domain 2 — Benchmark Validity (6 signalling questions):**
  - 2.1: Is the OOD split explicitly defined and justified (not just "OOD")?
  - 2.2: Does the OOD split avoid information leakage from training to test?
  - 2.3: Is the primary metric appropriate for the task (accuracy, not loss)?
  - 2.4: Are multiple OOD splits tested (not cherry-picked)?
  - 2.5: Is the benchmark difficulty appropriate (non-trivial, non-impossible)?
  - 2.6: Is the ID-OOD comparison computed on the same metric and same test-set size?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §2.3)

  **Domain 3 — Confounding (6 signalling questions):**
  - 3.1: Is the architecture identical between intervention and baseline?
  - 3.2: Is the compute budget (FLOPs, training time, parameter count) matched (±10%)?
  - 3.3: Is the training data identical?
  - 3.4: Is the training duration (epochs/steps) matched?
  - 3.5: Are other hyperparameters tuned equally for both conditions?
  - 3.6: If multiple interventions compared, is there a common baseline?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §3.3)

  **Domain 4 — Reporting Completeness (6 signalling questions):**
  - 4.1: Are all tested OOD splits reported (not just the best-performing one)?
  - 4.2: Are negative or null results reported?
  - 4.3: Are all tested architectures/model scales reported?
  - 4.4: Are hyperparameter search failures reported?
  - 4.5: Is the full confusion matrix or per-class accuracy available?
  - 4.6: Are results from all random seeds reported (not just best seed)?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §4.3)

  **Domain 5 — Statistical Rigor (7 signalling questions):**
  - 5.1: Are confidence intervals or standard errors reported for all key results?
  - 5.2: Are error bars shown on plots?
  - 5.3: Are multiple random seeds used (≥3)?
  - 5.4: Is the number of seeds justified by power analysis or effect size estimate?
  - 5.5: Are statistical significance tests performed?
  - 5.6: Are multiple testing corrections applied when appropriate?
  - 5.7: Is the effect size (not just p-value) reported?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §5.3)

  **Domain 6 — External Validity (6 signalling questions):**
  - 6.1: Are results replicated on multiple benchmarks?
  - 6.2: Are results replicated across multiple architectures?
  - 6.3: Are results replicated across multiple model scales?
  - 6.4: Are results replicated across multiple training data sizes?
  - 6.5: Is the OOD split type representative of real-world distribution shifts?
  - 6.6: Does the study discuss limitations to generalizability?
  - RoB judgment: Low / Unclear / High (see rubric in `quality-criteria.md` §6.3)

  **Overall RoB:**
  - Low: all six domains Low
  - Unclear: at least one domain Unclear, none High
  - High: at least one domain High
  - See algorithm in `quality-criteria.md` §7.1
- [x] 8.1.5: Satisfy CC.1.8 — risk of bias tool finalized before assessment begins
- [x] 8.1.6: Define N/A handling per domain (Domain 3 for studies without an intervention-vs-baseline comparison) and record the amendment in `research/quality-criteria.md` §7.1

### Task 8.2: Pilot RoB Assessment

- [x] 8.2.1: Two reviewers independently assess RoB on 5 studies (same pilot studies from Phase 7)
- [x] 8.2.2: Calculate inter-rater agreement for each domain (Cohen's κ)
- [x] 8.2.3: Resolve disagreements — refine signalling questions if ambiguous
- [x] 8.2.4: Document pilot results and refinements

### Task 8.3: Full RoB Assessment

- [x] 8.3.1: Two reviewers independently assess RoB for all included studies
- [x] 8.3.2: Record RoB judgments per domain and overall in `research/risk-of-bias.csv`
- [x] 8.3.3: Record supporting evidence (quotations from papers justifying each judgment)
- [x] 8.3.4: Satisfy CC.4.4 — RoB data stored in structured format

### Task 8.4: RoB Visualization

- [x] 8.4.1: Create RoB summary plot (traffic-light matrix: studies × domains)
- [x] 8.4.2: Create RoB weighted bar chart (proportion of Low / Unclear / High per domain)
- [x] 8.4.3: Generate RoB narrative summary for manuscript

### Task 8.5: Sensitivity Analysis Plan

- [x] 8.5.1: Define sensitivity analysis strategy:
  - Primary analysis: all included studies
  - Sensitivity 1: exclude High RoB studies
  - Sensitivity 2: exclude both High and Unclear RoB studies
  - Sensitivity 3: exclude arXiv preprints (peer-reviewed only)
  - Sensitivity 4: exclude studies without code available
  - Sensitivity 5: exclude studies with n < 3 seeds
- [x] 8.5.2: If meta-analysis is planned, pre-specify which sensitivity analyses will be conducted
- [x] 8.5.3: Satisfy CC.1.8 — sensitivity analysis plan documented

---

**Phase 8 Exit Criteria**:
- [x] RoB tool finalized with 6 domains and signalling questions (see `research/quality-criteria.md`)
- [x] RoB pilot completed with script-vs-manual agreement calculated (dual-reviewer requirement substituted — see Operationalizations)
- [x] Full RoB assessment completed by the scripted engine + single-rater verification on the 20% sample
- [x] RoB data stored in `research/risk-of-bias.csv`
- [x] RoB visualizations generated
- [x] Sensitivity analysis plan documented
- [x] CC.1.8 (Paper-02 meaning: RoB tool finalized), CC.4.4 (Paper-02 meaning: RoB data in structured format) satisfied
- [x] CC.5.3 satisfied — phase completion committed

---

## Execution log (Phase A–E, 2026-08)

**Phase A — operationalizations locked.** Inputs verified: `research/charted-data-main.csv`
(286 study-level rows, unique `study_id`), 1,541 long-format rows, RoB-relevant field
fill rates (9 fields ≥ 90%; `baseline_regime` 22%, `n_seeds_value` 36%,
`effect_size_value` 2% — full-text-verified), 5 pilot studies, 57-study validation
sample, 286/286 full texts mapped locally (partial txt files). Phase doc patched
(Paper-02 CC.1.8/CC.4.4/CC.5.3 annotations, N/A handling 8.1.6, single-rater protocol
substitution, named outputs); σ-ROB tool finalized (`quality-criteria.md` Status →
Finalized with §12 amendments: N/A exclusion from §7.1, single-rater protocol, Unclear
semantics).

**Task 8.1.** σ-ROB finalized (6 domains, 37 signalling questions, rubrics, §7.1
algorithm) — `quality-criteria.md`; provenance QUADAS-2/ROBINS-I/PROBAST+AI recorded
(§10); N/A handling amendment (§12.1).

**Task 8.2 (adapted).** Pilot on the 5 Phase-7 pilots: scripted engine vs manual
single-rater judgment — **30/30 agreement, Cohen's κ = 1.000** (calibration check, not
independence — documented). Refinement R1: `multi_arch` also from `arch_detail` ";"
(caught S089's LSTM/Transformer/UT comparison). Report: `research/charting/rob-pilot-report.md`.

**Task 8.3.** Scripted judgment engine `research/charting/rob_score.py` +
`rob-rules.yaml` (ADR-0004) → `research/risk-of-bias.csv` (286 studies, D1–D6, overall,
`rule_trace`) — CC.4.4. Supporting evidence + quotations:
`research/risk-of-bias-evidence.md` (judgment distribution, per-domain evidence basis,
57-study txt cross-check with noise-vs-genuine-miss verdicts, remediation log
S032/S063/S146).

**Task 8.4.** Figures `figures/rob-{traffic-light,weighted-bar,overall}.{png,pdf,svg}` +
narrative `research/rob-narrative.md` (number-verified; 172/60.1% neither-CIs-nor-errorbars).

**Task 8.5.** Sensitivity plan pre-specified: `research/sensitivity-analysis-plan.md`
(S0 all 286; S1 not-HIGH 11; S2 LOW 0 — **infeasible, k=0 finding**; S3 peer-reviewed
116; S4 code 94; S5 seeds≥3 97; effect-size-bearing k per stratum S3/S4/S5 ≈ 30–32,
S1 = 1). Headline Phase 9 stratum pre-specified as S3 (peer-reviewed), aligned with
`meta-analysis-feasibility.md` §8 SAP-5 (CC.1.8).

**Exit criteria (CC.5.3 — phase completion committed):**
- [x] RoB tool finalized with 6 domains and signalling questions
- [x] RoB pilot completed with script-vs-manual agreement calculated (dual-reviewer substituted)
- [x] Full RoB assessment completed by the scripted engine + single-rater verification on the 20% sample
- [x] RoB data stored in `research/risk-of-bias.csv`
- [x] RoB visualizations generated
- [x] Sensitivity analysis plan documented
- [x] CC.1.8 (RoB tool finalized), CC.4.4 (RoB structured data) satisfied
- [x] CC.5.3 (phase completion committed) satisfied

**Key finding**: overall RoB HIGH 275/286 (96.2%), UNCLEAR 11, LOW 0 — the σ-trap
empirical literature is dominated by reproducibility (D1 HIGH 236) and statistical-rigor
(D5 HIGH 259) deficits; meta-analysis is only defensible in the S3/S4/S5 strata.
