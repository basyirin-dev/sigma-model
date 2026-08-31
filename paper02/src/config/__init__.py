"""Configuration and matrix generation utilities for Paper 02."""

from paper02.src.config.matrix import (
    ArchitectureSpec,
    BenchmarkSpec,
    ConditionSpec,
    ExperimentManifest,
    MatrixSummary,
    compute_matrix_summary,
    filter_manifests,
    generate_matrix_manifests,
    load_matrix_config,
    validate_manifests,
)

__all__ = [
    "ArchitectureSpec",
    "BenchmarkSpec",
    "ConditionSpec",
    "ExperimentManifest",
    "MatrixSummary",
    "compute_matrix_summary",
    "filter_manifests",
    "generate_matrix_manifests",
    "load_matrix_config",
    "validate_manifests",
]
