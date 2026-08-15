# Σ-Model V3.0+ — Master Notation Registry

This registry indexes every mathematical symbol across:
- `paper/manuscript.tex` (M)
- `docs/proof-reconstruction/*.tex` (PR)
- `code/sigma/` (C)

## Type Legend

| Abbreviation | Meaning |
|-------------|---------|
| **SV** | State variable (evolves via ODE) |
| **P** | Parameter (fixed scalar) |
| **F** | Function (may vary with d,t) |
| **D** | Derived quantity (computed from state) |
| **Set** | Set-valued quantity |
| **S** | Signal (empirically estimated) |
| **M** | Metric (benchmark measurement) |

## Registry

### A — Latin Upper

| Symbol | Type | Domain | Dim | Scope (§) | Defining Eq | Code Name | Overload Notes |
|--------|------|--------|-----|-----------|-------------|-----------|----------------|
| `A` | — | Global | — | — | — | — | Agent index; used as subscript on all state variables |
| `Acc_ID` | M | [0,1] | Scalar | 3.1.4, 11 | (18) | `acc_id` | In-distribution accuracy |
| `Acc_OOD` | M | [0,1] | Scalar | 3.1.4, 11 | (18) | `acc_ood` | Out-of-distribution accuracy |
| `B` | — | — | — | 7.1, 8 | — | — | Benchmark instance; overloaded with `B_A(t)` below |
| `B_A(t)` | Set | `2^D` | Set | 3.3 | (7) | — | Breadth set; overloaded with benchmark `B` |
| `C_A(d,t)` | F | R_+ | Scalar | 5.1 | (31) | — | Training signal for attentional growth; added to registry per audit |
| `CI(B,f)` | M | [0,1] | Scalar | 7.1 | (43) | — | Construct isolation |
| `D` | Set | — | — | 3.1 | — | — | Set of knowledge domains |
| `D^*(d,t)` | D | `2^d` | Set | 3.6 | (16) | — | Shortcut threshold |
| `DG(B)` | M | [0,1] | Scalar | 7.1 | (43) | — | Difficulty gradient |
| `F_i` | — | — | — | 7.2 | — | — | Faculty index in validity theorem |
| `FD(B)` | M | [0,1] | Scalar | 7.1 | (43) | — | Format diversity |
| `G(d)` | — | — | Grammar | 3.1.4, PR | — | — | Generative grammar for domain d |
| `I(d_1,d_2)` | D | {0,1} | Boolean | 3.5 | (19) | — | Activation indicator |
| `M` | Set | — | Set | 6 | (35) | — | Modality set; overloaded with `M_A(t)` |
| `M_A(t)` | Set | `2^D` | Set | 3.3 | (6) | — | Mastery set |
| `P_A(d,t)` | F | R_+ | Scalar | 3.2, 5.1 | (34) | `p_a` | Principled structure availability |
| `P^*(t)` | F | [0,1] | Scalar | 5.3 | — | — | Executive planning target |
| `R_0` | D | R_+ | Scalar | 9.2 | (38) | `r0_min` | Basic schema reproduction number |
| `R_A(B,f,t)` | M | [0,1] | Scalar | 8 | (44) | — | Benchmark reliability |
| `R_A^{surface}(d,t)` | F | R_+ | Scalar | 5.1 | (31) | — | Surface-reward pressure; `A` subscript distinguishes from benchmark `R_A` |
| `T_A(d,t)` | F | R_+ | Scalar | 3.4 | (14) | `t_a` | Time-on-task; added to registry per audit |
| `V_A(B,f,t)` | D | [0,1] | Scalar | 7.1 | (43) | — | Benchmark validity |

### B — Latin Lower

| Symbol | Type | Domain | Dim | Scope (§) | Defining Eq | Code Name | Overload Notes |
|--------|------|--------|-----|-----------|-------------|-----------|----------------|
| `a` | P | R_+ | Scalar | 3.4 | (15) | `a` | Gompertz shape parameter; added per audit |
| `b` | P | R_+ | Scalar | 3.4 | (15) | `b` | Gompertz shape parameter; added per audit |
| `c_A(d,t)` | S | [0,1] | Scalar | 3.1.4 | (12) | — | Augmentation consistency (AC signal); added per audit |
| `d` | — | D | — | — | — | — | Domain index; used as argument |
| `d_{model}` | P | N | Scalar | 10 | — | `d_model` | Transformer embedding dimension |
| `f_{learn}(d,t)` | F | R_+ | Scalar | 3.4 | (14) | `f_learn` | Learning efficiency factor; added per audit |
| `g_A(d,t)` | S | [-1,1] | Scalar | 3.1.4 | (10) | — | Gradient-composition alignment (GCA); added per audit |
| `k` | P | R_+ | Scalar | 9.2 | (39) | — | Quadratic coefficient in bifurcation normal form |
| `m` | — | M | — | 6 | — | — | Modality index |
| `n_{batch}` | P | N | Scalar | PR 3.6 | — | — | Compositional probe batch size |
| `p` | — | [0,1] | Scalar | 11 | — | — | p-value (statistical testing); conventional overload |
| `q_A(d,t)` | D | [0,1] | Scalar | 3.5 | (20) | — | Effective mastery quality |
| `r_A(d,t)` | S | [-1,1] | Scalar | 3.1.4, 3.4 | (11), (13) | `r_a` | **OVERLOADED**: (1) RGA signal eq (11); (2) retrieval practice factor eq (13). Documented as same symbol for distinct quantities |
| `r_{net}` | D | R | Scalar | 9.2 | (39) | — | Net growth rate in bifurcation unfolding |
| `t` | — | R_+ | — | — | — | — | Time (continuous in ODE; step index in training) |
| `w_g, w_r, w_c` | P | [0,1] | Scalar | 3.1.4 | (14) | — | Stage 1 signal fusion weights |

