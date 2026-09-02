"""Smoke test suite for Paper 02 execution environment.

Verifies runtime availability and numerical stability of PyTorch, JAX,
SciPy, SymPy, Optax, and NumPy linear algebra routines.
"""

import sys

import jax
import jax.numpy as jnp
import numpy as np
import optax
import sympy as sp
import torch
from scipy.integrate import solve_ivp
from scipy.optimize import root_scalar


def test_python_version():
    """Verify runtime Python meets minimum version requirements."""
    assert sys.version_info >= (3, 11), f"Python version too old: {sys.version}"


def test_torch_tensor_ops_and_autodiff():
    """Verify PyTorch tensor math and backward autodiff on CPU."""
    x = torch.tensor([2.0, 3.0], requires_grad=True)
    y = (x**3).sum()
    y.backward()
    assert x.grad is not None
    assert torch.allclose(x.grad, torch.tensor([12.0, 27.0]))


def test_jax_grad_and_jit():
    """Verify JAX array operations, reverse-mode autodiff, and JIT compilation."""
    @jax.jit
    def loss_fn(w: jax.Array, x: jax.Array) -> jax.Array:
        return jnp.sum((jnp.dot(w, x) - 1.0) ** 2)

    w = jnp.array([[1.0, 2.0], [3.0, 4.0]])
    x = jnp.array([0.5, 0.5])
    grad_w = jax.grad(loss_fn)(w, x)
    assert grad_w.shape == (2, 2)
    assert not jnp.isnan(grad_w).any()


def test_scipy_ode_and_bifurcation():
    """Verify SciPy ODE integration and transcritical normal form root-finding."""
    # Transcritical normal form: dx/dt = r*x - x^2
    def ode_system(t: float, y: list[float], r: float) -> list[float]:
        return [r * y[0] - y[0] ** 2]

    sol = solve_ivp(ode_system, (0, 20), [0.1], args=(0.5,), method="RK45")
    assert sol.success
    # Stable branch converges asymptotically to r = 0.5
    assert abs(sol.y[0, -1] - 0.5) < 1e-3

    # Root finding for fixed point
    def toy_normal_form(x: float, r: float) -> float:
        return x * (r - x)

    sol_sub = root_scalar(toy_normal_form, args=(-0.5,), bracket=[-0.2, 0.2])
    assert sol_sub.converged
    assert abs(sol_sub.root) < 1e-6


def test_sympy_analytical_jacobian():
    """Verify SymPy symbolic derivation of coupled ODE Jacobian and eigenvalues."""
    sigma, delta, gamma_s, rho = sp.symbols("sigma delta gamma_s rho", real=True, positive=True)
    # Coupled toy system
    f_sigma = rho * sigma * (1 - sigma) - gamma_s * delta
    f_delta = delta * (1 - delta)

    jac = sp.Matrix([f_sigma, f_delta]).jacobian([sigma, delta])
    assert jac.shape == (2, 2)
    # Evaluate at origin (0, 0)
    jac_origin = jac.subs({sigma: 0, delta: 0})
    eigenvals = jac_origin.eigenvals()
    assert rho in eigenvals


def test_optax_optimizer_init():
    """Verify Optax optimizer gradient transformation initialization."""
    tx = optax.adam(learning_rate=1e-3)
    params = {"w": jnp.zeros((4, 4))}
    opt_state = tx.init(params)
    updates, _ = tx.update(params, opt_state, params)
    assert isinstance(updates, dict)
    assert "w" in updates


def test_numpy_subspace_principal_angles():
    """Verify NumPy orthogonal projection and principal angle calculation."""
    rng = np.random.default_rng(42)
    mat_a, _ = np.linalg.qr(rng.standard_normal((10, 3)))
    mat_b, _ = np.linalg.qr(rng.standard_normal((10, 3)))

    # Cosine of principal angles via SVD of mat_a^T mat_b
    mat_prod = mat_a.T @ mat_b
    singular_values = np.linalg.svd(mat_prod, compute_uv=False)
    assert len(singular_values) == 3
    assert np.all(singular_values >= 0.0)
    assert np.all(singular_values <= 1.0 + 1e-7)


