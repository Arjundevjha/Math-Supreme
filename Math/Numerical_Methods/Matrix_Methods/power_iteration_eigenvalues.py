# Finding dominant eigenvalue and eigenvector using Power Iteration
"""Power Iteration method for dominant eigenvalue and eigenvector."""

from typing import List, Optional, Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import validate_matrix
from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import (
    validate_vector,
    vector_magnitude,
)
from Math.Numerical_Methods.Matrix_Methods.jacobi_iteration import (
    validate_convergence_params,
)

Number = Union[int, float]


def _validate_power_inputs(
    a: Sequence[Sequence[Number]],
    v0: Optional[Sequence[Number]],
    tol: float,
    max_iter: int,
) -> Tuple[List[List[float]], List[float]]:
    """Validate inputs and return normalized starting vector."""
    mat_a = validate_matrix("a", a)
    n = len(mat_a)
    if n != len(mat_a[0]):
        raise ValueError("Matrix 'a' must be square.")

    if v0 is None:
        vec = [1.0] * n
    else:
        vec = validate_vector("v0", v0)
        if len(vec) != n:
            raise ValueError(
                "Length of 'v0' must match the dimension of matrix 'a'."
            )

    norm = vector_magnitude(vec)
    if norm == 0.0:
        raise ValueError("Initial vector 'v0' must not be the zero vector.")
    v_init = [val / norm for val in vec]

    validate_convergence_params(tol, max_iter)
    return mat_a, v_init


def _has_converged(
    v_next: List[float],
    v_curr: List[float],
    eig: float,
    prev_eig: Optional[float],
    tol: float,
) -> bool:
    """Check eigenvector (up to sign) and eigenvalue convergence."""
    if prev_eig is None or abs(eig - prev_eig) >= tol:
        return False
    diff_pos = vector_magnitude([x - y for x, y in zip(v_next, v_curr)])
    diff_neg = vector_magnitude([x + y for x, y in zip(v_next, v_curr)])
    return min(diff_pos, diff_neg) < tol


def power_iteration(
    a: Sequence[Sequence[Number]],
    v0: Optional[Sequence[Number]] = None,
    tol: float = 1e-10,
    max_iter: int = 1000,
) -> Tuple[float, List[float]]:
    """
    Estimate the dominant eigenvalue and unit eigenvector via Power Iteration.

    Parameters:
    a (Sequence[Sequence[Number]]): Square matrix A (n x n).
    v0 (Optional[Sequence[Number]]): Non-zero initial vector; defaults to ones.
    tol (float): Convergence tolerance for eigenvector and eigenvalue change.
    max_iter (int): Maximum number of iterations allowed.

    Returns:
    Tuple[float, List[float]]:
        Dominant eigenvalue (via Rayleigh quotient) and unit eigenvector.

    Examples:
    >>> power_iteration([[2, 0], [0, 1]])
    (2.0, [1.0, 0.0])
    """
    mat_a, v_curr = _validate_power_inputs(a, v0, tol, max_iter)
    prev_eig: Optional[float] = None

    for _ in range(max_iter):
        w = [dot_product(row, v_curr) for row in mat_a]
        if not all(-float("inf") < val < float("inf") for val in w):
            raise ValueError("Power iteration diverged (non-finite values).")

        w_norm = vector_magnitude(w)
        if w_norm == 0.0:
            return 0.0, v_curr

        v_next = [val / w_norm for val in w]
        av_next = [dot_product(row, v_next) for row in mat_a]
        eig = dot_product(v_next, av_next)

        if _has_converged(v_next, v_curr, eig, prev_eig, tol):
            return eig, v_next

        v_curr = v_next
        prev_eig = eig

    raise ValueError(
        f"Power iteration did not converge within {max_iter} iterations."
    )
