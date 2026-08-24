# Unit tests for trinomial general term function
import pytest

from Math.Discrete_Math.Combinatorics.trinomial_theorem_general_term import (
    trinomial_general_term,
)


def test_trinomial_general_term_basic():
    """Test basic integer inputs for (a + b + c)^n."""
    # (2 + 3 + 4)^2 = 81
    # T_(2,0,0) = 1 * 2^2 * 3^0 * 4^0 = 4
    assert trinomial_general_term(2, 2, 0, 2, 3, 4) == 4
    # T_(0,2,0) = 1 * 2^0 * 3^2 * 4^0 = 9
    assert trinomial_general_term(2, 0, 2, 2, 3, 4) == 9
    # T_(0,0,2) = 1 * 2^0 * 3^0 * 4^2 = 16
    assert trinomial_general_term(2, 0, 0, 2, 3, 4) == 16
    # T_(1,1,0) = 2 * 2^1 * 3^1 * 4^0 = 12
    assert trinomial_general_term(2, 1, 1, 2, 3, 4) == 12
    # T_(0,1,1) = 2 * 2^0 * 3^1 * 4^1 = 24
    assert trinomial_general_term(2, 0, 1, 2, 3, 4) == 24
    # T_(1,0,1) = 2 * 2^1 * 3^0 * 4^1 = 16
    assert trinomial_general_term(2, 1, 0, 2, 3, 4) == 16


def test_trinomial_general_term_expansion_sum():
    """Verify sum of all general terms equals (a + b + c)^n."""
    a, b, c = 1, 2, 3
    n = 3
    total_sum = 0
    for i in range(n + 1):
        for j in range(n - i + 1):
            total_sum += trinomial_general_term(n, i, j, a, b, c)

    expected = (a + b + c) ** n
    assert total_sum == expected


def test_trinomial_general_term_floats():
    """Test floating-point numbers for a, b, and c."""
    # (0.5 + 1.5 + 2.0)^3
    # Term with i=1, j=1, k=1: coeff = 3!/(1!1!1!) = 6
    # 6 * 0.5 * 1.5 * 2.0 = 9.0
    result = trinomial_general_term(3, 1, 1, 0.5, 1.5, 2.0)
    assert result == 9.0


def test_trinomial_general_term_zero_exponent():
    """Test n = 0, i = 0, j = 0 boundary case."""
    assert trinomial_general_term(0, 0, 0, 5, 6, 7) == 1


def test_trinomial_general_term_zero_bases():
    """Test when bases a, b, or c are zero."""
    assert trinomial_general_term(1, 1, 0, 0, 0, 0) == 0
    assert trinomial_general_term(2, 2, 0, 0, 5, 5) == 0
    assert trinomial_general_term(2, 0, 2, 5, 0, 5) == 0
    assert trinomial_general_term(2, 0, 0, 5, 5, 0) == 0


def test_trinomial_general_term_negative_bases():
    """Test negative values for base terms a, b, and c."""
    # (-2 + 3 - 1)^3 = 0^3 = 0
    # Term with i=2, j=0, k=1: C(3,2)*C(1,0) = 3
    # 3 * (-2)^2 * 3^0 * (-1)^1 = 3 * 4 * 1 * (-1) = -12
    assert trinomial_general_term(3, 2, 0, -2, 3, -1) == -12


def test_trinomial_general_term_invalid_inputs():
    """Test error handling for invalid values of n, i, and j."""
    with pytest.raises(ValueError, match="Invalid values for n, i, and j."):
        trinomial_general_term(2, -1, 0, 1, 1, 1)

    with pytest.raises(ValueError, match="Invalid values for n, i, and j."):
        trinomial_general_term(2, 0, -1, 1, 1, 1)

    with pytest.raises(ValueError, match="Invalid values for n, i, and j."):
        trinomial_general_term(2, 2, 1, 1, 1, 1)

    with pytest.raises(ValueError, match="Invalid values for n, i, and j."):
        trinomial_general_term(-1, 0, 0, 1, 1, 1)