### C — Greek Upper

| Symbol | Type | Domain | Dim | Scope (§) | Defining Eq | Code Name | Overload Notes |
|--------|------|--------|-----|-----------|-------------|-----------|----------------|
| `Δ(d,t)` | F | R_+ | Scalar | 3.1.1 | (1) | — | Domain frontier; also used as difference operator `ΔR²`, `Δβ` (statistical context) |
| `Δ_{max}` | P | R_+ | Scalar | 4.1 | — | — | Max frontier bound |
| `Θ_A(d,m_1,m_2,t)` | D | [0,1] | Scalar | 6.2 | (42) | — | Cross-modal schema transfer |
| `Ξ_A(t)` | SV | [0,1]³ | Vector (3) | 5.3 | (32) | — | Executive control state; `{Ξ_A^P, Ξ_A^I, Ξ_A^F}` |
| `Ξ_A^P(t)` | SV | [0,1] | Scalar | 5.3 | (33) | — | Executive planning quality |
| `Ξ_A^I(t)` | SV | [0,1] | Scalar | 5.3 | (33) | — | Executive inhibition quality |
| `Ξ_A^F(t)` | SV | [0,1] | Scalar | 5.3 | (33) | — | Executive cognitive flexibility |
| `Σ_{A,B}(d_1,d_2,t)` | D | [0,1] | Scalar | 5.2 | (29) | — | Collective schema field |
| `Ψ_A(d_1,d_2,t)` | D | R_+ | Scalar | 3.5 | (21) | `psi_geometric()` | Intersection discovery rate |
| `Ψ_0` | P | R_+ | Scalar | 3.5 | (21) | `psi_0` | Base discovery rate constant; added per audit |
| `Ω_{SL}(d,t)` | F | R_+ | Scalar | 3.2, 5.1 | (28) | `omega_ai` (→ should be `omega_sl`) | Shortcut-learning pressure |

### D — Greek Lower

