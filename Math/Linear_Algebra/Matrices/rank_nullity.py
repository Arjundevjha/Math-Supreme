"""Calculate matrix rank and nullity via row echelon reduction."""
from typing import Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import validate_matrix


def matrix_rank(
    matrix: Sequence[Sequence[Union[int, float]]], tol: float = 1e-10
) -> int:
    """
    Compute the rank of a matrix using Gaussian elimination with pivoting.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix.
    tol (float): Pivot tolerance for numerical zero.

    Returns:
    int: Rank of the matrix.
    """
    mat = validate_matrix("matrix", matrix)
    rows = len(mat)
    cols = len(mat[0])
    rank = 0
    pivot_row = 0

    for col in range(cols):
        if pivot_row >= rows:
            break
        best = max(
            range(pivot_row, rows), key=lambda r, c=col: abs(mat[r][c])
        )
        if abs(mat[best][col]) <= tol:
            continue
        mat[pivot_row], mat[best] = mat[best], mat[pivot_row]
        piv = mat[pivot_row][col]
        for r in range(pivot_row + 1, rows):
            factor = mat[r][col] / piv
            for c in range(col, cols):
                mat[r][c] -= factor * mat[pivot_row][c]
        rank += 1
        pivot_row += 1

    return rank


def matrix_nullity(
    matrix: Sequence[Sequence[Union[int, float]]], tol: float = 1e-10
) -> int:
    """
    Compute the nullity (dimension of null space) using Rank-Nullity theorem.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix.
    tol (float): Pivot tolerance for numerical zero.

    Returns:
    int: Nullity = n - rank(A).
    """
    mat = validate_matrix("matrix", matrix)
    return len(mat[0]) - matrix_rank(mat, tol=tol)


def rank_nullity(
    matrix: Sequence[Sequence[Union[int, float]]], tol: float = 1e-10
) -> Tuple[int, int]:
    """
    Return (rank, nullity) of a matrix.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix.
    tol (float): Pivot tolerance for numerical zero.

    Returns:
    Tuple[int, int]: (rank, nullity) satisfying rank + nullity == num_cols.
    """
    mat = validate_matrix("matrix", matrix)
    rank = matrix_rank(mat, tol=tol)
    return rank, len(mat[0]) - rank
