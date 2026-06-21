import os
import sys
import unittest

import pytest

# Add root directory to path to allow "Math.Discrete_Math..." imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

# the code has imports assuming "Math" is the root in some cases, so let's add it too
math_dir = os.path.abspath(os.path.join(root_dir, 'Math'))
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

# E.g. trinomial_theorem.py has `sys.path.append('..')` and `from combination import nCr`
# The internal code inside Math directory assumes sys.path has `Math/Discrete_Math/Combinatorics`
combinatorics_dir = os.path.abspath(os.path.join(math_dir, 'Discrete_Math', 'Combinatorics'))
if combinatorics_dir not in sys.path:
    sys.path.insert(0, combinatorics_dir)

from Math.Discrete_Math.Combinatorics.pascals_triangle import print_pascals_triangle, generate_pascals_triangle
from Math.Discrete_Math.Combinatorics.permutation import factorial, n_permute_r
from Math.Discrete_Math.Combinatorics.trinomial_theorem import expand_trinomial
from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import trinomial_general_term
from Math.Discrete_Math.Number_Theory.gcd import compute_gcd, prime_factorization_for_gcd
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm
from Math.Discrete_Math.Number_Theory.prime_factorisation import prime_factorization


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


class TestPermutation(unittest.TestCase):
    def test_n_permute_r_typical(self):
        self.assertEqual(n_permute_r(5, 3), 60)
        self.assertEqual(n_permute_r(10, 2), 90)

    def test_n_permute_r_boundary(self):
        self.assertEqual(n_permute_r(5, 0), 1)
        self.assertEqual(n_permute_r(5, 5), 120)
        self.assertEqual(n_permute_r(0, 0), 1)

    def test_n_permute_r_invalid(self):
        with self.assertRaises(ValueError):
            n_permute_r(3, 5)


class TestPascalsTriangle:
    def test_print_pascals_triangle_normal(self, capsys):
        """Test printing a normal Pascal's triangle."""
        triangle = [[1], [1, 1], [1, 2, 1]]
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        expected_output = "  1  \n 1 1 \n1 2 1\n"
        assert captured.out == expected_output

    def test_print_pascals_triangle_empty(self, capsys):
        """Test printing an empty Pascal's triangle."""
        triangle = []
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        assert captured.out == ""

    def test_generate_pascals_triangle_valid(self):
        """Test generating a valid Pascal's triangle."""
        assert generate_pascals_triangle(1) == [[1]]
        assert generate_pascals_triangle(3) == [[1], [1, 1], [1, 2, 1]]
        assert generate_pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_generate_pascals_triangle_invalid(self):
        """Test generating an invalid Pascal's triangle."""
        with pytest.raises(ValueError, match="Number of rows must be positive."):
            generate_pascals_triangle(0)

        with pytest.raises(ValueError, match="Number of rows must be positive."):
            generate_pascals_triangle(-1)


def test_prime_factorization_edge_case():
    assert prime_factorization(1) == []


def test_prime_factorization_prime_numbers():
    assert prime_factorization(2) == [2]
    assert prime_factorization(3) == [3]
    assert prime_factorization(7) == [7]
    assert prime_factorization(13) == [13]


def test_prime_factorization_composite_numbers():
    assert prime_factorization(4) == [2, 2]
    assert prime_factorization(6) == [2, 3]
    assert prime_factorization(8) == [2, 2, 2]
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(1024) == [2] * 10


def test_prime_factorization_invalid_input():
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(0)
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(-1)
    with pytest.raises(ValueError, match="Number must be positive."):
        prime_factorization(-10)


class TestDiscreteMath(unittest.TestCase):

    def test_expand_trinomial_n_0(self):
        result = expand_trinomial('a', 'b', 'c', 0)
        self.assertEqual(result, '1*a^0*b^0*c^0')

    def test_expand_trinomial_n_1(self):
        result = expand_trinomial('a', 'b', 'c', 1)
        # 1*a^0*b^0*c^1 + 1*a^0*b^1*c^0 + 1*a^1*b^0*c^0
        self.assertEqual(result, '1*a^0*b^0*c^1 + 1*a^0*b^1*c^0 + 1*a^1*b^0*c^0')

    def test_expand_trinomial_n_2(self):
        result = expand_trinomial('x', 'y', 'z', 2)
        # 1*x^0*y^0*z^2 + 2*x^0*y^1*z^1 + 1*x^0*y^2*z^0 + 2*x^1*y^0*z^1 + 2*x^1*y^1*z^0 + 1*x^2*y^0*z^0
        self.assertEqual(result, '1*x^0*y^0*z^2 + 2*x^0*y^1*z^1 + 1*x^0*y^2*z^0 + 2*x^1*y^0*z^1 + 2*x^1*y^1*z^0 + 1*x^2*y^0*z^0')

    def test_expand_trinomial_different_variables(self):
        result = expand_trinomial('p', 'q', 'r', 1)
        self.assertEqual(result, '1*p^0*q^0*r^1 + 1*p^0*q^1*r^0 + 1*p^1*q^0*r^0')

    def test_expand_trinomial_long_variable_names(self):
        result = expand_trinomial('alpha', 'beta', 'gamma', 1)
        self.assertEqual(result, '1*alpha^0*beta^0*gamma^1 + 1*alpha^0*beta^1*gamma^0 + 1*alpha^1*beta^0*gamma^0')

    def test_expand_trinomial_negative_n(self):
        with self.assertRaises(ValueError) as context:
            expand_trinomial('a', 'b', 'c', -1)
        self.assertTrue("Power n must be non-negative." in str(context.exception))


@pytest.mark.parametrize("n, expected", [
    # Test composite numbers
    (12, [2, 2, 3]),
    (60, [2, 2, 3, 5]),
    (100, [2, 2, 5, 5]),

    # Test prime numbers
    (2, [2]),
    (7, [7]),
    (13, [13]),

    # Test edge cases
    (1, []),
    (0, []),
    (-5, [])
])
def test_prime_factorization_for_gcd(n, expected):
    assert prime_factorization_for_gcd(n) == expected


if __name__ == '__main__':
    unittest.main()
