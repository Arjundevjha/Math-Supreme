import pytest
from Math.Calculus.Integration.NumIntegration import integrate_polynomial, format_polynomial_integration

def test_integrate_polynomial_basic():
    coeffs = [3, 2, 1]
    powers = [2, 1, 0]
    expected_coeffs = [1.0, 1.0, 1.0]
    expected_powers = [3, 2, 1]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_negative_powers():
    coeffs = [4, 5]
    powers = [-2, -3]
    expected_coeffs = [-4.0, -2.5]
    expected_powers = [-1, -2]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_fractional_powers():
    coeffs = [1.5, 2.5]
    powers = [0.5, 1.5]
    expected_coeffs = [1.0, 1.0]
    expected_powers = [1.5, 2.5]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_zero_coefficients():
    coeffs = [0, 0]
    powers = [2, 1]
    expected_coeffs = [0.0, 0.0]
    expected_powers = [3, 2]

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_empty():
    coeffs = []
    powers = []
    expected_coeffs = []
    expected_powers = []

    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_integrate_polynomial_power_minus_one():
    # ∫(x^-1)dx raises ValueError since ln|x| is unsupported
    coeffs = [1]
    powers = [-1]

    with pytest.raises(ValueError, match=r"Integration of x\^-1 results in ln\|x\|, which is not supported by this polynomial integration function."):
        integrate_polynomial(coeffs, powers)

    assert integrate_polynomial([], []) == ([], [])

def test_integrate_polynomial_mixed_terms():
    coeffs = [3, -2, 1.5, 0]
    powers = [2, -3, 0.5, 1]
    expected_coeffs = [1.0, 1.0, 1.0, 0.0]
    expected_powers = [3, -2, 1.5, 2]
    assert integrate_polynomial(coeffs, powers) == (expected_coeffs, expected_powers)

def test_format_polynomial_integration_basic():
    coeffs = [1.0, 1.0, 1.0]
    powers = [3, 2, 1]

    assert format_polynomial_integration(coeffs, powers) == "1.0x^3 + 1.0x^2 + 1.0x + C"

def test_format_polynomial_integration_zero_power():
    coeffs = [5.0]
    powers = [0]

    assert format_polynomial_integration(coeffs, powers) == "5.0 + C"

def test_format_polynomial_integration_multiple_terms():
    result = format_polynomial_integration([2.0, 3.5, 1.0], [2.0, 1.0, 0.0])

    expected = "2.0x^2 + 3.5x + 1.0 + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_single_term_power_zero():
    result = format_polynomial_integration([5.0], [0.0])

    expected = "5.0 + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_single_term_power_one():
    result = format_polynomial_integration([2.5], [1.0])

    expected = "2.5x + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_single_term_power_gt_one():
    result = format_polynomial_integration([4.0], [3.0])

    expected = "4.0x^3 + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_empty():
    result = format_polynomial_integration([], [])
    assert result == " + C"

def test_format_polynomial_integration_negative_coefficients():
    result = format_polynomial_integration([-2.0, -3.5], [2.0, 1.0])

    expected = "-2.0x^2 + -3.5x + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_negative_powers():
    result = format_polynomial_integration([4.0, 5.0], [-2.0, -3.0])

    expected = "4.0x^-2 + 5.0x^-3 + C"
    for term in expected.split(" + "):
        assert term in result

def test_format_polynomial_integration_zero_coefficients():
    result = format_polynomial_integration([0.0, 0.0], [2.0, 1.0])

    expected = "0.0x^2 + 0.0x + C"
    for term in expected.split(" + "):
        assert term in result
