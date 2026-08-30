import unittest
from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import (
    trinomial_general_term,
)


class TestTrinomialGeneralTerm(unittest.TestCase):
    def test_trinomial_general_term_happy_path(self):
        # Testing (2 + 3 + 4)^2
        # a^2 term: n=2, i=2, j=0, k=0 -> 1 * 2^2 * 3^0 * 4^0 = 4
        self.assertEqual(trinomial_general_term(2, 2, 0, 2, 3, 4), 4)
        # b^2 term: n=2, i=0, j=2, k=0 -> 1 * 2^0 * 3^2 * 4^0 = 9
        self.assertEqual(trinomial_general_term(2, 0, 2, 2, 3, 4), 9)
        # c^2 term: n=2, i=0, j=0, k=2 -> 1 * 2^0 * 3^0 * 4^2 = 16
        self.assertEqual(trinomial_general_term(2, 0, 0, 2, 3, 4), 16)
        # 2ab term: n=2, i=1, j=1, k=0 -> 2 * 2^1 * 3^1 * 4^0 = 12
        self.assertEqual(trinomial_general_term(2, 1, 1, 2, 3, 4), 12)
        # 2bc term: n=2, i=0, j=1, k=1 -> 2 * 2^0 * 3^1 * 4^1 = 24
        self.assertEqual(trinomial_general_term(2, 0, 1, 2, 3, 4), 24)
        # 2ca term: n=2, i=1, j=0, k=1 -> 2 * 2^1 * 3^0 * 4^1 = 16
        self.assertEqual(trinomial_general_term(2, 1, 0, 2, 3, 4), 16)

    def test_trinomial_general_term_floats(self):
        # Testing (0.5 + 1.5 + 2.0)^3
        # Term with a^1 b^1 c^1 (i=1, j=1, k=1), coefficient = 3!/(1!1!1!) = 6
        # 6 * 0.5^1 * 1.5^1 * 2.0^1 = 9.0
        self.assertEqual(trinomial_general_term(3, 1, 1, 0.5, 1.5, 2.0), 9.0)

    def test_trinomial_general_term_negative_base_values(self):
        # Testing (-1 + 2 - 3)^3 with i=1, j=1, k=1
        # coeff = 6, term = 6 * (-1)^1 * (2)^1 * (-3)^1 = 36
        self.assertEqual(trinomial_general_term(3, 1, 1, -1, 2, -3), 36)

    def test_trinomial_general_term_zero(self):
        # Base zero case (0 + 0 + 0)^1
        self.assertEqual(trinomial_general_term(1, 1, 0, 0, 0, 0), 0)

        # When exponent is 0: (2 + 3 + 4)^0 = 1
        self.assertEqual(trinomial_general_term(0, 0, 0, 2, 3, 4), 1)

    def test_trinomial_general_term_boundary_cases(self):
        # Corner terms where one power equals n and others are 0
        a, b, c, n = 3, 4, 5, 4
        # i = n (i=4, j=0, k=0) -> 1 * 3^4 = 81
        self.assertEqual(trinomial_general_term(n, 4, 0, a, b, c), 81)
        # j = n (i=0, j=4, k=0) -> 1 * 4^4 = 256
        self.assertEqual(trinomial_general_term(n, 0, 4, a, b, c), 256)
        # k = n (i=0, j=0, k=4) -> 1 * 5^4 = 625
        self.assertEqual(trinomial_general_term(n, 0, 0, a, b, c), 625)

    def test_trinomial_general_term_expansion_sum_property(self):
        # The sum of all trinomial_general_term(n, i, j, a, b, c) for 0<=i<=n and 0<=j<=n-i
        # must equal (a + b + c)^n.
        a, b, c, n = 2, 3, 5, 4
        expected_total = (a + b + c) ** n
        actual_total = 0
        for i in range(n + 1):
            for j in range(n - i + 1):
                actual_total += trinomial_general_term(n, i, j, a, b, c)
        self.assertEqual(actual_total, expected_total)

    def test_trinomial_general_term_zero_bases(self):
        # When a base is zero, terms with power > 0 for that base are 0
        # n=3, i=1, j=1, k=1, a=0, b=2, c=3 -> 6 * 0^1 * 2^1 * 3^1 = 0
        self.assertEqual(trinomial_general_term(3, 1, 1, 0, 2, 3), 0)
        # n=3, i=0, j=1, k=2, a=0, b=2, c=3 -> 3 * 0^0 * 2^1 * 3^2 = 54
        self.assertEqual(trinomial_general_term(3, 0, 1, 0, 2, 3), 54)

    def test_trinomial_general_term_invalid_values(self):
        # i < 0
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, -1, 0, 1, 1, 1)
        # j < 0
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, 0, -1, 1, 1, 1)
        # i + j > n
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, 2, 1, 1, 1, 1)
        # n < 0
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(-1, 0, 0, 1, 1, 1)


if __name__ == "__main__":
    unittest.main()
