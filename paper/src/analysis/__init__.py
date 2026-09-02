"""Analytical metrics, CKA subspace projections, Hessian curvature, and circuit diagnostics."""

from paper.src.analysis.analyze_gate import (
    compute_bootstrap_ci,
    compute_tost_equivalence,
    evaluate_gate_results,
    fit_logistic_separatrix,
    generate_gate_summary_table,
)
from paper.src.analysis.circuits import (
    compute_head_schema_specialization,
    decompose_residual_stream,
    project_to_subspace,
)
from paper.src.analysis.cka import (
    linear_cka,
    rbf_cka,
)
from paper.src.analysis.geometry import (
    compute_homomorphism_error,
    compute_subspace_orthogonality,
    compute_subspace_principal_angles,
)
from paper.src.analysis.hessian import (
    compute_hvp,
    compute_top_hessian_eigenvalue,
    estimate_hessian_trace,
)
from paper.src.analysis.hessian_lanczos import (
    compute_lanczos_eigenvalues,
)
from paper.src.analysis.power import (
    compute_bootstrap_threshold_ci,
    compute_granger_causality_test,
    compute_minimal_detectable_effect_size,
    compute_tost_power,
)
from paper.src.analysis.representation_geometry import (
    RGA_OPERATOR_TOKENS,
    compute_linear_cka,
    compute_rga_metric,
)
from paper.src.analysis.whitened_gca import (
    compute_flattened_gradients,
    compute_whitened_gca,
)

__all__: list[str] = [
    "RGA_OPERATOR_TOKENS",
    "compute_bootstrap_ci",
    "compute_bootstrap_threshold_ci",
    "compute_flattened_gradients",
    "compute_granger_causality_test",
    "compute_head_schema_specialization",
    "compute_homomorphism_error",
    "compute_hvp",
    "compute_lanczos_eigenvalues",
    "compute_linear_cka",
    "compute_minimal_detectable_effect_size",
    "compute_rga_metric",
    "compute_subspace_orthogonality",
    "compute_subspace_principal_angles",
    "compute_top_hessian_eigenvalue",
    "compute_tost_equivalence",
    "compute_tost_power",
    "compute_whitened_gca",
    "decompose_residual_stream",
    "estimate_hessian_trace",
    "evaluate_gate_results",
    "fit_logistic_separatrix",
    "generate_gate_summary_table",
    "linear_cka",
    "project_to_subspace",
    "rbf_cka",
]
