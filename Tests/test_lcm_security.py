import pytest
from Math.Discrete_Math.Number_Theory.lcm import compute_lcm


class TestLCMArgumentValidationSecurity:
    """Security tests for compute_lcm function input validation."""

    def test_compute_lcm_type_error_for_non_integers(self):
        """Ensure non-integer inputs raise TypeError to prevent invalid type handling."""
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(3.14, 5)  # type: ignore

        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(5, "10")  # type: ignore

        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm([5], 10)  # type: ignore

    def test_compute_lcm_type_error_for_booleans(self):
        """Ensure boolean inputs raise TypeError as booleans inherit from int in Python."""
        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(True, 10)

        with pytest.raises(TypeError, match="Both a and b must be integers."):
            compute_lcm(10, False)

    def test_compute_lcm_large_integers_supported(self):
        """Ensure large integers (e.g. 10^100) are computed correctly without arbitrary cap."""
        a = 10**100
        b = 10**50
        assert compute_lcm(a, b) == 10**100
