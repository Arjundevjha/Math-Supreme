import unittest
from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import (
    trinomial_general_term,
)


class TestTrinomialGeneralTerm(unittest.TestCase):
    def test_trinomial_general_term_basic(self):
        # (a + b + c)^2 expansion:
        # T_(2,0,0) = C(2,2,0) * a^2 * b^0 * c^0 = 1 * 2^2 = 4
        self.assertEqual(trinomial_general_term(2, 2, 0, 2, 3, 4), 4)

        # T_(1,1,0) = C(2,1,1) * a^1 * b^1 * c^0 = 2 * (2^1) * (3^1) * (4^0) = 12
        self.assertEqual(trinomial_general_term(2, 1, 1, 2, 3, 4), 12)

        # T_(0,1,1) = C(2,0,1) * a^0 * b^1 * c^1 = 2 * 3 * 4 = 24
        self.assertEqual(trinomial_general_term(2, 0, 1, 2, 3, 4), 24)

    def test_trinomial_general_term_exponent_zero(self):
        # (a + b + c)^0 = 1
        self.assertEqual(trinomial_general_term(0, 0, 0, 5, 10, 15), 1)

    def test_trinomial_general_term_floats(self):
        # n = 3, i = 1, j = 1, k = 1 -> coefficient = 6
        # 6 * (0.5^1) * (2.0^1) * (1.5^1) = 6 * 0.5 * 2.0 * 1.5 = 9.0
        self.assertAlmostEqual(
            trinomial_general_term(3, 1, 1, 0.5, 2.0, 1.5), 9.0
        )

    def test_trinomial_general_term_negative_bases(self):
        # (a + b + c)^3, i = 1, j = 1, k = 1
        # coefficient = 6, 6 * (-2)^1 * (3)^1 * (-1)^1 = 6 * -2 * 3 * -1 = 36
        self.assertEqual(trinomial_general_term(3, 1, 1, -2, 3, -1), 36)

    def test_trinomial_general_term_invalid_inputs(self):
        # Negative n
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(-1, 0, 0, 1, 1, 1)

        # Negative i
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, -1, 1, 1, 1, 1)

        # Negative j
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, 1, -1, 1, 1, 1)

        # i + j > n
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, 2, 1, 1, 1, 1)


if __name__ == "__main__":
    unittest.main()
