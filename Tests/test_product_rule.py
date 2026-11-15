import unittest

from Math.Calculus.Differentiation.product_rule import product_rule_derivative


class TestProductRule(unittest.TestCase):
    def test_product_rule_basic(self):
        # u(x) = x = [0, 1], v(x) = x^2 = [0, 0, 1] -> (x^3)' = 3x^2 = [0, 0, 3]
        self.assertEqual(product_rule_derivative([0, 1], [0, 0, 1]), [0, 0, 3])

    def test_product_rule_linear_factors(self):
        # (1 + x) * (2 + 3x) = 2 + 5x + 3x^2 -> derivative = 5 + 6x = [5, 6]
        self.assertEqual(product_rule_derivative([1, 1], [2, 3]), [5, 6])

    def test_product_rule_constants_and_zeros(self):
        self.assertEqual(product_rule_derivative([5], [7]), [])
        self.assertEqual(product_rule_derivative([], [2, 3]), [])
        self.assertEqual(product_rule_derivative([0, 0], [1, 2]), [])


if __name__ == "__main__":
    unittest.main()
