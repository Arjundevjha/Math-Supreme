import math
import unittest

from Math.Geometry.Euclidean_Geometry.Volume.cuboid import volume_of_cuboid


class TestVolumeOfCuboid(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(volume_of_cuboid(2, 3, 4), 24)

    def test_positive_floats(self):
        self.assertTrue(math.isclose(volume_of_cuboid(2.5, 3.5, 4.5), 39.375, rel_tol=1e-9))

    def test_mixed_types(self):
        self.assertTrue(math.isclose(volume_of_cuboid(2, 3.5, 4), 28.0, rel_tol=1e-9))

    def test_zero_dimensions(self):
        self.assertEqual(volume_of_cuboid(0, 5, 5), 0)
        self.assertEqual(volume_of_cuboid(5, 0, 5), 0)
        self.assertEqual(volume_of_cuboid(5, 5, 0), 0)
        self.assertEqual(volume_of_cuboid(0, 0, 0), 0)

    def test_negative_dimensions_raise_value_error(self):
        with self.assertRaisesRegex(ValueError, "Length, width, and height cannot be negative."):
            volume_of_cuboid(-1, 5, 5)
        with self.assertRaisesRegex(ValueError, "Length, width, and height cannot be negative."):
            volume_of_cuboid(5, -1, 5)
        with self.assertRaisesRegex(ValueError, "Length, width, and height cannot be negative."):
            volume_of_cuboid(5, 5, -1)
        with self.assertRaisesRegex(ValueError, "Length, width, and height cannot be negative."):
            volume_of_cuboid(-1, -1, -1)


if __name__ == '__main__':
    unittest.main()
