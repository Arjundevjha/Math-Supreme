import importlib
import unittest
import pytest

# Dynamic import due to apostrophe in filename
herons_module = importlib.import_module("Math.Geometry.Euclidean_Geometry.Area.heron's_area_of_triangle_formula")
herons_area_of_triangle = herons_module.herons_area_of_triangle


class TestHeronsAreaSecurity(unittest.TestCase):
    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Side a must be numeric \(int or float\)\."):
            herons_area_of_triangle(True, 4, 5)
        with pytest.raises(TypeError, match=r"Side b must be numeric \(int or float\)\."):
            herons_area_of_triangle(3, False, 5)
        with pytest.raises(TypeError, match=r"Side c must be numeric \(int or float\)\."):
            herons_area_of_triangle(3, 4, True)

    def test_invalid_types(self):
        # Non-numeric types should raise TypeError
        with pytest.raises(TypeError, match=r"Side a must be numeric \(int or float\)\."):
            herons_area_of_triangle("3", 4, 5)
        with pytest.raises(TypeError, match=r"Side b must be numeric \(int or float\)\."):
            herons_area_of_triangle(3, None, 5)
        with pytest.raises(TypeError, match=r"Side c must be numeric \(int or float\)\."):
            herons_area_of_triangle(3, 4, [5])

    def test_nan_inf_rejection(self):
        # NaN and infinity values should raise ValueError
        with pytest.raises(ValueError, match=r"Side a must be a finite number\."):
            herons_area_of_triangle(float("nan"), 4, 5)
        with pytest.raises(ValueError, match=r"Side b must be a finite number\."):
            herons_area_of_triangle(3, float("inf"), 5)
        with pytest.raises(ValueError, match=r"Side c must be a finite number\."):
            herons_area_of_triangle(3, 4, float("-inf"))


if __name__ == "__main__":
    unittest.main()
