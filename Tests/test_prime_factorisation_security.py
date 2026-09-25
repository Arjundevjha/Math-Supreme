import unittest
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization


class TestPrimeFactorisationSecurity(unittest.TestCase):
    def test_upper_bound_limit_exceeded(self):
        # Test that number > 10**12 raises ValueError to prevent DoS via CPU exhaustion
        with self.assertRaisesRegex(ValueError, "number exceeds maximum limit of 1000000000000."):
            prime_factorization(10**12 + 1)

    def test_valid_boundary_value(self):
        # Boundary value 10**12 should pass without raising limit error
        self.assertEqual(prime_factorization(10**12), [2] * 12 + [5] * 12)

    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            prime_factorization(True)
        with self.assertRaises(TypeError):
            prime_factorization(False)

    def test_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            prime_factorization("100")
        with self.assertRaises(TypeError):
            prime_factorization(100.5)


if __name__ == "__main__":
    unittest.main()
