# Author-adjudication report — Paper 01 (Review #17, Concern 1/2/4/7 response)

Date: 2026-08 · Instruments: `research/charting/adjudication/` (README.md + 3 forms)
Role: the author (Basyirin Amsyar Basri) acted as the independent second reviewer on three
seeded samples. The original pipeline decisions were hidden during adjudication. This report
is written by the pipeline; every disagreement is listed, none was silently resolved.

---

## Round 1 — Screening adjudication (n = 100)

Seeded: 50 included / 50 excluded (27 not-structural, 17 no-subdomain, 4 date, 2 language),
random, original decisions hidden. Author decisions: 50 include / 50 exclude (no "uncertain").

| Measure | Value |
|---|---|
| Raw agreement | **74%** |
| Cohen's κ (2-category) | **0.480** |
| Include precision / recall (author vs original) | 74% / 74% |

Comparison with the pipeline's mechanical re-screen (n = 430): raw 69%, κ = 0.39.
**The author's own screening reproduces the original calibrated decisions better than the
mechanical rule does** — the paper's previously weakest statistic (κ = 0.39) now has a
human anchor at κ = 0.48, 74% raw.

Disagreement pattern (26 of 100): 13 records the author would exclude that were included —
predominantly human-AI interaction / HCI-style work (e.g., TouchAI perceptual alignment,
AI ageism, textiles, multimodal creation); 13 the author would include that were excluded —
predominantly safety-adjacent conceptual work (mechanistic interpretability, corrigibility,
bootstrapped alignment, value-forks, ALBA). The author's boundary is systematically stricter
on human-interaction studies and more inclusive of safety-theory studies. Full list in
`screening-100-analysed.csv`.

**Interpretation**: the original screen's inclusion of HCI-flavoured human-AI work was
liberal relative to the author's own current application of the rule (consistent with
Review #17 Concern 7's "broad inclusion may inflate the corpus"); the subdomain shares
(notably human-AI interaction, 106 studies) should be read with this boundary in mind.
Claims remain provisional.

## Round 2 — σ-trap relevance adjudication (n = 30)

Seeded: 15 signal (final ≥ 4) / 15 non-signal, original ratings hidden. Author ratings
spread 1–5 (6×1, 7×2, 2×3, 13×4, 2×5).

| Measure | Value |
|---|---|
| Raw agreement, 5-category | **80%** |
| Cohen's κ, 5-category | **0.715** (substantial) |
| Raw agreement, dichotomised (signal = rating ≥ 4) | **100%** |
| Cohen's κ, dichotomised | **1.000** |
| Signal precision / recall (author vs pipeline) | 100% / 100% |

The 6 rating disagreements are all ±1 point (e.g., 4 vs 5, 1 vs 2) with no directional
bias (3 higher, 3 lower by the author). Full list in `relevance-30-analysed.csv`.

**Interpretation**: the human check **fully confirms the pipeline's signal membership**
(15/15 in both directions). The reviewer-defined σ-trap relevance variable — the
highest-inference coding in the review — is now anchored to human judgment with κ = 1.000
on membership and 0.715 on the full scale.

## Round 3 — Borderline eligibility adjudication (n = 15)

The 15 records the original screen flagged *Uncertain* (carried to full text). Final
status: all 15 were ultimately included. Author decisions: 12 include / 3 exclude.

| Measure | Value |
|---|---|
| Raw agreement with final status | **80%** (12/15) |
| Cohen's κ | not meaningful (final column is constant) |
| Author would exclude | TAUCHI-GPT (P01_1197), PHIVE (P01_0287), Child Helpline Counselors (P01_0501) — value-alignment applications in applied/HCI contexts |

**Interpretation**: the uncertain→include resolution was correct for 12/15; 3 included
studies sit outside the author's current boundary. The eligibility rule's precision on the
uncertain tail is 80%, with the same HCI-flavoured pattern as Round 1. κ is undefined here
because one rater's column is constant — reported as raw agreement with that caveat.

---

## Headline for the manuscript

- **Screening**: author re-screen n=100 — raw 74%, κ = 0.48 (vs mechanical rule κ = 0.39).
- **Relevance signal**: author adjudication n=30 — 5-cat κ = 0.72, membership κ = 1.00 (15/15).
- **Borderline**: author adjudication n=15 — 80% agreement with final status; 3 exclusions.

The human layer improves on the mechanical screening rule, fully confirms the high-inference
signal, and flags a liberal HCI-flavoured inclusion boundary (26% screening disagreement).
Claims in the manuscript are therefore reported as provisional, per Review #17's priority
revision 1.

## Files

- `screening-100-analysed.csv`, `relevance-30-analysed.csv`, `borderline-15-analysed.csv` —
  adjudicated rows with original decisions and agreement flags.

---

## Round 4 — Keyword critique + signal-definition correction (author notes)

The author's round-4 notes (relevance-30-v2.csv `user_notes` column) flagged
semantic false positives in the keyword rules and exposed a definitional bug in
the σ-trap signal headline:

1. **Signal definition corrected**: the working export file was defined as
   "final rating ≥ 4 OR AI-revised", which pulled 70 revised-but-non-signal rows
   (final < 4) into the reported count. The corrected signal is **final rating
   ≥ 4: 464 studies (40.8%)**, replacing 534 (47.0%) in the manuscript, abstract,
   discussion, sensitivity (49.5% in the A+B subset), and submission artifacts.
   Example: P047 (chemometrics, final = 1, AI-revised) was in the export and is
   now correctly outside the signal.
2. **Proposed-token sensitivity**: the author's synonym additions were tested
   (deltas in `keyword-dictionary.md`); two broad tokens (OOD, pluralism) were
   rejected on the author's own over-inclusion criterion; six safe tokens
   adopted for future re-operationalisations.
3. **Two external-AI claims were checked and rejected**: the claimed `reward
   missecif` typo does not exist (the script has `reward misspecif`), and
   `sigma-trap` was already present in Theme 13 — both were verified against
   `phase9_themes.py` before any change.

Outcome: the human layer not only confirmed pipeline decisions (Rounds 1–3) but
caught a real error in a headline number, which is now corrected.
