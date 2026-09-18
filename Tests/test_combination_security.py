import unittest
from Math.Discrete_Math.Combinatorics.combination import nCr


class TestCombinationSecurity(unittest.TestCase):
    def test_nCr_upper_bound_limit(self):
        # Test that n > 100000 raises ValueError to prevent DoS via CPU resource exhaustion
        with self.assertRaisesRegex(ValueError, "n exceeds maximum limit of 100000."):
            nCr(100001, 5)

    def test_nCr_valid_boundary_value(self):
        # Boundary value n = 100000 should pass without raising limit error
        self.assertEqual(nCr(100000, 1), 100000)

    def test_nCr_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            nCr(True, 5)
        with self.assertRaises(TypeError):
            nCr(10, False)

    def test_nCr_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            nCr("10", 5)
        with self.assertRaises(TypeError):
            nCr(10, "5")
        with self.assertRaises(TypeError):
            nCr(10.5, 2)


if __name__ == "__main__":
    unittest.main()
