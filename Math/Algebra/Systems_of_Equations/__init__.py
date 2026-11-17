# Shared validation utilities for systems of linear equations
"""Shared validation utilities for systems of linear equations."""
from typing import List, Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)


def validate_linear_system(
    coefficients: Sequence[Sequence[Union[int, float]]],
    constants: Sequence[Union[int, float]],
) -> Tuple[Matrix, List[float]]:
    """
    Validate a square linear system Ax = b and return float copies.

    Parameters:
    coefficients (Sequence[Sequence[Union[int, float]]]): Square n x n
        coefficient matrix A.
    constants (Sequence[Union[int, float]]): Right-hand side vector b of
        length n.

    Returns:
    Tuple[Matrix, List[float]]: Validated matrix A and vector b as floats.
    """
    a_mat = validate_matrix("coefficients", coefficients)
    n = len(a_mat)
    if n != len(a_mat[0]):
        raise ValueError("Coefficient matrix must be square.")

    if not isinstance(constants, (list, tuple)) or not constants:
        raise TypeError("constants must be a non-empty list or tuple.")

    b_col = validate_matrix("constants", [[val] for val in constants])
    if len(b_col) != n:
        raise ValueError(
            "Length of constants must match the number of equations."
        )

    return a_mat, [row[0] for row in b_col]
