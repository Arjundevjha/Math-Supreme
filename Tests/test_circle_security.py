import unittest
import pytest
from Math.Geometry.Euclidean_Geometry.Area.circle import area_of_circle


class TestCircleSecurity(unittest.TestCase):
    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle(True)
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle(False)

    def test_invalid_types(self):
        # Non-numeric types should raise TypeError
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle("5")
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle([5])
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle(None)


if __name__ == "__main__":
    unittest.main()
