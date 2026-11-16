"""Calculate matrix inverse using Gauss-Jordan elimination."""
from typing import Sequence, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)


def matrix_inverse(matrix: Sequence[Sequence[Union[int, float]]]) -> Matrix:
    """
    Compute the inverse A^(-1) of an invertible square matrix.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Square n x n matrix.

    Returns:
    Matrix: Inverse matrix A^(-1).
    """
    mat = validate_matrix("matrix", matrix)
    n = len(mat)
    if n != len(mat[0]):
        raise ValueError("Inverse is only defined for square matrices.")

    aug = [
        mat[i] + [1.0 if i == j else 0.0 for j in range(n)]
        for i in range(n)
    ]

    for col in range(n):
        pivot_row = max(
            range(col, n), key=lambda r, c=col: abs(aug[r][c])
        )
        if abs(aug[pivot_row][col]) <= 1e-12:
            raise ValueError("Matrix is singular and cannot be inverted.")
        if pivot_row != col:
            aug[col], aug[pivot_row] = aug[pivot_row], aug[col]

        pivot = aug[col][col]
        aug[col] = [val / pivot for val in aug[col]]

        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor != 0.0:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j] for j in range(2 * n)
                ]

    return [row[n:] for row in aug]
