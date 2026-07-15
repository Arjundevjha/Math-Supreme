import unittest
import math

from Math.Probability_and_Statistics.Descriptive_Statistics.mean import mean

class TestMean(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(mean([]), 0.0)

    def test_positive_integers(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)

    def test_negative_integers(self):
        self.assertEqual(mean([-1, -2, -3, -4, -5]), -3.0)

    def test_mixed_integers(self):
        self.assertEqual(mean([-10, 0, 10]), 0.0)

    def test_single_element(self):
        self.assertEqual(mean([42]), 42.0)

    def test_zeroes(self):
        self.assertEqual(mean([0, 0, 0, 0]), 0.0)

    def test_floating_point_numbers(self):
        data = [1.5, 2.5, 3.5]
        expected = 2.5
        self.assertTrue(math.isclose(mean(data), expected, rel_tol=1e-9))

    def test_mixed_types(self):
        data = [1, 2.5, 3, 4.5]
        expected = 2.75
        self.assertTrue(math.isclose(mean(data), expected, rel_tol=1e-9))

    def test_large_numbers(self):
        data = [1e10, 2e10, 3e10]
        expected = 2e10
        self.assertTrue(math.isclose(mean(data), expected, rel_tol=1e-9))

    def test_small_numbers(self):
        data = [1e-10, 2e-10, 3e-10]
        expected = 2e-10
        self.assertTrue(math.isclose(mean(data), expected, rel_tol=1e-9))

if __name__ == '__main__':
    unittest.main()
