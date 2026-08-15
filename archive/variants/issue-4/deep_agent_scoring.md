# Issue #4 — DEEP AGENT Scoring (MODE 2)

## Scoring Criteria Reference

| Code | Criterion | Scale |
|------|-----------|-------|
| C1 | ODE System Coherence | 0–10 |
| C2 | Novelty Defence | 0–10 |
| C3 | Falsifiability | 0–10 |
| C4 | Scope Discipline | 0–10 |
| C5 | Hackathon Relevance | 0–10 |
| C6 | Version Integration | 0–10 |

**Composite = mean(C1, C2, C3, C4, C5, C6)**
**Suppression threshold: composite < 6.0**

---

## Variant A — Prose-Only Fix (local)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **5** | No equations changed, so no ODE breakage. However, the σ_A-to-decay coupling is removed from the prose and replaced with an indirect P_A pathway. The Appendix A.1 still contains the direct (1 − γ_σ · σ_A) coupling — so the main text now contradicts the Appendix. System coherence is reduced, not improved. |
| C2 | **7** | No conflation introduced. σ_A and r_A remain distinct. The indirect coupling via P_A is a defensible differentiation argument. |
| C3 | **5** | Neutral. The fix does not sharpen or dull any prediction. Predictions 1–8 are unaffected. |
| C4 | **9** | No boundary violations. Single-agent ✓, cognitive bridge ✓ (no psychological language), version boundary ✓ (no V2.0+ bleed). |
| C5 | **2** | Tangentially related. Prose clarity improves readability of the mathematical framework but does not directly enable or improve any benchmark protocol. |
| C6 | **4** | Negative impact on version integration. The main text now explicitly denies the σ_A-d coupling that the Appendix A.1 contains. This deepens the version seam between §3.3 and §12. |

**Composite: (5+7+5+9+2+4)/6 = 32/6 = 5.33 → [SUPPRESSED]**

---

## Variant B — Align Main Text with Appendix A.1 (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **9** | Directly closes the ODE gap. Equation 7 gains the (1 − γ_σ · σ_A) factor matching A.1. The coupled system (depth + schema coherence + attention + executive + metacognitive) is now internally consistent. No new unclosed variables introduced; γ_σ is already declared as Π_4 in the dimensionless parameter groups. Equation 12 must also be updated (propagation noted in justification). |
| C2 | **7** | Maintains distinctness. The λ_c modulated by σ_A is cleanly separated from the engagement term (1 − r_A). σ_A remains distinct from structured/disentangled/causal representations per Table 1. No conflating language introduced. |
| C3 | **5** | Neutral. The fix resolves an internal inconsistency but does not add new observable proxies or sharpen §9 predictions. Predictions 1–8 unchanged. |
| C4 | **9** | All three boundaries clean. Single-agent ✓, cognitive bridge ✓ (no psychological vocabulary), version boundary ✓ (σ_A is a V1.0 variable entering a V1.0 equation — no V2.0+ bleed). |
| C5 | **2** | Tangentially related. Resolving the decay mechanism improves theoretical clarity but does not directly produce, improve, or enable a Kaggle evaluation protocol. |
| C6 | **5** | Version-neutral. The main text and Appendix are now consistent, but the fix does not actively integrate language or structure across a version boundary. It resolves a seam without creating new cross-version coupling. |

**Composite: (9+7+5+9+2+5)/6 = 37/6 = 6.17 → [QUALIFIES]**

---

## Variant C — Embed σ_A into r_A (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **7** | Equation 8 gains a σ_A coupling, creating a closed feedback: σ_A → r_A → decay rate. This is internally consistent. However, it conflicts with Appendix A.1 which uses a different coupling channel (direct λ_c modulation). The system has two competing σ_A-to-decay pathways, reducing closure clarity. |
| C2 | **5** | Risk of conflation. r_A is the rehearsal engagement rate — a time-dependent retrieval variable. Adding σ_A (schema coherence) directly to r_A blurs the boundary between "how recently was this engaged" and "how coherently is this structured." These are categorically distinct mechanisms. The Table 1 differentiation argument is weakened. |
| C3 | **5** | Neutral. Same as B — resolves internal inconsistency without sharpening predictions. |
| C4 | **7** | Single-agent ✓, cognitive bridge ✓. Version boundary: σ_A is a V1.0 variable entering Eq. 8 (a V1.0 equation), so no V2.0+ bleed. However, the mechanism mixes engagement dynamics (time-dependent) with schema quality (structural), which is a mild conceptual boundary issue. |
| C5 | **2** | Tangentially related. No direct benchmark protocol impact. |
| C6 | **4** | Negative. r_A now depends on σ_A, creating an additional coupling that the Appendix A.1 does not account for. The version seam between main text and Appendix is worsened because A.1 would need to remove its own (1 − γ_σ · σ_A) factor to avoid double-counting — but it already contains it. |

**Composite: (7+5+5+7+2+4)/6 = 30/6 = 5.00 → [SUPPRESSED]**

---

