"""QR decomposition using Modified Gram-Schmidt orthogonalization."""
from typing import Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)
from Math.Linear_Algebra.Matrices.matrix_transpose import matrix_transpose
from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import vector_magnitude


def qr_decomposition(
    matrix: Sequence[Sequence[Union[int, float]]],
) -> Tuple[Matrix, Matrix]:
    """
    Compute thin QR decomposition A = Q * R using Modified Gram-Schmidt.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix
        with m >= n and linearly independent columns.

    Returns:
    Tuple[Matrix, Matrix]: (Q, R) where Q is m x n orthonormal and R is n x n
        upper triangular.
    """
    mat = validate_matrix("matrix", matrix)
    rows = len(mat)
    cols = len(mat[0])
    if rows < cols:
        raise ValueError("QR decomposition requires rows >= columns.")

    # Work on columns of A
    v_cols = [[mat[r][c] for r in range(rows)] for c in range(cols)]
    q_cols = []
    r_mat: Matrix = [[0.0] * cols for _ in range(cols)]

    for i in range(cols):
        norm = vector_magnitude(v_cols[i])
        if norm <= 1e-12:
            raise ValueError("Columns of matrix are linearly dependent.")
        r_mat[i][i] = norm
        q_i = [x / norm for x in v_cols[i]]
        q_cols.append(q_i)

        for j in range(i + 1, cols):
            proj = dot_product(q_i, v_cols[j])
            r_mat[i][j] = proj
            v_cols[j] = [
                vj - proj * qi for vj, qi in zip(v_cols[j], q_i)
            ]

    q_mat = matrix_transpose(q_cols)
    return q_mat, r_mat
