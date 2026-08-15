# Paper 06 v2 — Phase Roadmap (σ-Trap Narrow Paper + arXiv Companion)

**Date**: 2026-08-16
**Status**: Approved by user; implementation in progress
**Decision context**: JAIR desk-rejection 2026-07-15 (exposition/notation, overbroad claims, scope). Eight external-AI consultations distilled; structure decision = **Option 3** (one narrow σ-Trap paper for submission + a full arXiv companion preserving the extended framework), experiment-first (**mechanism gate** locks the claim level), venue path = **arXiv → direct TMLR**.

## Deliverables (locked)

| # | Deliverable | Path | Phase |
|:--|:------------|:-----|:------|
| D1 | Cross-cutting standards (standalone adaptation) | `paper/planning/cross-cutting.md` | 00 |
| D2 | Claim ledger | `paper/planning/claim-ledger.md` | 00 |
| D3 | Clean committed working tree (repo settlement) | repo root | 01 |
| D4 | Thesis + Σ-Align archived (reversible) | `archive/thesis/`, `archive/Σ-Align/` | 02 |
| D5 | Novelty audit + positioning note | `paper/planning/novelty-audit.md` | 03 |
| D6 | Gate-experiment result + decision | `paper/planning/gate-result.md` | 04 |
| D7 | Claim-level lock + paper blueprint | `paper/planning/paper-blueprint.md` | 05 |
| D8 | Narrow manuscript (TMLR format, self-contained) | `paper/manuscript.tex` → PDF | 06–09 |
| D9 | arXiv companion technical report | `paper/companion/` | 10 |
| D10 | Verification report | `paper/planning/verification-report.md` | 11 |
| D11 | arXiv bundle + TMLR submission package | `arxiv-submission/`, `paper/submission/` | 12 |
| D12 | Post-submission docs + follow-up roadmap | `paper/planning/follow-up-roadmap.md` | 13 |

## Phase exit criteria

- **P00 — Scope lock**: cross-cutting.md + claim-ledger.md + roadmap.md committed (`[I][L][Δ]`).
- **P01 — Repo settlement**: `git status` clean of unintended files; `ruff check code/sigma_align/` passes; rename verified; refactor commit made.
- **P02 — Thesis archive**: `make paper06` still builds; no references to `thesis/` or `Σ-Align/` in active docs; archive commit made.
- **P03 — Novelty audit**: novelty-audit.md committed; σ-vs-grokking distinction and novelty statement approved; **halt-and-flag** if an equivalent bifurcation/order-parameter already exists.
- **P04 — Mechanism gate**: 3-arm experiment (baseline / fixed-weight / ODE-guided, n=15) + σ-leading-indicator analysis run; decision rule applied and recorded in gate-result.md; claim level locked.
- **P05 — Claim lock**: claim taxonomy, relabeling plan, title, section blueprint, circularity decision all in paper-blueprint.md, committed and user-approved.
- **P06 — Front half**: §§1–3, 7, 9 restructured per blueprint; §§4–6, 8 removed from manuscript (content preserved in companion).
- **P07 — Empirical sections**: §§10–13 rebuilt with gate results and claim-status table; full draft assembled; ledger re-checked.
- **P08 — Epistemology pass**: phenomenological statement, claim separation, ethics paragraph, research-programme paragraph, abstract (≤250 words) done.
- **P09 — Format/build**: tmlr.sty format, notation pruned, proofs in appendix, stale paths fixed; `make pdf` = 0 errors, 0 undefined references.
- **P10 — Companion**: companion builds; self-containment cross-check passes (narrow paper depends on nothing in companion).
- **P11 — Verification**: stranger-test, claim audit, notation sweep pass; review skill run; verification-report.md committed.
- **P12 — Release/submit**: arXiv bundle compiles standalone; TMLR package (cover letter + summary) prepared; commit made.
- **P13 — Post-submission**: README/AGENTS updated; follow-up roadmap + pivot decision record committed.

## Non-negotiables (from the consultations, enforced at Phase 11)

1. The narrow paper is **fully self-contained**; the companion is referenced as "complementary material", never as a prerequisite.
2. No "SGD creates the σ-trap" claim — the model is **phenomenological**; the SGD↔ODE mapping is an explicit Conjecture.
3. No "as the Origin of…" title claim; mechanism-level title only.
4. The foundational-AI hypothesis appears **only** as a labeled research programme in the Discussion.
5. The circularity of the Stage-2 diagnostic (σ̂_A = Acc_OOD/Acc_ID) is stated plainly wherever used.
6. Per-seed reporting, confidence intervals, per-benchmark effect sizes — no pooled giant effect sizes.
