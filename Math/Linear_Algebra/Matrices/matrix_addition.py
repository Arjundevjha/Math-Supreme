"""Matrix addition, subtraction, and shared matrix validation."""
from typing import List, Sequence, Union

Number = Union[int, float]
Matrix = List[List[float]]


def validate_matrix(
    name: str, matrix: Sequence[Sequence[Number]]
) -> Matrix:
    """
    Validate a rectangular 2D numeric matrix and return a float copy.

    Parameters:
    name (str): Parameter name for error messages.
    matrix (Sequence[Sequence[Number]]): 2D sequence of numbers.

    Returns:
    Matrix: Validated 2D list of floats.
    """
    if not isinstance(matrix, (list, tuple)) or not matrix:
        raise TypeError(f"{name} must be a non-empty list or tuple of rows.")
    if len(matrix) > 500:
        raise ValueError(f"{name} row count exceeds maximum limit of 500.")

    cols = None
    result: Matrix = []
    for r_idx, row in enumerate(matrix):
        if not isinstance(row, (list, tuple)) or not row:
            raise TypeError(
                f"Row {r_idx} of {name} must be a non-empty list or tuple."
            )
        if len(row) > 500:
            raise ValueError(
                f"{name} column count exceeds maximum limit of 500."
            )
        if cols is None:
            cols = len(row)
        elif len(row) != cols:
            raise ValueError(f"All rows in {name} must have equal length.")

        clean_row: List[float] = []
        for val in row:
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise TypeError(
                    f"All elements in {name} must be int or float."
                )
            if not -float("inf") < val < float("inf"):
                raise ValueError(f"All elements in {name} must be finite.")
            clean_row.append(float(val))
        result.append(clean_row)
    return result


def matrix_add(
    a: Sequence[Sequence[Number]], b: Sequence[Sequence[Number]]
) -> Matrix:
    """
    Add two matrices of identical dimensions (A + B).

    Parameters:
    a (Sequence[Sequence[Number]]): First matrix.
    b (Sequence[Sequence[Number]]): Second matrix.

    Returns:
    Matrix: Sum matrix A + B.
    """
    mat_a = validate_matrix("a", a)
    mat_b = validate_matrix("b", b)
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        raise ValueError("Matrices must have identical dimensions.")
    return [
        [x + y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(mat_a, mat_b)
    ]


def matrix_subtract(
    a: Sequence[Sequence[Number]], b: Sequence[Sequence[Number]]
) -> Matrix:
    """
    Subtract two matrices of identical dimensions (A - B).

    Parameters:
    a (Sequence[Sequence[Number]]): First matrix.
    b (Sequence[Sequence[Number]]): Second matrix.

    Returns:
    Matrix: Difference matrix A - B.
    """
    mat_a = validate_matrix("a", a)
    mat_b = validate_matrix("b", b)
    if len(mat_a) != len(mat_b) or len(mat_a[0]) != len(mat_b[0]):
        raise ValueError("Matrices must have identical dimensions.")
    return [
        [x - y for x, y in zip(row_a, row_b)]
        for row_a, row_b in zip(mat_a, mat_b)
    ]
