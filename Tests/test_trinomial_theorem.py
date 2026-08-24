import unittest
from Math.Discrete_Math.Combinatorics.trinomial_theorem import (
    expand_trinomial,
    trinomial_coefficient,
)
from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import (
    trinomial_general_term,
)

class TestTrinomialTheorem(unittest.TestCase):
    def test_expand_trinomial_n_0(self):
        result = expand_trinomial("a", "b", "c", 0)
        self.assertEqual(result, "1*a^0*b^0*c^0")

    def test_expand_trinomial_n_1(self):
        result = expand_trinomial("a", "b", "c", 1)
        expected = "1*a^0*b^0*c^1 + 1*a^0*b^1*c^0 + 1*a^1*b^0*c^0"
        self.assertEqual(result, expected)

    def test_expand_trinomial_n_2(self):
        result = expand_trinomial("x", "y", "z", 2)
        expected = (
            "1*x^0*y^0*z^2 + 2*x^0*y^1*z^1 + 1*x^0*y^2*z^0 + "
            "2*x^1*y^0*z^1 + 2*x^1*y^1*z^0 + 1*x^2*y^0*z^0"
        )
        self.assertEqual(result, expected)

    def test_expand_trinomial_different_variables(self):
        result = expand_trinomial("p", "q", "r", 1)
        expected = "1*p^0*q^0*r^1 + 1*p^0*q^1*r^0 + 1*p^1*q^0*r^0"
        self.assertEqual(result, expected)

    def test_expand_trinomial_long_variable_names(self):
        result = expand_trinomial("alpha", "beta", "gamma", 1)
        expected = (
            "1*alpha^0*beta^0*gamma^1 + 1*alpha^0*beta^1*gamma^0 + "
            "1*alpha^1*beta^0*gamma^0"
        )
        self.assertEqual(result, expected)

    def test_expand_trinomial_negative_n(self):
        with self.assertRaisesRegex(ValueError, "Power n must be non-negative."):
            expand_trinomial("a", "b", "c", -1)

    def test_trinomial_coefficient_positive_values(self):
        self.assertEqual(trinomial_coefficient(2, 1, 1), 2)
        self.assertEqual(trinomial_coefficient(3, 1, 1), 6)
        self.assertEqual(trinomial_coefficient(3, 2, 1), 3)
        self.assertEqual(trinomial_coefficient(3, 3, 0), 1)
        self.assertEqual(trinomial_coefficient(0, 0, 0), 1)

    def test_trinomial_coefficient_i_plus_j_greater_than_n(self):
        self.assertEqual(trinomial_coefficient(2, 2, 1), 0)
        self.assertEqual(trinomial_coefficient(3, 2, 2), 0)

    def test_trinomial_coefficient_negative_indices(self):
        self.assertEqual(trinomial_coefficient(2, -1, 1), 0)
        self.assertEqual(trinomial_coefficient(2, 1, -1), 0)

    def test_trinomial_general_term(self):
        self.assertEqual(trinomial_general_term(2, 1, 1, 2, 3, 4), 12)
        self.assertEqual(trinomial_general_term(3, 1, 1, 0.5, 1.5, 2.0), 9.0)
        self.assertEqual(trinomial_general_term(0, 0, 0, 1, 2, 3), 1)

    def test_trinomial_general_term_invalid_values(self):
        with self.assertRaisesRegex(ValueError, "Invalid values for n, i, and j."):
            trinomial_general_term(2, -1, 0, 1, 1, 1)

if __name__ == "__main__":
    unittest.main()
