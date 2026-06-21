import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Math')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import trinomial_general_term

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

if __name__ == '__main__':
    unittest.main()
