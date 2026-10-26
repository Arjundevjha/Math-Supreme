import unittest
from Math.Algebra.Polynomials.cubic_formula import cubic_formula


class TestCubicSecurity(unittest.TestCase):
    def test_cubic_formula_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            cubic_formula(True, 2, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, False, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, True, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, 1, False)

    def test_cubic_formula_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            cubic_formula("1", 2, 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, [2], 1, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, None, 1)
        with self.assertRaises(TypeError):
            cubic_formula(1, 2, 1, "1")

    def test_cubic_formula_overflow_handling(self):
        # Coefficients causing numerical float overflow should raise ValueError instead of unhandled OverflowError
        with self.assertRaisesRegex(
            ValueError, "Input coefficients cause numerical overflow"
        ):
            cubic_formula(1e100, 2, 1, 1)
        with self.assertRaisesRegex(
            ValueError, "Input coefficients cause numerical overflow"
        ):
            cubic_formula(1, 1e100, 1, 1)

    def test_cubic_formula_valid_large_coefficients(self):
        # Coefficients within valid float limits should compute without error
        roots = cubic_formula(1e10, 2e10, 1e10, 0)
        self.assertEqual(len(roots), 3)


if __name__ == "__main__":
    unittest.main()
