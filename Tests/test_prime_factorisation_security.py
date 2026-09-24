import unittest
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization


class TestPrimeFactorisationSecurity(unittest.TestCase):
    def test_prime_factorization_upper_bound_limit(self):
        # Test that number > 10^12 raises ValueError to prevent DoS via excessive CPU consumption
        with self.assertRaisesRegex(ValueError, "number exceeds maximum limit of 10\\^12\\."):
            prime_factorization(10**12 + 1)

    def test_prime_factorization_valid_boundary_value(self):
        # Boundary value 10^12 = 2^12 * 5^12 should pass without raising limit error
        # 10^12 = (2**12) * (5**12)
        expected = [2] * 12 + [5] * 12
        self.assertEqual(prime_factorization(10**12), expected)

    def test_prime_factorization_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with self.assertRaises(TypeError):
            prime_factorization(True)
        with self.assertRaises(TypeError):
            prime_factorization(False)

    def test_prime_factorization_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            prime_factorization("1000")
        with self.assertRaises(TypeError):
            prime_factorization(10.5)
        with self.assertRaises(TypeError):
            prime_factorization(None)


if __name__ == "__main__":
    unittest.main()
