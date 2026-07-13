import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from Math.Geometry.Trigonometry.Formulas.cosine_rule import sqrt_newton, cosine_rule_for_side, cosine_rule_for_angle

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
