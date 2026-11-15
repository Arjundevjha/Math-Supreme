import math
import unittest

from Math.Algebra.Polynomials.factor_theorem import check_factor


class TestCheckFactor(unittest.TestCase):
    def test_check_factor_true_and_false(self):
        # x^2 - 1 = [-1, 0, 1]
        self.assertTrue(check_factor([-1, 0, 1], 1))
        self.assertTrue(check_factor([-1, 0, 1], -1))
        self.assertFalse(check_factor([-1, 0, 1], 2))

    def test_check_factor_cubic(self):
        # (x - 1)(x - 2)(x - 3) = x^3 - 6x^2 + 11x - 6 = [-6, 11, -6, 1]
        poly = [-6, 11, -6, 1]
        self.assertTrue(check_factor(poly, 1))
        self.assertTrue(check_factor(poly, 2))
        self.assertTrue(check_factor(poly, 3))
        self.assertFalse(check_factor(poly, 4))

    def test_check_factor_float_and_irrational(self):
        # 2x^2 - x - 1 = [-1, -1, 2] -> roots -0.5, 1.0
        poly = [-1, -1, 2]
        self.assertTrue(check_factor(poly, -0.5))
        self.assertTrue(check_factor(poly, 1.0))
        self.assertFalse(check_factor(poly, 0.5))
        # x^2 - 2 = [-2, 0, 1]
        self.assertTrue(check_factor([-2, 0, 1], math.sqrt(2)))
        self.assertTrue(check_factor([-2, 0, 1], -math.sqrt(2)))

    def test_check_factor_empty_and_zero(self):
        self.assertTrue(check_factor([], 5))
        self.assertTrue(check_factor([0, 0, 0], 10))


if __name__ == "__main__":
    unittest.main()
