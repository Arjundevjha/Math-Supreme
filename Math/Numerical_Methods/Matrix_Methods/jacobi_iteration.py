# Solving a linear system Ax = b using the Jacobi iterative method
"""Jacobi iterative method for solving diagonally dominant linear systems."""

from typing import List, Optional, Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import validate_matrix
from Math.Linear_Algebra.Vectors.magnitude import (
    validate_vector,
    vector_magnitude,
)

Number = Union[int, float]


def validate_convergence_params(tol: float, max_iter: int) -> None:
    """
    Validate tolerance and maximum iteration parameters.

    Parameters:
    tol (float): Positive finite convergence tolerance.
    max_iter (int): Positive integer maximum iteration count.

    Returns:
    None
    """
    if isinstance(tol, bool) or not isinstance(tol, (int, float)):
        raise TypeError("tol must be a numeric int or float.")
    if not 0.0 < tol < float("inf"):
        raise ValueError("tol must be a positive finite number.")

    if isinstance(max_iter, bool) or not isinstance(max_iter, int):
        raise TypeError("max_iter must be an integer.")
    if max_iter < 1:
        raise ValueError("max_iter must be at least 1.")


def validate_iterative_inputs(
    a: Sequence[Sequence[Number]],
    b: Sequence[Number],
    x0: Optional[Sequence[Number]],
    tol: float,
    max_iter: int,
) -> Tuple[List[List[float]], List[float], List[float]]:
    """
    Validate inputs for iterative linear system solvers (Ax = b).

    Parameters:
    a (Sequence[Sequence[Number]]): Square coefficient matrix A.
    b (Sequence[Number]): Right-hand side vector b.
    x0 (Optional[Sequence[Number]]): Optional initial guess vector.
    tol (float): Positive convergence tolerance.
    max_iter (int): Positive maximum number of iterations.

    Returns:
    Tuple[List[List[float]], List[float], List[float]]:
        Validated matrix A, vector b, and initial guess vector x0.
    """
    mat_a = validate_matrix("a", a)
    n = len(mat_a)
    if n != len(mat_a[0]):
        raise ValueError("Coefficient matrix 'a' must be square.")

    vec_b = validate_vector("b", b)
    if len(vec_b) != n:
        raise ValueError(
            "Length of vector 'b' must match the dimension of matrix 'a'."
        )

    if x0 is None:
        vec_x0 = [0.0] * n
    else:
        vec_x0 = validate_vector("x0", x0)
        if len(vec_x0) != n:
            raise ValueError(
                "Length of 'x0' must match the dimension of matrix 'a'."
            )

    validate_convergence_params(tol, max_iter)

    for i in range(n):
        if mat_a[i][i] == 0.0:
            raise ValueError(
                f"Zero diagonal element at index ({i}, {i}); "
                "iterative solver cannot divide by zero."
            )

    return mat_a, vec_b, vec_x0


def jacobi_iteration(
    a: Sequence[Sequence[Number]],
    b: Sequence[Number],
    x0: Optional[Sequence[Number]] = None,
    tol: float = 1e-10,
    max_iter: int = 1000,
) -> List[float]:
    """
    Solve a linear system Ax = b using the Jacobi iterative method.

    Parameters:
    a (Sequence[Sequence[Number]]): Square coefficient matrix A (n x n).
    b (Sequence[Number]): Right-hand side vector b of length n.
    x0 (Optional[Sequence[Number]]): Initial guess vector; defaults to zeros.
    tol (float): Convergence tolerance on step norm ||x_new - x_old||_2.
    max_iter (int): Maximum number of iterations allowed.

    Returns:
    List[float]: Approximate solution vector x.

    Examples:
    >>> jacobi_iteration([[4, 1], [1, 3]], [1, 2])
    [0.090909090909..., 0.636363636363...]
    """
    mat_a, vec_b, x_curr = validate_iterative_inputs(a, b, x0, tol, max_iter)
    n = len(mat_a)

    for _ in range(max_iter):
        x_next: List[float] = []
        for i in range(n):
            sigma = sum(
                mat_a[i][j] * x_curr[j] for j in range(n) if j != i
            )
            val = (vec_b[i] - sigma) / mat_a[i][i]
            if not -float("inf") < val < float("inf"):
                raise ValueError(
                    "Jacobi iteration diverged (non-finite values)."
                )
            x_next.append(val)

        diff = [x_next[i] - x_curr[i] for i in range(n)]
        if vector_magnitude(diff) < tol:
            return x_next
        x_curr = x_next

    raise ValueError(
        f"Jacobi iteration did not converge within {max_iter} iterations."
    )
