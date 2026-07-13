import sys
import os
import math
import pytest

# Add both the project root and Math/ directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
math_dir = os.path.join(parent_dir, 'Math')

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Geometry.Euclidean_Geometry.Volume.cone import volume_of_cone

class TestVolumeOfCone:
    def test_volume_positive_integers(self):
        pi = 3.14159265358979323846
        expected = (1 / 3) * pi * (3 ** 2) * 4
        assert math.isclose(volume_of_cone(3, 4), expected, rel_tol=1e-9)

    def test_volume_positive_floats(self):
        pi = 3.14159265358979323846
        expected = (1 / 3) * pi * (2.5 ** 2) * 5.5
        assert math.isclose(volume_of_cone(2.5, 5.5), expected, rel_tol=1e-9)

    def test_volume_zero_radius(self):
        assert volume_of_cone(0, 5) == 0.0

    def test_volume_zero_height(self):
        assert volume_of_cone(5, 0) == 0.0

    def test_volume_zero_both(self):
        assert volume_of_cone(0, 0) == 0.0

    def test_negative_radius(self):
        with pytest.raises(ValueError, match="Radius and height cannot be negative."):
            volume_of_cone(-1, 5)

    def test_negative_height(self):
        with pytest.raises(ValueError, match="Radius and height cannot be negative."):
            volume_of_cone(3, -2)

    def test_negative_both(self):
        with pytest.raises(ValueError, match="Radius and height cannot be negative."):
            volume_of_cone(-3, -2)
