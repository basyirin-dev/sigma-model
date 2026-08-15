import numpy as np


def sigma_critical(gamma_sigma: float, r0_min: float) -> float:
    """Compute the Phase 1→2 bifurcation threshold for schema coherence.

    Maps to: Eq. ~70 in manuscript.tex (sigma_critical derivation, Proposition 4.1).

    Args:
        gamma_sigma: Schema-mediated decay protection [0, 1].
        r0_min: Minimum basic schema reproduction number (R_0 = rho * P_A * alpha_A / epsilon_sigma * Omega_SL).

    Returns:
        sigma_critical: Threshold value in [0, 1]; crossing this triggers Phase 2 entry.
    """
    return (1.0 / gamma_sigma) * (1.0 - r0_min ** (-1))


def sigma_ode(
    sigma: float,
    rho: float,
    p_a: float,
    alpha_a: float,
    epsilon_sigma: float,
    omega_ai: float,
    gamma_sigma: float = 0.5,
) -> float:
    """Compute the schema coherence ODE right-hand side (d sigma_A / dt).

    Maps to: Eq. 28 in manuscript.tex (sigma_A ODE, autocatalytic form).
    Autocatalytic structure: sigma_A * [rho * P_A * alpha_A * (1 - gamma_sigma * sigma_A) - epsilon_sigma * Omega_SL].
    The sigma_A factor creates a true transcritical bifurcation at R_0 = 1.

    Args:
        sigma: Current schema coherence [0, 1].
        rho: Schema growth rate constant.
        p_a: Principled structure availability (P_A).
        alpha_a: Attentional fidelity [0, 1].
        epsilon_sigma: Shortcut suppression coefficient.
        omega_ai: Shortcut-learning pressure (Omega_SL).
        gamma_sigma: Schema saturation coefficient [0, 1]; governs carrying capacity.

    Returns:
        Time derivative d sigma_A / dt (unbounded float, should be clipped to [0,1]).
    """
    bracket = rho * p_a * alpha_a * (1.0 - gamma_sigma * sigma) - epsilon_sigma * omega_ai
    return sigma * bracket


def delta_ode(
    delta: float,
    delta_rel: float,
    f_learn: float,
    eta: float,
    t_a: float,
    lambda_c: float,
    gamma_sigma: float,
    sigma: float,
    r_a: float,
) -> float:
    """Compute the parametric depth ODE right-hand side (d delta_A / dt).

    Maps to: Eq. 15 in manuscript.tex (depth ODE with schema-mediated decay reduction).
    Growth: f_learn * eta * T_A.
    Decay: lambda_c * (1 - gamma_sigma * sigma) * delta_A * (1 - r_A).

    Args:
        delta: Current parametric depth.
        delta_rel: Relative depth (fraction of frontier achieved), used by Gompertz eta.
        f_learn: Learning function value.
        eta: Learning efficiency (Gompertz form).
        t_a: Time-on-task (T_A).
        lambda_c: Parametric decay rate.
        gamma_sigma: Schema-mediated decay protection [0, 1].
        sigma: Schema coherence [0, 1].
        r_a: Retrieval practice indicator [0, 1].

    Returns:
        Time derivative d delta_A / dt.
    """
    decay_mod = lambda_c * (1.0 - gamma_sigma * sigma)
    return f_learn * eta * t_a - decay_mod * delta * (1.0 - r_a)


def psi_geometric(sigma_1: float, sigma_2: float, psi_0: float = 1.0, phi: float = 1.0) -> float:
    """Compute the intersection activation rate between two domains.

    Maps to: Eq. 18 in manuscript.tex (activation condition, psi_geometric).
    Uses geometric mean of schema coherences modulated by structural overlap phi.

    Args:
        sigma_1: Schema coherence of domain 1 [0, 1].
        sigma_2: Schema coherence of domain 2 [0, 1].
        psi_0: Base activation rate (default 1.0).
        phi: Domain structural similarity [0, 1] (default 1.0 = identical).

    Returns:
        Activation rate Psi_A(d_1, d_2) [0, 1].
    """
    return psi_0 * phi * np.sqrt(sigma_1 * sigma_2)


def gompertz(step: int, a: float = -4.0, b: float = -3e-3) -> float:
    """Compute learning efficiency via Gompertz growth function.

    Maps to: Eq. 17 in manuscript.tex (Gompertz learning efficiency eta).
    Asymmetric double-exponential: rapid early growth, asymptotic plateau.

    Args:
        step: Current training step index.
        a: Scale parameter (default -4.0; controls initial efficiency).
        b: Rate parameter (default -3e-3; controls growth speed).

    Returns:
        Learning efficiency eta in [0, 1].
    """
    return float(np.exp(a * np.exp(b * step)))


def phase_transition(
    sigma: float, delta_rel: float, phase: int,
    sigma_crit: float, delta_star: float,
) -> int:
    """Advance the training phase based on ODE state thresholds.

    Maps to: Algorithm 3.1 and Proposition 3.2 in manuscript.tex.
    Phase 1→2 triggered when sigma exceeds sigma_critical (Eq. 28).
    Phase 2→3 triggered when delta_rel exceeds delta_star.

    Args:
        sigma: Current schema coherence [0, 1].
        delta_rel: Current relative parametric depth [0, 1].
        phase: Current phase index {0, 1, 2}.
        sigma_crit: Phase 1→2 sigma threshold [0, 1].
        delta_star: Phase 2→3 delta_rel threshold [0, 1].

    Returns:
        Updated phase index {0, 2, 3} (monotonic, never decreases).
    """
    new_phase = phase
    if sigma > sigma_crit and phase < 2:
        new_phase = 2
    if delta_rel > delta_star and phase < 3:
        new_phase = 3
    return new_phase


def additive_coupling(task_loss: float, sigma: float, coupling_strength: float) -> float:
    """Apply additive sigma-targeting curriculum to task loss.

    Maps to: Eq. 50 in manuscript.tex (additive coupling form).
    Scales loss by (1 + C * (1 - sigma)): penalises low sigma; decreases
    penalty as sigma approaches 1.

    Args:
        task_loss: Base task loss (scalar).
        sigma: Current schema coherence [0, 1].
        coupling_strength: Coupling intensity C [0, 1].

    Returns:
        Modulated loss (upscaled when sigma is low).
    """
    return task_loss * (1.0 + coupling_strength * (1.0 - sigma))


def multiplicative_coupling(task_loss: float, sigma: float, coupling_strength: float) -> float:
    """Apply multiplicative sigma-boosting curriculum to task loss.

    Maps to: Eq. 51 in manuscript.tex (multiplicative coupling form).
    Scales loss by (1 + C * sigma): amplifies training signal when sigma
    is high, encouraging further coherence growth.

    Args:
        task_loss: Base task loss (scalar).
        sigma: Current schema coherence [0, 1].
        coupling_strength: Coupling intensity C [0, 1].

    Returns:
        Modulated loss (upscaled when sigma is high).
    """
    return task_loss * (1.0 + coupling_strength * sigma)
