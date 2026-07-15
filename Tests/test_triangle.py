import unittest
import math

from Math.Geometry.Euclidean_Geometry.Area.triangle import area_of_triangle

class TestAreaOfTriangle(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(area_of_triangle(10, 5), 25.0)
        self.assertEqual(area_of_triangle(3, 4), 6.0)

    def test_positive_floats(self):
        self.assertTrue(math.isclose(area_of_triangle(10.5, 5.2), 27.3))
        self.assertTrue(math.isclose(area_of_triangle(3.14, 2.0), 3.14))

    def test_zero_base(self):
        self.assertEqual(area_of_triangle(0, 5), 0.0)

    def test_zero_height(self):
        self.assertEqual(area_of_triangle(10, 0), 0.0)

    def test_zero_base_and_height(self):
        self.assertEqual(area_of_triangle(0, 0), 0.0)

    def test_negative_base(self):
        with self.assertRaisesRegex(ValueError, "Base and height cannot be negative."):
            area_of_triangle(-5, 10)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "Base and height cannot be negative."):
            area_of_triangle(10, -5)

    def test_negative_base_and_height(self):
        with self.assertRaisesRegex(ValueError, "Base and height cannot be negative."):
            area_of_triangle(-10, -5)

if __name__ == '__main__':
    unittest.main()
