import unittest
from decimal import Decimal
from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan
from Math.Numerical_Methods.Constants.Pi_Algorithms.S_Ramanujan_algo import calculate_pi_ramanujan

class TestArcTan(unittest.TestCase):
    def get_expected_arctan(self, x_val):
        """Helper to compute an expected arctan using a well-known series directly or reference."""
        # For our test purposes, since we can't use python math module,
        # we can just use fixed known decimal values up to a reasonable precision,
        # or calculate it via the internal formula but avoiding circularity isn't strictly necessary
        # as long as we know the algorithm output is correct and we just need a happy path test.
        # But wait, math module usage is banned.
        pass

    def test_calculate_arctan_positive_integer(self):
        # arctan(1/2) = 0.4636476090008061
        result = calculate_arctan(2, precision=10)
        self.assertAlmostEqual(float(result), 0.4636476090, places=9)

    def test_calculate_arctan_positive_float(self):
        # arctan(1/2.5) = 0.3805063771123649
        result = calculate_arctan(2.5, precision=10)
        self.assertAlmostEqual(float(result), 0.3805063771, places=9)

    def test_calculate_arctan_decimal(self):
        # arctan(1/3) = 0.3217505543966422
        result = calculate_arctan(Decimal('3'), precision=10)
        self.assertAlmostEqual(float(result), 0.3217505543, places=9)

    def test_calculate_arctan_negative_value(self):
        # arctan(1/-2) = -0.4636476090008061
        result = calculate_arctan(-2, precision=10)
        self.assertAlmostEqual(float(result), -0.4636476090, places=9)

    def test_calculate_arctan_zero(self):
        # Custom logic returns 0 when x=0
        result = calculate_arctan(0)
        self.assertEqual(result, Decimal(0))

    def test_calculate_arctan_x_equals_one_fixed_terms(self):
        # arctan(1/1) = pi/4
        # Since it converges slowly, we use fixed number of terms
        result = calculate_arctan(1, number_of_terms=10000)
        pi = calculate_pi_ramanujan(10)
        expected = float(pi / 4)
        self.assertAlmostEqual(float(result), expected, places=4)

if __name__ == '__main__':
    unittest.main()
