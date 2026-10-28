import unittest
from Math.Calculus.Integration.NumIntegration import integrate_polynomial, format_polynomial_integration


class TestNumIntegrationSecurity(unittest.TestCase):
    def test_integrate_polynomial_invalid_container_types(self):
        with self.assertRaises(TypeError):
            integrate_polynomial("invalid", [1, 0])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 0], "invalid")
        with self.assertRaises(TypeError):
            integrate_polynomial(None, [1, 0])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 0], None)

    def test_integrate_polynomial_invalid_element_types(self):
        with self.assertRaises(TypeError):
            integrate_polynomial(["1"], [1])
        with self.assertRaises(TypeError):
            integrate_polynomial([True], [1])
        with self.assertRaises(TypeError):
            integrate_polynomial([1], ["1"])
        with self.assertRaises(TypeError):
            integrate_polynomial([1], [True])

    def test_integrate_polynomial_invalid_numeric_values(self):
        with self.assertRaises(ValueError):
            integrate_polynomial([float('nan')], [1])
        with self.assertRaises(ValueError):
            integrate_polynomial([1], [float('nan')])
        with self.assertRaises(ValueError):
            integrate_polynomial([float('inf')], [1])
        with self.assertRaises(ValueError):
            integrate_polynomial([1], [float('-inf')])

    def test_integrate_polynomial_power_bounds(self):
        with self.assertRaises(ValueError):
            integrate_polynomial([1], [10001])
        with self.assertRaises(ValueError):
            integrate_polynomial([1], [-10001])

        # Valid bounds
        coeffs, powers = integrate_polynomial([1], [10000])
        self.assertEqual(powers, [10001])

    def test_format_polynomial_integration_invalid_types(self):
        with self.assertRaises(TypeError):
            format_polynomial_integration("invalid", [1, 0])
        with self.assertRaises(TypeError):
            format_polynomial_integration([1, 0], None)
        with self.assertRaises(TypeError):
            format_polynomial_integration(["1"], [1])
        with self.assertRaises(TypeError):
            format_polynomial_integration([1], [True])

    def test_format_polynomial_integration_invalid_numeric_values(self):
        with self.assertRaises(ValueError):
            format_polynomial_integration([float('nan')], [1])
        with self.assertRaises(ValueError):
            format_polynomial_integration([1], [10001])


if __name__ == "__main__":
    unittest.main()
