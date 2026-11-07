import unittest
import pytest
from Math.Calculus.Differentiation.product_rule import product_rule_derivative


class TestProductRuleSecurity(unittest.TestCase):
    def test_product_rule_derivative_invalid_container_types(self):
        with pytest.raises(
            TypeError, match="Coefficients and powers must be lists or tuples."
        ):
            product_rule_derivative("invalid", [1], [1], [1])
        with pytest.raises(
            TypeError, match="Coefficients and powers must be lists or tuples."
        ):
            product_rule_derivative([1], "invalid", [1], [1])
        with pytest.raises(
            TypeError, match="Coefficients and powers must be lists or tuples."
        ):
            product_rule_derivative([1], [1], "invalid", [1])
        with pytest.raises(
            TypeError, match="Coefficients and powers must be lists or tuples."
        ):
            product_rule_derivative([1], [1], [1], "invalid")
        with pytest.raises(
            TypeError, match="Coefficients and powers must be lists or tuples."
        ):
            product_rule_derivative(None, [1], [1], [1])

    def test_product_rule_derivative_invalid_element_types(self):
        err_coeff = "Coefficients must be numeric values \\(int or float\\)."
        with pytest.raises(TypeError, match=err_coeff):
            product_rule_derivative(["1"], [1], [1], [1])
        with pytest.raises(TypeError, match=err_coeff):
            product_rule_derivative([True], [1], [1], [1])
        with pytest.raises(TypeError, match=err_coeff):
            product_rule_derivative([1], [1], ["1"], [1])
        with pytest.raises(TypeError, match=err_coeff):
            product_rule_derivative([1], [1], [False], [1])

        err_power = "Powers must be numeric values \\(int or float\\)."
        with pytest.raises(TypeError, match=err_power):
            product_rule_derivative([1], ["1"], [1], [1])
        with pytest.raises(TypeError, match=err_power):
            product_rule_derivative([1], [True], [1], [1])
        with pytest.raises(TypeError, match=err_power):
            product_rule_derivative([1], [1], [1], ["1"])
        with pytest.raises(TypeError, match=err_power):
            product_rule_derivative([1], [1], [1], [False])

    def test_product_rule_derivative_bounds(self):
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            product_rule_derivative([1], [10001], [1], [1])
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            product_rule_derivative([1], [-10001], [1], [1])
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            product_rule_derivative([1], [1], [1], [10001])
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            product_rule_derivative([1], [1], [1], [-10001])

        # Valid boundary test
        result = product_rule_derivative([1], [10000], [1], [10000])
        self.assertIn("10000x^9999", result)


if __name__ == "__main__":
    unittest.main()
