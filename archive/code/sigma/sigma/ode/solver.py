import numpy as np


class SigmaODESolver:
    """Numerical integrator for the Σ-Model coupled ODE system.

    Maintains internal state (sigma, delta_rel, phase) and advances
    one step per call. Uses simplified phenomenological dynamics
    for training simulation (not a full ODE solver).
    """

    def __init__(self, sigma_init: float = 0.1, delta_rel_init: float = 0.05):
        """Initialize the ODE solver state.

        Args:
            sigma_init: Initial schema coherence [0, 1].
            delta_rel_init: Initial relative depth [0, 1].
        """
        self.sigma = sigma_init
        self.delta_rel = delta_rel_init
        self.phase = 0

    def step(
        self,
        global_step: int,
        n_timesteps: int,
        sigma_crit: float = 0.15,
        delta_star: float = 0.55,
        noise_std: float = 0.012,
        coupling_mode: str | None = None,
        coupling_str: float = 0.0,
        sigma_init: float = 0.1,
    ) -> dict:
        """Advance the ODE state by one training step.

        Maps to: Algorithm 3.1 in manuscript.tex (numerical integration protocol).
        Simplified: sigma follows a phenomenological curve per coupling mode,
        delta_rel increases linearly with training progress.

        Args:
            global_step: Current training step index.
            n_timesteps: Total training steps (for step_ratio computation).
            sigma_crit: Phase 1→2 threshold [0, 1].
            delta_star: Phase 2→3 relative depth threshold [0, 1].
            noise_std: Standard deviation of Gaussian noise added to sigma.
            coupling_mode: None (baseline), "additive", or "multiplicative".
            coupling_str: Coupling strength (unused in simplified solver).
            sigma_init: Initial sigma value for baseline mode.

        Returns:
            dict with keys:
                - "sigma": Updated schema coherence [0, 1].
                - "delta_rel": Updated relative depth [0, 1].
                - "phase": Current phase index {0, 2, 3}.
        """
        noise = np.random.normal(0, noise_std)

        if coupling_mode is None:
            self.sigma = float(np.clip(sigma_init + 3e-4 * global_step + noise, 0.0, 1.0))
        elif coupling_mode == "additive":
            self.sigma = float(np.clip(sigma_init + 2.5e-4 * global_step + noise, 0.0, 1.0))
        elif coupling_mode == "multiplicative":
            gompertz_val = float(np.exp(-4.0 * np.exp(-3e-3 * global_step)))
            self.sigma = float(np.clip(sigma_init + 0.85 * gompertz_val + noise, 0.0, 1.0))

        step_ratio = global_step / n_timesteps if n_timesteps > 0 else 0
        self.delta_rel = min(1.0, 0.05 + 0.90 * step_ratio)

        if self.sigma > sigma_crit and self.phase < 2:
            self.phase = 2
        if self.delta_rel > delta_star and self.phase < 3:
            self.phase = 3

        return {"sigma": self.sigma, "delta_rel": self.delta_rel, "phase": self.phase}
