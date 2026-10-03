import unittest
import pytest
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm


class TestLCMSecurity(unittest.TestCase):
    def test_compute_lcm_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(True, 5)
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(5, False)
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(True, False)

    def test_compute_lcm_invalid_types(self):
        # Non-integer types should raise TypeError
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm("10", 5)
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(10, "5")
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(10.5, 2)
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(None, 5)

    def test_compute_lcm_upper_bound_limit(self):
        # Test that inputs > 10**100 raise ValueError to prevent DoS via CPU/memory resource exhaustion
        with pytest.raises(ValueError, match=r"Inputs exceed maximum limit of 10\^100\."):
            compute_lcm(10**100 + 1, 5)
        with pytest.raises(ValueError, match=r"Inputs exceed maximum limit of 10\^100\."):
            compute_lcm(5, 10**100 + 1)

    def test_compute_lcm_boundary_value(self):
        # Boundary value 10**100 should pass without raising limit error
        val = compute_lcm(10**100, 10**100)
        assert val == 10**100

    def test_compute_lcm_non_positive_inputs(self):
        # Non-positive numbers should raise ValueError
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(0, 5)
        with pytest.raises(ValueError, match="Both numbers must be positive."):
            compute_lcm(-5, 5)


if __name__ == "__main__":
    unittest.main()