| Symbol | Type | Domain | Dim | Scope (§) | Defining Eq | Code Name | Overload Notes |
|--------|------|--------|-----|-----------|-------------|-----------|----------------|
| `α_A(d,t)` | SV | [0,1] | Scalar | 5.1 | (31) | `alpha_a` | Attentional fidelity |
| `α_{critical}` | D | [0,1] | Scalar | 5.1 | — | — | Minimum α_A for schema-coherent equilibrium |
| `β_A(d,t)` | SV | R_+ | Scalar | 3.1.2 | — | — | Functional breadth |
| `γ` | P | R_+ | Scalar | 5.1 | (31) | — | Attention growth rate |
| `γ_σ` | P | [0,1] | Scalar | 3.4 | (13) | `gamma_sigma` | Schema-mediated decay protection |
| `δ_A(d,t)` | SV | [0, Δ] | Scalar | 3.1.1 | (14) | `delta` | Parametric depth |
| `δ_A^{relative}(d,t)` | D | [0,1] | Scalar | 3.1.1 | (2) | `delta_rel` | Relative depth |
| `δ^*` | D | [0,1] | Scalar | 9.3 | (40) | `delta_star` | Phase 2→3 depth threshold |
| `δ_S(s,t)` | F | [0,Δ] | Scalar | 3.6 | (16) | — | Shortcut depth |
| `δ_σ(d,t)` | D | [-1,1] | Scalar | PR 3.6–3.7 | (17) | — | Stage 1–2 proxy discrepancy; added per audit |
| `ϵ` | P | R_+ | Scalar | 4.2 | (23) | — | Timescale separation parameter |
| `ϵ_σ` | P | R_+ | Scalar | 5.1 | (28) | `epsilon_sigma` | Shortcut suppression coefficient |
| `ϵ_{model}` | P | R_+ | Scalar | PR 3.6 | (17) | — | Model misspecification error |
| `ζ_A(d,t)` | D | [-1,1] | Scalar | 5.4 | (36) | — | Calibration error |
| `ζ_α` | P | R_+ | Scalar | 5.1 | (31) | — | Surface-reward attention suppression |
| `η(d,t)` | D | R_+ | Scalar | 3.4 | (15) | `eta` | Learning efficiency (Gompertz) |
| `η_{max}` | P | R_+ | Scalar | 3.4 | (15) | — | Maximum learning efficiency |
| `η_{effective}` | D | R_+ | Scalar | 3.7 | (26) | `effective_lr` | Learning rate after α_A modulation |
| `θ_I, θ_δ, θ_σ, θ_β` | P | [0,1] | Scalar | 3.3 | (6)–(7) | — | Activation/mastery/breadth thresholds |
| `κ(𝐉)` | D | R_+ | Scalar | 4.5 | (25) | — | Jacobian condition number |
| `κ_P, κ_I, κ_F` | P | R_+ | Scalar | 5.3 | (33) | — | Executive control convergence rates |
| `λ_c` | P | R_+ | Scalar | 3.4 | (13) | `lambda_c` | Parametric decay rate |
| `λ_c^{eff}` | D | R_+ | Scalar | 3.4 | (12) | — | Effective decay rate (schema-modulated) |
| `λ_f(d,t)` | P | R_+ | Scalar | 3.4 | — | — | Frontier obsolescence rate |
| `μ_{AB}(d,t)` | D | [0,1] | Scalar | 5.2 | (27) | — | Schema legibility (inter-agent) |
| `ν` | P | R_+ | Scalar | 9.5, PR 4.4 | (45) | `noise_std` | Estimation noise standard deviation |
| `ν_M` | P | R_+ | Scalar | 5.4 | (37) | — | Self-model convergence rate |
| `ξ_M` | P | R_+ | Scalar | 5.4 | (37) | — | Shortcut metacognitive inflation |
| `ρ` | P | R_+ | Scalar | 5.1 | (28) | `rho` | Schema growth rate constant |
| `ρ_i` | P | [0,1] | Scalar | 7.2 | (41) | — | Faculty-specific reliability threshold |
| `σ_A(d,t)` | SV | [0,1] | Scalar | 3.1.3 | (28) | `sigma` | Schema coherence (true latent) |
| `σ̃_A(d,t)` | S | [0,1] | Scalar | 3.1.4 | (14) | `sigma_tilde` | Stage 1 training-time proxy |
| `σ̂_A(d,t)` | S | [0,1] | Scalar | 3.1.4 | (18) | — | Stage 2 evaluation-time estimate |
| `σ_{critical}` | D | [0,1] | Scalar | 9.1 | (38) | `sigma_crit` | Phase 1→2 bifurcation threshold |
| `τ` | P | — | Scalar | 9.5 | (50) | `tau` | Segregated regression breakpoint (Prediction 9); distinct from `τ_A` below |
| `τ_A(B,d,t)` | P | [0,1] | Scalar | 5.2 | — | — | Theory-of-mind coupling |
| `τ_i` | P | [0,1] | Scalar | 7.2 | (41) | — | Faculty-specific validity threshold |
| `φ(d_1,d_2)` | F | [0,1] | Scalar | 3.5 | (21) | `phi` | Domain similarity coupling; added per audit |
| `Φ` | F | [0,1] | Scalar | 9.5 | (45) | — | Standard normal CDF |
| `ω(m_1,m_2)` | P | [0,1] | Scalar | 6.2 | (42) | — | Modality similarity weight; no conflict with asymptotic ω |

### E — Decorated / Composite

| Symbol | Type | Domain | Dim | Scope (§) | Defining Eq | Overload Notes |
|--------|------|--------|-----|-----------|-------------|----------------|
| `𝐱_A(t)` | SV | 𝒳 | N‑dim | 4.1 | (22) | Bold denotes vector; state vector |
| `𝐉_{fast}` | D | R^{3×3} | Matrix | 4.3 | (24) | Fast subsystem Jacobian (3×3) |
| `𝐟` | F | R^N | Vector | 4.2 | — | ODE vector field |
| `ℳ_0, ℳ_ϵ` | Set | 𝒳 | Manifold | 4.3 | (23) | Critical/slow manifold |
| `𝒳` | Set | R^N | Set | 4.1 | (22) | State space |
| `ℒ_{task}, ℒ_{comp}` | F | R_+ | Scalar | 3.7 | (25) | Loss components |
| `ℙ(·)` | — | [0,1] | — | 9.5, PR | (45) | Probability measure (use `\mathbb{P}`) |
| `𝔼[·]` | — | — | — | PR 3.6, 10 | — | Expectation operator |

## F — Overloading Summary

