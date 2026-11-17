# Solving systems of linear equations using Cramer's Rule
"""Solve systems of linear equations Ax = b using Cramer's Rule."""
from typing import List, Sequence, Union

from Math.Algebra.Systems_of_Equations import validate_linear_system
from Math.Linear_Algebra.Matrices.determinant import determinant


def cramers_rule(
    coefficients: Sequence[Sequence[Union[int, float]]],
    constants: Sequence[Union[int, float]],
) -> List[float]:
    """
    Solve a system of linear equations Ax = b using Cramer's Rule.

    Parameters:
    coefficients (Sequence[Sequence[Union[int, float]]]): Square n x n
        coefficient matrix A.
    constants (Sequence[Union[int, float]]): Right-hand side vector b of
        length n.

    Returns:
    List[float]: Solution vector x = [x_1, x_2, ..., x_n].

    Examples:
    >>> cramers_rule([[2, 1], [1, 3]], [5, 10])
    [1.0, 3.0]
    """
    a_mat, b_vec = validate_linear_system(coefficients, constants)
    det_a = determinant(a_mat)
    if abs(det_a) <= 1e-12:
        raise ValueError(
            "System has no unique solution (determinant is zero)."
        )

    n = len(a_mat)
    solution: List[float] = []
    for col in range(n):
        # Replace column `col` with the constants vector b
        modified = [
            [b_vec[row] if j == col else a_mat[row][j] for j in range(n)]
            for row in range(n)
        ]
        solution.append(determinant(modified) / det_a)

    return solution
