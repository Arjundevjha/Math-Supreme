import unittest
from Math.Algebra.Polynomials.cubic_formula import cubic_formula


class TestCubicSecurity(unittest.TestCase):
    def test_cubic_formula_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            cubic_formula(True, 1, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, False, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 1, True, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 1, 1, False)

    def test_cubic_formula_invalid_types(self):
        # String representations and non-numeric containers should raise TypeError
        with self.assertRaises(TypeError):
            cubic_formula("1", 1, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, [1], 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 1, None, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 1, 1, "invalid")

    def test_cubic_formula_upper_bound_limit(self):
        # Coefficients with magnitude > 1e51 should raise ValueError to prevent DoS/overflow
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e51."):
            cubic_formula(1e52, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e51."):
            cubic_formula(1, 1e52, 1, 1)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e51."):
            cubic_formula(1, 1, 1e52, 1)
        with self.assertRaisesRegex(ValueError, "exceeds maximum allowed limit of 1e51."):
            cubic_formula(1, 1, 1, 1e52)

    def test_cubic_formula_valid_boundary_value(self):
        # Boundary value magnitude <= 1e51 should pass without raising limit error
        roots = cubic_formula(1e20, 2e20, 1e20, 0)
        self.assertEqual(len(roots), 3)


if __name__ == "__main__":
    unittest.main()
