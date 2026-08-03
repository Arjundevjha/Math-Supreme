import pytest
from Math.Geometry.Trigonometry.Trig_Functions.sine import factorial, sine


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    with pytest.raises(ValueError, match="Factorial not defined for negative numbers."):
        factorial(-1)

    with pytest.raises(ValueError, match="Factorial calculation limit exceeded"):
        factorial(1001)


def test_sine():
    pi = 3.141592653589793
    assert abs(sine(0) - 0.0) < 1e-5
    assert abs(sine(pi / 2) - 1.0) < 1e-5
    assert abs(sine(pi) - 0.0) < 1e-5
    assert abs(sine(3 * pi / 2) - (-1.0)) < 1e-5
    assert abs(sine(2 * pi) - 0.0) < 1e-5
