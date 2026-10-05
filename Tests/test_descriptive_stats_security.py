import unittest
import pytest
from Math.Probability_and_Statistics.Descriptive_Statistics.mean import mean
from Math.Probability_and_Statistics.Descriptive_Statistics.median import median
from Math.Probability_and_Statistics.Descriptive_Statistics.mode import mode


class TestDescriptiveStatsSecurity(unittest.TestCase):
    def test_invalid_container_types(self):
        for func in (mean, median, mode):
            with pytest.raises(
                TypeError, match="Data must be a list or tuple of numbers."
            ):
                func("invalid")
            with pytest.raises(
                TypeError, match="Data must be a list or tuple of numbers."
            ):
                func(None)
            with pytest.raises(
                TypeError, match="Data must be a list or tuple of numbers."
            ):
                func(123)

    def test_valid_tuples(self):
        self.assertEqual(mean((1, 2, 3, 4, 5)), 3.0)
        self.assertEqual(median((1, 2, 3, 4, 5)), 3)
        self.assertEqual(mode((1, 2, 2, 3)), 2)

    def test_invalid_element_types(self):
        for func in (mean, median, mode):
            # Non-numeric elements
            with pytest.raises(
                TypeError, match="All elements in data must be integers or floats."
            ):
                func([1, 2, "3"])
            with pytest.raises(
                TypeError, match="All elements in data must be integers or floats."
            ):
                func([None])

            # Boolean element rejection (bool inherits from int in Python)
            with pytest.raises(
                TypeError, match="All elements in data must be integers or floats."
            ):
                func([1, True, 3])
            with pytest.raises(
                TypeError, match="All elements in data must be integers or floats."
            ):
                func([False, 2])


if __name__ == "__main__":
    unittest.main()
