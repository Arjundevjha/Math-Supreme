import os
import sys
import pytest
import math

# Add root and Math directory to path to allow imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Math'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Geometry.Euclidean_Geometry.Volume.sphere import volume_of_sphere

class TestVolumeOfSphere:
    def test_volume_zero_radius(self):
        """Test volume with zero radius."""
        assert volume_of_sphere(0) == 0.0
        assert volume_of_sphere(0.0) == 0.0

    def test_volume_positive_integer_radius(self):
        """Test volume with a positive integer radius."""
        # For r = 3, V = (4/3) * pi * 27 = 36 * pi
        pi = 3.14159265358979323846
        expected_volume = (4 / 3) * pi * (3 ** 3)
        assert math.isclose(volume_of_sphere(3), expected_volume, rel_tol=1e-9)

    def test_volume_positive_float_radius(self):
        """Test volume with a positive float radius."""
        # For r = 1.5, V = (4/3) * pi * 3.375 = 4.5 * pi
        pi = 3.14159265358979323846
        expected_volume = (4 / 3) * pi * (1.5 ** 3)
        assert math.isclose(volume_of_sphere(1.5), expected_volume, rel_tol=1e-9)

    def test_volume_negative_radius(self):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative."):
            volume_of_sphere(-1)

        with pytest.raises(ValueError, match="Radius cannot be negative."):
            volume_of_sphere(-2.5)
