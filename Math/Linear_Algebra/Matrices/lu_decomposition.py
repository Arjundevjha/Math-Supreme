"""LU decomposition (PA = LU) with partial pivoting."""
# pylint: disable=too-many-locals
from typing import Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)


def lu_decomposition(
    matrix: Sequence[Sequence[Union[int, float]]],
) -> Tuple[Matrix, Matrix, Matrix]:
    """
    Compute Doolittle LU decomposition with partial pivoting: P * A = L * U.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Square n x n matrix.

    Returns:
    Tuple[Matrix, Matrix, Matrix]: (P, L, U) where P is permutation, L is
        unit lower triangular, and U is upper triangular.
    """
    mat = validate_matrix("matrix", matrix)
    n = len(mat)
    if n != len(mat[0]):
        raise ValueError("LU decomposition requires a square matrix.")

    p_mat: Matrix = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    l_mat: Matrix = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    u_mat: Matrix = [list(row) for row in mat]

    for k in range(n):
        pivot_row = max(
            range(k, n), key=lambda r, c=k: abs(u_mat[r][c])
        )
        if abs(u_mat[pivot_row][k]) <= 1e-12:
            raise ValueError("Matrix is singular; LU decomposition failed.")

        if pivot_row != k:
            u_mat[k], u_mat[pivot_row] = u_mat[pivot_row], u_mat[k]
            p_mat[k], p_mat[pivot_row] = p_mat[pivot_row], p_mat[k]
            for j in range(k):
                l_mat[k][j], l_mat[pivot_row][j] = (
                    l_mat[pivot_row][j],
                    l_mat[k][j],
                )

        for i in range(k + 1, n):
            factor = u_mat[i][k] / u_mat[k][k]
            l_mat[i][k] = factor
            for j in range(k, n):
                u_mat[i][j] -= factor * u_mat[k][j]

    return p_mat, l_mat, u_mat
