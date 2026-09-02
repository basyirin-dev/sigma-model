# Audit Response Plan — Manuscript Claim Triage & Residual Overclaiming Fix

## Context

An external formal-claims audit was conducted against the σ-Trap manuscript. The audit identifies ~30 formal claims as flawed, overstated, or incorrect, and issues a **FATAL DEFECT (HALT)** verdict. However, critical finding: the audit was generated against a **different version** of the manuscript — likely the earlier monograph or an intermediate draft. The current `paper01/manuscript.tex` (post Phase 00–13 rewrite, TMLR submission) has already excised the vast majority of the material the audit condemns:

**Not present in current manuscript** (already removed in prior rewrites):
- Fenichel persistence / Proposition 1 / invariant manifold claims (Appendix B.2)
- Center-manifold cross-coupling analysis (Appendix B.5, `γuv²` coupling)
- Generic bilinear coupling `γuv` and boundary invariance analysis
- Kramers escape / stochastic barrier / 16.7% escape probability
- AdamW bridge / Riemannian metric invariance / frozen preconditioner proof
- Edge-of-Stability (EOS) argument / discrete-continuous equivalence
- Lyapunov quartic confinement / radius R ≈ 0.887
- Two-Subspace Law / `M = U ⊕ V` manifold
- PCA `D_eff ≈ 2.14` claim / Hessian-trace "derivation" of coefficients
- Observable mappings `u(t) = 1 - L_task(t)/L_task(0)` and `v(t) = CKA · AC`
- RK45 unconditional stability claim
- Lemma 1 (strict dissipativity on W⊥) — the current Lemma 1 is Picard-Lindelöf
- Granger/VAR causal mediation claims

**Present in current manuscript and correctly scoped** (audit marks "valid, narrowly" — manuscript already frames these as model-conditional):
- Theorem about the stipulated 2D ODE: equilibria, stability exchange at R₀ = 1 (Propositions 2–4)
- Transcritical bifurcation classification
- R₀ nondimensionalization
- Interior global convergence for σ_A(0) > 0 (Proposition 3)
- Forward invariance (Lemma 2)
- SGD↔ODE mapping explicitly labeled as unproven Conjecture 1
- Claim-status table (Table 3) separating proven-in-model / empirical / open
- "Phenomenological" framing throughout

**Residual overclaiming issues** in the current manuscript — the only actionable findings from the audit:

1. **"Threshold Law" terminology** — lines 100, 125, 138: Using "law" implies a discovered natural regularity rather than a model-conditional prediction. The audit correctly flags this as overclaiming.

2. **Abstract line 93**: "compositional generalization is fundamentally governed by a macroscopic dynamical bifurcation" — asserts governance as fact about neural networks, not about the model.

3. **Abstract line 95**: "The model establishes that standard empirical risk minimization drives networks into..." — the model establishes this about itself; the "drives networks" phrasing attributes model behavior to real networks.

4. **Abstract line 105**: "compositional learning is governed by a global threshold bifurcation" — same issue; should scope to "within the model" or "is consistent with".

5. **Introduction line 126**: "we prove that escaping the σ-trap is governed by a transcritical bifurcation" — the proof is about the ODE, not about neural network training.

6. **Introduction line 128**: "the vector field forces convergence toward the coherent state" — true in the model; the phrasing slides into claiming it about real training.

7. **Conclusion line 934**: "The framework establishes that escaping the σ-trap is governed by a transcritical bifurcation" — same overclaim.

8. **Conclusion line 941**: "compositional understanding in deep neural networks is governed by macroscopic attractor landscapes and threshold bifurcations" — strongest overclaim remaining; presents model conjecture as established fact about DNNs.

9. **Title**: "Compositional Generalization as a Threshold Phase Transition" — presents model prediction as established characterization of the phenomenon.

10. **Line 482 "topologically invariant"**: Claims qualitative bifurcation structure is "topologically invariant to parameter variations" — this is true within the model but the sentence context implies invariance of neural network behavior.

11. **"identical" language** (lines 100, 936): "achieves asymptotic OOD recovery identical to" — previously addressed with "no detectable difference" in some locations but "identical" persists in the abstract and conclusion.

## Approach

All changes are scoped text edits in `paper01/manuscript.tex`. No structural reorganization needed — the manuscript's epistemic architecture (Conjecture 1, claim-status table, phenomenological framing) is sound; only specific sentences leak model-scope claims into neural-network-scope assertions.

### Step 1: Replace "Threshold Law" with "threshold principle" or "threshold prediction"

The term "law" implies a discovered regularity in nature. The manuscript's content is a model-conditional prediction empirically supported on one benchmark. Replace all instances of "Threshold Law" (lines 100, 125, 138) with "threshold principle" — which conveys the same conceptual content without the "discovered law of nature" connotation.

- Line 100: `The Threshold Law and Fixed-Weight Parity` → `The Threshold Principle and Fixed-Weight Parity`
- Line 125: `The Threshold Law: Why adaptive curricula are unnecessary` → `The threshold principle: why adaptive curricula are unnecessary`
- Line 138: `Empirical validation of the threshold law` → `Empirical validation of the threshold principle`

