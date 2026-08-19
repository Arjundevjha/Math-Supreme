import unittest


from Math.Geometry.Analytic_Geometry.line_equations.line_from_points import line_from_points

class TestLineFromPoints(unittest.TestCase):

    def test_positive_slope(self):
        # Slope: (4-2)/(3-1) = 1.0, Intercept: 2 - 1.0*1 = 1.0
        result = line_from_points(1, 2, 3, 4)
        self.assertEqual(result, "y = 1.0x + 1.0")

    def test_negative_slope(self):
        # Slope: (1-5)/(2-0) = -2.0, Intercept: 5 - (-2.0)*0 = 5.0
        result = line_from_points(0, 5, 2, 1)
        self.assertEqual(result, "y = -2.0x + 5.0")

    def test_zero_slope_horizontal_line(self):
        # Slope: (3-3)/(4-1) = 0.0, Intercept: 3 - 0.0*1 = 3.0
        result = line_from_points(1, 3, 4, 3)
        self.assertEqual(result, "y = 0.0x + 3.0")

    def test_fractional_slope(self):
        # Slope: (4-1)/(3-1) = 1.5, Intercept: 1 - 1.5*1 = -0.5
        result = line_from_points(1, 1, 3, 4)
        self.assertEqual(result, "y = 1.5x + -0.5")

    def test_vertical_line_raises_value_error(self):
        # Vertical line: x2 == x1
        with self.assertRaises(ValueError) as context:
            line_from_points(2, 1, 2, 5)
        self.assertEqual(str(context.exception), "Slope is undefined for vertical lines.")

    def test_floating_point_inputs(self):
        # Using floats:
        # Slope: (3.5 - 1.5)/(4.0 - 0.0) = 0.5
        # Intercept: 1.5 - 0.5*0.0 = 1.5
        result = line_from_points(0.0, 1.5, 4.0, 3.5)
        self.assertEqual(result, "y = 0.5x + 1.5")


if __name__ == '__main__':
    unittest.main()