| Symbol | Locations | Severity | Resolution |
|--------|-----------|----------|------------|
| `R_A` | (1) Benchmark reliability `R_A(B,f,t)`; (2) surface reward `R_A^{surface}(d,t)` | Moderate | `surface` superscript disambiguates; documented |
| `r_A` | (1) RGA signal eq (11); (2) retrieval practice eq (13) | Moderate | Same symbol for distinct physical quantities — **recommend renaming retrieval practice to `ρ_A` or clarifying in prose** |
| `B` | (1) Benchmark instance; (2) breadth set `B_A(t)` | Mild | Subscript `_A` disambiguates |
| `M` | (1) Modality set; (2) mastery set `M_A(t)` | Mild | Subscript `_A` disambiguates |
| `Δ` | (1) Domain frontier; (2) difference operator | Mild | Conventional in statistics |
| `τ` | (1) Theory-of-mind `τ_A`; (2) breakpoint `τ` | Mild | Notation table notes this explicitly |
| `ω` | (1) Modality weight; (2) asymptotic ω | Potential | Not yet active; document pre-emptively |

## G — Visual Convention Verification

| Convention | Is it used consistently? | Violations |
|-----------|------------------------|------------|
| Bold for vectors/matrices (`\mathbf{x}`, `\mathbf{J}`) | Yes | None found |
| Hat for Stage 2 estimates (`\hat{σ}_A`) | Yes | None found |
| Tilde for Stage 1 proxies (`\tilde{σ}_A`) | Yes | None found |
| `\text{relative}` superscript for normalised | Yes | None found |
| `\text{eff}` superscript for effective | Yes | None found |
| `\text{surface}` superscript for behavioural | Yes | Should be documented in App A (now done) |
| `_A` subscript for agent-relative | Yes, but `CA` in Table 1 was missing it | Fixed (A4) |
| `_SL` subscript for shortcut-learning | Yes | None found |
| Function composition `f(g(x))` (no `∘`) | N/A — no `∘` used | No ambiguity |

## H — Asymptotic Notation (Knuth/CLRS Compliance)

All `O()` uses are for upper bounds or order-of-magnitude estimates, consistent
with Knuth/CLRS conventions. No `Ω`, `Θ`, `ω` are used in asymptotic sense.

| Expression | Meaning | Compliant? |
|-----------|---------|------------|
| `η_max ~ O(1)` | Upper-bound estimate | ✓ |
| `O(ϵ)` | Upper bound on manifold distance | ✓ |
| `O(σ_A^2)` | Taylor remainder bound | ✓ |
| `≪ 1` | Small parameter (not asymptotic) | N/A |

## I — Probabilistic Notation Verification

| Notation | Convention | Status |
|----------|-----------|--------|
| `\mathbb{E}[·]` | Expectation | ✓ Manuscript + PR consistent |
| `\mathcal{N}(μ,σ^2)` | Gaussian | ✓ Consistent |
| `\Phi` | Normal CDF | ✓ Consistent |
| `\mathbb{P}(·)` | Probability | ✓ PR uses this; manuscript now uses it (A3 fixed `P` → `\mathbb{P}`) |
| `p` | p-value | ✓ Conventional; distinct from probability measure |

## J — Code Naming Divergence Map

For full detail, see `docs/code-alignment-plan.md`. Key divergences:

| LaTeX | Python | Status |
|-------|--------|--------|
| `Ω_{SL}` | `omega_ai` | **D1 — should be `omega_sl`** |
| `R_0` | `r0_min` | **D5 — consider `r_0`** |
| `σ_A` | `sigma` (dropped `_A`) | D2 — document as intentional |
| `δ_A^{relative}` | `delta_rel` | D3 — defer rename |
| `coupling_strength` | `coupling_str` | D4 — ambiguous abbreviation |

## K — Gaps Identified and Fixed

| Gap | Description | Status |
|-----|-------------|--------|
| Missing `C_A(d,t)` in App A | Training signal for α-ODE | FIXED |
| Missing `T_A(d,t)` in App A | Time-on-task in δ-ODE | FIXED |
| Missing `f_{learn}(d,t)` in App A | Learning factor in δ-ODE | FIXED |
| Missing `a, b` in App A | Gompertz parameters | FIXED |
| Missing `g_A, r_A, c_A` in App A | GCA/RGA/AC signals | FIXED |
| Missing `δ_σ(d,t)` in App A | Stage 1–2 discrepancy | FIXED |
| Missing `Ψ_0, φ` in App A | Discovery rate constant + coupling | FIXED |
| Missing `\text{surface}` convention | Visual syntax | FIXED |
| `CA(d,t)` missing `_A` | Table 1 subscript | FIXED |
| `P(error)` → `\mathbb{P}(error)` | Manuscript eq (45) | FIXED |
