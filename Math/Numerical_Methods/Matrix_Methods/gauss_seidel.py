# Solving a linear system Ax = b using the Gauss-Seidel iterative method
"""Gauss-Seidel iterative method for solving linear systems."""

from typing import List, Optional, Sequence, Union

from Math.Linear_Algebra.Vectors.magnitude import vector_magnitude
from Math.Numerical_Methods.Matrix_Methods.jacobi_iteration import (
    validate_iterative_inputs,
)

Number = Union[int, float]


def gauss_seidel(
    a: Sequence[Sequence[Number]],
    b: Sequence[Number],
    x0: Optional[Sequence[Number]] = None,
    tol: float = 1e-10,
    max_iter: int = 1000,
) -> List[float]:
    """
    Solve a linear system Ax = b using the Gauss-Seidel iterative method.

    Parameters:
    a (Sequence[Sequence[Number]]): Square coefficient matrix A (n x n).
    b (Sequence[Number]): Right-hand side vector b of length n.
    x0 (Optional[Sequence[Number]]): Initial guess vector; defaults to zeros.
    tol (float): Convergence tolerance on step norm ||x_new - x_old||_2.
    max_iter (int): Maximum number of iterations allowed.

    Returns:
    List[float]: Approximate solution vector x.

    Examples:
    >>> gauss_seidel([[4, 1], [1, 3]], [1, 2])
    [0.090909090909..., 0.636363636363...]
    """
    mat_a, vec_b, x_curr = validate_iterative_inputs(a, b, x0, tol, max_iter)
    n = len(mat_a)

    for _ in range(max_iter):
        x_new = list(x_curr)
        for i in range(n):
            sigma = sum(
                mat_a[i][j] * x_new[j] for j in range(n) if j != i
            )
            val = (vec_b[i] - sigma) / mat_a[i][i]
            if not -float("inf") < val < float("inf"):
                raise ValueError(
                    "Gauss-Seidel iteration diverged (non-finite values)."
                )
            x_new[i] = val

        diff = [x_new[i] - x_curr[i] for i in range(n)]
        if vector_magnitude(diff) < tol:
            return x_new
        x_curr = x_new

    raise ValueError(
        f"Gauss-Seidel iteration did not converge within {max_iter} "
        "iterations."
    )
