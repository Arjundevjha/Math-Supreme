import pytest
from Math.Geometry.Trigonometry.Trig_Functions.cosecant import cosecant


def test_cosecant_standard_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # pi / 2: csc(pi/2) = 1 / sin(pi/2) = 1.0
    assert abs(cosecant(pi / 2) - 1.0) < tol

    # pi / 6: csc(pi/6) = 1 / sin(pi/6) = 1 / 0.5 = 2.0
    assert abs(cosecant(pi / 6) - 2.0) < tol

    # pi / 4: csc(pi/4) = 1 / sin(pi/4) = sqrt(2) approx 1.4142135623730951
    assert abs(cosecant(pi / 4) - 1.4142135623730951) < tol

    # pi / 3: csc(pi/3) = 2 / sqrt(3) approx 1.1547005383792515
    assert abs(cosecant(pi / 3) - 1.1547005383792515) < tol

    # 3pi / 2: csc(3pi/2) = -1.0
    assert abs(cosecant(3 * pi / 2) - (-1.0)) < tol


def test_cosecant_negative_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # -pi / 6: csc(-pi/6) = -2.0
    assert abs(cosecant(-pi / 6) - (-2.0)) < tol

    # -pi / 2: csc(-pi/2) = -1.0
    assert abs(cosecant(-pi / 2) - (-1.0)) < tol


def test_cosecant_undefined_value_error():
    # 0 radians evaluates sine_taylor to exactly 0.0, raising ValueError
    with pytest.raises(ValueError, match=r"Cosecant is undefined for angles where sin\(x\) = 0\."):
        cosecant(0)
