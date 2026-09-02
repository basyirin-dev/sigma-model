"""Mechanistic Interpretability and Subspace Attribution Engine for Paper 02.

This module implements residual stream projection, shortcut vs schema subspace
decomposition, and attention head specialization metrics under the Two-Subspace Law.
"""

from __future__ import annotations

import numpy as np


def project_to_subspace(activations: np.ndarray, basis: np.ndarray) -> np.ndarray:
    """Project activation vectors onto the linear subspace spanned by basis.

    Args:
        activations: Array of shape (n_samples, d_model).
        basis: Matrix of shape (d_model, d_subspace) with orthogonal or non-orthogonal columns.

    Returns:
        Projected activations of shape (n_samples, d_model).
    """
    if activations.ndim != 2:
        raise ValueError(f"Expected 2D activations array, got shape {activations.shape}")
    if basis.ndim != 2 or basis.shape[0] != activations.shape[1]:
        raise ValueError(
            f"Basis dimension mismatch: basis {basis.shape} vs activations {activations.shape}"
        )

    # Orthonormalize basis via QR decomposition
    q, _ = np.linalg.qr(basis)
    # Projection operator Pi = Q Q^T
    projected = activations @ q @ q.T
    return projected


def decompose_residual_stream(
    activations: np.ndarray,
    shortcut_basis: np.ndarray,
    schema_basis: np.ndarray,
) -> dict[str, np.ndarray]:
    """Decompose residual stream activations into shortcut, schema, and orthogonal components.

    h(x) = h_S(x) + h_C(x) + h_perp(x)

    Args:
        activations: Hidden representations of shape (n_samples, d_model).
        shortcut_basis: Matrix of shape (d_model, d_s).
        schema_basis: Matrix of shape (d_model, d_c).

    Returns:
        Dictionary with keys:
            - 'shortcut_component': array of shape (n_samples, d_model)
            - 'schema_component': array of shape (n_samples, d_model)
            - 'residual_component': array of shape (n_samples, d_model)
            - 'energy_fraction_shortcut': float
            - 'energy_fraction_schema': float
    """
    h_s = project_to_subspace(activations, shortcut_basis)
    h_c = project_to_subspace(activations, schema_basis)
    h_perp = activations - h_s - h_c

    total_energy = float(np.sum(activations**2) + 1e-12)
    s_energy = float(np.sum(h_s**2))
    c_energy = float(np.sum(h_c**2))

    return {
        "shortcut_component": h_s,
        "schema_component": h_c,
        "residual_component": h_perp,
        "energy_fraction_shortcut": s_energy / total_energy,
        "energy_fraction_schema": c_energy / total_energy,
    }


def compute_head_schema_specialization(
    head_activations: np.ndarray,
    shortcut_basis: np.ndarray,
    schema_basis: np.ndarray,
    eps: float = 1e-6,
) -> float:
    """Compute the schema specialization ratio S_head for an individual attention head.

    S_head = ||Pi_C(H)||^2 / (||Pi_S(H)||^2 + eps)

    Args:
        head_activations: Head output vectors of shape (n_samples, d_head) or (n_samples, d_model).
        shortcut_basis: Subspace basis for shortcut features.
        schema_basis: Subspace basis for schema features.
        eps: Small numerical constant.

    Returns:
        Specialization score S_head >= 0.0 (higher indicates schema specialization).
    """
    decomp = decompose_residual_stream(head_activations, shortcut_basis, schema_basis)
    s_energy = np.sum(decomp["shortcut_component"] ** 2)
    c_energy = np.sum(decomp["schema_component"] ** 2)
    return float(c_energy / (s_energy + eps))
