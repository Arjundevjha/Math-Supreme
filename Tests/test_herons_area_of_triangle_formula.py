import importlib
import pytest

# Dynamic import due to apostrophe in filename
herons_module = importlib.import_module("Math.Geometry.Euclidean_Geometry.Area.heron's_area_of_triangle_formula")
herons_area_of_triangle = herons_module.herons_area_of_triangle


class TestHeronsAreaOfTriangle:
    def test_valid_right_triangle(self):
        # 3-4-5 right triangle: area = 0.5 * 3 * 4 = 6.0
        area = herons_area_of_triangle(3, 4, 5)
        assert area == pytest.approx(6.0)

    def test_valid_equilateral_triangle(self):
        # Equilateral triangle side 2: area = (sqrt(3)/4) * 2^2 = sqrt(3)
        area = herons_area_of_triangle(2, 2, 2)
        assert area == pytest.approx(3 ** 0.5)

    def test_valid_isosceles_triangle(self):
        # Isosceles triangle with sides 5, 5, 8: area = 12.0
        area = herons_area_of_triangle(5, 5, 8)
        assert area == pytest.approx(12.0)

    def test_valid_scalene_triangle(self):
        # Scalene triangle with sides 7, 8, 9: semi-perimeter s = 12, area = sqrt(12 * 5 * 4 * 3) = sqrt(720)
        area = herons_area_of_triangle(7, 8, 9)
        assert area == pytest.approx(720 ** 0.5)

    def test_valid_float_sides(self):
        # Floating point triangle sides
        area = herons_area_of_triangle(3.5, 4.5, 5.5)
        expected_area = 7.854885024620029
        assert area == pytest.approx(expected_area)

    def test_non_positive_sides(self):
        # Zero side length
        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(0, 4, 5)

        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(3, 0, 5)

        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(3, 4, 0)

        # Negative side length
        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(-3, 4, 5)

        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(3, -4, 5)

        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(3, 4, -5)

        with pytest.raises(ValueError, match=r"All sides must be positive\."):
            herons_area_of_triangle(-3, -4, -5)

    def test_invalid_triangle_inequality(self):
        # Sum of two sides equals third side (degenerate triangle line segment)
        with pytest.raises(ValueError, match=r"Invalid triangle: the sum of any two sides must be greater than the third side\."):
            herons_area_of_triangle(1, 2, 3)

        # Sum of two sides strictly less than third side
        with pytest.raises(ValueError, match=r"Invalid triangle: the sum of any two sides must be greater than the third side\."):
            herons_area_of_triangle(1, 10, 2)

        with pytest.raises(ValueError, match=r"Invalid triangle: the sum of any two sides must be greater than the third side\."):
            herons_area_of_triangle(5, 2, 2)
