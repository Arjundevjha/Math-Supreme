import pytest

from Math.Calculus.Differentiation.second_derivatives import second_derivative


def test_second_derivative_basic():
    # 1 + 2x + 3x^2 + 4x^3 -> f'(x) = 2 + 6x + 12x^2 -> f''(x) = 6 + 24x
    assert second_derivative([1, 2, 3, 4]) == [6, 24]


def test_second_derivative_empty_and_low_degree():
    assert second_derivative([]) == []
    assert second_derivative([5]) == []
    assert second_derivative([5, 3]) == []


def test_second_derivative_floats_and_negatives():
    # -2.5x^3 -> -15.0x
    assert second_derivative([0, 0, 0, -2.5]) == [0, -15.0]


def test_second_derivative_zero_coeffs():
    assert second_derivative([0, 0, 0, 0]) == []


def test_second_derivative_validation():
    with pytest.raises(TypeError):
        second_derivative("invalid")
    with pytest.raises(TypeError):
        second_derivative([True, 1, 2])
    with pytest.raises(ValueError):
        second_derivative([1, 2, float("inf")])
