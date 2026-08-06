import pytest

from Math.Geometry.Trigonometry.Trig_Functions.sine import sine

def test_sine_standard_angles():
    pi = 3.141592653589793

    # Tolerance for floating point comparison
    tol = 1e-9

    # 0
    assert abs(sine(0) - 0.0) < tol

    # pi / 6
    assert abs(sine(pi / 6) - 0.5) < tol

    # pi / 4
    assert abs(sine(pi / 4) - 0.7071067811865476) < tol

    # pi / 3
    assert abs(sine(pi / 3) - 0.8660254037844386) < tol

    # pi / 2
    assert abs(sine(pi / 2) - 1.0) < tol

    # pi
    assert abs(sine(pi) - 0.0) < tol

    # 3pi / 2
    assert abs(sine(3 * pi / 2) - (-1.0)) < tol

    # 2pi
    assert abs(sine(2 * pi) - 0.0) < tol

def test_sine_negative_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # -pi / 6
    assert abs(sine(-pi / 6) - (-0.5)) < tol

    # -pi / 2
    assert abs(sine(-pi / 2) - (-1.0)) < tol

    # -pi
    assert abs(sine(-pi) - 0.0) < tol

def test_sine_large_angles():
    pi = 3.141592653589793
    tol = 1e-5 # Taylor series might diverge slightly for large inputs if not wrapped to [-pi, pi]

    # The sine function in sine.py uses a fixed number of terms (up to 100),
    # so for very large angles it might be less precise.
    # 3pi
    assert abs(sine(3 * pi) - 0.0) < tol

    # 4pi
    assert abs(sine(4 * pi) - 0.0) < tol
