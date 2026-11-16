"""Singular Value Decomposition (SVD) via Jacobi eigenvalue method."""
# pylint: disable=too-many-locals
from typing import List, Sequence, Tuple, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)
from Math.Linear_Algebra.Matrices.matrix_multiplication import matrix_multiply
from Math.Linear_Algebra.Matrices.matrix_transpose import matrix_transpose
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root


def _jacobi_symmetric_eigen(
    sym: Matrix, max_iter: int = 200
) -> Tuple[List[float], Matrix]:
    """Compute eigenvalues and eigenvectors of a real symmetric matrix."""
    n = len(sym)
    a = [list(row) for row in sym]
    v = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

    for _ in range(max_iter * n * n):
        # Find largest off-diagonal element
        p, q = 0, 1
        max_val = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > max_val:
                    max_val = abs(a[i][j])
                    p, q = i, j
        if max_val <= 1e-12:
            break

        if abs(a[p][p] - a[q][q]) <= 1e-15:
            tau = 0.0
            t = 1.0
        else:
            tau = (a[q][q] - a[p][p]) / (2.0 * a[p][q])
            sign_tau = 1.0 if tau >= 0 else -1.0
            t = sign_tau / (
                abs(tau) + float(nth_root(1.0 + tau * tau, 2))
            )

        c = 1.0 / float(nth_root(1.0 + t * t, 2))
        s = t * c

        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = app - t * apq
        a[q][q] = aqq + t * apq
        a[p][q] = 0.0
        a[q][p] = 0.0

        for k in range(n):
            if k in (p, q):
                continue
            akp, akq = a[k][p], a[k][q]
            a[k][p] = c * akp - s * akq
            a[p][k] = a[k][p]
            a[k][q] = s * akp + c * akq
            a[q][k] = a[k][q]

        for k in range(n):
            vkp, vkq = v[k][p], v[k][q]
            v[k][p] = c * vkp - s * vkq
            v[k][q] = s * vkp + c * vkq

    eigenvalues = [a[i][i] for i in range(n)]
    return eigenvalues, v


def svd(
    matrix: Sequence[Sequence[Union[int, float]]], max_iter: int = 200
) -> Tuple[Matrix, List[float], Matrix]:
    """
    Compute thin Singular Value Decomposition A = U * diag(S) * V^T.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input m x n matrix.
    max_iter (int): Maximum Jacobi sweeps for eigendecomposition.

    Returns:
    Tuple[Matrix, List[float], Matrix]: (U, singular_values, V_T).
    """
    mat = validate_matrix("matrix", matrix)
    if isinstance(max_iter, bool) or not isinstance(max_iter, int):
        raise TypeError("max_iter must be an integer.")
    if max_iter < 1 or max_iter > 10000:
        raise ValueError("max_iter must be between 1 and 10000.")

    rows = len(mat)
    cols = len(mat[0])
    if cols == 1:
        col_vec = [mat[r][0] for r in range(rows)]
        sq_sum = sum(x * x for x in col_vec)
        sigma = float(nth_root(sq_sum, 2)) if sq_sum > 0 else 0.0
        if sigma > 1e-12:
            u_col = [[x / sigma] for x in col_vec]
        else:
            u_col = [[1.0 if i == 0 else 0.0] for i in range(rows)]
        return u_col, [sigma], [[1.0]]

    ata = matrix_multiply(matrix_transpose(mat), mat)
    eigvals, v_mat = _jacobi_symmetric_eigen(ata, max_iter=max_iter)

    # Sort singular values descending
    pairs = sorted(
        [(max(0.0, ev), i) for i, ev in enumerate(eigvals)],
        key=lambda item: item[0],
        reverse=True,
    )
    sigmas = [float(nth_root(ev, 2)) if ev > 0 else 0.0 for ev, _ in pairs]
    v_sorted = [[v_mat[r][idx] for _, idx in pairs] for r in range(cols)]

    # Compute U columns: u_i = (A * v_i) / sigma_i
    av_mat = matrix_multiply(mat, v_sorted)
    u_mat: Matrix = [[0.0] * cols for _ in range(rows)]
    for j, sigma in enumerate(sigmas):
        if sigma > 1e-12:
            for i in range(rows):
                u_mat[i][j] = av_mat[i][j] / sigma

    return u_mat, sigmas, matrix_transpose(v_sorted)
