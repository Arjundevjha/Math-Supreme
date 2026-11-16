"""Matrix multiplication and scalar multiplication."""
from typing import Sequence, Union

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    validate_matrix,
)


def scalar_multiply(
    matrix: Sequence[Sequence[Union[int, float]]], scalar: Union[int, float]
) -> Matrix:
    """
    Multiply every element of a matrix by a scalar.

    Parameters:
    matrix (Sequence[Sequence[Union[int, float]]]): Input matrix.
    scalar (Union[int, float]): Scalar multiplier.

    Returns:
    Matrix: Scaled matrix.
    """
    mat = validate_matrix("matrix", matrix)
    if isinstance(scalar, bool) or not isinstance(scalar, (int, float)):
        raise TypeError("scalar must be a numeric int or float.")
    if not -float("inf") < scalar < float("inf"):
        raise ValueError("scalar must be a finite number.")
    s = float(scalar)
    return [[val * s for val in row] for row in mat]


def matrix_multiply(
    a: Sequence[Sequence[Union[int, float]]],
    b: Sequence[Sequence[Union[int, float]]],
) -> Matrix:
    """
    Multiply two compatible matrices A (m x k) and B (k x n).

    Parameters:
    a (Sequence[Sequence[Union[int, float]]]): Left matrix (m x k).
    b (Sequence[Sequence[Union[int, float]]]): Right matrix (k x n).

    Returns:
    Matrix: Product matrix A * B (m x n).
    """
    mat_a = validate_matrix("a", a)
    mat_b = validate_matrix("b", b)
    if len(mat_a[0]) != len(mat_b):
        raise ValueError(
            "Number of columns in 'a' must equal number of rows in 'b'."
        )

    rows_a = len(mat_a)
    cols_b = len(mat_b[0])
    inner = len(mat_b)
    return [
        [
            sum(mat_a[i][k] * mat_b[k][j] for k in range(inner))
            for j in range(cols_b)
        ]
        for i in range(rows_a)
    ]
