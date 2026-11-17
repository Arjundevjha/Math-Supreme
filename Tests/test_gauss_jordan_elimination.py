"""Unit tests for Gauss-Jordan elimination and RREF."""
import pytest

from Math.Linear_Algebra.Linear_Systems.gauss_jordan_elimination import (
    gauss_jordan_elimination,
    gauss_jordan_solve,
    reduced_row_echelon_form,
)


def _assert_matrix_close(mat_a, mat_b, tol=1e-9):
    assert len(mat_a) == len(mat_b)
    assert len(mat_a[0]) == len(mat_b[0])
    for row_a, row_b in zip(mat_a, mat_b):
        for val_a, val_b in zip(row_a, row_b):
            assert val_a == pytest.approx(val_b, abs=tol)


class TestReducedRowEchelonForm:
    def test_invertible_matrix_gives_identity(self):
        mat = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        expected = [
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
        ]
        _assert_matrix_close(reduced_row_echelon_form(mat), expected)

    def test_wide_rectangular_matrix(self):
        mat = [[1, 2, -1, 3], [2, 4, 1, 9], [1, 2, 2, 6]]
        expected = [
            [1.0, 2.0, 0.0, 4.0],
            [0.0, 0.0, 1.0, 1.0],
            [0.0, 0.0, 0.0, 0.0],
        ]
        _assert_matrix_close(reduced_row_echelon_form(mat), expected)

    def test_tall_rectangular_matrix(self):
        mat = [[1, 2], [2, 4], [3, 1]]
        expected = [[1.0, 0.0], [0.0, 1.0], [0.0, 0.0]]
        _assert_matrix_close(reduced_row_echelon_form(mat), expected)

    def test_zero_matrix(self):
        mat = [[0, 0, 0], [0, 0, 0]]
        expected = [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]
        assert reduced_row_echelon_form(mat) == expected

    def test_row_swap_with_zero_leading_entry(self):
        mat = [[0, 2, 4], [1, 3, 5]]
        expected = [[1.0, 0.0, -1.0], [0.0, 1.0, 2.0]]
        _assert_matrix_close(reduced_row_echelon_form(mat), expected)

    def test_does_not_mutate_input(self):
        original = [[2, 4], [1, 3]]
        snapshot = [row[:] for row in original]
        reduced_row_echelon_form(original)
        assert original == snapshot

    def test_invalid_inputs(self):
        with pytest.raises(TypeError):
            reduced_row_echelon_form([])
        with pytest.raises(ValueError):
            reduced_row_echelon_form([[1, 2], [3]])
        with pytest.raises(TypeError):
            reduced_row_echelon_form([[True, 1], [0, 1]])
        with pytest.raises(ValueError):
            reduced_row_echelon_form([[1, float("inf")], [0, 1]])
        with pytest.raises(ValueError):
            reduced_row_echelon_form([[1, 0], [0, 1]], tol=-1e-5)
        with pytest.raises(TypeError):
            reduced_row_echelon_form([[1, 0], [0, 1]], tol=True)


class TestGaussJordanSolve:
    def test_unique_solution_3x3(self):
        coeffs = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        consts = [8, -11, -3]
        sol = gauss_jordan_solve(coeffs, consts)
        assert sol == pytest.approx([2.0, 3.0, -1.0], abs=1e-9)

    def test_unique_solution_requires_pivoting(self):
        coeffs = [[0, 2, 1], [1, -2, -3], [-1, 1, 2]]
        consts = [-8, 0, 3]
        sol = gauss_jordan_solve(coeffs, consts)
        assert sol == pytest.approx([-4.0, -5.0, 2.0], abs=1e-9)

    def test_overdetermined_consistent_unique(self):
        coeffs = [[1, 0], [0, 1], [1, 1]]
        consts = [2, 3, 5]
        sol = gauss_jordan_solve(coeffs, consts)
        assert sol == pytest.approx([2.0, 3.0], abs=1e-9)

    def test_inconsistent_raises_value_error(self):
        with pytest.raises(ValueError, match="inconsistent"):
            gauss_jordan_solve([[1, 2], [2, 4]], [3, 5])
        with pytest.raises(ValueError, match="inconsistent"):
            gauss_jordan_solve([[1, 0], [0, 1], [1, 1]], [2, 3, 6])

    def test_infinite_solutions_raises_value_error(self):
        with pytest.raises(ValueError, match="infinitely many"):
            gauss_jordan_solve([[1, 2], [2, 4]], [3, 6])
        with pytest.raises(ValueError, match="infinitely many"):
            gauss_jordan_solve([[1, 2, 3], [4, 5, 6]], [7, 8])

    def test_invalid_constants_vector(self):
        with pytest.raises(ValueError):
            gauss_jordan_solve([[1, 0], [0, 1]], [1])
        with pytest.raises(TypeError):
            gauss_jordan_solve([[1, 0], [0, 1]], [])
        with pytest.raises(TypeError):
            gauss_jordan_solve([[1, 0], [0, 1]], [True, 1])
        with pytest.raises(ValueError):
            gauss_jordan_solve([[1, 0], [0, 1]], [1, float("nan")])


class TestGaussJordanElimination:
    def test_unique_status_and_metadata(self):
        res = gauss_jordan_elimination([[2, 1], [1, -1]], [5, 1])
        assert res["status"] == "unique"
        assert res["solution"] == pytest.approx([2.0, 1.0], abs=1e-9)
        assert res["pivot_columns"] == [0, 1]
        assert res["free_variables"] == []
        _assert_matrix_close(
            res["rref"], [[1.0, 0.0, 2.0], [0.0, 1.0, 1.0]]
        )

    def test_infinite_status_and_metadata(self):
        res = gauss_jordan_elimination([[1, 2, -1], [2, 4, -2]], [3, 6])
        assert res["status"] == "infinite"
        assert res["solution"] is None
        assert res["pivot_columns"] == [0]
        assert res["free_variables"] == [1, 2]
        _assert_matrix_close(
            res["rref"], [[1.0, 2.0, -1.0, 3.0], [0.0, 0.0, 0.0, 0.0]]
        )

    def test_inconsistent_status_and_metadata(self):
        res = gauss_jordan_elimination([[1, 2], [2, 4]], [3, 7])
        assert res["status"] == "inconsistent"
        assert res["solution"] is None
        assert res["pivot_columns"] == [0]
        assert res["free_variables"] == [1]
        _assert_matrix_close(
            res["rref"], [[1.0, 2.0, 0.0], [0.0, 0.0, 1.0]]
        )

    def test_zero_coefficient_matrix(self):
        res_inf = gauss_jordan_elimination([[0, 0], [0, 0]], [0, 0])
        assert res_inf["status"] == "infinite"
        assert res_inf["pivot_columns"] == []
        assert res_inf["free_variables"] == [0, 1]

        res_inc = gauss_jordan_elimination([[0, 0], [0, 0]], [0, 2])
        assert res_inc["status"] == "inconsistent"
        assert res_inc["pivot_columns"] == []
        assert res_inc["free_variables"] == [0, 1]
