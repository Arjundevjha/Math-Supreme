import pytest
import math


from Math.Geometry.Analytic_Geometry.line_equations.slope import calculate_slope

class TestCalculateSlope:
    def test_positive_slope(self):
        assert math.isclose(calculate_slope(1, 1, 3, 5), 2.0)

    def test_negative_slope(self):
        assert math.isclose(calculate_slope(0, 5, 2, 1), -2.0)

    def test_zero_slope(self):
        # Horizontal line
        assert math.isclose(calculate_slope(-2, 3, 4, 3), 0.0)

    def test_fractional_slope(self):
        assert math.isclose(calculate_slope(0, 0, 3, 1), 1/3)

    def test_float_coordinates(self):
        assert math.isclose(calculate_slope(1.5, 2.5, 3.5, 7.5), 2.5)

    def test_negative_coordinates(self):
        assert math.isclose(calculate_slope(-1, -2, -3, -8), 3.0)

    def test_vertical_line_raises_value_error(self):
        with pytest.raises(ValueError, match="Slope is undefined for vertical lines"):
            calculate_slope(2, 3, 2, 5)

    def test_identical_points_raises_value_error(self):
        # x2 - x1 == 0 will also catch identical points
        with pytest.raises(ValueError, match="Slope is undefined for vertical lines"):
            calculate_slope(4, 4, 4, 4)

if __name__ == '__main__':
    pytest.main()
