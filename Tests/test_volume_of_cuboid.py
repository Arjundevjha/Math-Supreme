import sys
import os
import unittest
import math

# Add project root and Math/ to sys.path
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
if parent_dir_path not in sys.path:
    sys.path.insert(0, parent_dir_path)
math_dir = os.path.join(parent_dir_path, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

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
        with self.assertRaises(ValueError):
            volume_of_cuboid(-1, 5, 5)
        with self.assertRaises(ValueError):
            volume_of_cuboid(5, -1, 5)
        with self.assertRaises(ValueError):
            volume_of_cuboid(5, 5, -1)
        with self.assertRaises(ValueError):
            volume_of_cuboid(-1, -1, -1)

if __name__ == '__main__':
    unittest.main()
