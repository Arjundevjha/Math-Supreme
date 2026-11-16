"""Matrix transpose operation."""
from typing import Sequence, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)


def matrix_transpose(matrix: Sequence[Sequence[Union[int, float]]]) -> Matrix:
    """
    Compute the transpose A^T of a matrix A.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix.

    Returns:
    Matrix: Transposed n x m matrix.
    """
    mat = validate_matrix("matrix", matrix)
    rows = len(mat)
    cols = len(mat[0])
    return [[mat[r][c] for r in range(rows)] for c in range(cols)]
