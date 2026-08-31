"""Unit tests for representation geometry and homomorphism metrics (Paper 02 Task 4.2)."""

from __future__ import annotations

import numpy as np
import pytest
from paper02.src.analysis.geometry import (
    compute_homomorphism_error,
    compute_subspace_orthogonality,
    compute_subspace_principal_angles,
    linear_cka,
    rbf_cka,
)
from paper02.src.analysis.representation_geometry import (
    SubspaceReductionResult,
    compute_participation_ratio,
    compute_representation_trajectory_pca,
    simulate_empirical_trajectory_projection,
)

class TestCKAMetrics:
    """Test Linear and RBF CKA invariance and bounds."""

    def test_linear_cka_identity(self) -> None:
        rng = np.random.default_rng(42)
        x_mat = rng.normal(size=(50, 16))
        assert pytest.approx(linear_cka(x_mat, x_mat), abs=1e-5) == 1.0

    def test_linear_cka_orthogonal_invariance(self) -> None:
        rng = np.random.default_rng(42)
        x_mat = rng.normal(size=(50, 16))
        # Random orthogonal rotation matrix Q
        q_rot, _ = np.linalg.qr(rng.normal(size=(16, 16)))
        y_mat = x_mat @ q_rot
        assert pytest.approx(linear_cka(x_mat, y_mat), abs=1e-4) == 1.0

    def test_rbf_cka_identity(self) -> None:
        rng = np.random.default_rng(42)
        x_mat = rng.normal(size=(40, 8))
        assert pytest.approx(rbf_cka(x_mat, x_mat, sigma=1.0), abs=1e-4) == 1.0

    def test_cka_sample_mismatch_raises(self) -> None:
        x_mat = np.ones((10, 4))
        y_mat = np.ones((12, 4))
        with pytest.raises(ValueError, match="Sample count mismatch"):
            linear_cka(x_mat, y_mat)


class TestHomomorphismError:
    """Test Representational Homomorphism Error (HE) calculation."""

    def test_perfect_additive_homomorphism(self) -> None:
        rng = np.random.default_rng(42)
        phi_a = rng.normal(size=(30, 8))
        phi_b = rng.normal(size=(30, 8))
        phi_y = phi_a + phi_b  # Perfect homomorphism: phi(y) = phi(a) + phi(b)

        he = compute_homomorphism_error(phi_a, phi_b, phi_y)
        assert pytest.approx(he, abs=1e-6) == 0.0

    def test_random_non_homomorphic_representations(self) -> None:
        rng = np.random.default_rng(42)
        phi_a = rng.normal(size=(30, 8))
        phi_b = rng.normal(size=(30, 8))
        phi_y = rng.normal(size=(30, 8))  # Uncorrelated target

        he = compute_homomorphism_error(phi_a, phi_b, phi_y)
        assert he > 0.5  # High relative error


class TestSubspaceAnglesAndOrthogonality:
    """Test subspace principal angles and orthogonality metrics."""

    def test_strictly_orthogonal_subspaces(self) -> None:
        # Standard basis e1..e4 in R^8
        u_basis = np.eye(8)[:, :4]
        # Standard basis e5..e8 in R^8
        v_basis = np.eye(8)[:, 4:]

        angles = compute_subspace_principal_angles(u_basis, v_basis)
        assert len(angles) == 4
        assert np.allclose(angles, np.pi / 2.0)

        ortho_score = compute_subspace_orthogonality(u_basis, v_basis)
        assert pytest.approx(ortho_score, abs=1e-5) == 1.0

    def test_identical_subspaces(self) -> None:
        u_basis = np.eye(8)[:, :4]
        v_basis = np.eye(8)[:, :4]

        angles = compute_subspace_principal_angles(u_basis, v_basis)
        assert np.allclose(angles, 0.0)

        ortho_score = compute_subspace_orthogonality(u_basis, v_basis)
        assert pytest.approx(ortho_score, abs=1e-5) == 0.0


class Test2DSubspaceReductionAndPCA:
    """Test Participation Ratio and PCA trajectory concentration onto (u, v) manifold."""

    def test_participation_ratio_calculation(self) -> None:
        # Strictly 2-dimensional uniform spectrum: eigenvalues = [1, 1, 0, 0] -> PR = (2)^2 / 2 = 2.0
        eigs_2d = np.array([1.0, 1.0, 0.0, 0.0])
        pr_2d = compute_participation_ratio(eigs_2d)
        assert pytest.approx(pr_2d, abs=1e-5) == 2.0

        # 1-dimensional concentrated spectrum: eigenvalues = [1, 0, 0] -> PR = 1.0
        eigs_1d = np.array([10.0, 0.0, 0.0])
        pr_1d = compute_participation_ratio(eigs_1d)
        assert pytest.approx(pr_1d, abs=1e-5) == 1.0

    def test_representation_trajectory_pca_concentration(self) -> None:
        rng = np.random.default_rng(42)
        n_points = 100
        # Synthetic 2D dominant manifold embedded in 16D with small noise
        pc1 = rng.normal(size=(n_points, 1)) * 3.0
        pc2 = rng.normal(size=(n_points, 1)) * 2.0
        noise = rng.normal(scale=0.15, size=(n_points, 14))
        trajectories = np.hstack([pc1, pc2, noise])

        res = compute_representation_trajectory_pca(trajectories, n_components=5)
        assert isinstance(res, SubspaceReductionResult)
        assert res.top2_variance_ratio > 0.85
        assert res.participation_ratio < 3.0
        assert res.is_2d_subspace_dominant
        assert res.pc1_shortcut_correlation > 0.90
        assert res.pc2_coherent_correlation > 0.90

    def test_simulate_empirical_trajectory_projection(self) -> None:
        # Subcritical regime (lambda = 0.00)
        sub_res = simulate_empirical_trajectory_projection(lambda_val=0.00, total_steps=1000)
        assert sub_res["u_trajectory"][-1] > 0.90
        assert sub_res["v_trajectory"][-1] < 0.10
        assert "E_S" in str(sub_res["target_equilibrium"][0])

        # Supercritical regime (lambda = 0.50)
        sup_res = simulate_empirical_trajectory_projection(lambda_val=0.50, total_steps=1000)
        assert sup_res["v_trajectory"][-1] > 0.40
        assert "E_C" in str(sup_res["target_equilibrium"][0])
