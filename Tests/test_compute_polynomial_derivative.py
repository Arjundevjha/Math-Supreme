import pytest
from Math.Calculus.Differentiation.utils import compute_polynomial_derivative


def test_basic_polynomial():
    # d/dx(3x^2 + 2x^1) = 6x^1 + 2x^0
    coeffs = [3, 2]
    powers = [2, 1]
    expected_coeffs = [6, 2]
    expected_powers = [1, 0]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_zero_power_constant_term():
    # d/dx(5x^0) = 0 (constant terms with power 0 are ignored)
    coeffs = [5]
    powers = [0]
    assert compute_polynomial_derivative(coeffs, powers) == ([], [])


def test_mixed_terms_including_zero_power():
    # d/dx(4x^3 + 7x^0 + 2x^1) = 12x^2 + 2x^0
    coeffs = [4, 7, 2]
    powers = [3, 0, 1]
    expected_coeffs = [12, 2]
    expected_powers = [2, 0]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_high_powers():
    # d/dx(5x^1000 + 2x^1000000) = 5000x^999 + 2000000x^999999
    coeffs = [5, 2]
    powers = [1000, 1000000]
    expected_coeffs = [5000, 2000000]
    expected_powers = [999, 999999]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_empty_inputs():
    # Empty inputs should return empty lists
    assert compute_polynomial_derivative([], []) == ([], [])


def test_negative_powers():
    # d/dx(3x^-2 - 4x^-1) = -6x^-3 + 4x^-2
    coeffs = [3, -4]
    powers = [-2, -1]
    expected_coeffs = [-6, 4]
    expected_powers = [-3, -2]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_fractional_and_float_inputs():
    # d/dx(1.5x^2.5 + 4.0x^0.5) = 3.75x^1.5 + 2.0x^-0.5
    coeffs = [1.5, 4.0]
    powers = [2.5, 0.5]
    expected_coeffs = [3.75, 2.0]
    expected_powers = [1.5, -0.5]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_zero_coefficients():
    # d/dx(0x^5 + 0x^2) = 0x^4 + 0x^1
    coeffs = [0, 0]
    powers = [5, 2]
    expected_coeffs = [0, 0]
    expected_powers = [4, 1]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)


def test_mismatched_input_lengths():
    # zip() stops at the shorter list length
    # coeffs longer than powers
    coeffs1 = [3, 2, 5]
    powers1 = [2, 1]
    assert compute_polynomial_derivative(coeffs1, powers1) == ([6, 2], [1, 0])

    # powers longer than coeffs
    coeffs2 = [3, 2]
    powers2 = [2, 1, 0]
    assert compute_polynomial_derivative(coeffs2, powers2) == ([6, 2], [1, 0])


def test_negative_coefficients():
    # d/dx(-3x^3 - 2x^2) = -9x^2 - 4x^1
    coeffs = [-3, -2]
    powers = [3, 2]
    expected_coeffs = [-9, -4]
    expected_powers = [2, 1]
    assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)
