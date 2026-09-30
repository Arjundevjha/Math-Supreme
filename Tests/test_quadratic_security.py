import unittest
from Math.Algebra.Polynomials.quadratic_formula import solve_quadratic


class TestQuadraticSecurity(unittest.TestCase):
    def test_solve_quadratic_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            solve_quadratic(True, 2, 1)
        with self.assertRaises(TypeError):
            solve_quadratic(1, False, 1)
        with self.assertRaises(TypeError):
            solve_quadratic(1, 2, True)

    def test_solve_quadratic_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            solve_quadratic("1", 2, 1)
        with self.assertRaises(TypeError):
            solve_quadratic(1, [2], 1)
        with self.assertRaises(TypeError):
            solve_quadratic(1, 2, None)

    def test_solve_quadratic_upper_bound_limit(self):
        # Coefficients with magnitude > 1e300 should raise ValueError to prevent DoS/overflow
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e300."):
            solve_quadratic(1e301, 2, 1)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e300."):
            solve_quadratic(1, 1e301, 1)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e300."):
            solve_quadratic(1, 2, 1e301)

    def test_solve_quadratic_valid_boundary_value(self):
        # Boundary value magnitude <= 1e300 should pass without raising limit error
        r1, r2 = solve_quadratic(1e150, 2e150, 1e150)
        self.assertIsNotNone(r1)
        self.assertIsNotNone(r2)


if __name__ == "__main__":
    unittest.main()
