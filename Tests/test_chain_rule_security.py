import unittest

from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative


class TestChainRuleSecurity(unittest.TestCase):
    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            chain_rule_derivative("invalid", 2)
        with self.assertRaises(TypeError):
            chain_rule_derivative([True, 1], 2)
        with self.assertRaises(TypeError):
            chain_rule_derivative([1, 1], "2")
        with self.assertRaises(TypeError):
            chain_rule_derivative([1, 1], True)

    def test_bounds(self):
        with self.assertRaises(ValueError):
            chain_rule_derivative([1, 1], -1)
        with self.assertRaises(ValueError):
            chain_rule_derivative([1, 1], 10001)
        with self.assertRaises(ValueError):
            chain_rule_derivative([float("nan"), 1], 2)


if __name__ == "__main__":
    unittest.main()
