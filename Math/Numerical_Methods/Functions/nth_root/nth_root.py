# Calculating the n-th root of a number
from typing import Union, Optional
from decimal import Decimal, getcontext


def nth_root(
    x: Union[int, float, Decimal],
    n: Union[int, float, Decimal],
    precision: Optional[int] = None,
) -> Union[float, Decimal]:
    """
    Calculate the n-th root of a number x.

    Parameters:
    x (Union[int, float, Decimal]): The number to find the root of.
    n (Union[int, float, Decimal]): The degree of the root.
    precision (Optional[int]): If specified, sets the Decimal calculation
                               precision and returns a Decimal result.

    Returns:
    Union[float, Decimal]: The n-th root of x.
    """
    if precision is not None:
        if precision <= 0 or precision > 10000:
            raise ValueError("precision must be between 1 and 10000")
        getcontext().prec = precision

    is_decimal = (
        isinstance(x, Decimal)
        or isinstance(n, Decimal)
        or (precision is not None)
    )

    if n == 0:
        raise ValueError("The root degree 'n' cannot be zero.")

    if x == 0:
        if n > 0:
            return Decimal("0") if is_decimal else 0.0
        else:
            raise ValueError(
                "Zero cannot be raised to a negative power or root."
            )

    # Handle negative base
    if x < 0:
        # Check if n is an odd integer
        is_odd_int = False
        if isinstance(n, (int, Decimal)):
            is_odd_int = (int(n) % 2 != 0) if n == int(n) else False
        elif isinstance(n, float):
            is_odd_int = n.is_integer() and (int(n) % 2 != 0)

        if is_odd_int:
            return -nth_root(-x, n, precision)
        else:
            raise ValueError(
                "Real n-th root of a negative number is undefined "
                "for even or non-integer roots."
            )

    if n < 0:
        root_val = nth_root(x, -n, precision)
        return (
            (Decimal("1") / root_val)
            if isinstance(root_val, Decimal)
            else 1.0 / root_val
        )

    if is_decimal:
        x_dec = Decimal(str(x)) if isinstance(x, (int, float)) else x
        n_dec = Decimal(str(n)) if isinstance(n, (int, float)) else n

        # Initial guess from float calculation to speed up convergence
        try:
            y_dec = Decimal(str(float(x_dec) ** (1.0 / float(n_dec))))
        except (OverflowError, ValueError):
            y_dec = x_dec / n_dec if x_dec > 1 else Decimal("1")

        # Newton-Raphson loop for Decimal
        for _ in range(100):
            try:
                power_term = y_dec ** (n_dec - 1)
                if power_term == 0:
                    break
                next_y = ((n_dec - 1) * y_dec + x_dec / power_term) / n_dec
                if next_y == y_dec:
                    break
                y_dec = next_y
            except (OverflowError, ZeroDivisionError):
                break
        return y_dec
    else:
        # Float path
        y = float(x) ** (1.0 / float(n))
        for _ in range(100):
            try:
                power_term = y ** (float(n) - 1.0)
                if power_term == 0:
                    break
                next_y = (
                    (float(n) - 1.0) * y + float(x) / power_term
                ) / float(n)
                if next_y == y or abs(next_y - y) <= abs(y) * 1e-16:
                    y = next_y
                    break
                y = next_y
            except (OverflowError, ZeroDivisionError):
                break
        return y
