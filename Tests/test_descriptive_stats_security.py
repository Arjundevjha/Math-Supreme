import unittest
from Math.Probability_and_Statistics.Descriptive_Statistics.mean import mean
from Math.Probability_and_Statistics.Descriptive_Statistics.median import median
from Math.Probability_and_Statistics.Descriptive_Statistics.mode import mode


class TestDescriptiveStatsSecurity(unittest.TestCase):
    def test_mean_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            mean("invalid")
        with self.assertRaises(TypeError):
            mean(123)
        with self.assertRaises(TypeError):
            mean(None)

        # Invalid element types
        with self.assertRaises(TypeError):
            mean(["1", "2"])
        with self.assertRaises(TypeError):
            mean([True, False])
        with self.assertRaises(TypeError):
            mean([1, None])

    def test_mean_length_bound(self):
        # Data exceeding maximum length limit (1,000,000)
        huge_data = [1] * 1000001
        with self.assertRaises(ValueError):
            mean(huge_data)

    def test_median_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            median("invalid")
        with self.assertRaises(TypeError):
            median(123)
        with self.assertRaises(TypeError):
            median(None)

        # Invalid element types
        with self.assertRaises(TypeError):
            median(["1", "2"])
        with self.assertRaises(TypeError):
            median([True, False])
        with self.assertRaises(TypeError):
            median([1, None])

    def test_median_length_bound(self):
        huge_data = [1] * 1000001
        with self.assertRaises(ValueError):
            median(huge_data)

    def test_mode_invalid_types(self):
        # Invalid container types
        with self.assertRaises(TypeError):
            mode("invalid")
        with self.assertRaises(TypeError):
            mode(123)
        with self.assertRaises(TypeError):
            mode(None)

        # Invalid element types
        with self.assertRaises(TypeError):
            mode(["1", "2"])
        with self.assertRaises(TypeError):
            mode([True, False])
        with self.assertRaises(TypeError):
            mode([1, None])

    def test_mode_length_bound(self):
        huge_data = [1] * 1000001
        with self.assertRaises(ValueError):
            mode(huge_data)


if __name__ == "__main__":
    unittest.main()
