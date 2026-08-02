import pytest
import math
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
    assert math.isclose(sine(0), 0.0, abs_tol=1e-5)
    assert math.isclose(sine(math.pi / 2), 1.0, abs_tol=1e-5)
    assert math.isclose(sine(math.pi), 0.0, abs_tol=1e-5)
    assert math.isclose(sine(3 * math.pi / 2), -1.0, abs_tol=1e-5)
    assert math.isclose(sine(2 * math.pi), 0.0, abs_tol=1e-5)
