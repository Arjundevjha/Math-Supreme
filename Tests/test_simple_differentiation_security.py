import unittest

from Math.Algebra.Polynomials.polynomial import MAX_DEGREE
from Math.Calculus.Differentiation.simple_diffrentiation_function import (
    differentiate_polynomial,
)


class TestSimpleDifferentiationSecurity(unittest.TestCase):
    def test_invalid_container_types(self):
        with self.assertRaises(TypeError):
            differentiate_polynomial("1, 2, 3")
        with self.assertRaises(TypeError):
            differentiate_polynomial(None)

    def test_invalid_element_types(self):
        with self.assertRaises(TypeError):
            differentiate_polynomial(["1", 2])
        with self.assertRaises(TypeError):
            differentiate_polynomial([True, 2])

    def test_bounds_and_finiteness(self):
        with self.assertRaises(ValueError):
            differentiate_polynomial([1] * (MAX_DEGREE + 2))
        with self.assertRaises(ValueError):
            differentiate_polynomial([float("nan"), 1])
        with self.assertRaises(ValueError):
            differentiate_polynomial([1, float("inf")])


if __name__ == "__main__":
    unittest.main()
