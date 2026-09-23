import unittest
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization


class TestPrimeFactorisationSecurity(unittest.TestCase):
    def test_prime_factorization_upper_bound_limit(self):
        # Exceeding 1000000000000 should raise ValueError to prevent DoS via CPU resource exhaustion
        with self.assertRaisesRegex(ValueError, "number exceeds maximum limit of 1000000000000."):
            prime_factorization(1000000000001)

    def test_prime_factorization_valid_boundary_value(self):
        # Boundary value 1000000000000 should pass without raising upper bound limit error
        self.assertEqual(prime_factorization(1000000000000), [2] * 12 + [5] * 12)

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
            prime_factorization(12.34)


if __name__ == "__main__":
    unittest.main()
