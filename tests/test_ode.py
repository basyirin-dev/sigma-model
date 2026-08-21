"""Unit tests for the Sigma-Model ODE dynamical equations and solver."""

import pytest
from sigma_align.ode.equations import delta_ode, psi_geometric, sigma_critical, sigma_ode
from sigma_align.ode.solver import SigmaODESolver


def test_sigma_critical_calculation():
    """Verify sigma_critical calculation at basic reproduction threshold R0."""
    gamma_sigma = 0.8
    # When R_0 = 1.0, sigma_critical should be exactly 0
    assert sigma_critical(gamma_sigma, 1.0) == pytest.approx(0.0, abs=1e-6)

    # When R_0 = 2.0 and gamma_sigma = 0.5: (1 / 0.5) * (1 - 0.5) = 2.0 * 0.5 = 1.0
    assert sigma_critical(0.5, 2.0) == pytest.approx(1.0, abs=1e-6)

    # When R_0 = 1.25 and gamma_sigma = 0.8: (1 / 0.8) * (1 - 0.8) = 1.25 * 0.2 = 0.25
    assert sigma_critical(0.8, 1.25) == pytest.approx(0.25, abs=1e-6)


def test_sigma_ode_transcritical_bifurcation():
    """Test transcritical stability exchange at R0 = 1 in sigma_ode."""
    rho = 1.0
    p_a = 1.0
    alpha_a = 1.0
    gamma_sigma = 0.5

    # Case 1: Subcritical R0 < 1 (epsilon_sigma * omega > rho * p_a * alpha_a)
    # sigma_ode should be negative for small sigma > 0 (E_S = 0 is attractive)
    dsigma_sub = sigma_ode(
        sigma=0.1,
        rho=rho,
        p_a=p_a,
        alpha_a=alpha_a,
        epsilon_sigma=1.0,
        omega_ai=1.5,  # R0 = 1.0 / 1.5 = 0.67 < 1
        gamma_sigma=gamma_sigma,
    )
    assert dsigma_sub < 0, "Below critical threshold, dsigma/dt must be negative"

    # Case 2: Supercritical R0 > 1 (epsilon_sigma * omega < rho * p_a * alpha_a)
    # sigma_ode should be positive for small sigma > 0 (E_S is repelling, flows toward E_C)
    dsigma_super = sigma_ode(
        sigma=0.1,
        rho=rho,
        p_a=p_a,
        alpha_a=alpha_a,
        epsilon_sigma=1.0,
        omega_ai=0.5,  # R0 = 1.0 / 0.5 = 2.0 > 1
        gamma_sigma=gamma_sigma,
    )
    assert dsigma_super > 0, "Above critical threshold, dsigma/dt must be positive"


def test_delta_ode_dynamics():
    """Test parametric depth ODE response to learning vs decay."""
    # When retrieval practice r_a = 1.0, decay is completely arrested
    ddelta = delta_ode(
        delta=1.0,
        delta_rel=0.5,
        f_learn=1.0,
        eta=0.5,
        t_a=1.0,
        lambda_c=0.1,
        gamma_sigma=0.5,
        sigma=0.5,
        r_a=1.0,
    )
    assert ddelta == pytest.approx(0.5, abs=1e-6)


def test_psi_geometric():
    """Test geometric mean activation between schema fields."""
    # Equal coherence
    psi = psi_geometric(sigma_1=0.64, sigma_2=0.64, psi_0=1.0, phi=1.0)
    assert psi == pytest.approx(0.64, abs=1e-6)

    # Orthogonal overlap phi = 0 -> zero activation
    psi_ortho = psi_geometric(sigma_1=0.8, sigma_2=0.8, psi_0=1.0, phi=0.0)
    assert psi_ortho == pytest.approx(0.0, abs=1e-6)


def test_solver_step_execution():
    """Test numerical integration step across modes in SigmaODESolver."""
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)

    # Baseline mode step
    res_base = solver.step(global_step=10, n_timesteps=1000, coupling_mode=None)
    assert "sigma" in res_base and "delta_rel" in res_base and "phase" in res_base
    assert 0.0 <= res_base["sigma"] <= 1.0

    # Additive mode step
    res_add = solver.step(global_step=500, n_timesteps=1000, coupling_mode="additive")
    assert 0.0 <= res_add["sigma"] <= 1.0

    # Multiplicative mode step
    res_mult = solver.step(global_step=500, n_timesteps=1000, coupling_mode="multiplicative")
    assert 0.0 <= res_mult["sigma"] <= 1.0
