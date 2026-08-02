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

from Math.Geometry.Euclidean_Geometry.Volume.prism import volume_of_prism

class TestVolumeOfPrism:
    def test_volume_positive_integers(self):
        assert volume_of_prism(10, 5) == 50

    def test_volume_positive_floats(self):
        assert math.isclose(volume_of_prism(2.5, 4.2), 10.5, rel_tol=1e-9)

    def test_volume_mixed_types(self):
        assert math.isclose(volume_of_prism(3.5, 4), 14.0, rel_tol=1e-9)
        assert math.isclose(volume_of_prism(10, 4.5), 45.0, rel_tol=1e-9)

    def test_volume_zero_base_area(self):
        assert volume_of_prism(0, 5) == 0

    def test_volume_zero_height(self):
        assert volume_of_prism(5, 0) == 0

    def test_volume_zero_both(self):
        assert volume_of_prism(0, 0) == 0

    def test_negative_base_area(self):
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(-1, 5)

    def test_negative_height(self):
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(5, -1)

    def test_negative_both(self):
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(-1, -1)
