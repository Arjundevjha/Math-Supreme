import pytest
import sys
import os

# Ensure the root directory is in the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Calculus.Integration.NumIntegration import integrate_polynomial, format_polynomial_integration

def test_integrate_polynomial_basic():
    # ∫(3x^2 + 2x + 1)dx = x^3 + x^2 + x + C
    coeffs = [3, 2, 1]
    powers = [2, 1, 0]
    expected_coeffs = [1.0, 1.0, 1.0]
    expected_powers = [3, 2, 1]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_negative_powers():
    # ∫(x^-2)dx = -x^-1
    coeffs = [1]
    powers = [-2]
    expected_coeffs = [-1.0]
    expected_powers = [-1]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_fractional_powers():
    # ∫(x^0.5)dx = (2/3)x^1.5
    coeffs = [1]
    powers = [0.5]
    expected_coeffs = [1 / 1.5]
    expected_powers = [1.5]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_zero_coefficients():
    # ∫(0x^2)dx = 0
    coeffs = [0]
    powers = [2]
    expected_coeffs = [0.0]
    expected_powers = [3]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_format_polynomial_integration_basic():
    # x^3 + x^2 + x + C
    coeffs = [1.0, 1.0, 1.0]
    powers = [3, 2, 1]

    assert format_polynomial_integration(coeffs, powers) == "1.0x^3 + 1.0x^2 + 1.0x + C"

def test_format_polynomial_integration_zero_power():
    # 5
    coeffs = [5.0]
    powers = [0]

    assert format_polynomial_integration(coeffs, powers) == "5.0 + C"
