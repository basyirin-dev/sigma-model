"""Continuous dynamical systems and gradient flow integration modules."""

from paper.src.continuous.observable_signatures import (
    generate_observable_signatures_figure,
    simulate_escape_probability,
    simulate_late_onset_destabilization,
    simulate_rate_ordering,
)
from paper.src.continuous.solver import (
    ContinuousTwoSubspaceSolver,
    SolverResult,
)
from paper.src.continuous.two_subspace_ode import (
    EquilibriumPoint,
    TwoSubspaceParams,
    TwoSubspaceSystem,
    generate_bifurcation_diagram,
    generate_phase_portraits,
)

__all__: list[str] = [
    "ContinuousTwoSubspaceSolver",
    "EquilibriumPoint",
    "SolverResult",
    "TwoSubspaceParams",
    "TwoSubspaceSystem",
    "generate_bifurcation_diagram",
    "generate_observable_signatures_figure",
    "generate_phase_portraits",
    "simulate_escape_probability",
    "simulate_late_onset_destabilization",
    "simulate_rate_ordering",
]
