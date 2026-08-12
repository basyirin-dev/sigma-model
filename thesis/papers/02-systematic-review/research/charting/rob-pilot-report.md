# RoB Pilot Report — Paper 02 Phase 8 (Task 8.2)

**Status**: Complete (2026-08)
**Protocol**: adapted — single human rater + scripted engine (see phase-doc
Operationalizations; dual-reviewer requirement substituted)
**Pilot studies**: S089 (CFQ, P02_0622), S109 (gSCAN, P02_0643), S061 (COGS,
P02_0594), S046 (E2A/SAM, P02_0386), S038 (VL2V-ADiP, P02_0151) — same pilot
studies as Phase 7 (stratified: 3 compositional benchmarks, 1 vision domain
shift, 1 σ-coupled intervention)

## 1. Method

- **Scripted pass**: `charting/rob_score.py` judgments from charted fields.
- **Manual pass**: independent single-rater judgment per σ-ROB rubric
  (`research/quality-criteria.md` §1.3–§6.3), informed by the charted fields and
  targeted full-text evidence extraction from `research/full-text-txt/`
  (seed/code/CI/significance/hyperparameter/limitation patterns).
- **Note on full text**: local txt files are **partial** (e.g., S089's file ends
  mid-appendix); manual judgments therefore lean on charted + available text and
  use the same blank→Unclear / FALSE→High semantics as the engine.

## 2. Results

| Study | D1 | D2 | D3 | D4 | D5 | D6 | Overall |
|---|---|---|---|---|---|---|---|
| S089 | LOW/LOW | LOW/LOW | UNCLEAR/UNCLEAR | LOW/LOW | HIGH/HIGH | LOW/LOW | HIGH |
| S109 | LOW/LOW | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | HIGH/HIGH | UNCLEAR/UNCLEAR | HIGH |
| S061 | LOW/LOW | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | HIGH/HIGH | UNCLEAR/UNCLEAR | HIGH |
| S046 | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | HIGH/HIGH | UNCLEAR/UNCLEAR | HIGH |
| S038 | HIGH/HIGH | UNCLEAR/UNCLEAR | UNCLEAR/UNCLEAR | HIGH/HIGH | HIGH/HIGH | LOW/LOW | HIGH |

Format: scripted/manual. **Agreement: 30/30 domain judgments (100%); Cohen's κ =
1.000 (pe = 0.393).**

## 3. Interpretation and caveats

- The manual pass is **informed by the same charted fields** as the engine, so
  this is a **calibration/consistency check, not an independence measure**; the
  κ = 1.000 should be read as "the rules faithfully implement the rubric over the
  charted data as read by the rater", not as dual-reviewer agreement. The
  dual-reviewer IRR protocol (quality-criteria.md §8) remains normative for
  future runs.
- S061: the full text's "significantly more challenging" is rhetorical, not a
  statistical test — charted `sig_test_reported=FALSE` confirmed; D5 HIGH stands.
- S046: hyperparameters (param_count, data sizes) are blank in charted data and
  unverifiable from the partial text → D1 UNCLEAR stands.

## 4. Refinements from the pilot

- **R1 (D6 External Validity)**: `multi_arch` computed from `arch_id` multiplicity
  alone under-detects multi-architecture studies (S089 compares LSTM/Transformer/
  Universal Transformer). Refinement: `multi_arch` also TRUE when `arch_detail`
  contains ";" (verified against 27 D6-LOW studies; e.g., S038 student ViT +
  teacher CLIP, S026 64-model collection, S126 ResNet-18 + XLM-R — all genuine
  multi-arch). Applied in `rob_score.py`.
- No other rule changes: the pilot confirmed the blank→Unclear / FALSE→High
  semantics and the per-domain defaults (D3 default UNCLEAR, D4/D5/D6 default
  UNCLEAR unless positive evidence).

## 5. Follow-ups

- Full-text verification on the 20% validation sample (57 studies) quantified
  charted-FALSE vs text-presence contradictions (code 14, seeds 13, ci 12, sig 1);
  spot-checks identified genuine charting misses (S032 code, S063 seeds, S146
  bootstrap CIs + seeds) → logged in `research/risk-of-bias-evidence.md` for
  remediation, with the engine documented as conservative.
