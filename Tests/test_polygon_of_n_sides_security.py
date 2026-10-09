import unittest
import pytest
from Math.Geometry.Euclidean_Geometry.Area.polygon_of_n_sides import area_of_polygon


class TestPolygonOfNSidesSecurity(unittest.TestCase):
    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Number of sides n must be an integer\."):
            area_of_polygon(True, 5)
        with pytest.raises(TypeError, match=r"Side length s must be numeric \(int or float\)\."):
            area_of_polygon(5, False)

    def test_invalid_types(self):
        # Non-integer types for n or non-numeric for s should raise TypeError
        with pytest.raises(TypeError, match=r"Number of sides n must be an integer\."):
            area_of_polygon("5", 5)
        with pytest.raises(TypeError, match=r"Number of sides n must be an integer\."):
            area_of_polygon(5.5, 5)
        with pytest.raises(TypeError, match=r"Side length s must be numeric \(int or float\)\."):
            area_of_polygon(5, "5")
        with pytest.raises(TypeError, match=r"Side length s must be numeric \(int or float\)\."):
            area_of_polygon(5, None)


if __name__ == "__main__":
    unittest.main()
