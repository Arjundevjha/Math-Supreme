import unittest
from Math.Discrete_Math.Combinatorics.permutation import n_permute_r

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

if __name__ == '__main__':
    unittest.main()
