import math
import pytest
from Math.Geometry.Trigonometry.Arc_Functions.arcsin import arcsin_numerical


def test_arcsin_numerical_valid_inputs():
    # Test for sin_value = 0.0
    res_zero = arcsin_numerical(0.0)
    assert res_zero is not None
    assert abs(res_zero - 0.0) < 0.02

    # Test for sin_value = 0.5 (arcsin(0.5) = pi / 6 ≈ 0.5236)
    res_half = arcsin_numerical(0.5)
    assert res_half is not None
    assert abs(res_half - math.asin(0.5)) < 0.02

    # Test for sin_value = 1.0 (arcsin(1.0) = pi / 2 ≈ 1.5708)
    res_one = arcsin_numerical(1.0)
    assert res_one is not None
    assert abs(res_one - math.asin(1.0)) < 0.02

    # Test with custom higher precision
    res_half_prec = arcsin_numerical(0.5, precision=1e-5)
    assert res_half_prec is not None
    assert abs(res_half_prec - math.asin(0.5)) < 0.005


def test_arcsin_numerical_invalid_inputs():
    with pytest.raises(ValueError, match=r"Sine value must be between -1 and 1."):
        arcsin_numerical(1.5)

    with pytest.raises(ValueError, match=r"Sine value must be between -1 and 1."):
        arcsin_numerical(-1.5)


def test_arcsin_numerical_negative_sin_value_returns_none():
    # Negative sine values are out of the search range [0, pi/2]
    res_neg = arcsin_numerical(-0.5)
    assert res_neg is None
