"""Calculate matrix determinant using Gaussian elimination with pivoting."""
from typing import Sequence, Union

from Math.Linear_Algebra.Matrices.matrix_addition import validate_matrix


def determinant(matrix: Sequence[Sequence[Union[int, float]]]) -> float:
    """
    Calculate the determinant of a square matrix.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Square n x n matrix.

    Returns:
    float: Determinant det(A).
    """
    mat = validate_matrix("matrix", matrix)
    n = len(mat)
    if n != len(mat[0]):
        raise ValueError("Determinant is only defined for square matrices.")

    det = 1.0
    for col in range(n):
        pivot_row = max(
            range(col, n), key=lambda r, c=col: abs(mat[r][c])
        )
        if abs(mat[pivot_row][col]) <= 1e-12:
            return 0.0
        if pivot_row != col:
            mat[col], mat[pivot_row] = mat[pivot_row], mat[col]
            det = -det

        pivot = mat[col][col]
        det *= pivot
        for row in range(col + 1, n):
            factor = mat[row][col] / pivot
            for j in range(col, n):
                mat[row][j] -= factor * mat[col][j]

    return det
