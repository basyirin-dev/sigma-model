# Phase P02: Theoretical Foundations & ODE Derivations

## 1. Objective
Formulate the continuous-time coupled dynamical system equations for the $\Sigma$-Model, derive bifurcation conditions, and establish mathematical proofs for the two-subspace law.

## 2. Inputs & Dependencies
- `P01` literature audit.

## 3. Required Deliverables
- Mathematical specification of $\dot{D}$ and $\dot{S}$ ODE system.
- Equilibrium points, Jacobian linearization, and Lyapunov stability proofs.
- ADR documenting ODE parameter bounds and bifurcation regimes.
- Draft theory section in `writing/manuscript/index.qmd`.

## 4. Exit Criteria & Definition of Done
- All mathematical proofs verified.
- Clear distinction between *Model Theorem* and *Empirical Observation* maintained (CC.3.2).
- `python scripts/check_phase_exit.py P02` returns `PASS`.
