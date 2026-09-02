import pytest
from Math.Geometry.Trigonometry.Arc_Functions.arcsin import arcsin_numerical

def test_arcsin_numerical_zero():
    # arcsin(0) = 0
    result = arcsin_numerical(0)
    assert result is not None
    assert abs(result - 0.0) < 0.001

def test_arcsin_numerical_half():
    # arcsin(0.5) ≈ pi/6 ≈ 0.523598775...
    pi_over_6 = 3.141592653589793 / 6
    result = arcsin_numerical(0.5)
    assert result is not None
    assert abs(result - pi_over_6) < 0.001

def test_arcsin_numerical_one():
    # arcsin(1) ≈ pi/2 ≈ 1.570796326...
    pi_over_2 = 3.141592653589793 / 2
    result = arcsin_numerical(1)
    assert result is not None
    assert abs(result - pi_over_2) < 0.05

def test_arcsin_numerical_custom_precision():
    # Test custom precision parameter
    result = arcsin_numerical(0.5, precision=0.01)
    assert result is not None
    pi_over_6 = 3.141592653589793 / 6
    assert abs(result - pi_over_6) < 0.05

def test_arcsin_numerical_out_of_bounds_high():
    with pytest.raises(ValueError, match="Sine value must be between -1 and 1."):
        arcsin_numerical(1.5)

def test_arcsin_numerical_out_of_bounds_low():
    with pytest.raises(ValueError, match="Sine value must be between -1 and 1."):
        arcsin_numerical(-1.5)

def test_arcsin_numerical_negative_input():
    # Range searched is [0, pi/2], so negative valid inputs return None
    result = arcsin_numerical(-0.5)
    assert result is None
