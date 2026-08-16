# Cover Letter — TMLR Submission

**Title**: The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation

*(This letter is anonymized for double-blind review. Author identities, affiliations, ORCID, and conflict disclosures are entered in the OpenReview submission form, not here.)*

---

Dear TMLR Action Editor,

We are submitting *The σ-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation* for consideration at TMLR. This manuscript is the direct product of an earlier desk rejection at JAIR (2026-07-15), whose stated grounds were exposition/notation, overbroad claims, and scope. We took that decision as the editorial instruction it was intended to be, and this paper is the result of following it: a deliberately small, narrowly scoped contribution, written to be impossible to misread.

**The paper, in one paragraph.** Standard training on compositional benchmarks reliably produces a dissociation — high in-distribution accuracy alongside a persistent out-of-distribution gap. We formalise this with two quantities: parametric depth (fit to the training distribution) and schema coherence (organisation around compositional structure), and we posit a two-variable phenomenological ODE whose phase-space structure — a stable low-coherence equilibrium (the "σ-trap") and a transcritical bifurcation at R₀ = 1 — describes the observed trajectories. A four-arm gate experiment (n = 15 per arm) reproduces the trap, shows that exposure to compositional loss closes the gap with no detectable difference between a plain fixed-weight loss and the full σ-modulated curriculum, and reports honestly that the measured coherence proxy does not precede OOD improvement. The claim level is explicitly descriptive: the ODEs are posited, not derived from SGD, and the SGD↔ODE mapping is labelled an open conjecture.

**How this addresses the JAIR desk rejection.**

1. *Scope* — The previous submission was a five-faculty framework with breadth, attention, and metacognitive extensions. This paper is the two-variable core only: one mechanism, one discriminating experiment, one flagship prediction (the Phase-2 inflection), and three appendices (notation, stability, proofs). The extended framework is preserved in a separate arXiv companion technical report, referenced as complementary material — the paper is self-contained and does not depend on it.
2. *Exposition/notation* — Every symbol is defined before first use; a notation reference (Appendix A) and a claim-status table (Table 3) separate what is proven in the model, proven under assumptions, empirically supported, and open. The JAIR reviewers' notation concerns are addressed by construction.
3. *Overbroad claims* — The manuscript contains no "SGD creates the σ-trap" claim, no "origin" claim, and no universality claim. The abstract, introduction, and conclusion all state the same claim level; the negative results (fixed-weight parity, proxy non-leading) are reported in the abstract rather than hidden. Conjecture 1 (the SGD↔ODE mapping) is stated as an unproven modelling assumption.

**The "series of small steps".** The JAIR editor's recommendation was a series of small steps rather than one large claim. This paper is one such step: a reproducible behavioural pattern, a two-variable dynamical description of it, and a controlled experiment that constrains how the description may be interpreted (descriptive, not mechanistic). The companion preserves the larger programme; this paper is the step that can be defended today.

**A note for the editor.** We are aware that the main text runs to 15 pages before references (appendices and references excluded), above the 12-page threshold after which review timescales lengthen; we judged the content to justify the length and accept the longer timescale rather than compress consultation-locked wording. We believe the submission satisfies TMLR's two acceptance criteria: the claims are supported by accurate, convincing, and clear evidence (per-comparison statistics, per-seed trajectories, pre-registered segmented regression), and there is a clear audience interested in a formal dynamical description of compositional-generalisation failure that is honest about the limits of its own evidence.

Sincerely,
The authors

---

*Anonymized for double-blind review. Upload path: include as a non-PDF note via the OpenReview submission's metadata/comment fields, or attach as an anonymized supplementary PDF — do not include author identities here.*
