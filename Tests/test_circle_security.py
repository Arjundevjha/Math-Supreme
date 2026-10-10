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
            area_of_circle("10")
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle(None)
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            area_of_circle([5])

    def test_upper_bound_limit_exceeded(self):
        # Test that radius > 1e150 raises ValueError to prevent DoS via OverflowError
        with pytest.raises(ValueError, match=r"Radius exceeds maximum limit of 1e150\."):
            area_of_circle(1e151)

    def test_valid_boundary_value(self):
        # Boundary value radius = 1e150 should pass without raising limit error
        result = area_of_circle(1e150)
        self.assertGreater(result, 0)


if __name__ == "__main__":
    unittest.main()
