from sigma.ode import (
    additive_coupling,
    delta_ode,
    multiplicative_coupling,
    phase_transition,
    psi_geometric,
    sigma_critical,
    sigma_ode,
)
from sigma.ode.solver import SigmaODESolver


def test_sigma_ode_growth_dominates():
    ds = sigma_ode(sigma=0.1, rho=1.0, p_a=0.9, alpha_a=1.0, epsilon_sigma=0.01, omega_ai=0.5)
    assert ds > 0, "At low sigma, growth should dominate decay"


def test_sigma_ode_decay_dominates():
    ds = sigma_ode(sigma=0.9, rho=0.1, p_a=0.1, alpha_a=0.1, epsilon_sigma=1.0, omega_ai=1.0)
    assert ds < 0, "At high sigma with low growth params, decay should dominate"


def test_delta_ode_positive():
    dd = delta_ode(
        delta=0.1, delta_rel=0.1, f_learn=1.0, eta=0.5, t_a=0.1,
        lambda_c=0.1, gamma_sigma=1.0, sigma=0.5, r_a=0.0,
    )
    assert dd > 0, "With strong learning signal, delta should increase"


def test_delta_ode_negative():
    dd = delta_ode(
        delta=0.9, delta_rel=0.9, f_learn=0.0, eta=0.5, t_a=0.0,
        lambda_c=1.0, gamma_sigma=1.0, sigma=0.9, r_a=0.9,
    )
    assert dd < 0, "With strong decay and no learning, delta should decrease"


def test_psi_geometric_symmetric():
    p = psi_geometric(0.5, 0.5, psi_0=1.0, phi=1.0)
    assert abs(p - 0.5) < 1e-6, "psi(s1, s1) should equal s1 for psi_0=1, phi=1"


def test_psi_geometric_identity():
    p = psi_geometric(0.0, 1.0, psi_0=1.0, phi=1.0)
    assert p == 0.0, "psi(0, anything) should be 0"


def test_psi_geometric_order_independent():
    p12 = psi_geometric(0.3, 0.7, psi_0=1.0, phi=1.0)
    p21 = psi_geometric(0.7, 0.3, psi_0=1.0, phi=1.0)
    assert abs(p12 - p21) < 1e-6, "psi should be symmetric"


def test_phase_transition_initial():
    pt = phase_transition(sigma=0.0, delta_rel=0.0, phase=0, sigma_crit=0.15, delta_star=0.55)
    assert pt == 0, "Phase should stay 0 with low sigma and delta"


def test_phase_transition_to_phase2():
    pt = phase_transition(sigma=0.5, delta_rel=0.0, phase=1, sigma_crit=0.15, delta_star=0.55)
    assert pt == 2, "sigma above crit should trigger phase 2"


def test_phase_transition_to_phase3():
    pt = phase_transition(sigma=0.5, delta_rel=0.8, phase=2, sigma_crit=0.15, delta_star=0.55)
    assert pt == 3, "delta above star should trigger phase 3"


def test_sigma_critical_formula():
    sc = sigma_critical(gamma_sigma=2.0, r0_min=2.0)
    assert sc > 0, "Critical sigma should be positive"
    assert isinstance(sc, float)


def test_additive_coupling():
    result = additive_coupling(task_loss=1.0, sigma=0.3, coupling_strength=0.2)
    assert result == 1.0 * (1.0 + 0.2 * (1.0 - 0.3)), "Additive coupling formula incorrect"
    assert result > 1.0, "Coupling should increase loss when sigma < 1"


def test_additive_coupling_no_effect():
    result = additive_coupling(task_loss=1.0, sigma=1.0, coupling_strength=0.2)
    assert result == 1.0, "Additive coupling should have no effect when sigma=1"


def test_multiplicative_coupling():
    result = multiplicative_coupling(task_loss=1.0, sigma=0.5, coupling_strength=0.2)
    assert result == 1.0 * (1.0 + 0.2 * 0.5), "Multiplicative coupling formula incorrect"


def test_multiplicative_coupling_zero_sigma():
    result = multiplicative_coupling(task_loss=1.0, sigma=0.0, coupling_strength=0.2)
    assert result == 1.0, "Multiplicative coupling should have no effect when sigma=0"


def test_solver_initial_state():
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)
    assert solver.sigma == 0.1
    assert solver.delta_rel == 0.05
    assert solver.phase == 0


def test_solver_step_no_coupling():
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)
    result = solver.step(global_step=100, n_timesteps=2000, coupling_mode=None)
    assert "sigma" in result
    assert "delta_rel" in result
    assert "phase" in result


def test_solver_additive_step():
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)
    result = solver.step(
        global_step=100, n_timesteps=2000,
        coupling_mode="additive", coupling_str=0.2,
    )
    assert 0.0 <= result["sigma"] <= 1.0
    assert 0.0 <= result["delta_rel"] <= 1.0


def test_solver_multiplicative_step():
    solver = SigmaODESolver(sigma_init=0.1, delta_rel_init=0.05)
    result = solver.step(global_step=100, n_timesteps=2000, coupling_mode="multiplicative")
    assert 0.0 <= result["sigma"] <= 1.0
