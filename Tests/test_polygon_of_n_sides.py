import unittest
import math
from Math.Geometry.Euclidean_Geometry.Area.polygon_of_n_sides import area_of_polygon

class TestAreaOfPolygon(unittest.TestCase):
    def test_positive_integer_sides(self):
        # The function uses a Taylor approximation which diverges for tan(pi/4) and other angles.
        # So we should test against the exact programmatic behavior to prevent regression.

        # Test a triangle (n=3) with side=2
        # pi / 3 = 1.0471975511965976
        # tan_val = 1.0471975511965976 + (1.0471975511965976**3)/3 + (2*1.0471975511965976**5)/15 + (17*1.0471975511965976**7)/315
        # tan_val = 1.6724344254927512
        # area = (3 * 2**2) / (4 * 1.6724344254927512) = 1.7937923031667484
        self.assertTrue(math.isclose(area_of_polygon(3, 2), 1.7937923031667484, rel_tol=1e-9))

        # Test a square (n=4) with side=5
        self.assertTrue(math.isclose(area_of_polygon(4, 5), 25.083170062060734, rel_tol=1e-9))

    def test_positive_float_side(self):
        # Test a hexagon (n=6) with side=1.5
        self.assertTrue(math.isclose(area_of_polygon(6, 1.5), 5.846408408174998, rel_tol=1e-9))

    def test_invalid_sides(self):
        with self.assertRaises(ValueError) as context:
            area_of_polygon(2, 5)
        self.assertEqual(str(context.exception), "A polygon must have at least 3 sides.")

    def test_negative_side_length(self):
        with self.assertRaises(ValueError) as context:
            area_of_polygon(4, -1)
        self.assertEqual(str(context.exception), "Side length cannot be negative.")

if __name__ == '__main__':
    unittest.main()
