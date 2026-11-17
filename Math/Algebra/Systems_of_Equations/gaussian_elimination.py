# Solving systems of linear equations using Gaussian Elimination
"""Solve systems of linear equations Ax = b via Gaussian elimination."""
from typing import List, Sequence, Union

from Math.Algebra.Systems_of_Equations import validate_linear_system


def gaussian_elimination(
    coefficients: Sequence[Sequence[Union[int, float]]],
    constants: Sequence[Union[int, float]],
) -> List[float]:
    """
    Solve Ax = b using Gaussian elimination with partial pivoting.

    Parameters:
    coefficients (Sequence[Sequence[Union[int, float]]]): Square n x n
        coefficient matrix A.
    constants (Sequence[Union[int, float]]): Right-hand side vector b of
        length n.

    Returns:
    List[float]: Solution vector x = [x_1, x_2, ..., x_n].

    Examples:
    >>> gaussian_elimination([[2, 1], [1, 3]], [5, 10])
    [1.0, 3.0]
    """
    a_mat, b_vec = validate_linear_system(coefficients, constants)
    n = len(a_mat)

    # Form the augmented matrix [A | b]
    aug = [a_mat[i] + [b_vec[i]] for i in range(n)]

    # Forward elimination with partial pivoting
    for col in range(n):
        pivot_row = max(
            range(col, n), key=lambda r, c=col: abs(aug[r][c])
        )
        if abs(aug[pivot_row][col]) <= 1e-12:
            raise ValueError("System is singular and has no unique solution.")

        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        for row in range(col + 1, n):
            factor = aug[row][col] / pivot
            if factor != 0.0:
                for j in range(col, n + 1):
                    aug[row][j] -= factor * aug[col][j]

    # Back substitution
    solution: List[float] = [0.0] * n
    for row in range(n - 1, -1, -1):
        known_sum = sum(
            aug[row][j] * solution[j] for j in range(row + 1, n)
        )
        solution[row] = (aug[row][n] - known_sum) / aug[row][row]

    return solution
