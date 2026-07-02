import os
import sys
import pytest

# Add root directory to path to allow "Math..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.factor_theorem import check_factor

def test_check_factor_true():
    # P(x) = x^2 - 4x + 4, check if (x - 2) is a factor
    # P(2) = 2^2 - 4*2 + 4 = 4 - 8 + 4 = 0 -> True
    assert check_factor([1, -4, 4], [2, 1, 0], 2) is True

def test_check_factor_false():
    # P(x) = x^2 - 4x + 4, check if (x - 3) is a factor
    # P(3) = 3^2 - 4*3 + 4 = 9 - 12 + 4 = 1 -> False
    assert check_factor([1, -4, 4], [2, 1, 0], 3) is False

def test_check_factor_linear():
    # P(x) = 2x - 6, check if (x - 3) is a factor
    # P(3) = 2*3 - 6 = 0 -> True
    assert check_factor([2, -6], [1, 0], 3) is True

def test_check_factor_linear_false():
    # P(x) = 2x - 6, check if (x - 2) is a factor
    # P(2) = 2*2 - 6 = -2 -> False
    assert check_factor([2, -6], [1, 0], 2) is False

def test_check_factor_cubic():
    # P(x) = x^3 - 6x^2 + 11x - 6
    # Factors are (x-1)(x-2)(x-3)
    coefficients = [1, -6, 11, -6]
    powers = [3, 2, 1, 0]
    assert check_factor(coefficients, powers, 1) is True
    assert check_factor(coefficients, powers, 2) is True
    assert check_factor(coefficients, powers, 3) is True
    assert check_factor(coefficients, powers, 4) is False

def test_check_factor_float():
    # P(x) = 2x^2 - x - 1
    # Factors are (2x+1)(x-1) => x = -0.5, x = 1
    coefficients = [2, -1, -1]
    powers = [2, 1, 0]
    assert check_factor(coefficients, powers, -0.5) is True
    assert check_factor(coefficients, powers, 1.0) is True
    assert check_factor(coefficients, powers, 0.5) is False
