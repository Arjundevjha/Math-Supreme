import pytest
import math
from Math.Geometry.Euclidean_Geometry.Volume.prism import volume_of_prism

class TestVolumeOfPrism:
    def test_volume_zero_base_area(self):
        """Test volume with zero base area."""
        assert volume_of_prism(0, 10) == 0.0
        assert volume_of_prism(0.0, 10.5) == 0.0

    def test_volume_zero_height(self):
        """Test volume with zero height."""
        assert volume_of_prism(10, 0) == 0.0
        assert volume_of_prism(10.5, 0.0) == 0.0

    def test_volume_both_zero(self):
        """Test volume with both zero."""
        assert volume_of_prism(0, 0) == 0.0

    def test_volume_positive_integers(self):
        """Test volume with positive integer base area and height."""
        assert volume_of_prism(5, 10) == 50.0

    def test_volume_positive_floats(self):
        """Test volume with positive float base area and height."""
        assert math.isclose(volume_of_prism(2.5, 4.2), 10.5, rel_tol=1e-9)

    def test_volume_negative_base_area(self):
        """Test that negative base area raises ValueError."""
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(-5, 10)

    def test_volume_negative_height(self):
        """Test that negative height raises ValueError."""
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(5, -10)

    def test_volume_negative_both(self):
        """Test that negative base area and height raises ValueError."""
        with pytest.raises(ValueError, match="Base area and height cannot be negative."):
            volume_of_prism(-5, -10)