## Variant D — Independent Schema-Reconstruction Term (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **7** | Equations 7 and 8 preserved exactly. New Eq. 8a adds a positive recovery term. Net decay = −(λ_c − λ_σ · σ_A) · δ_A · (1 − r_A). Closure is maintained as long as λ_c ≥ λ_σ (boundedness condition stated). However, the Appendix A.1 uses a multiplicative modulation (1 − γ_σ · σ_A) rather than a subtractive term — two different mathematical forms for the same conceptual mechanism. |
| C2 | **7** | Schema-reconstruction is treated as a distinct physical process (recovery from partial decay), well-separated from engagement decay and frontier obsolescence. The error-correcting code analogy provides a clear differentiation argument. |
| C3 | **5** | Neutral. Does not sharpen §9 predictions. |
| C4 | **7** | Single-agent ✓, cognitive bridge ✓, version boundary ✓. The new term uses only V1.0 variables. |
| C5 | **2** | Tangentially related. No direct hackathon protocol impact. |
| C6 | **5** | Version-neutral to slightly positive. The additive term structure is transparent and could be integrated across versions, but currently it introduces a parallel mechanism to A.1's multiplicative form without reconciling them. |

**Composite: (7+7+5+7+2+5)/6 = 33/6 = 5.50 → [SUPPRESSED]**

---

## Variant E — Restructure §3.3 (systemic)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **8** | Fully resolves the main text / Appendix inconsistency. Equation 7 revised to match A.1 exactly. Three-mechanism architecture (engagement decay, schema-mediated decay reduction, frontier obsolescence) is internally consistent. Each mechanism has one coupling channel. Boundedness maintained. One point deducted because the restructured comparison table (§3.3.5) needs careful construction to avoid misrepresenting prior frameworks. |
| C2 | **8** | Three distinct mechanisms with explicit names and separate coupling channels improve the distinctness argument. Engagement decay (time-dependent) is cleanly separated from schema-mediated decay reduction (σ_A-dependent). The comparison table now shows a three-way differentiation rather than a confused two-way, strengthening the novelty defence against EWC/replay accounts. |
| C3 | **7** | Cleaner architecture makes it easier to reason about which decay process dominates under different training regimes. While no new observable proxy is added, the separation of engagement decay from schema-mediated decay reduction clarifies the conditions under which Prediction 2 (AI augmentation and schema suppression) operates — specifically, that Ω_AI suppresses σ_A which in turn reduces the schema-mediated decay protection. |
| C4 | **7** | Single-agent ✓, cognitive bridge ✓, version boundary ✓. The restructuring introduces no new variables and uses only V1.0 quantities. Minor concern: the term "schema-mediated decay reduction" could be read as psychological language, but it refers to a mathematical factor (1 − γ_σ · σ_A) so it is technical, not psychological. |
| C5 | **3** | Tangentially related with slight improvement over other variants. The three-mechanism decay architecture clarifies the conditions under which parametric decay dominates vs. schema-mediated protection — this has indirect relevance to the Learning track's "AI-Augmentation OOD Gap" benchmark, which tests how Ω_AI affects σ_A decay dynamics. Not a direct protocol improvement. |
| C6 | **7** | The three-mechanism structure makes cross-version coupling more transparent. The revised §3.3 explicitly names γ_σ as the dimensionless parameter group Π_4, creating a clear cross-reference to the Appendix. The restructuring does not actively integrate V2.0+ variables into V1.0 equations, but it creates a cleaner foundation for future extensions. |

**Composite: (8+8+7+7+3+7)/6 = 40/6 = 6.67 → [QUALIFIES]**

---

## Rankings

| Rank | Variant | Composite | Status | Flags |
|------|---------|-----------|--------|-------|
| 1 | **E** (Restructure §3.3) | **6.67** | QUALIFIES | — |
| 2 | **B** (Align with A.1) | **6.17** | QUALIFIES | — |
| 3 | A (Prose-only) | 5.33 | SUPPRESSED | — |
| 4 | D (Independent term) | 5.50 | SUPPRESSED | — |
| 5 | C (Embed in r_A) | 5.00 | SUPPRESSED | — |

**No variants flagged [HACKATHON PRIORITY] (C5 ≥ 8 required).**
**No variants flagged [INTEGRATION PRIORITY] (C6 ≥ 9 required).**

---

## HACKATHON UPDATE:
None for both variants. Issue #4 addresses a mathematical inconsistency in the depth decay mechanism (§3.3.1). The fix does not directly produce, improve, or enable any benchmark protocol across the five hackathon tracks. No changes to /hackathon/track_*.md files are warranted.

## INTEGRATION UPDATE:
- **Variant B:** Update integration_map.md row for "σ_A-d decay coupling" to reflect that the coupling is now explicit in Eq. 7 (main text) and consistent with Eq. A.1 (Appendix). The parameter γ_σ (= Π_4) is now formally declared in §3.3.1.
- **Variant E:** Same as B, plus update integration_map.md row for "Decay Architecture" to reflect the new three-mechanism structure (engagement decay / schema-mediated reduction / frontier obsolescence) replacing the prior two-mechanism framing.

## NEGATIVE LOG:
- **Issue #4, Variant A:** Prose-only fix does not resolve the equation-level inconsistency; main text now contradicts Appendix A.1, worsening version seam.
- **Issue #4, Variant C:** Embedding σ_A into r_A conflates engagement dynamics with schema quality, weakening novelty defence; also creates competing coupling pathway with A.1.
- **Issue #4, Variant D:** Adds a new equation (8a) that duplicates the conceptual role of A.1's multiplicative modulation without reconciling the two forms; unnecessary complexity.

## CHECKPOINT RECOMMENDATION:
Not yet at Checkpoint threshold (1st approved edit; threshold is every 8th).
