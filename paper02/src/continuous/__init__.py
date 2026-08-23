"""Continuous dynamical systems and gradient flow integration modules."""

from paper02.src.continuous.observable_signatures import (
    generate_observable_signatures_figure,
    simulate_escape_probability,
    simulate_late_onset_destabilization,
    simulate_rate_ordering,
)
from paper02.src.continuous.two_subspace_ode import (
    EquilibriumPoint,
    TwoSubspaceParams,
    TwoSubspaceSystem,
    generate_bifurcation_diagram,
    generate_phase_portraits,
)

__all__: list[str] = [
    "EquilibriumPoint",
    "TwoSubspaceParams",
    "TwoSubspaceSystem",
    "generate_bifurcation_diagram",
    "generate_observable_signatures_figure",
    "generate_phase_portraits",
    "simulate_escape_probability",
    "simulate_late_onset_destabilization",
    "simulate_rate_ordering",
]
