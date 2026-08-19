import math
import pytest



from Math.Geometry.Euclidean_Geometry.Volume.cone import volume_of_cone

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
