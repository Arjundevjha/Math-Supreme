import pytest
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.utils.math_utils import factorial

PI = 3.14159265358979323846


def test_sine_zero():
    """Test sine of 0 is 0."""
    assert abs(sine(0) - 0.0) < 1e-9


def test_sine_pi_over_two():
    """Test sine of pi/2 is 1."""
    assert abs(sine(PI / 2) - 1.0) < 1e-9


def test_sine_pi():
    """Test sine of pi is 0."""
    assert abs(sine(PI) - 0.0) < 1e-9


def test_sine_negative_pi_over_two():
    """Test sine of -pi/2 is -1."""
    assert abs(sine(-PI / 2) - (-1.0)) < 1e-9


def test_factorial_negative():
    """Test factorial with a negative number raises ValueError."""
    with pytest.raises(
        ValueError, match=r"Factorial (is )?not defined for negative numbers\."
    ):
        factorial(-1)


def test_factorial_limit_exceeded():
    """Test factorial exceeding limit raises ValueError."""
    with pytest.raises(
        ValueError,
        match=r"Factorial calculation limit exceeded \(maximum allowed is 1000\).",
    ):
        factorial(1001)
