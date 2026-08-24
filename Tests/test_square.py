import os
import sys
import unittest
import math

# Fix imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
math_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Math"))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Geometry.Euclidean_Geometry.Area.square import area_of_square

class TestAreaOfSquare(unittest.TestCase):
    def test_positive_integer(self):
        # Area of square with side length 4 is 16
        self.assertEqual(area_of_square(4), 16)

    def test_positive_float(self):
        # Area of square with side length 2.5 is 6.25
        self.assertTrue(math.isclose(area_of_square(2.5), 6.25, rel_tol=1e-9))

    def test_zero(self):
        # Area of square with side length 0 is 0
        self.assertEqual(area_of_square(0), 0)

    def test_negative_side_length(self):
        # Negative side lengths should raise ValueError
        with self.assertRaises(ValueError):
            area_of_square(-1)

    def test_negative_float_side_length(self):
        # Negative side lengths should raise ValueError
        with self.assertRaises(ValueError):
            area_of_square(-3.14)

if __name__ == '__main__':
    unittest.main()
