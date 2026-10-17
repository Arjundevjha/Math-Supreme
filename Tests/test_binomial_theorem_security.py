import unittest
from Math.Discrete_Math.Combinatorics.binomial_theorem import expand_binomial


class TestBinomialTheoremSecurity(unittest.TestCase):
    def test_expand_binomial_invalid_term_types(self):
        # Non-string term 'a' or 'b' should raise TypeError
        with self.assertRaises(TypeError):
            expand_binomial(123, "y", 2)
        with self.assertRaises(TypeError):
            expand_binomial("x", 456, 2)
        with self.assertRaises(TypeError):
            expand_binomial(None, "y", 2)
        with self.assertRaises(TypeError):
            expand_binomial("x", ["y"], 2)

    def test_expand_binomial_invalid_power_types(self):
        # Non-integer power 'n' should raise TypeError
        with self.assertRaises(TypeError):
            expand_binomial("x", "y", "2")
        with self.assertRaises(TypeError):
            expand_binomial("x", "y", 2.5)

    def test_expand_binomial_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected
        with self.assertRaises(TypeError):
            expand_binomial("x", "y", True)
        with self.assertRaises(TypeError):
            expand_binomial("x", "y", False)

    def test_expand_binomial_negative_power(self):
        # Negative power n should raise ValueError
        with self.assertRaises(ValueError):
            expand_binomial("x", "y", -1)

    def test_expand_binomial_upper_bound_limit(self):
        # Power n exceeding 1000 should raise ValueError to prevent DoS via resource exhaustion
        with self.assertRaises(ValueError):
            expand_binomial("x", "y", 1001)

    def test_expand_binomial_valid_boundaries(self):
        # Boundary n = 0
        self.assertEqual(expand_binomial("x", "y", 0), "1*x^0*y^0")
        # Valid n = 2
        self.assertEqual(expand_binomial("x", "y", 2), "1*x^2*y^0 + 2*x^1*y^1 + 1*x^0*y^2")


if __name__ == "__main__":
    unittest.main()
