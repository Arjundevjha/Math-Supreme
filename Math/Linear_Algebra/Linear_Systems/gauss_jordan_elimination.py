# Gauss-Jordan elimination for RREF and solving linear systems
"""Gauss-Jordan elimination for RREF and solving linear systems."""

from typing import Any, Dict, List, Sequence, Tuple

from Math.Linear_Algebra.Matrices.matrix_addition import (
    Matrix,
    Number,
    validate_matrix,
)


def _validate_tolerance(tol: Number) -> float:
    """Validate that numerical tolerance is a non-negative finite number."""
    if isinstance(tol, bool) or not isinstance(tol, (int, float)):
        raise TypeError("Tolerance tol must be an int or float.")
    if not 0.0 <= tol < float("inf"):
        raise ValueError("Tolerance tol must be non-negative and finite.")
    return float(tol)


def _validate_vector(
    name: str, vector: Sequence[Number], expected_len: int
) -> List[float]:
    """Validate a 1D numeric vector and return a float copy."""
    if not isinstance(vector, (list, tuple)) or not vector:
        raise TypeError(f"{name} must be a non-empty list or tuple.")
    if len(vector) != expected_len:
        raise ValueError(
            f"{name} length ({len(vector)}) must match row count "
            f"({expected_len})."
        )
    clean: List[float] = []
    for val in vector:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"All elements in {name} must be int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"All elements in {name} must be finite.")
        clean.append(float(val))
    return clean


def _rref_with_pivots(
    mat: Matrix, tol: float
) -> Tuple[Matrix, List[int]]:
    """Compute RREF in place on a validated matrix and return pivot cols."""
    rows = len(mat)
    cols = len(mat[0])
    pivot_cols: List[int] = []
    lead = 0

    for col in range(cols):
        if lead >= rows:
            break
        pivot_row = max(
            range(lead, rows), key=lambda r, c=col: abs(mat[r][c])
        )
        if abs(mat[pivot_row][col]) <= tol:
            continue

        if pivot_row != lead:
            mat[lead], mat[pivot_row] = mat[pivot_row], mat[lead]

        pivot = mat[lead][col]
        mat[lead] = [val / pivot for val in mat[lead]]
        mat[lead][col] = 1.0

        for row in range(rows):
            if row == lead:
                continue
            factor = mat[row][col]
            if abs(factor) > tol:
                mat[row] = [
                    mat[row][j] - factor * mat[lead][j]
                    for j in range(cols)
                ]
            mat[row][col] = 0.0

        pivot_cols.append(col)
        lead += 1

    for r_idx in range(rows):
        for c_idx in range(cols):
            if abs(mat[r_idx][c_idx]) <= tol:
                mat[r_idx][c_idx] = 0.0

    return mat, pivot_cols


def reduced_row_echelon_form(
    matrix: Sequence[Sequence[Number]], tol: Number = 1e-12
) -> Matrix:
    """
    Compute the Reduced Row Echelon Form (RREF) of a matrix.

    Parameters:
    matrix (Sequence[Sequence[Number]]): Rectangular m x n numeric matrix.
    tol (Number): Non-negative pivot tolerance for numerical zero.

    Returns:
    Matrix: The matrix in Reduced Row Echelon Form.

    Examples:
    >>> reduced_row_echelon_form([[1, 2, -1], [2, 4, -2]])
    [[1.0, 2.0, -1.0], [0.0, 0.0, 0.0]]
    """
    clean_tol = _validate_tolerance(tol)
    mat = validate_matrix("matrix", matrix)
    rref_mat, _ = _rref_with_pivots(mat, clean_tol)
    return rref_mat


def gauss_jordan_elimination(
    coefficients: Sequence[Sequence[Number]],
    constants: Sequence[Number],
    tol: Number = 1e-12,
) -> Dict[str, Any]:
    """
    Analyze and solve linear system Ax = b via Gauss-Jordan elimination.

    Handles unique, inconsistent, and infinitely-many-solutions cases.

    Parameters:
    coefficients (Sequence[Sequence[Number]]): Coefficient matrix A (m x n).
    constants (Sequence[Number]): Right-hand side vector b of length m.
    tol (Number): Non-negative pivot tolerance for numerical zero.

    Returns:
    Dict[str, Any]: Dictionary with keys:
        - "status" (str): "unique", "inconsistent", or "infinite".
        - "solution" (Optional[List[float]]): Solution x if unique, else None.
        - "rref" (Matrix): RREF of the augmented matrix [A | b].
        - "pivot_columns" (List[int]): Pivot column indices in A.
        - "free_variables" (List[int]): Free variable column indices in A.
    """
    clean_tol = _validate_tolerance(tol)
    mat_a = validate_matrix("coefficients", coefficients)
    vec_b = _validate_vector("constants", constants, len(mat_a))

    n_cols = len(mat_a[0])
    augmented = [row + [b_val] for row, b_val in zip(mat_a, vec_b)]
    rref_aug, all_pivots = _rref_with_pivots(augmented, clean_tol)

    if n_cols in all_pivots:
        status = "inconsistent"
        pivot_cols = [c for c in all_pivots if c < n_cols]
        solution = None
    elif len(all_pivots) < n_cols:
        status = "infinite"
        pivot_cols = all_pivots
        solution = None
    else:
        status = "unique"
        pivot_cols = all_pivots
        solution = [rref_aug[i][n_cols] for i in range(n_cols)]

    pivot_set = set(pivot_cols)
    free_vars = [col for col in range(n_cols) if col not in pivot_set]

    return {
        "status": status,
        "solution": solution,
        "rref": rref_aug,
        "pivot_columns": pivot_cols,
        "free_variables": free_vars,
    }


def gauss_jordan_solve(
    coefficients: Sequence[Sequence[Number]],
    constants: Sequence[Number],
    tol: Number = 1e-12,
) -> List[float]:
    """
    Solve the linear system Ax = b for a unique solution.

    Parameters:
    coefficients (Sequence[Sequence[Number]]): Coefficient matrix A (m x n).
    constants (Sequence[Number]): Right-hand side vector b of length m.
    tol (Number): Non-negative pivot tolerance for numerical zero.

    Returns:
    List[float]: Unique solution vector x of length n.
    """
    result = gauss_jordan_elimination(coefficients, constants, tol=tol)
    status = result["status"]
    if status == "inconsistent":
        raise ValueError(
            "The linear system is inconsistent and has no solution."
        )
    if status == "infinite":
        raise ValueError(
            "The linear system is singular or underdetermined and has "
            "infinitely many solutions."
        )
    return result["solution"]
