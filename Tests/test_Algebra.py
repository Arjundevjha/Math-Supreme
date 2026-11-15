import math
import pytest

from Math.Algebra.Polynomials.polynomial import (
    evaluate_polynomial,
    format_polynomial,
)
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn
from Math.Algebra.Polynomials.factor_theorem import check_factor


def test_format_polynomial_basic():
    result = format_polynomial([4, 3, 2])
    terms = [t.strip() for t in result.split("+")]
    assert "4" in terms
    assert "3x" in terms
    assert "2x^2" in terms


def test_format_polynomial_negative_and_zero():
    result = format_polynomial([0, 0, 0, -1])
    assert result == "-1x^3"


def test_format_polynomial_empty():
    assert format_polynomial([]) == "0"


def test_format_polynomial_floats():
    result = format_polynomial([3.1, -2.5, 1.5])
    terms = [t.strip() for t in result.split("+")]
    assert "3.1" in terms
    assert "-2.5x" in terms
    assert "1.5x^2" in terms


def test_format_polynomial_single_term():
    assert format_polynomial([0, 0, 0, 5]) == "5x^3"


def test_linear_eqn_positive_slope():
    assert linear_eqn(1, 2, 3, 6) == "y = 2.0x + 0.0"


def test_linear_eqn_negative_slope():
    assert linear_eqn(0, 5, 5, 0) == "y = -1.0x + 5.0"


def test_linear_eqn_zero_slope():
    assert linear_eqn(1, 4, 5, 4) == "y = 0.0x + 4.0"


def test_linear_eqn_floats():
    assert linear_eqn(1.5, 2.5, 3.5, 6.5) == "y = 2.0x + -0.5"


def test_linear_eqn_vertical_line():
    with pytest.raises(
        ValueError, match="The x-coordinates cannot be the same \\(vertical line\\)."
    ):
        linear_eqn(2, 3, 2, 7)


def test_linear_eqn_identical_points():
    with pytest.raises(
        ValueError, match="The x-coordinates cannot be the same \\(vertical line\\)."
    ):
        linear_eqn(2, 3, 2, 3)


def test_linear_eqn_origin():
    assert linear_eqn(0, 0, 2, 4) == "y = 2.0x + 0.0"


def test_linear_eqn_all_negative():
    assert linear_eqn(-2, -3, -4, -7) == "y = 2.0x + 1.0"


def test_linear_eqn_fractional_slope():
    m = (2.0 - 1.0) / (4.0 - 1.0)
    b = 1.0 - m * 1.0
    assert linear_eqn(1, 1, 4, 2) == f"y = {m}x + {b}"


def test_linear_eqn_large_coordinates():
    assert linear_eqn(1000000, 2000000, 3000000, 6000000) == "y = 2.0x + 0.0"


class TestEvaluatePolynomial:
    def test_evaluate_polynomial_complex_floats(self):
        assert math.isclose(evaluate_polynomial([0, 0.2, 0.1], 0.1), 0.021)

    def test_evaluate_polynomial_basic(self):
        assert math.isclose(
            evaluate_polynomial([1, 2, 1], 2), 9, rel_tol=1e-9
        )

    def test_evaluate_polynomial_zero_x(self):
        assert math.isclose(
            evaluate_polynomial([1, 2, 1], 0), 1, rel_tol=1e-9
        )

    def test_evaluate_polynomial_negative_x(self):
        assert math.isclose(
            evaluate_polynomial([1, 2, 1], -1), 0, abs_tol=1e-9
        )

    def test_evaluate_polynomial_float_coefficients(self):
        assert math.isclose(
            evaluate_polynomial([0.5, 0, 1.5], 2.0), 6.5, rel_tol=1e-9
        )

    def test_evaluate_polynomial_empty(self):
        assert math.isclose(evaluate_polynomial([], 5), 0, abs_tol=1e-9)

    def test_evaluate_polynomial_precision_variance(self):
        assert math.isclose(
            evaluate_polynomial([0.2, 0.1], 1), 0.3, rel_tol=1e-9
        )

    def test_evaluate_polynomial_zero_coefficient(self):
        assert math.isclose(
            evaluate_polynomial([0, 0, 2, 0], 3), 18, rel_tol=1e-9
        )

    def test_evaluate_polynomial_large_inputs(self):
        poly = [0] * 10 + [1]
        assert math.isclose(
            evaluate_polynomial(poly, 10), 10**10, rel_tol=1e-9
        )

    def test_evaluate_polynomial_zero_to_zero_power(self):
        assert evaluate_polynomial([5], 0) == 5

    def test_evaluate_polynomial_all_zero_coeffs(self):
        assert evaluate_polynomial([0, 0, 0], 5) == 0

    def test_evaluate_polynomial_sparse_terms(self):
        # 3x^5 - 2 = [-2, 0, 0, 0, 0, 3] at x=2 -> 94
        assert evaluate_polynomial([-2, 0, 0, 0, 0, 3], 2) == 94

    def test_evaluate_polynomial_large_power(self):
        poly = [0] * 1001 + [1]
        assert evaluate_polynomial(poly, 2) == 2**1001


class TestCheckFactorAlgebra:
    def test_check_factor_cubic(self):
        poly = [-6, 11, -6, 1]
        assert check_factor(poly, 1) is True
        assert check_factor(poly, 2) is True
        assert check_factor(poly, 3) is True
        assert check_factor(poly, 4) is False

    def test_check_factor_float(self):
        poly = [-1, -1, 2]
        assert check_factor(poly, -0.5) is True
        assert check_factor(poly, 1.0) is True
        assert check_factor(poly, 0.5) is False

    def test_check_factor_irrational(self):
        assert check_factor([-2, 0, 1], math.sqrt(2)) is True
        assert check_factor([-2, 0, 1], -math.sqrt(2)) is True

    def test_check_factor_empty_and_zero(self):
        assert check_factor([], 5) is True
        assert check_factor([0, 0, 0], 100) is True
