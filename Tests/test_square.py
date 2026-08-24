import unittest

from Math.Geometry.Euclidean_Geometry.Area.square import area_of_square


class TestAreaOfSquare(unittest.TestCase):
    def test_positive_integer(self):
        # Area of square with side length 4 is 16
        self.assertEqual(area_of_square(4), 16)

    def test_positive_float(self):
        # Area of square with side length 2.5 is 6.25
        self.assertAlmostEqual(area_of_square(2.5), 6.25, delta=1e-9)

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
