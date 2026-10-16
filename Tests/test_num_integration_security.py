import unittest
from Math.Calculus.Integration.NumIntegration import integrate_polynomial


class TestNumIntegrationSecurity(unittest.TestCase):
    def test_integrate_polynomial_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            integrate_polynomial("invalid", [1, 0])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 0], "invalid")
        with self.assertRaises(TypeError):
            integrate_polynomial(None, [1, 0])

        # Invalid element types in coefficients
        with self.assertRaises(TypeError):
            integrate_polynomial(["1", "2"], [1, 0])
        with self.assertRaises(TypeError):
            integrate_polynomial([True, False], [1, 0])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, None], [1, 0])

        # Invalid element types in powers
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 2], ["1", "0"])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 2], [True, False])
        with self.assertRaises(TypeError):
            integrate_polynomial([1, 2], [1, None])

    def test_integrate_polynomial_length_bound(self):
        # Data exceeding maximum length limit (1,000,000)
        huge_coeffs = [1] * 1000001
        valid_powers = [1] * 1000001
        with self.assertRaises(ValueError):
            integrate_polynomial(huge_coeffs, [1])
        with self.assertRaises(ValueError):
            integrate_polynomial([1], valid_powers)


if __name__ == "__main__":
    unittest.main()
