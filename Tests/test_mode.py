import unittest

from Math.Probability_and_Statistics.Descriptive_Statistics.mode import mode

class TestMode(unittest.TestCase):
    def test_empty_list(self):
        """Test mode with an empty list."""
        self.assertEqual(mode([]), 0.0)

    def test_single_element(self):
        """Test mode with a single element list."""
        self.assertEqual(mode([5]), 5)

    def test_single_mode(self):
        """Test mode with a single mode."""
        self.assertEqual(mode([1, 2, 2, 3]), 2)

    def test_multiple_modes(self):
        """Test mode with multiple modes."""
        result = mode([1, 1, 2, 2, 3])
        self.assertIsInstance(result, list)
        self.assertEqual(sorted(result), [1, 2])

    def test_all_elements_are_modes(self):
        """Test mode when all elements have the same frequency."""
        result = mode([1, 2, 3])
        self.assertIsInstance(result, list)
        self.assertEqual(sorted(result), [1, 2, 3])

    def test_float_values(self):
        """Test mode with float values."""
        self.assertEqual(mode([1.5, 2.5, 2.5, 3.5]), 2.5)
        result = mode([1.1, 1.1, 2.2, 2.2])
        self.assertIsInstance(result, list)
        self.assertEqual(sorted(result), [1.1, 2.2])

    def test_negative_numbers(self):
        """Test mode with negative numbers."""
        self.assertEqual(mode([-1, -2, -2, -3]), -2)
        result = mode([-1, -1, -2, -2])
        self.assertIsInstance(result, list)
        self.assertEqual(sorted(result), [-2, -1])

    def test_mixed_types(self):
        """Test mode with mixed int and float values."""
        self.assertEqual(mode([1, 2.0, 2.0, 3]), 2.0)

    def test_zeroes(self):
        """Test mode with zero values."""
        self.assertEqual(mode([0, 0, 1]), 0)

if __name__ == '__main__':
    unittest.main()
