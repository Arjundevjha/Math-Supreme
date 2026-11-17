import pytest

from Math.Algebra.Linear_Algebra_Basics.matrix_method_solver import (
    matrix_method_solver,
)
from Math.Algebra.Systems_of_Equations.cramers_rule import cramers_rule
from Math.Algebra.Systems_of_Equations.gaussian_elimination import (
    gaussian_elimination,
)


SOLVERS = [cramers_rule, gaussian_elimination, matrix_method_solver]


def _assert_solution_close(actual, expected, tol=1e-9):
    assert len(actual) == len(expected)
    for act, exp in zip(actual, expected):
        assert act == pytest.approx(exp, abs=tol)


@pytest.mark.parametrize("solver", SOLVERS)
class TestLinearSystemSolvers:
    def test_1x1_system(self, solver):
        _assert_solution_close(solver([[4]], [12]), [3.0])

    def test_2x2_system(self, solver):
        a = [[2, 1], [1, 3]]
        b = [5, 10]
        _assert_solution_close(solver(a, b), [1.0, 3.0])

    def test_3x3_system(self, solver):
        a = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
        b = [8, -11, -3]
        _assert_solution_close(solver(a, b), [2.0, 3.0, -1.0])

    def test_4x4_system(self, solver):
        a = [
            [1, 1, 1, 1],
            [2, -1, 1, 0],
            [1, 2, -1, 3],
            [3, 0, 2, -1],
        ]
        b = [10, 3, 14, 5]
        _assert_solution_close(solver(a, b), [1.0, 2.0, 3.0, 4.0])

    def test_partial_pivoting_zero_diagonal(self, solver):
        a = [[0, 2, 1], [1, -2, -3], [-1, 1, 2]]
        b = [-8, 0, 3]
        _assert_solution_close(solver(a, b), [-4.0, -5.0, 2.0])

    def test_float_and_tuple_inputs(self, solver):
        a = ((1.5, -0.5), (0.5, 2.5))
        b = (2.0, 6.0)
        _assert_solution_close(solver(a, b), [2.0, 2.0])

    def test_inputs_not_mutated(self, solver):
        a = [[2, 1], [1, 3]]
        b = [5, 10]
        solver(a, b)
        assert a == [[2, 1], [1, 3]]
        assert b == [5, 10]

    def test_singular_system_raises(self, solver):
        with pytest.raises(ValueError):
            solver([[1, 2], [2, 4]], [3, 6])
        with pytest.raises(ValueError):
            solver([[1, 2], [2, 4]], [3, 7])

    def test_non_square_matrix_raises(self, solver):
        with pytest.raises(ValueError):
            solver([[1, 2, 3], [4, 5, 6]], [7, 8])

    def test_dimension_mismatch_raises(self, solver):
        with pytest.raises(ValueError):
            solver([[1, 0], [0, 1]], [1, 2, 3])

    def test_invalid_inputs_raise(self, solver):
        with pytest.raises(TypeError):
            solver([], [1])
        with pytest.raises(TypeError):
            solver([[1, 0], [0, 1]], [])
        with pytest.raises(TypeError):
            solver([[True, 0], [0, 1]], [1, 2])
        with pytest.raises(TypeError):
            solver([[1, 0], [0, 1]], [1, "2"])
        with pytest.raises(ValueError):
            solver([[float("inf"), 0], [0, 1]], [1, 2])
        with pytest.raises(ValueError):
            solver([[1, 0], [0, 1]], [1, float("nan")])
        with pytest.raises(ValueError):
            solver([[1, 2], [3]], [1, 2])
