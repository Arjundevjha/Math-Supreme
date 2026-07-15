import math
import unittest

from Math.Probability_and_Statistics.Descriptive_Statistics.median import median

class TestMedian(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(median([]), 0.0)

    def test_odd_elements(self):
        self.assertEqual(median([1, 3, 2]), 2)
        self.assertEqual(median([5, 1, 9, 3, 7]), 5)

    def test_even_elements(self):
        self.assertEqual(median([1, 4, 2, 3]), 2.5)
        self.assertEqual(median([10, 20, 30, 40]), 25.0)

    def test_negative_numbers(self):
        self.assertEqual(median([-5, -1, -3]), -3)
        self.assertEqual(median([-10, -20, -30, -40]), -25.0)

    def test_floating_point_numbers(self):
        self.assertTrue(math.isclose(median([1.5, 2.5, 3.5]), 2.5))
        self.assertTrue(math.isclose(median([1.1, 2.2, 3.3, 4.4]), 2.75))

    def test_mixed_integers_and_floats(self):
        self.assertEqual(median([1, 2.5, 3]), 2.5)
        self.assertEqual(median([1, 2.5, 3, 4.5]), 2.75)

    def test_duplicate_numbers(self):
        self.assertEqual(median([1, 2, 2, 3]), 2.0)
        self.assertEqual(median([1, 1, 1]), 1.0)
        self.assertEqual(median([2, 2, 2, 2]), 2.0)

if __name__ == '__main__':
    unittest.main()
