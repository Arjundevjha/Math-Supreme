import unittest

from Math.Algebra.Polynomials.polynomial import (
    MAX_DEGREE,
    evaluate_polynomial,
    format_polynomial,
    power_polynomial,
)


class TestPolynomialSecurity(unittest.TestCase):
    def test_evaluate_polynomial_invalid_types(self):
        with self.assertRaises(TypeError):
            evaluate_polynomial("invalid", 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial(None, 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([1, 2], "2")
        with self.assertRaises(TypeError):
            evaluate_polynomial([1, 2], True)
        with self.assertRaises(TypeError):
            evaluate_polynomial(["1"], 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([True], 2)

    def test_evaluate_polynomial_bounds(self):
        with self.assertRaises(ValueError):
            evaluate_polynomial([1] * (MAX_DEGREE + 2), 1)
        with self.assertRaises(ValueError):
            evaluate_polynomial([float("nan")], 1)
        with self.assertRaises(ValueError):
            evaluate_polynomial([1], float("inf"))
        self.assertEqual(evaluate_polynomial([1] + [0] * 9999 + [1], 1), 2.0)

    def test_format_polynomial_invalid_types(self):
        with self.assertRaises(TypeError):
            format_polynomial("invalid")
        with self.assertRaises(TypeError):
            format_polynomial(None)
        with self.assertRaises(TypeError):
            format_polynomial(["1"])
        with self.assertRaises(TypeError):
            format_polynomial([True])

    def test_power_polynomial_validation(self):
        with self.assertRaises(TypeError):
            power_polynomial([1, 1], True)
        with self.assertRaises(ValueError):
            power_polynomial([1, 1], -1)
        with self.assertRaises(ValueError):
            power_polynomial([1, 1], MAX_DEGREE + 1)


if __name__ == "__main__":
    unittest.main()
