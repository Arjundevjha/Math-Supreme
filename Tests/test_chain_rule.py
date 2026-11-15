import unittest

from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative


class TestChainRule(unittest.TestCase):
    def test_chain_rule_basic(self):
        # g(x) = x^2 = [0, 0, 1], n = 3 -> d/dx (x^2)^3 = 6x^5 = [0,0,0,0,0,6]
        self.assertEqual(chain_rule_derivative([0, 0, 1], 3), [0, 0, 0, 0, 0, 6])

    def test_chain_rule_linear(self):
        # g(x) = 1 + 2x = [1, 2], n = 2 -> d/dx (1+2x)^2 = 4(1+2x) = [4, 8]
        self.assertEqual(chain_rule_derivative([1, 2], 2), [4, 8])

    def test_chain_rule_exponent_one_and_zero(self):
        self.assertEqual(chain_rule_derivative([1, 2, 3], 1), [2, 6])
        self.assertEqual(chain_rule_derivative([1, 2, 3], 0), [])

    def test_chain_rule_constant_inner(self):
        self.assertEqual(chain_rule_derivative([5], 3), [])


if __name__ == "__main__":
    unittest.main()
