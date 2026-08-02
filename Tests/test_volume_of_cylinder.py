import sys
import os
import unittest
import math


from Math.Geometry.Euclidean_Geometry.Volume.cylinder import volume_of_cylinder

class TestVolumeOfCylinder(unittest.TestCase):
    def test_volume_positive_integers(self):
        # r=2, h=3 -> V = pi * 4 * 3 = 12 * pi
        self.assertTrue(math.isclose(volume_of_cylinder(2, 3), 12 * math.pi, rel_tol=1e-9))

    def test_volume_positive_floats(self):
        # r=1.5, h=2.5 -> V = pi * 2.25 * 2.5 = 5.625 * pi
        self.assertTrue(math.isclose(volume_of_cylinder(1.5, 2.5), 5.625 * math.pi, rel_tol=1e-9))

    def test_volume_zero_radius(self):
        self.assertEqual(volume_of_cylinder(0, 5), 0.0)

    def test_volume_zero_height(self):
        self.assertEqual(volume_of_cylinder(5, 0), 0.0)

    def test_volume_both_zero(self):
        self.assertEqual(volume_of_cylinder(0, 0), 0.0)

    def test_negative_radius_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Radius and height cannot be negative."):
            volume_of_cylinder(-1, 5)

    def test_negative_height_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Radius and height cannot be negative."):
            volume_of_cylinder(5, -1)

    def test_negative_both_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Radius and height cannot be negative."):
            volume_of_cylinder(-2, -3)

if __name__ == '__main__':
    unittest.main()
