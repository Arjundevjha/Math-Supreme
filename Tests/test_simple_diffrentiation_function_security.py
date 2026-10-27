import unittest
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)


class TestDifferentiatePolynomialSecurity(unittest.TestCase):
    def test_differentiate_polynomial_invalid_container_types(self):
        # Invalid container types should raise TypeError
        with self.assertRaises(TypeError):
            differentiate_polynomial("invalid", [1, 0])
        with self.assertRaises(TypeError):
            differentiate_polynomial([1, 0], "invalid")
        with self.assertRaises(TypeError):
            differentiate_polynomial(None, [1, 0])
        with self.assertRaises(TypeError):
            differentiate_polynomial([1, 0], None)

    def test_differentiate_polynomial_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            differentiate_polynomial([True], [1])
        with self.assertRaises(TypeError):
            differentiate_polynomial([1], [True])

    def test_differentiate_polynomial_invalid_element_types(self):
        # Non-numeric element types should raise TypeError
        with self.assertRaises(TypeError):
            differentiate_polynomial(["1"], [1])
        with self.assertRaises(TypeError):
            differentiate_polynomial([1], ["1"])
        with self.assertRaises(TypeError):
            differentiate_polynomial([None], [1])

    def test_differentiate_polynomial_power_bounds(self):
        # Power exceeding 10000 or -10000 should raise ValueError
        with self.assertRaises(ValueError):
            differentiate_polynomial([1], [10001])
        with self.assertRaises(ValueError):
            differentiate_polynomial([1], [-10001])

        # Valid high power should pass
        self.assertEqual(differentiate_polynomial([1], [10000]), [(10000, 9999)])


if __name__ == "__main__":
    unittest.main()
