import unittest
import pytest
from Math.Calculus.Differentiation.chain_rule import chain_rule_derivative


class TestChainRuleSecurity(unittest.TestCase):
    def test_chain_rule_derivative_invalid_container_types(self):
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            chain_rule_derivative("invalid", [2, 1], 3)
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            chain_rule_derivative([3, 2], "invalid", 3)
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            chain_rule_derivative(None, [2, 1], 3)

    def test_chain_rule_derivative_invalid_element_types(self):
        with pytest.raises(TypeError, match="Coefficients must be numeric values \\(int or float\\)."):
            chain_rule_derivative(["3", 2], [2, 1], 3)
        with pytest.raises(TypeError, match="Coefficients must be numeric values \\(int or float\\)."):
            chain_rule_derivative([True, 2], [2, 1], 3)
        with pytest.raises(TypeError, match="Powers must be numeric values \\(int or float\\)."):
            chain_rule_derivative([3, 2], ["2", 1], 3)
        with pytest.raises(TypeError, match="Powers must be numeric values \\(int or float\\)."):
            chain_rule_derivative([3, 2], [True, 1], 3)

    def test_chain_rule_derivative_invalid_exponent_type(self):
        with pytest.raises(TypeError, match="Exponent must be an integer."):
            chain_rule_derivative([1, 2], [2, 1], "3")
        with pytest.raises(TypeError, match="Exponent must be an integer."):
            chain_rule_derivative([1, 2], [2, 1], True)
        with pytest.raises(TypeError, match="Exponent must be an integer."):
            chain_rule_derivative([1, 2], [2, 1], 2.5)

    def test_chain_rule_derivative_bounds(self):
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            chain_rule_derivative([1], [10001], 2)
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            chain_rule_derivative([1], [-10001], 2)
        with pytest.raises(ValueError, match="Exponent must be non-negative."):
            chain_rule_derivative([1], [2], -1)
        with pytest.raises(ValueError, match="Exponent exceeds maximum limit of 10000."):
            chain_rule_derivative([1], [2], 10001)

        # Boundary test
        result = chain_rule_derivative([1], [10000], 10000)
        self.assertTrue(result.startswith("10000("))


if __name__ == "__main__":
    unittest.main()
