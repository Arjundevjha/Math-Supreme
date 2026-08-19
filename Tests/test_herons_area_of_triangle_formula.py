import math
import pytest

# Ensure the module can be imported


import importlib
herons_module = importlib.import_module("Math.Geometry.Euclidean_Geometry.Area.heron's_area_of_triangle_formula")
herons_area_of_triangle = herons_module.herons_area_of_triangle

class TestHeronsAreaOfTriangle:
    def test_valid_triangles(self):
        # 3-4-5 right triangle
        area = herons_area_of_triangle(3, 4, 5)
        assert math.isclose(area, 6.0)

        # Equilateral triangle
        area = herons_area_of_triangle(2, 2, 2)
        assert math.isclose(area, math.sqrt(3))

        # Isosceles triangle
        area = herons_area_of_triangle(5, 5, 8)
        assert math.isclose(area, 12.0)

        # Floating point triangle
        area = herons_area_of_triangle(3.5, 4.5, 5.5)
        expected_area = 7.854885024620029
        assert math.isclose(area, expected_area, rel_tol=1e-9)

    def test_non_positive_sides(self):
        with pytest.raises(ValueError, match="All sides must be positive."):
            herons_area_of_triangle(0, 4, 5)

        with pytest.raises(ValueError, match="All sides must be positive."):
            herons_area_of_triangle(3, -4, 5)

        with pytest.raises(ValueError, match="All sides must be positive."):
            herons_area_of_triangle(-3, -4, -5)

    def test_invalid_triangles_inequality(self):
        with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
            herons_area_of_triangle(1, 2, 3)  # 1 + 2 = 3

        with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
            herons_area_of_triangle(1, 10, 2) # 1 + 2 < 10

        with pytest.raises(ValueError, match="Invalid triangle: the sum of any two sides must be greater than the third side."):
            herons_area_of_triangle(5, 2, 2)  # 2 + 2 < 5
