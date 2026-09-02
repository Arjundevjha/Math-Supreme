import pytest
from Math.Algebra.Linear_Equations.linear_eqn import linear_eqn


def test_linear_eqn_positive_slope():
    # Points: (1, 2) and (3, 6)
    # m = (6 - 2) / (3 - 1) = 2.0
    # b = 2 - 2.0 * 1 = 0.0
    assert linear_eqn(1, 2, 3, 6) == "y = 2.0x + 0.0"


def test_linear_eqn_negative_slope():
    # Points: (0, 5) and (5, 0)
    # m = (0 - 5) / (5 - 0) = -1.0
    # b = 5 - (-1.0) * 0 = 5.0
    assert linear_eqn(0, 5, 5, 0) == "y = -1.0x + 5.0"


def test_linear_eqn_zero_slope():
    # Points: (1, 4) and (5, 4)
    # Horizontal line: m = 0.0, b = 4.0
    assert linear_eqn(1, 4, 5, 4) == "y = 0.0x + 4.0"


def test_linear_eqn_floats():
    # Points: (1.5, 2.5) and (3.5, 6.5)
    # m = (6.5 - 2.5) / (3.5 - 1.5) = 2.0
    # b = 2.5 - 2.0 * 1.5 = -0.5
    assert linear_eqn(1.5, 2.5, 3.5, 6.5) == "y = 2.0x + -0.5"


def test_linear_eqn_vertical_line_raises_value_error():
    # Vertical line: x1 == x2
    with pytest.raises(
        ValueError, match=r"The x-coordinates cannot be the same \(vertical line\)\."
    ):
        linear_eqn(2, 3, 2, 7)


def test_linear_eqn_identical_points_raises_value_error():
    # Identical points: (2, 3) and (2, 3)
    with pytest.raises(
        ValueError, match=r"The x-coordinates cannot be the same \(vertical line\)\."
    ):
        linear_eqn(2, 3, 2, 3)


def test_linear_eqn_through_origin():
    # Points: (0, 0) and (2, 4)
    assert linear_eqn(0, 0, 2, 4) == "y = 2.0x + 0.0"


def test_linear_eqn_negative_coordinates():
    # Points: (-2, -3) and (-4, -7)
    # m = (-7 - -3) / (-4 - -2) = 2.0
    # b = -3 - 2.0 * (-2) = 1.0
    assert linear_eqn(-2, -3, -4, -7) == "y = 2.0x + 1.0"


def test_linear_eqn_fractional_slope():
    # Points: (1, 1) and (4, 2)
    m = (2.0 - 1.0) / (4.0 - 1.0)
    b = 1.0 - m * 1.0
    assert linear_eqn(1, 1, 4, 2) == f"y = {m}x + {b}"


def test_linear_eqn_large_coordinates():
    # Points: (1000000, 2000000) and (3000000, 6000000)
    assert linear_eqn(1000000, 2000000, 3000000, 6000000) == "y = 2.0x + 0.0"
