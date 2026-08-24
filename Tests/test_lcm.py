import random
import math

import pytest  # noqa: E402
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm  # noqa: E402

class TestLCM:
    def test_compute_lcm_basic(self):
        assert compute_lcm(4, 6) == 12
        assert compute_lcm(21, 6) == 42

    def test_compute_lcm_primes(self):
        assert compute_lcm(7, 5) == 35
        assert compute_lcm(11, 13) == 143

    def test_compute_lcm_coprimes(self):
        assert compute_lcm(8, 9) == 72

    def test_compute_lcm_multiples(self):
        assert compute_lcm(5, 15) == 15
        assert compute_lcm(12, 4) == 12

    def test_compute_lcm_same_numbers(self):
        assert compute_lcm(7, 7) == 7

    def test_compute_lcm_large_numbers(self):
        assert compute_lcm(100, 250) == 500

    def test_compute_lcm_random_against_math_lcm(self):
        """Test compute_lcm against Python's built-in math.lcm with random numbers."""
        random.seed(42)
        for _ in range(100):
            a = random.randint(1, 10000)
            b = random.randint(1, 10000)
            assert compute_lcm(a, b) == math.lcm(a, b)

    def test_compute_lcm_invalid_input(self):
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(0, 5)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(5, 0)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(-1, 5)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(5, -1)
