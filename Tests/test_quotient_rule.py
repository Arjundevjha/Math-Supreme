import unittest

from Math.Calculus.Differentiation.quotient_rule import quotient_rule_derivative


class TestQuotientRule(unittest.TestCase):
    def test_quotient_rule_basic(self):
        # u(x) = x^2 = [0, 0, 1], v(x) = x = [0, 1]
        # (u'v - uv') / v^2 = (2x*x - x^2*1) / x^2 = x^2 / x^2
        num, den = quotient_rule_derivative([0, 0, 1], [0, 1])
        self.assertEqual(num, [0, 0, 1])
        self.assertEqual(den, [0, 0, 1])

    def test_quotient_rule_constant_numerator(self):
        # u(x) = 1 = [1], v(x) = x + 1 = [1, 1]
        # num = 0 - 1*1 = [-1], den = (1+x)^2 = [1, 2, 1]
        num, den = quotient_rule_derivative([1], [1, 1])
        self.assertEqual(num, [-1])
        self.assertEqual(den, [1, 2, 1])

    def test_quotient_rule_zero_numerator(self):
        num, den = quotient_rule_derivative([], [1, 1])
        self.assertEqual(num, [])
        self.assertEqual(den, [1, 2, 1])


if __name__ == "__main__":
    unittest.main()