### Step 2: Scope abstract claims to the model

Four sentences in the abstract (lines 93, 95, 105) assert model properties as facts about neural networks.

- Line 93: "we propose that compositional generalization is fundamentally governed by a macroscopic dynamical bifurcation" — already says "propose", which is acceptable. Keep.
- Line 95: "The model establishes that standard empirical risk minimization drives networks into an asymptotically stable, low-coherence equilibrium" → "The model predicts that, under its dynamics, standard training drives the system into an asymptotically stable, low-coherence equilibrium" — avoids attributing model behavior to networks directly.
- Line 95 continued: "within the ODE model, once the parameter boundary..." — already scoped, keep.
- Line 105: "By demonstrating that compositional learning is governed by a global threshold bifurcation" → "By providing model-level and empirical evidence that compositional learning on H-Bar is consistent with a threshold bifurcation"

### Step 3: Scope introduction "prove" / "governed" claims

- Line 126: "we prove that escaping the σ-trap is governed by a transcritical bifurcation" → "we prove that, within the model, escaping the σ-trap requires a transcritical bifurcation at R₀ = 1" — the "within the model" qualifier is the key addition.
- Line 128: "the vector field forces convergence toward the coherent state" — already in a paragraph that begins "because entering the basin of attraction of E_C in the model". Acceptable, but add "in the model" after "the vector field": "the model's vector field forces convergence".

### Step 4: Scope conclusion claims

- Line 934: "The framework establishes that escaping the σ-trap is governed by a transcritical bifurcation" → "Within the model, escaping the σ-trap is governed by a transcritical bifurcation at R₀ = 1"
- Line 936: "identical" → "showing no detectable difference from" (matching the already-actioned reviewer fix elsewhere).
- Line 941: "compositional understanding in deep neural networks is governed by macroscopic attractor landscapes and threshold bifurcations" → "compositional understanding in deep neural networks may be fruitfully modeled through macroscopic attractor landscapes and threshold bifurcations" — downgrades from established fact to research programme framing, which is what this paragraph is (it's literally labeled "Research programme").

### Step 5: Fix "identical" in abstract

- Line 100: "achieves asymptotic OOD recovery identical to complex adaptive σ-modulated curricula" → "achieves asymptotic OOD recovery with no detectable difference from complex adaptive σ-modulated curricula"

### Step 6: Soften title if appropriate

The title "Compositional Generalization as a Threshold Phase Transition" presents the model's prediction as a characterization of the phenomenon. Adding "Modeling" or "Evidence for" would be more epistemically precise: "Compositional Generalization as a Threshold Phase Transition: Why Adaptive Curricula are Unnecessary for Asymptotic Recovery" → keep, because (a) this is a common title convention in ML theory papers — asserting the framing you propose, not proven fact, (b) the subtitle "Why Adaptive Curricula are Unnecessary" correctly scopes to the empirical finding, (c) the abstract immediately clarifies "we propose" and "phenomenological". No change.

### Step 7: Verify line 482 topological invariance scoping

Line 482 says "the qualitative bifurcation structure of the system is topologically invariant to parameter variations". Since "the system" refers to the ODE system defined in the prior section, this is a correct mathematical statement about the model. The sentence is preceded by "While the exact quantitative numerical timing τ̂ depends on optimization hyperparameters" which contextualizes it. No change needed — the mathematical claim is correct and properly scoped.

## Critical files & anchors

| File | Region | Reason |
|------|--------|--------|
| `paper01/manuscript.tex` lines 93–105 | Abstract | Overclaiming "governed" / "identical" |
| `paper01/manuscript.tex` lines 125–128 | Intro Threshold Law paragraph | "prove... governed" + "law" |
| `paper01/manuscript.tex` line 138 | Contribution 2 | "threshold law" |
| `paper01/manuscript.tex` lines 934–941 | Conclusion | "governed" + "identical" + DNN governance claim |

## Verification

1. After edits, `grep -i "threshold law" paper01/manuscript.tex` returns zero matches.
2. After edits, `grep -i "governed by" paper01/manuscript.tex` returns only the loss-coupling line (378) and the dynamical-rate-ordering line (101, which says "scheduling governs transient efficiency" — a statement about the experiment, not a neural-network-level claim).
3. `make paper01` compiles without errors.
4. Manual review: read abstract, introduction §1, and conclusion §9 end-to-end to verify no remaining model-to-network scope leakage.

## Assumptions & contingencies

- The audit was generated against an older draft. If the user intends the audit to apply to companion report material or a planned extension, the current plan does not cover those — it covers only `paper01/manuscript.tex`. If the companion exists and contains the flagged material (Fenichel, Kramers, etc.), a separate plan is needed.
- "Threshold principle" vs "threshold prediction" vs "threshold hypothesis": choosing "principle" as it carries appropriate weight for a model-conditional result with empirical support, without implying "law". If the user prefers a different term, substitute throughout.
