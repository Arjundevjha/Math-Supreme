import unittest
import pytest
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn


class TestLinearEqnSecurity(unittest.TestCase):
    def test_linear_eqn_boolean_type_rejection(self):
        # Booleans inherit from int in Python, but must be rejected with TypeError
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(True, 2, 3, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, False, 3, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, 2, True, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, 2, 3, False)

    def test_linear_eqn_invalid_types(self):
        # Non-numeric types should raise TypeError
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn("1", 2, 3, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, [2], 3, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, 2, None, 6)
        with pytest.raises(TypeError, match=r"Coordinates must be numeric values \(int or float\)\."):
            linear_eqn(1, 2, 3, "6")

    def test_linear_eqn_upper_bound_limit(self):
        # Coordinates with magnitude > 1e300 should raise ValueError to prevent DoS/OverflowError
        with pytest.raises(
            ValueError,
            match=r"Coordinates exceed maximum allowed magnitude limit of 1e300\.",
        ):
            linear_eqn(1e301, 2, 3, 6)
        with pytest.raises(
            ValueError,
            match=r"Coordinates exceed maximum allowed magnitude limit of 1e300\.",
        ):
            linear_eqn(1, -1e301, 3, 6)
        with pytest.raises(
            ValueError,
            match=r"Coordinates exceed maximum allowed magnitude limit of 1e300\.",
        ):
            linear_eqn(1, 2, 1e301, 6)
        with pytest.raises(
            ValueError,
            match=r"Coordinates exceed maximum allowed magnitude limit of 1e300\.",
        ):
            linear_eqn(1, 2, 3, -1e301)

    def test_linear_eqn_valid_boundary_value(self):
        # Boundary value magnitude <= 1e300 should pass without raising limit error
        res = linear_eqn(1e150, 2e150, 3e150, 6e150)
        assert res.startswith("y = ")


if __name__ == "__main__":
    unittest.main()
