import pytest
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine, factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

    with pytest.raises(ValueError, match="Factorial not defined for negative numbers."):
        factorial(-1)

    with pytest.raises(ValueError, match="Factorial calculation limit exceeded"):
        factorial(1001)

def test_sine_known_values():
    pi = 3.141592653589793
    tolerance = 1e-5

    # Test known values
    assert abs(sine(0) - 0.0) < tolerance
    assert abs(sine(pi / 6) - 0.5) < tolerance
    assert abs(sine(pi / 4) - 0.7071067811865476) < tolerance
    assert abs(sine(pi / 3) - 0.8660254037844386) < tolerance
    assert abs(sine(pi / 2) - 1.0) < tolerance
    assert abs(sine(pi) - 0.0) < tolerance

def test_sine_negative_angles():
    pi = 3.141592653589793
    tolerance = 1e-5

    assert abs(sine(-pi / 2) - (-1.0)) < tolerance
    assert abs(sine(-pi / 6) - (-0.5)) < tolerance
    assert abs(sine(-pi) - 0.0) < tolerance

def test_sine_types():
    tolerance = 1e-5
    assert abs(sine(0) - 0.0) < tolerance  # int
    assert abs(sine(0.0) - 0.0) < tolerance  # float

def test_sine_large_angles():
    pi = 3.141592653589793
    tolerance = 1e-5

    # Test 2pi (should be 0)
    assert abs(sine(2 * pi) - 0.0) < tolerance

    # The Taylor series might have precision loss for very large numbers
    # Let's test a moderately larger number where it still converges
    assert abs(sine(3 * pi / 2) - (-1.0)) < tolerance
