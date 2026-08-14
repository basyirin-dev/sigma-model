# Claim–Evidence Ledger

**Purpose**: Living thesis-management document (FastTrack audit recommendation). Tracks every
claim C1–C10 with its tier, the evidence currently visible, and the chapter that must establish it.
Updated whenever evidence status changes. Source decisions: `Σ-Align/13-external-assessment-response.md`.

**Tiers**: F = foundation · P = primary thesis · S = secondary thesis · I = bounded implication.

| # | Claim | Tier | Status | Evidence currently visible | Must be established by | Notes / falsification |
|---|-------|:----:|--------|---------------------------|------------------------|-----------------------|
| C1 | Internal representation structure matters for safety | F | **Strong** | Ch 2: 15.5% of 1,136 studies discuss internal representations; structure treated operationally, not axiomatically | Ch 2 (done) | Gap establishes novelty, not truth (FastTrack §4) |
| C2 | Representation structure can be characterised by schema coherence σ | F | Moderate | Glossary definition (back-matter); heuristic lens used in Ch 2 | Ch 4 | Must pass discriminant validity vs accuracy/robustness/simplicity/MI/compositionality |
| C3 | σ can be measured | P | **Not yet demonstrated** | Planned Ch 4 | Ch 4 | Requires operational spec: construct, unit, metric, range, invariance (rotation/permutation/scaling/reparameterisation) |
| C4 | σ exhibits a bifurcation (σ-trap: stable low-σ regime) | P | **Not yet demonstrated** | Planned Ch 7; Σ-Model ODE exists in `code/sigma_align/ode/` | Ch 7 | σcrit checklist: multiple equilibria, control parameter, hysteresis/basin, stability, initial-condition reproducibility, parameterisation robustness; σ-causes-vs-accompanies distinction |
| C5 | The σ-trap explains compositional generalisation failure | P | **Not yet demonstrated** | Planned Ch 7 (flagship question) | Ch 7 | Falsified if low-σ regime observed with intact systematic generalisation |
| C6 | The same σ-trap mechanism explains alignment failure | S | **Not yet demonstrated** | Planned Ch 8 | Ch 8 | Some alignment failures explicitly allowed outside the framework (Ch 9) |
| C7 | Raising σ improves compositional generalisation | P | **Not yet demonstrated** | Planned Ch 5 (pilot) | Ch 5 | Mediation: intervention → σ → CG; if σ rises but CG unchanged, framework needs revision |
| C8 | Raising σ reduces safety-relevant optimisation problems | S | **Not yet demonstrated** | Planned Ch 8 | Ch 8 | Requires mesa-opt diagnostic criteria (proxy-vs-mesa distinction) |
| C9 | Schema-coherent training is an alignment intervention | S/I | Speculative (as stated strength) | Ch 9 argument (planned) | Ch 8 + Ch 9 | Derive from C7+C8 if established |
| C10 | Schema-coherent training is the optimal path to safe AGI | I | **Currently speculative — retracted as working claim** | none | Ch 9 (bounded) | Replaced by "candidate component of alignment strategy" |

## Ledger rules

- No claim may be cited as established in later chapters before its "Must be established by"
  chapter has produced the evidence and this ledger has been updated.
- Statuses: **Strong** (evidence visible) · Moderate (partial) · **Not yet demonstrated** (planned) ·
  Speculative (argument only).
- Update cadence: at every chapter phase completion and before each milestone (M1–M10).
