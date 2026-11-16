import pytest

from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)
from Math.Calculus.Integration.NumIntegration import (
    format_polynomial_integration,
    integrate_polynomial,
)


def test_integrate_polynomial_basic():
    # 1 + 2x + 3x^2 = [1, 2, 3] -> [0.0, 1.0, 1.0, 1.0]
    assert integrate_polynomial([1, 2, 3]) == [0.0, 1.0, 1.0, 1.0]


def test_integrate_polynomial_roundtrip_with_differentiation():
    poly = [4, -6, 9, 12]
    antideriv = integrate_polynomial(poly)
    assert differentiate_polynomial(antideriv) == [4.0, -6.0, 9.0, 12.0]


def test_integrate_polynomial_zero_and_empty():
    assert integrate_polynomial([]) == []
    assert integrate_polynomial([0, 0, 0]) == []


def test_integrate_polynomial_floats_and_negatives():
    # -2 + 3x = [-2, 3] -> [0.0, -2.0, 1.5]
    assert integrate_polynomial([-2, 3]) == [0.0, -2.0, 1.5]


def test_integrate_polynomial_trailing_zeros_trimmed():
    assert integrate_polynomial([2, 0, 0]) == [0.0, 2.0]


def test_format_polynomial_integration_basic():
    assert (
        format_polynomial_integration([0.0, 1.0, 1.0, 1.0])
        == "1.0x + 1.0x^2 + 1.0x^3 + C"
    )


def test_format_polynomial_integration_constant_only():
    assert format_polynomial_integration([5.0]) == "5.0 + C"


def test_format_polynomial_integration_empty_and_zero():
    assert format_polynomial_integration([]) == "C"
    assert format_polynomial_integration([0, 0]) == "C"


def test_format_polynomial_integration_single_term_linear():
    assert format_polynomial_integration([0, 2.5]) == "2.5x + C"
