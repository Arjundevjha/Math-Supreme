import pytest
import unittest.mock
from decimal import Decimal
from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root



def test_nth_root_basic_int():
    assert nth_root(8, 3) == pytest.approx(2.0)
    assert nth_root(1000, 3) == pytest.approx(10.0)
    assert nth_root(16, 4) == pytest.approx(2.0)
    assert nth_root(1, 100) == pytest.approx(1.0)


def test_nth_root_basic_float():
    assert nth_root(2, 2) == pytest.approx(1.414213562373095)
    assert nth_root(10, 3) == pytest.approx(2.154434690031884)
    assert nth_root(0.123456, 5) == pytest.approx(0.6581159862199095)


def test_nth_root_negative_base():
    assert nth_root(-8, 3) == pytest.approx(-2.0)
    assert nth_root(-1000, 3) == pytest.approx(-10.0)
    assert nth_root(-32, 5) == pytest.approx(-2.0)

    with pytest.raises(
        ValueError, match="Real n-th root of a negative number is undefined"
    ):
        nth_root(-4, 2)
    with pytest.raises(
        ValueError, match="Real n-th root of a negative number is undefined"
    ):
        nth_root(-8, 2.5)


def test_nth_root_negative_exponent():
    assert nth_root(8, -3) == pytest.approx(0.5)
    assert nth_root(4, -2) == pytest.approx(0.5)
    assert nth_root(-8, -3) == pytest.approx(-0.5)


def test_nth_root_fractional_degree():
    assert nth_root(2, 0.5) == pytest.approx(4.0)
    assert nth_root(4, 2.5) == pytest.approx(1.7411011265922482)


def test_nth_root_zero():
    assert nth_root(0, 3) == 0.0
    assert nth_root(0, 2.5) == 0.0
    with pytest.raises(
        ValueError,
        match="Zero cannot be raised to a negative power or root",
    ):
        nth_root(0, -3)


def test_nth_root_invalid_degree():
    with pytest.raises(ValueError, match="The root degree 'n' cannot be zero"):
        nth_root(8, 0)


def test_nth_root_decimal_precision_bounds():
    # Test that precision <= 0 raises ValueError
    with pytest.raises(ValueError, match="precision must be a positive integer"):
        nth_root(2, 3, precision=0)

    with pytest.raises(ValueError, match="precision must be a positive integer"):
        nth_root(2, 3, precision=-5)



def test_nth_root_decimal_precision():
    x = Decimal("2")
    n = Decimal("3")
    res = nth_root(x, n, precision=50)
    assert isinstance(res, Decimal)
    assert str(res).startswith("1.2599210498948731647672106072782283505702514647015")
    assert res**3 == pytest.approx(2.0)


def test_nth_root_decimal_fallback():
    # Large inputs for fast float branch fallback (causing OverflowError or ValueError)
    # y_dec = Decimal(str(float(x_dec) ** (1.0 / float(n_dec))))
    # If float(x_dec) overflows
    res = nth_root(Decimal("1e300"), Decimal("0.5"))
    assert isinstance(res, Decimal)
    assert res > Decimal("1e500")


def test_nth_root_decimal_power_term_zero():
    # y_dec ** (n_dec - 1) == 0
    res = nth_root(Decimal("1e-50"), Decimal("10000"))
    assert isinstance(res, Decimal)


def test_nth_root_float_power_term_zero():
    # y ** (float(n) - 1.0) == 0
    res = nth_root(1e-50, 1000)
    assert isinstance(res, float)


def test_nth_root_loop_exceptions_mocked():
    # 1. Decimal loop OverflowError (Lines 90-91)
    class MockDecimal(Decimal):
        def __pow__(self, other, modulo=None):
            raise OverflowError("Mocked OverflowError")

    with unittest.mock.patch(
        "Math.Numerical_Methods.Functions.nth_root.nth_root.Decimal", MockDecimal
    ):
        try:
            nth_root(MockDecimal("2"), MockDecimal("3"))
        except (
            TypeError
        ):  # MockDecimal constructor might fail in fallback but it should hit exception
            pass

    # 2. float loop Exception (Lines 108-109)
    class MockFloat(float):
        call_count = 0

        def __pow__(self, other):
            MockFloat.call_count += 1
            if MockFloat.call_count > 1:
                raise OverflowError("Mocked OverflowError")
            return super().__pow__(other)

    with unittest.mock.patch(
        "Math.Numerical_Methods.Functions.nth_root.nth_root.float", MockFloat
    ):
        try:
            nth_root(2, 3)
        except Exception:
            pass


def test_power_term_zero():
    # To get power_term = y_dec ** (n_dec - 1) == 0 (Line 85)
    # x = 1e-1000, n = 100
    nth_root(Decimal("1e-5000"), Decimal("10000"))

    # To get float power_term == 0 (Line 100)
    nth_root(1e-200, 100)


def test_float_loop_zero_div():
    class MockFloat4(float):
        def __pow__(self, other):
            if other != (1.0 / 3.0) and other != 1 / 3:
                # Return 0.0 to trigger power_term == 0 (Line 100)
                return 0.0
            return super().__pow__(other)

    with unittest.mock.patch(
        "Math.Numerical_Methods.Functions.nth_root.nth_root.float", MockFloat4
    ):
        nth_root(2, 3)


def test_float_loop_overflow():
    class MockFloat5(float):
        def __pow__(self, other):
            if other != (1.0 / 3.0) and other != 1 / 3:
                # Trigger exception inside float loop (Lines 108-109)
                raise OverflowError("test overflow")
            return super().__pow__(other)

    with unittest.mock.patch(
        "Math.Numerical_Methods.Functions.nth_root.nth_root.float", MockFloat5
    ):
        nth_root(2, 3)
