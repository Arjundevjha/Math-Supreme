import unittest
import pytest
from Math.Calculus.Differentiation.simple_diffrentiation_function import differentiate_polynomial


class TestSimpleDifferentiationSecurity(unittest.TestCase):
    def test_differentiate_polynomial_invalid_container_types(self):
        # Invalid container types for coeffs or powers
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            differentiate_polynomial("invalid", [2, 1])
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            differentiate_polynomial([3, 2], "invalid")
        with pytest.raises(TypeError, match="Coefficients and powers must be lists or tuples."):
            differentiate_polynomial(None, [2, 1])

    def test_differentiate_polynomial_invalid_element_types(self):
        # String or boolean elements in coeffs or powers must raise TypeError
        with pytest.raises(TypeError, match="Coefficients must be numeric values \\(int or float\\)."):
            differentiate_polynomial(["3", 2], [2, 1])
        with pytest.raises(TypeError, match="Coefficients must be numeric values \\(int or float\\)."):
            differentiate_polynomial([True, 2], [2, 1])
        with pytest.raises(TypeError, match="Powers must be numeric values \\(int or float\\)."):
            differentiate_polynomial([3, 2], ["2", 1])
        with pytest.raises(TypeError, match="Powers must be numeric values \\(int or float\\)."):
            differentiate_polynomial([3, 2], [True, 1])

    def test_differentiate_polynomial_power_bounds(self):
        # Power exceeding 10000 or -10000 should raise ValueError to prevent DoS
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            differentiate_polynomial([1], [10001])
        with pytest.raises(ValueError, match="Power exceeds maximum limit of 10000."):
            differentiate_polynomial([1], [-10001])

        # Valid boundary power 10000 should pass
        result = differentiate_polynomial([1], [10000])
        self.assertEqual(result, [(10000, 9999)])


if __name__ == "__main__":
    unittest.main()
