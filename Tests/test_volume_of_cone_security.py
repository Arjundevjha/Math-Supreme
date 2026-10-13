import unittest
import pytest
from Math.Geometry.Euclidean_Geometry.Volume.cone import volume_of_cone


class TestVolumeOfConeSecurity(unittest.TestCase):
    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            volume_of_cone(True, 5)
        with pytest.raises(TypeError, match=r"Height must be numeric \(int or float\)\."):
            volume_of_cone(5, False)

    def test_invalid_types(self):
        # Non-numeric types for radius or height should raise TypeError
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            volume_of_cone("5", 5)
        with pytest.raises(TypeError, match=r"Radius must be numeric \(int or float\)\."):
            volume_of_cone(None, 5)
        with pytest.raises(TypeError, match=r"Height must be numeric \(int or float\)\."):
            volume_of_cone(5, "5")
        with pytest.raises(TypeError, match=r"Height must be numeric \(int or float\)\."):
            volume_of_cone(5, [5])

    def test_negative_values(self):
        # Negative values should raise ValueError
        with pytest.raises(ValueError, match=r"Radius and height cannot be negative\."):
            volume_of_cone(-5, 5)
        with pytest.raises(ValueError, match=r"Radius and height cannot be negative\."):
            volume_of_cone(5, -5)


if __name__ == "__main__":
    unittest.main()
