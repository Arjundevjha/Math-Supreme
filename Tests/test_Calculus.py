import math

from Math.Algebra.Polynomials.polynomial import format_polynomial
from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative
from Math.Calculus.Differentiation.product_rule import product_rule_derivative
from Math.Calculus.Differentiation.quotient_rule import quotient_rule_derivative
from Math.Calculus.Differentiation.second_derivatives import second_derivative
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)
from Math.Calculus.Differentiation.utils import (
    compute_polynomial_derivative,
    compute_polynomial_derivative_str,
)
from Math.Calculus.Integration.TrigIntegration import integrate_cos


def test_differentiation_pipeline_dense_lists():
    poly = [1, 2, 3, 4]  # 1 + 2x + 3x^2 + 4x^3
    d1 = differentiate_polynomial(poly)
    d2 = second_derivative(poly)
    assert d1 == [2, 6, 12]
    assert d2 == [6, 24]
    assert compute_polynomial_derivative(poly) == d1
    assert compute_polynomial_derivative_str(poly) == "2 + 6x + 12x^2"
    assert format_polynomial(d2) == "6 + 24x"


def test_rules_return_dense_lists():
    assert product_rule_derivative([1, 1], [1, -1]) == [0, -2]
    assert chain_rule_derivative([1, 1], 2) == [2, 2]
    num, den = quotient_rule_derivative([0, 1], [1, 1])
    assert num == [1]
    assert den == [1, 2, 1]


def test_trig_integration_cos():
    assert math.isclose(integrate_cos(-math.pi, 0), 0.0, abs_tol=1e-9)
    assert math.isclose(integrate_cos(math.pi / 2, 0), -1.0, rel_tol=1e-5)
    expected = math.sin(math.pi / 3) - math.sin(math.pi / 6)
    assert math.isclose(
        integrate_cos(math.pi / 6, math.pi / 3), expected, rel_tol=1e-5
    )
