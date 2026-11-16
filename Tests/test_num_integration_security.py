import unittest

from Math.Algebra.Polynomials.polynomial import MAX_DEGREE
from Math.Calculus.Integration.NumIntegration import (
    format_polynomial_integration,
    integrate_polynomial,
)


class TestNumIntegrationSecurity(unittest.TestCase):
    def test_integrate_polynomial_invalid_container_types(self):
        with self.assertRaises(TypeError):
            integrate_polynomial("invalid")
        with self.assertRaises(TypeError):
            integrate_polynomial(None)

    def test_integrate_polynomial_invalid_element_types(self):
        with self.assertRaises(TypeError):
            integrate_polynomial(["1", 2])
        with self.assertRaises(TypeError):
            integrate_polynomial([True, 2])

    def test_integrate_polynomial_invalid_numeric_values(self):
        with self.assertRaises(ValueError):
            integrate_polynomial([float("nan")])
        with self.assertRaises(ValueError):
            integrate_polynomial([float("inf")])
        with self.assertRaises(ValueError):
            integrate_polynomial([float("-inf")])

    def test_integrate_polynomial_degree_bounds(self):
        with self.assertRaises(ValueError):
            integrate_polynomial([1] * (MAX_DEGREE + 2))

        res = integrate_polynomial([0] * MAX_DEGREE + [MAX_DEGREE + 1])
        self.assertEqual(len(res), MAX_DEGREE + 2)
        self.assertEqual(res[-1], 1.0)

    def test_format_polynomial_integration_invalid_types(self):
        with self.assertRaises(TypeError):
            format_polynomial_integration("invalid")
        with self.assertRaises(TypeError):
            format_polynomial_integration(None)
        with self.assertRaises(TypeError):
            format_polynomial_integration(["1"])
        with self.assertRaises(TypeError):
            format_polynomial_integration([True])

    def test_format_polynomial_integration_invalid_numeric_values(self):
        with self.assertRaises(ValueError):
            format_polynomial_integration([float("nan")])
        with self.assertRaises(ValueError):
            format_polynomial_integration([1] * (MAX_DEGREE + 2))


if __name__ == "__main__":
    unittest.main()
