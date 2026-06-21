import unittest

import pytest

from Math.Discrete_Math.Combinatorics.permutation import factorial
from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import trinomial_general_term
from Math.Discrete_Math.Number_Theory.gcd import compute_gcd
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm


def test_factorial_zero():
    """Test that factorial of 0 is 1."""
    assert factorial(0) == 1


def test_factorial_one():
    """Test that factorial of 1 is 1."""
    assert factorial(1) == 1


def test_factorial_positive_integers():
    """Test factorial calculation for positive integers."""
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120
    assert factorial(10) == 3628800


def test_factorial_large_number():
    """Test factorial calculation for a slightly larger number."""
    # 20! = 2432902008176640000
    assert factorial(20) == 2432902008176640000


def test_factorial_negative_number():
    """Test factorial with a negative number, which should raise RecursionError due to infinite recursion."""
    with pytest.raises(RecursionError):
        factorial(-1)


def test_compute_gcd_coprime():
    assert compute_gcd(17, 19) == 1
    assert compute_gcd(8, 9) == 1


def test_compute_gcd_multiples():
    assert compute_gcd(10, 5) == 5
    assert compute_gcd(5, 10) == 5
    assert compute_gcd(12, 36) == 12


def test_compute_gcd_identical():
    assert compute_gcd(7, 7) == 7
    assert compute_gcd(100, 100) == 100


def test_compute_gcd_common_factors():
    assert compute_gcd(48, 18) == 6
    assert compute_gcd(54, 24) == 6


def test_compute_gcd_errors():
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(0, 5)
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(5, 0)
    with pytest.raises(ValueError, match="Both numbers must be positive."):
        compute_gcd(-5, 5)


class TestTrinomialGeneralTerm(unittest.TestCase):

    def test_trinomial_general_term_happy_path(self):
        # Testing (2 + 3 + 4)^2
        # a^2
        self.assertEqual(trinomial_general_term(2, 2, 0, 2, 3, 4), 4)
        # b^2
        self.assertEqual(trinomial_general_term(2, 0, 2, 2, 3, 4), 9)
        # c^2
        self.assertEqual(trinomial_general_term(2, 0, 0, 2, 3, 4), 16)
        # 2ab
        self.assertEqual(trinomial_general_term(2, 1, 1, 2, 3, 4), 12)
        # 2bc
        self.assertEqual(trinomial_general_term(2, 0, 1, 2, 3, 4), 24)
        # 2ca
        self.assertEqual(trinomial_general_term(2, 1, 0, 2, 3, 4), 16)

    def test_trinomial_general_term_floats(self):
        # Testing (0.5 + 1.5 + 2.0)^3
        # We can just test a few terms and check if it handles floats correctly
        # Term with a^1 b^1 c^1 (i=1, j=1, k=1), coefficient = 3!/(1!1!1!) = 6
        # 6 * 0.5 * 1.5 * 2.0 = 6 * 1.5 = 9.0
        self.assertEqual(trinomial_general_term(3, 1, 1, 0.5, 1.5, 2.0), 9.0)

    def test_trinomial_general_term_zero(self):
        # Base zero case (0 + 0 + 0)^1
        self.assertEqual(trinomial_general_term(1, 1, 0, 0, 0, 0), 0)

        # When exponent is 0: (2 + 3 + 4)^0 = 1
        self.assertEqual(trinomial_general_term(0, 0, 0, 2, 3, 4), 1)

    def test_trinomial_general_term_invalid_values(self):
        # i < 0
        with self.assertRaises(ValueError):
            trinomial_general_term(2, -1, 0, 1, 1, 1)
        # j < 0
        with self.assertRaises(ValueError):
            trinomial_general_term(2, 0, -1, 1, 1, 1)
        # i + j > n
        with self.assertRaises(ValueError):
            trinomial_general_term(2, 2, 1, 1, 1, 1)
        # n < 0
        with self.assertRaises(ValueError):
            trinomial_general_term(-1, 0, 0, 1, 1, 1)


class TestLCM:
    def test_compute_lcm_basic(self):
        assert compute_lcm(4, 6) == 12
        assert compute_lcm(21, 6) == 42

    def test_compute_lcm_primes(self):
        assert compute_lcm(7, 5) == 35
        assert compute_lcm(11, 13) == 143

    def test_compute_lcm_coprimes(self):
        assert compute_lcm(8, 9) == 72

    def test_compute_lcm_multiples(self):
        assert compute_lcm(5, 15) == 15
        assert compute_lcm(12, 4) == 12

    def test_compute_lcm_same_numbers(self):
        assert compute_lcm(7, 7) == 7

    def test_compute_lcm_large_numbers(self):
        assert compute_lcm(100, 250) == 500

    def test_compute_lcm_invalid_input(self):
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(0, 5)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(5, 0)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(-1, 5)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(5, -1)


if __name__ == '__main__':
    unittest.main()
