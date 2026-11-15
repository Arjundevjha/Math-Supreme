import unittest

from Math.Algebra.Polynomials.remainnder_theorem import remainder_theorem


class TestRemainderTheorem(unittest.TestCase):
    def test_remainder_theorem_basic(self):
        # P(x) = 2x^2 + 3x + 1 = [1, 3, 2], at x=2 -> 1 + 6 + 8 = 15
        self.assertEqual(remainder_theorem([1, 3, 2], 2), 15.0)

    def test_remainder_theorem_zero_x(self):
        # P(x) = 5x^3 - 2x^2 + 4 = [4, 0, -2, 5], at x=0 -> 4
        self.assertEqual(remainder_theorem([4, 0, -2, 5], 0), 4.0)

    def test_remainder_theorem_negative_x(self):
        # P(x) = x^3 - x^2 + x - 1 = [-1, 1, -1, 1], at x=-2 -> -15
        self.assertEqual(remainder_theorem([-1, 1, -1, 1], -2), -15.0)

    def test_remainder_theorem_empty(self):
        self.assertEqual(remainder_theorem([], 5), 0.0)


if __name__ == "__main__":
    unittest.main()
