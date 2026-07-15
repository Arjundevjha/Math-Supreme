import math
import unittest

from Math.Geometry.Euclidean_Geometry.Area.circle import area_of_circle

class TestAreaOfCircle(unittest.TestCase):
    def setUp(self):
        self.pi = 3.14159265358979323846

    def test_positive_integer_radius(self):
        # A = pi * r^2
        # r = 1 -> A = pi
        self.assertTrue(math.isclose(area_of_circle(1), self.pi, rel_tol=1e-9))

        # r = 5 -> A = 25 * pi
        self.assertTrue(math.isclose(area_of_circle(5), 25 * self.pi, rel_tol=1e-9))

    def test_positive_float_radius(self):
        # r = 2.5 -> A = 6.25 * pi
        self.assertTrue(math.isclose(area_of_circle(2.5), 6.25 * self.pi, rel_tol=1e-9))

    def test_zero_radius(self):
        # r = 0 -> A = 0
        self.assertEqual(area_of_circle(0), 0.0)

    def test_negative_radius(self):
        # r < 0 should raise ValueError
        with self.assertRaises(ValueError) as context:
            area_of_circle(-1)
        self.assertEqual(str(context.exception), "Radius cannot be negative.")

        with self.assertRaises(ValueError):
            area_of_circle(-2.5)

if __name__ == '__main__':
    unittest.main()
