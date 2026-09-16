import unittest
from Math.Algebra.Polynomials.polynomial import evaluate_polynomial, format_polynomial


class TestPolynomialSecurity(unittest.TestCase):
    def test_evaluate_polynomial_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            evaluate_polynomial("invalid", [1, 0], 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([1, 0], "invalid", 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial(None, [1, 0], 2)

        # Invalid x type
        with self.assertRaises(TypeError):
            evaluate_polynomial([1], [1], "2")
        with self.assertRaises(TypeError):
            evaluate_polynomial([1], [1], True)

        # Invalid coefficient or power elements
        with self.assertRaises(TypeError):
            evaluate_polynomial(["1"], [1], 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([True], [1], 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([1], ["1"], 2)
        with self.assertRaises(TypeError):
            evaluate_polynomial([1], [True], 2)

    def test_evaluate_polynomial_power_bounds(self):
        # Power exceeding 10000 or -10000 should raise ValueError
        with self.assertRaises(ValueError):
            evaluate_polynomial([1], [10001], 2)
        with self.assertRaises(ValueError):
            evaluate_polynomial([1], [-10001], 2)

        # Valid high power should pass
        self.assertEqual(evaluate_polynomial([1], [10000], 1), 1)

    def test_format_polynomial_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            format_polynomial("invalid", [1, 0])
        with self.assertRaises(TypeError):
            format_polynomial([1, 0], None)

        # Invalid element types
        with self.assertRaises(TypeError):
            format_polynomial(["1"], [1])
        with self.assertRaises(TypeError):
            format_polynomial([1], [True])


if __name__ == "__main__":
    unittest.main()
