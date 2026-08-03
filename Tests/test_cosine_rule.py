import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
math_dir = os.path.join(project_root, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

import pytest
from Math.Geometry.Trigonometry.Formulas.cosine_rule import (
    sqrt_newton, cosine_rule_for_side, cosine_rule_for_angle, factorial, arccos_series, cosine_taylor
)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Math.Geometry.Trigonometry.Formulas.cosine_rule import sqrt_newton, cosine_rule_for_side, cosine_rule_for_angle, factorial, arccos_series, cosine_taylor

def test_sqrt_newton_precision_zero():
    with pytest.raises(ValueError, match="Precision must be strictly greater than zero."):
        sqrt_newton(5, 0)

def test_sqrt_newton_precision_negative():
    with pytest.raises(ValueError, match="Precision must be strictly greater than zero."):
        sqrt_newton(5, -0.01)

def test_sqrt_newton_valid():
    assert abs(sqrt_newton(4) - 2) < 0.000001
    assert abs(sqrt_newton(2, 1e-10) - 1.4142135623) < 1e-9

def test_cosine_rule_for_side():
    # Right-angled triangle: sides 3, 4, angle 90 degrees (pi/2)
    # Expected side 5
    pi = 3.141592653589793
    c = cosine_rule_for_side(3, 4, pi / 2)
    assert abs(c - 5) < 0.00001

def test_cosine_rule_for_angle():
    # Triangle with sides 3, 4, 5. Angle opposite 5 is 90 degrees (pi/2)
    pi = 3.141592653589793
    angle = cosine_rule_for_angle(3, 4, 5)
    assert abs(angle - pi / 2) < 0.00001

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers."):
        factorial(-1)

def test_sqrt_newton_negative():
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number."):
        sqrt_newton(-4)

def test_sqrt_newton_zero():
    assert sqrt_newton(0) == 0

def test_sqrt_newton_max_iterations():
    import unittest.mock
    # To hit max iterations, we can patch the max_iterations variable if possible,
    # but we can't patch a local variable easily.
    # What if we pass an extreme case where precision is smaller than float representation?
    # e.g., precision = 1e-323
    # Actually, a simpler way is to mock 'abs' to always return a number > precision
    with unittest.mock.patch('builtins.abs', return_value=1.0):
        with pytest.raises(RuntimeError, match="Maximum iterations reached without converging to the specified precision."):
            sqrt_newton(4, 0.5)

def test_cosine_taylor():
    pi = 3.141592653589793
    assert abs(cosine_taylor(0) - 1.0) < 1e-5
    assert abs(cosine_taylor(pi) - (-1.0)) < 1e-5
    assert abs(cosine_taylor(pi/2) - 0.0) < 1e-5

def test_arccos_series():
    with pytest.raises(ValueError, match="arccos is only defined for values between -1 and 1."):
        arccos_series(1.5)
    with pytest.raises(ValueError, match="arccos is only defined for values between -1 and 1."):
        arccos_series(-2)

    assert arccos_series(1) == 0
    pi = 3.14159265358979323846
    assert arccos_series(-1) == pi

    # Test valid value
    res = arccos_series(0)
    assert abs(res - pi/2) < 1e-5

def test_cosine_rule_for_side_invalid():
    with pytest.raises(ValueError, match="Side lengths must be positive."):
        cosine_rule_for_side(0, 4, 1)
    with pytest.raises(ValueError, match="Side lengths must be positive."):
        cosine_rule_for_side(3, -1, 1)

def test_cosine_rule_for_angle_invalid():
    with pytest.raises(ValueError, match="All side lengths must be positive."):
        cosine_rule_for_angle(0, 4, 5)
    with pytest.raises(ValueError, match="All side lengths must be positive."):
        cosine_rule_for_angle(3, -1, 5)
    with pytest.raises(ValueError, match="All side lengths must be positive."):
        cosine_rule_for_angle(3, 4, 0)

    with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
        cosine_rule_for_angle(1, 2, 4)
    with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
        cosine_rule_for_angle(10, 2, 4)
    with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
        cosine_rule_for_angle(3, 10, 4)

def test_cosine_taylor():
    pi = 3.141592653589793
    assert abs(cosine_taylor(0) - 1.0) < 1e-5
    assert abs(cosine_taylor(pi / 2) - 0.0) < 1e-5
    assert abs(cosine_taylor(pi) - (-1.0)) < 1e-5
    assert abs(cosine_taylor(pi / 3) - 0.5) < 1e-5
    assert abs(cosine_taylor(pi / 4) - 0.70710678118) < 1e-5
