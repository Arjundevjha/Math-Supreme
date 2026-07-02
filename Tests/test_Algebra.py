import os
import sys
import pytest

# Add root directory to path to allow imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn


def test_linear_eqn_positive_slope():
    # Points: (1, 2) and (3, 6)
    # m = (6 - 2) / (3 - 1) = 4 / 2 = 2.0
    # b = 2 - 2.0 * 1 = 0.0
    # Result: y = 2.0x + 0.0
    assert linear_eqn(1, 2, 3, 6) == "y = 2.0x + 0.0"

def test_linear_eqn_negative_slope():
    # Points: (0, 5) and (5, 0)
    # m = (0 - 5) / (5 - 0) = -5 / 5 = -1.0
    # b = 5 - (-1.0) * 0 = 5.0
    # Result: y = -1.0x + 5.0
    assert linear_eqn(0, 5, 5, 0) == "y = -1.0x + 5.0"

def test_linear_eqn_zero_slope():
    # Points: (1, 4) and (5, 4)
    # Horizontal line
    # m = (4 - 4) / (5 - 1) = 0.0
    # b = 4 - 0.0 * 1 = 4.0
    # Result: y = 0.0x + 4.0
    assert linear_eqn(1, 4, 5, 4) == "y = 0.0x + 4.0"

def test_linear_eqn_floats():
    # Points: (1.5, 2.5) and (3.5, 6.5)
    # m = (6.5 - 2.5) / (3.5 - 1.5) = 4.0 / 2.0 = 2.0
    # b = 2.5 - 2.0 * 1.5 = 2.5 - 3.0 = -0.5
    # Result: y = 2.0x + -0.5
    assert linear_eqn(1.5, 2.5, 3.5, 6.5) == "y = 2.0x + -0.5"

def test_linear_eqn_vertical_line():
    # Points: (2, 3) and (2, 7)
    # x1 == x2, expects ValueError
    with pytest.raises(ValueError, match="The x-coordinates cannot be the same \\(vertical line\\)."):
        linear_eqn(2, 3, 2, 7)
