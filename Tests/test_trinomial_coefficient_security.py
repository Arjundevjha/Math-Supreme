import unittest
import pytest
from Math.Discrete_Math.Combinatorics.trinomial_theorem import trinomial_coefficient


class TestTrinomialCoefficientSecurity(unittest.TestCase):
    def test_trinomial_coefficient_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(True, 1, 1)
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(5, False, 1)
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(5, 1, True)

    def test_trinomial_coefficient_invalid_types(self):
        # Non-integer types should raise TypeError
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient("5", 1, 1)
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(5, "1", 1)
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(5, 1, 2.5)
        with pytest.raises(TypeError, match="Power n, i, and j must be integers."):
            trinomial_coefficient(None, 1, 1)

    def test_trinomial_coefficient_negative_n(self):
        # Negative exponent n should raise ValueError
        with pytest.raises(ValueError, match="Power n must be non-negative."):
            trinomial_coefficient(-1, 0, 0)

    def test_trinomial_coefficient_upper_bound_limit(self):
        # Test that n > 1000 raises ValueError to prevent DoS via CPU/memory resource exhaustion
        with pytest.raises(ValueError, match="Power n exceeds maximum limit of 1000."):
            trinomial_coefficient(1001, 1, 1)

    def test_trinomial_coefficient_boundary_value(self):
        # Boundary value n = 1000 should pass without raising limit error
        val = trinomial_coefficient(1000, 0, 0)
        assert val == 1


if __name__ == "__main__":
    unittest.main()
