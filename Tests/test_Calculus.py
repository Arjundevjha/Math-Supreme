import pytest
from Math.Calculus.Differentiation.chain_rule import compute_polynomial_derivative

class TestComputePolynomialDerivative:
    def test_basic_polynomial(self):
        # f(x) = 3x^2 + 2x^1
        # f'(x) = 6x^1 + 2x^0
        coeffs = [3, 2]
        powers = [2, 1]
        expected_coeffs = [6, 2]
        expected_powers = [1, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_constant_term(self):
        # f(x) = 5x^0
        # f'(x) = 0
        coeffs = [5]
        powers = [0]
        expected_coeffs = []
        expected_powers = []
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_mixed_terms_with_constant(self):
        # f(x) = 4x^3 + 2x^0 + x^1
        # f'(x) = 12x^2 + 1x^0
        coeffs = [4, 2, 1]
        powers = [3, 0, 1]
        expected_coeffs = [12, 1]
        expected_powers = [2, 0]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_negative_powers(self):
        # f(x) = 2x^-2
        # f'(x) = -4x^-3
        coeffs = [2]
        powers = [-2]
        expected_coeffs = [-4]
        expected_powers = [-3]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_fractional_powers(self):
        # f(x) = 4x^0.5
        # f'(x) = 2.0x^-0.5
        coeffs = [4]
        powers = [0.5]
        expected_coeffs = [2.0]
        expected_powers = [-0.5]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_float_coefficients(self):
        # f(x) = 1.5x^2
        # f'(x) = 3.0x^1
        coeffs = [1.5]
        powers = [2]
        expected_coeffs = [3.0]
        expected_powers = [1]
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)

    def test_empty_polynomial(self):
        # f(x) = 0
        # f'(x) = 0
        coeffs = []
        powers = []
        expected_coeffs = []
        expected_powers = []
        assert compute_polynomial_derivative(coeffs, powers) == (expected_coeffs, expected_powers)
