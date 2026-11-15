import unittest

from Math.Algebra.Polynomials.polynomial import MAX_DEGREE
from Math.Calculus.Differentiation.product_rule import product_rule_derivative


class TestProductRuleSecurity(unittest.TestCase):
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            product_rule_derivative("invalid", [1, 2])
        with self.assertRaises(TypeError):
            product_rule_derivative([1, 2], None)
        with self.assertRaises(TypeError):
            product_rule_derivative([True, 1], [1, 2])
        with self.assertRaises(TypeError):
            product_rule_derivative([1, 2], ["1", 2])

    def test_bounds(self):
        with self.assertRaises(ValueError):
            product_rule_derivative([1] * (MAX_DEGREE + 2), [1])
        with self.assertRaises(ValueError):
            product_rule_derivative([float("nan")], [1, 2])


if __name__ == "__main__":
    unittest.main()
