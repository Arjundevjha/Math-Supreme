import unittest
import pytest
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization


class TestPrimeFactorisationSecurity(unittest.TestCase):
    def test_upper_bound_limit_exceeded(self):
        # Test that number > 10**12 raises ValueError to prevent DoS via CPU resource exhaustion
        with pytest.raises(ValueError, match=r"[Nn]umber exceeds maximum limit of 10\^12\."):
            prime_factorization(10**12 + 1)

    def test_valid_boundary_value(self):
        # Boundary value number = 10**12 should pass without raising limit error
        # 10**12 = (2**12) * (5**12)
        factors = prime_factorization(10**12)
        self.assertEqual(factors.count(2), 12)
        self.assertEqual(factors.count(5), 12)
        self.assertEqual(len(factors), 24)

    def test_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match="number must be an integer."):
            prime_factorization(True)
        with pytest.raises(TypeError, match="number must be an integer."):
            prime_factorization(False)

    def test_invalid_types(self):
        # Non-integer types should raise TypeError
        with pytest.raises(TypeError, match="number must be an integer."):
            prime_factorization("1000")
        with pytest.raises(TypeError, match="number must be an integer."):
            prime_factorization(100.5)
        with pytest.raises(TypeError, match="number must be an integer."):
            prime_factorization(None)

    def test_non_positive_values(self):
        # Zero and negative integers should raise ValueError
        with pytest.raises(ValueError, match="Number must be positive."):
            prime_factorization(0)
        with pytest.raises(ValueError, match="Number must be positive."):
            prime_factorization(-100)


if __name__ == "__main__":
    unittest.main()
