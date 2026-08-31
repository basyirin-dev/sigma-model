"""Representation Geometry and Homomorphism Error Analysis Engine for Paper 02.

This module implements Centered Kernel Alignment (CKA), Representational
Homomorphism Error (HE), and subspace principal angle metrics to quantify the
geometric reorganization of hidden representations under the Two-Subspace Law.
"""

from __future__ import annotations

from typing import Callable

import numpy as np


def _center_gram_matrix(gram_k: np.ndarray) -> np.ndarray:
    """Center a Gram matrix K using H = I - (1/n) 1 1^T."""
    n = gram_k.shape[0]
    if n <= 1:
        return np.zeros_like(gram_k)
    unit = np.ones((n, n), dtype=gram_k.dtype) / n
    return gram_k - unit @ gram_k - gram_k @ unit + unit @ gram_k @ unit


def _hsic(gram_k: np.ndarray, gram_l: np.ndarray) -> float:
    """Compute empirical Hilbert-Schmidt Independence Criterion (HSIC)."""
    k_c = _center_gram_matrix(gram_k)
    l_c = _center_gram_matrix(gram_l)
    n = gram_k.shape[0]
    if n <= 1:
        return 0.0
    return float(np.sum(k_c * l_c) / ((n - 1) ** 2))


def linear_cka(x_repr: np.ndarray, y_repr: np.ndarray) -> float:
    """Compute Linear Centered Kernel Alignment between activation matrices X and Y.

    Args:
        x_repr: Representation matrix of shape (n_samples, d_x).
        y_repr: Representation matrix of shape (n_samples, d_y).

    Returns:
        Linear CKA similarity score in [0.0, 1.0].
    """
    if x_repr.shape[0] != y_repr.shape[0]:
        raise ValueError(
            f"Sample count mismatch: X has {x_repr.shape[0]} samples, Y has {y_repr.shape[0]} samples."
        )
    if x_repr.shape[0] <= 1:
        return 1.0

    gram_k = x_repr @ x_repr.T
    gram_l = y_repr @ y_repr.T

    hsic_xy = _hsic(gram_k, gram_l)
    hsic_xx = _hsic(gram_k, gram_k)
    hsic_yy = _hsic(gram_l, gram_l)

    denominator = np.sqrt(max(hsic_xx * hsic_yy, 1e-12))
    score = hsic_xy / denominator
    return float(np.clip(score, 0.0, 1.0))


def rbf_cka(x_repr: np.ndarray, y_repr: np.ndarray, sigma: float = 1.0) -> float:
    """Compute RBF Kernel Centered Kernel Alignment between activation matrices X and Y.

    Args:
        x_repr: Representation matrix of shape (n_samples, d_x).
        y_repr: Representation matrix of shape (n_samples, d_y).
        sigma: Kernel bandwidth parameter.

    Returns:
        RBF CKA similarity score in [0.0, 1.0].
    """
    if x_repr.shape[0] != y_repr.shape[0]:
        raise ValueError(
            f"Sample count mismatch: X has {x_repr.shape[0]} samples, Y has {y_repr.shape[0]} samples."
        )
    if x_repr.shape[0] <= 1:
        return 1.0

    # Pairwise squared Euclidean distances
    dist_x = np.sum((x_repr[:, None, :] - x_repr[None, :, :]) ** 2, axis=-1)
    dist_y = np.sum((y_repr[:, None, :] - y_repr[None, :, :]) ** 2, axis=-1)

    gram_k = np.exp(-dist_x / (2.0 * (sigma**2)))
    gram_l = np.exp(-dist_y / (2.0 * (sigma**2)))

    hsic_xy = _hsic(gram_k, gram_l)
    hsic_xx = _hsic(gram_k, gram_k)
    hsic_yy = _hsic(gram_l, gram_l)

    denominator = np.sqrt(max(hsic_xx * hsic_yy, 1e-12))
    score = hsic_xy / denominator
    return float(np.clip(score, 0.0, 1.0))


def compute_homomorphism_error(
    phi_a: np.ndarray,
    phi_b: np.ndarray,
    phi_y: np.ndarray,
    composition_fn: Callable[[np.ndarray, np.ndarray], np.ndarray] | None = None,
) -> float:
    """Compute Normalized Representational Homomorphism Error (HE per An & Du 2026).

    Measures the relative geometric deviation between predicted composite representation
    T(phi(a), phi(b)) and actual composite representation phi(y) across all rules (a, b) -> y.

    Args:
        phi_a: Representations of first operands of shape (n_rules, d_model).
        phi_b: Representations of second operands of shape (n_rules, d_model).
        phi_y: Representations of composed outputs of shape (n_rules, d_model).
        composition_fn: Optional composition operator. Defaults to vector addition (phi_a + phi_b).

    Returns:
        Mean normalized homomorphism error (HE >= 0.0). Lower is more homomorphic.
    """
    if not (phi_a.shape == phi_b.shape == phi_y.shape):
        raise ValueError(
            f"Shape mismatch in operands: phi_a {phi_a.shape}, phi_b {phi_b.shape}, phi_y {phi_y.shape}"
        )
    if phi_a.shape[0] == 0:
        return 0.0

    if composition_fn is None:
        predicted_y = phi_a + phi_b
    else:
        predicted_y = composition_fn(phi_a, phi_b)

    # Relative squared error per sample: ||phi_y - pred_y||^2 / (||phi_y||^2 + eps)
    numerator = np.sum((phi_y - predicted_y) ** 2, axis=-1)
    denominator = np.sum(phi_y**2, axis=-1) + 1e-10
    relative_errors = numerator / denominator

    return float(np.mean(relative_errors))


def compute_subspace_principal_angles(u_basis: np.ndarray, v_basis: np.ndarray) -> np.ndarray:
    """Compute principal angles between two subspace bases U and V via SVD.

    Args:
        u_basis: Matrix of shape (d_ambient, d_subspace_u).
        v_basis: Matrix of shape (d_ambient, d_subspace_v).

    Returns:
        Array of principal angles in radians, sorted in ascending order.
    """
    # Orthonormalize columns of U and V via QR decomposition
    q_u, _ = np.linalg.qr(u_basis)
    q_v, _ = np.linalg.qr(v_basis)

    # Singular values of Q_u^T Q_v give cos(theta_i)
    m = q_u.T @ q_v
    singular_vals = np.linalg.svd(m, compute_uv=False)
    # Clip singular values to [0.0, 1.0] to avoid numerical arccos NaNs
    clipped_s = np.clip(singular_vals, 0.0, 1.0)
    angles_rad = np.arccos(clipped_s)
    return np.sort(angles_rad)


def compute_subspace_orthogonality(u_basis: np.ndarray, v_basis: np.ndarray) -> float:
    """Compute mean subspace orthogonality score in [0.0, 1.0].

    Score = 1.0 means strictly orthogonal (all principal angles = pi/2).
    Score = 0.0 means fully overlapping (principal angles = 0).
    """
    angles = compute_subspace_principal_angles(u_basis, v_basis)
    if len(angles) == 0:
        return 1.0
    mean_angle = float(np.mean(angles))
    return float(mean_angle / (np.pi / 2.0))
