# Phase 08 — Epistemology & Framing Pass

**Duration**: 2–3 days
**Deadline**: after P07
**Dependencies**: P07 draft
**Output**: framing-passed manuscript + abstract
**Executor**: Agent + user approval of abstract/title
**Status**: ✅ Complete (pending user approval of abstract/title) — phenomenological framing verified, overclaims removed, ethics + research-programme paragraphs added, abstract rewritten (215 words), build clean with 0 undefined references

## Result (2026-08-16)

- **Abstract rewritten** (215 words ≤ 250): structured Problem/Method/Results/Conclusion, gate numbers (gap 44.3 pp; fixed-weight = additive, p=0.99; proxy does not precede OOD), phenomenological framing, descriptive conclusion — the last `??` (eq:lr-modulation) is cleared; 0 undefined refs.
- **Overclaim sweep**: ledger-§E grep list returns zero hits across the whole manuscript (incl. appendices); §1/§3 phenomenological statements verified; three-layer separation clean (§3 Lemmas/Props + Conjecture, §7 Model-vs-SGD boundary, §11 empirical, §12 claim-status table).
- **Broader Impact** subsection added after §13 (clinical dual-use note, limited scope, no AGI-safety language).
- **Research-programme** paragraph in §13: foundational hypothesis as a labelled future hypothesis.
- Title A retained; **user approval of abstract + title** is the remaining exit criterion.

## Purpose

Apply the epistemic discipline that directly answers the JAIR desk-rejection grounds
("strong claims obscured by opaque language", "overbroad claims"): explicit
phenomenological framing, three-layer claim separation, deletion of overclaiming
sentences, a clinical ethics paragraph, and a research-programme statement for the
foundational hypothesis.

## Tasks & subtasks

1. **Phenomenological statement** — §1 and §3: "we posit these ODEs; we do not derive them
   from SGD"; the SGD↔ODE mapping is Conjecture 1 (not a theorem)
2. **Three-layer separation sweep** — every §3/§7/§11/§12 result labelled as
   model theorem / empirical observation / interpretation; no bleeding between layers
3. **Delete overclaiming sentences** (ledger §E): "not only know more, but understand
   better"; "convert every depth-accumulating agent into a principled generaliser";
   unqualified "bifurcation phenomenon, not a capacity or data problem";
   "necessary and sufficient" Phase-2 phrasing → "necessary within the model"
4. **Ethics / Broader Impact** — one clinical paragraph (3–5 sentences): the same
   σ-targeting curricula could in principle be inverted to keep σ_A below threshold;
   dual-use direction not developed here. No AGI-safety/alignment language in intro or
   conclusion
5. **Research-programme paragraph** (Discussion): the foundational hypothesis
   ("schema-coherence dynamics may be a general mechanism underlying transitions from
   statistical competence to systematic understanding") stated explicitly as a labelled
   future hypothesis, not a claim
6. **Abstract rewrite (≤250 words)** per the locked claim level; structured
   (Problem/Method/Results/Conclusion); no "origin"; ambition via results, not framing
7. **Title finalisation** per P05 with gate-aware wording

## Expected outputs

- Framing-passed `paper/manuscript.tex`; approved abstract and title

## Decisions

- The foundational belief lives only in the Discussion research-programme paragraph
  (non-negotiable, from the consultations)

## Exit criteria

- No overclaiming sentence remains (grep-checkable list); abstract ≤250 words;
  user approval of abstract/title
