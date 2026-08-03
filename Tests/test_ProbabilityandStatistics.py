import os
import sys
import pytest

# Add root directory to path


from Math.Probability_and_Statistics.Descriptive_Statistics.mode import mode

class TestMode:
    def test_empty_list(self):
        """Test mode with an empty list."""
        assert mode([]) == 0.0

    def test_single_mode(self):
        """Test mode with a single mode."""
        assert mode([1, 2, 2, 3]) == 2

    def test_multiple_modes(self):
        """Test mode with multiple modes."""
        assert sorted(mode([1, 1, 2, 2, 3])) == [1, 2]

    def test_all_elements_are_modes(self):
        """Test mode when all elements have the same frequency."""
        assert sorted(mode([1, 2, 3])) == [1, 2, 3]

    def test_float_values(self):
        """Test mode with float values."""
        assert mode([1.5, 2.5, 2.5, 3.5]) == 2.5
        assert sorted(mode([1.1, 1.1, 2.2, 2.2])) == [1.1, 2.2]

    def test_mixed_types(self):
        """Test mode with mixed int and float values."""
        assert mode([1, 2.0, 2.0, 3]) == 2.0
        assert sorted(mode([1, 1.0, 2, 2.0])) == [1, 2.0]

if __name__ == '__main__':
    pytest.main()
