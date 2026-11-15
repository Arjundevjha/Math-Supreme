import unittest

from Math.Calculus.Differentiation.utils import (
    compute_polynomial_derivative,
    compute_polynomial_derivative_str,
)


class TestComputePolynomialDerivative(unittest.TestCase):
    def test_compute_polynomial_derivative_list(self):
        # 1 + 2x + 3x^2 -> [2, 6]
        self.assertEqual(compute_polynomial_derivative([1, 2, 3]), [2, 6])
        self.assertEqual(compute_polynomial_derivative([5]), [])
        self.assertEqual(compute_polynomial_derivative([]), [])

    def test_compute_polynomial_derivative_str(self):
        self.assertEqual(
            compute_polynomial_derivative_str([1, 4, 3]), "4 + 6x"
        )
        self.assertEqual(compute_polynomial_derivative_str([5]), "0")
        self.assertEqual(compute_polynomial_derivative_str([]), "0")


if __name__ == "__main__":
    unittest.main()
