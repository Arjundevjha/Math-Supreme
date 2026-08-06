import unittest
import math
from Math.Geometry.Euclidean_Geometry.Area.polygon_of_n_sides import area_of_polygon

class TestAreaOfPolygon(unittest.TestCase):

    def test_triangle(self):
        # n = 3, s = 2, Area = sqrt(3)/4 * 2^2 = sqrt(3) ~ 1.73205
        # area_of_polygon(3, 2)
        # Using exact expected formula:
        expected = math.sqrt(3)
        actual = area_of_polygon(3, 2)
        self.assertTrue(math.isclose(actual, expected, rel_tol=1e-5))

    def test_square(self):
        # n = 4, s = 2, Area = 2^2 = 4
        expected = 4.0
        actual = area_of_polygon(4, 2)
        self.assertTrue(math.isclose(actual, expected, rel_tol=1e-5))

    def test_hexagon(self):
        # n = 6, s = 2, Area = 3 * sqrt(3)/2 * 2^2 = 6 * sqrt(3) ~ 10.3923
        expected = 6 * math.sqrt(3)
        actual = area_of_polygon(6, 2)
        self.assertTrue(math.isclose(actual, expected, rel_tol=1e-5))

    def test_invalid_n(self):
        with self.assertRaisesRegex(ValueError, "A polygon must have at least 3 sides."):
            area_of_polygon(2, 5)

    def test_invalid_s(self):
        with self.assertRaisesRegex(ValueError, "Side length cannot be negative."):
            area_of_polygon(4, -1)

if __name__ == '__main__':
    unittest.main()
