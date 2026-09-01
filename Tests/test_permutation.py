import unittest
from Math.Discrete_Math.Combinatorics.permutation import n_permute_r


class TestPermutation(unittest.TestCase):
    def test_n_permute_r_typical(self):
        self.assertEqual(n_permute_r(5, 3), 60)
        self.assertEqual(n_permute_r(10, 2), 90)
        self.assertEqual(n_permute_r(7, 4), 840)
        self.assertEqual(n_permute_r(20, 3), 6840)

    def test_n_permute_r_boundary(self):
        self.assertEqual(n_permute_r(5, 0), 1)
        self.assertEqual(n_permute_r(5, 5), 120)
        self.assertEqual(n_permute_r(0, 0), 1)
        self.assertEqual(n_permute_r(1, 1), 1)
        self.assertEqual(n_permute_r(1, 0), 1)

    def test_n_permute_r_invalid_values(self):
        with self.assertRaisesRegex(
            ValueError,
            "n should be greater than or equal to r for permutations to be valid.",
        ):
            n_permute_r(3, 5)

        with self.assertRaisesRegex(
            ValueError,
            "n should be greater than or equal to r for permutations to be valid.",
        ):
            n_permute_r(-1, 0)

        with self.assertRaisesRegex(
            ValueError,
            "n should be greater than or equal to r for permutations to be valid.",
        ):
            n_permute_r(5, -1)

    def test_n_permute_r_type_errors(self):
        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r(5.0, 3)

        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r(5, 3.0)

        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r(True, 1)

        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r(5, False)

        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r("5", 3)

        with self.assertRaisesRegex(TypeError, "Inputs must be integers."):
            n_permute_r(5, "3")

    def test_n_permute_r_large(self):
        self.assertEqual(n_permute_r(100, 2), 9900)
        self.assertEqual(n_permute_r(50, 4), 5527200)


if __name__ == "__main__":
    unittest.main()

