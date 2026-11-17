# Solving systems of linear equations using the matrix inverse method
"""Solve systems of linear equations Ax = b via x = A^(-1) b."""
from typing import List, Sequence, Union

from Math.Algebra.Systems_of_Equations import validate_linear_system
from Math.Linear_Algebra.Matrices.matrix_inverse import matrix_inverse
from Math.Linear_Algebra.Matrices.matrix_multiplication import matrix_multiply


def matrix_method_solver(
    coefficients: Sequence[Sequence[Union[int, float]]],
    constants: Sequence[Union[int, float]],
) -> List[float]:
    """
    Solve a system of linear equations Ax = b using x = A^(-1) b.

    Parameters:
    coefficients (Sequence[Sequence[Union[int, float]]]): Square n x n
        invertible coefficient matrix A.
    constants (Sequence[Union[int, float]]): Right-hand side vector b of
        length n.

    Returns:
    List[float]: Solution vector x = [x_1, x_2, ..., x_n].

    Examples:
    >>> matrix_method_solver([[2, 1], [1, 3]], [5, 10])
    [1.0, 3.0]
    """
    a_mat, b_vec = validate_linear_system(coefficients, constants)
    inv_a = matrix_inverse(a_mat)
    b_col = [[val] for val in b_vec]
    result = matrix_multiply(inv_a, b_col)
    return [row[0] for row in result]
