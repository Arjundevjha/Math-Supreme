import unittest
from Math.Algebra.Polynomials.cubic_formula import cubic_formula


class TestCubicSecurity(unittest.TestCase):
    def test_cubic_formula_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            cubic_formula(True, 2, 3, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, False, 3, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, True, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, 3, False)

    def test_cubic_formula_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            cubic_formula("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, [2], 3, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, None, 4)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, 3, {"d": 4})

    def test_cubic_formula_upper_bound_limit(self):
        # Coefficients with magnitude > 1e100 should raise ValueError to prevent DoS/overflow
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e100."):
            cubic_formula(1e101, 2, 3, 4)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e100."):
            cubic_formula(1, 1e101, 3, 4)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e100."):
            cubic_formula(1, 2, 1e101, 4)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e100."):
            cubic_formula(1, 2, 3, 1e101)

    def test_cubic_formula_valid_boundary_value(self):
        # Boundary value magnitude <= 1e100 (e.g. 1e50) should pass without raising limit or overflow error
        roots = cubic_formula(1e50, 2e50, 3e50, 4e50)
        self.assertEqual(len(roots), 3)


if __name__ == "__main__":
    unittest.main()
