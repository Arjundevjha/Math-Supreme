import unittest

from Math.Algebra.Polynomials.polynomial import MAX_DEGREE
from Math.Calculus.Differentiation.quotient_rule import quotient_rule_derivative


class TestQuotientRuleSecurity(unittest.TestCase):
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            quotient_rule_derivative("invalid", [1, 2])
        with self.assertRaises(TypeError):
            quotient_rule_derivative([1, 2], None)
        with self.assertRaises(TypeError):
            quotient_rule_derivative([True, 1], [1, 2])
        with self.assertRaises(TypeError):
            quotient_rule_derivative([1, 2], ["1", 2])

    def test_zero_denominator_and_bounds(self):
        with self.assertRaises(ValueError):
            quotient_rule_derivative([1, 2], [])
        with self.assertRaises(ValueError):
            quotient_rule_derivative([1, 2], [0, 0])
        with self.assertRaises(ValueError):
            quotient_rule_derivative([1] * (MAX_DEGREE + 2), [1])
        with self.assertRaises(ValueError):
            quotient_rule_derivative([float("inf")], [1, 2])


if __name__ == "__main__":
    unittest.main()
