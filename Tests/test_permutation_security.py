import unittest
from Math.Discrete_Math.Combinatorics.permutation import n_permute_r


class TestPermutationSecurity(unittest.TestCase):
    def test_n_permute_r_upper_bound_limit(self):
        # Test that n > 100000 raises ValueError to prevent DoS via CPU and memory resource exhaustion
        with self.assertRaisesRegex(ValueError, "n exceeds maximum limit of 100000."):
            n_permute_r(100001, 5)

    def test_n_permute_r_valid_boundary_value(self):
        # Boundary value n = 100000 should pass without raising limit error
        self.assertEqual(n_permute_r(100000, 1), 100000)

    def test_n_permute_r_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            n_permute_r(True, 5)
        with self.assertRaises(TypeError):
            n_permute_r(10, False)

    def test_n_permute_r_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            n_permute_r("10", 5)
        with self.assertRaises(TypeError):
            n_permute_r(10, "5")
        with self.assertRaises(TypeError):
            n_permute_r(10.5, 2)


if __name__ == "__main__":
    unittest.main()
