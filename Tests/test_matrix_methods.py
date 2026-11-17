"""Unit tests for Jacobi, Gauss-Seidel, and Power Iteration methods."""

import pytest

from Math.Linear_Algebra.Vectors.dot_product import dot_product
from Math.Linear_Algebra.Vectors.magnitude import vector_magnitude
from Math.Numerical_Methods.Matrix_Methods.gauss_seidel import gauss_seidel
from Math.Numerical_Methods.Matrix_Methods.jacobi_iteration import (
    jacobi_iteration,
)
from Math.Numerical_Methods.Matrix_Methods.power_iteration_eigenvalues import (
    power_iteration,
)


def _assert_vec_close(actual, expected, tol=1e-7):
    assert len(actual) == len(expected)
    for a_val, e_val in zip(actual, expected):
        assert a_val == pytest.approx(e_val, abs=tol)


class TestJacobiIteration:
    def test_2x2_system(self):
        a = [[4, 1], [1, 3]]
        b = [1, 2]
        sol = jacobi_iteration(a, b)
        _assert_vec_close(sol, [1.0 / 11.0, 7.0 / 11.0])

    def test_3x3_diagonally_dominant(self):
        a = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
        b = [6, 22, -10]
        sol = jacobi_iteration(a, b)
        _assert_vec_close(sol, [1.0, 2.0, -1.0])
        for row, rhs in zip(a, b):
            assert dot_product(row, sol) == pytest.approx(rhs, abs=1e-8)

    def test_1x1_and_custom_x0(self):
        assert jacobi_iteration([[5]], [15]) == pytest.approx([3.0])
        sol = jacobi_iteration([[4, 1], [1, 3]], [1, 2], x0=[0.1, 0.6])
        _assert_vec_close(sol, [1.0 / 11.0, 7.0 / 11.0])

    def test_error_cases(self):
        with pytest.raises(ValueError, match="Zero diagonal"):
            jacobi_iteration([[0, 1], [1, 2]], [1, 2])
        with pytest.raises(ValueError, match="square"):
            jacobi_iteration([[1, 2, 3], [4, 5, 6]], [1, 2])
        with pytest.raises(ValueError, match="dimension"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2, 3])
        with pytest.raises(ValueError, match="x0"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2], x0=[1])
        with pytest.raises(ValueError, match="did not converge"):
            jacobi_iteration(
                [[1, 5], [5, 1]], [6, 6], x0=[0, 1], max_iter=5
            )
        with pytest.raises(ValueError, match="tol"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2], tol=0)
        with pytest.raises(TypeError, match="tol"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2], tol=True)
        with pytest.raises(ValueError, match="max_iter"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2], max_iter=0)
        with pytest.raises(TypeError, match="max_iter"):
            jacobi_iteration([[2, 0], [0, 2]], [1, 2], max_iter=1.5)


class TestGaussSeidel:
    def test_2x2_and_3x3_systems(self):
        sol_2 = gauss_seidel([[4, 1], [1, 3]], [1, 2])
        _assert_vec_close(sol_2, [1.0 / 11.0, 7.0 / 11.0])

        a = [[10, -1, 2], [-1, 11, -1], [2, -1, 10]]
        b = [6, 22, -10]
        sol_3 = gauss_seidel(a, b)
        _assert_vec_close(sol_3, [1.0, 2.0, -1.0])

    def test_symmetric_positive_definite(self):
        a = [[4, 1, 1], [1, 3, 1], [1, 1, 2]]
        b = [6, 5, 4]
        sol = gauss_seidel(a, b, x0=[0, 0, 0])
        _assert_vec_close(sol, [1.0, 1.0, 1.0])

    def test_error_cases(self):
        with pytest.raises(ValueError, match="Zero diagonal"):
            gauss_seidel([[2, 1], [1, 0]], [1, 2])
        with pytest.raises(ValueError, match="square"):
            gauss_seidel([[1, 2], [3, 4], [5, 6]], [1, 2, 3])
        with pytest.raises(ValueError, match="did not converge"):
            gauss_seidel(
                [[1, 5], [5, 1]], [6, 6], x0=[0, 0], max_iter=5
            )


class TestPowerIteration:
    def test_diagonal_and_symmetric_matrices(self):
        eig, vec = power_iteration([[3, 0], [0, 1]])
        assert eig == pytest.approx(3.0, abs=1e-8)
        assert vector_magnitude(vec) == pytest.approx(1.0, abs=1e-8)
        _assert_vec_close(vec, [1.0, 0.0])

        eig2, vec2 = power_iteration([[2, 1], [1, 2]])
        assert eig2 == pytest.approx(3.0, abs=1e-8)
        assert vector_magnitude(vec2) == pytest.approx(1.0, abs=1e-8)
        expected_v = [1.0 / (2.0 ** 0.5), 1.0 / (2.0 ** 0.5)]
        _assert_vec_close(vec2, expected_v)

    def test_negative_dominant_eigenvalue(self):
        a = [[-4, 0], [0, 2]]
        eig, vec = power_iteration(a, v0=[1, 1])
        assert eig == pytest.approx(-4.0, abs=1e-8)
        assert abs(vec[0]) == pytest.approx(1.0, abs=1e-8)
        assert vec[1] == pytest.approx(0.0, abs=1e-8)

    def test_3x3_eigenpair(self):
        a = [[2, 0, 0], [0, 3, 4], [0, 4, 9]]
        eig, vec = power_iteration(a)
        av = [dot_product(row, vec) for row in a]
        scaled_v = [eig * val for val in vec]
        _assert_vec_close(av, scaled_v, tol=1e-7)
        assert eig == pytest.approx(11.0, abs=1e-7)

    def test_zero_matrix(self):
        eig, vec = power_iteration([[0, 0], [0, 0]], v0=[3, 4])
        assert eig == 0.0
        _assert_vec_close(vec, [0.6, 0.8])

    def test_error_cases(self):
        with pytest.raises(ValueError, match="square"):
            power_iteration([[1, 2, 3], [4, 5, 6]])
        with pytest.raises(ValueError, match="zero vector"):
            power_iteration([[2, 0], [0, 1]], v0=[0, 0])
        with pytest.raises(ValueError, match="v0"):
            power_iteration([[2, 0], [0, 1]], v0=[1, 2, 3])
        with pytest.raises(ValueError, match="did not converge"):
            power_iteration([[0, 1], [1, 0]], v0=[1, 0], max_iter=10)
