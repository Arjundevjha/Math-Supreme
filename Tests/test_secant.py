import pytest
from unittest.mock import patch
from Math.Geometry.Trigonometry.Trig_Functions.secant import secant


def test_secant_standard_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # sec(0) = 1 / cos(0) = 1
    assert abs(secant(0) - 1.0) < tol

    # sec(pi / 3) = 1 / cos(pi / 3) = 1 / 0.5 = 2.0
    assert abs(secant(pi / 3) - 2.0) < tol

    # sec(pi / 4) = 1 / cos(pi / 4) = 1 / (1/sqrt(2)) = sqrt(2) ~ 1.4142135623730951
    assert abs(secant(pi / 4) - 1.4142135623730951) < tol

    # sec(pi) = 1 / cos(pi) = 1 / (-1) = -1.0
    assert abs(secant(pi) - (-1.0)) < tol


def test_secant_negative_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # sec(-pi / 3) = 1 / cos(-pi / 3) = 2.0
    assert abs(secant(-pi / 3) - 2.0) < tol

    # sec(-pi) = 1 / cos(-pi) = -1.0
    assert abs(secant(-pi) - (-1.0)) < tol


def test_secant_undefined_value_error():
    with patch("Math.Geometry.Trigonometry.Trig_Functions.secant.cosine_taylor", return_value=0.0):
        with pytest.raises(ValueError, match=r"Secant is undefined for angles where cos\(x\) = 0\."):
            secant(0)
