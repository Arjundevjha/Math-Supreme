"""Dense list-based polynomial representation and operations."""
from typing import List, Sequence, Union

Number = Union[int, float]
MAX_DEGREE = 10000


def validate_polynomial(poly: Sequence[Number]) -> List[Number]:
    """
    Validate a dense coefficient list [c0, c1, c2, ...] where index i is x^i.

    Parameters:
    poly (Sequence[Number]): Sequence of numeric coefficients.

    Returns:
    List[Number]: Validated list of coefficients.
    """
    if not isinstance(poly, (list, tuple)):
        raise TypeError("Polynomial must be a list or tuple of numbers.")
    if len(poly) > MAX_DEGREE + 1:
        raise ValueError(
            f"Polynomial length exceeds maximum limit of {MAX_DEGREE + 1}."
        )
    for coeff in poly:
        if isinstance(coeff, bool) or not isinstance(coeff, (int, float)):
            raise TypeError(
                "Coefficients must be numeric values (int or float)."
            )
        if not -float("inf") < coeff < float("inf"):
            raise ValueError("Coefficients must be finite numbers.")
    return list(poly)


def trim_polynomial(poly: Sequence[Number]) -> List[Number]:
    """
    Remove trailing zero coefficients from a dense polynomial list.

    Parameters:
    poly (Sequence[Number]): Dense coefficient list.

    Returns:
    List[Number]: Trimmed coefficient list ([] for the zero polynomial).
    """
    coeffs = validate_polynomial(poly)
    while coeffs and coeffs[-1] == 0:
        coeffs.pop()
    return coeffs


def evaluate_polynomial(poly: Sequence[Number], x: Number) -> float:
    """
    Evaluate a polynomial P(x) = sum(c_i * x^i) using Horner's method.

    Parameters:
    poly (Sequence[Number]): Dense coefficient list [c0, c1, ...].
    x (Number): The value at which to evaluate the polynomial.

    Returns:
    float: The value of the polynomial at x.
    """
    coeffs = validate_polynomial(poly)
    if isinstance(x, bool) or not isinstance(x, (int, float)):
        raise TypeError("x must be a numeric value (int or float).")
    if not -float("inf") < x < float("inf"):
        raise ValueError("x must be a finite number.")

    result = 0.0
    for coeff in reversed(coeffs):
        result = result * x + coeff
    return float(result)


def add_polynomials(p: Sequence[Number], q: Sequence[Number]) -> List[Number]:
    """
    Add two dense polynomials p(x) + q(x).

    Parameters:
    p (Sequence[Number]): First polynomial coefficient list.
    q (Sequence[Number]): Second polynomial coefficient list.

    Returns:
    List[Number]: Sum polynomial coefficient list.
    """
    p_list = validate_polynomial(p)
    q_list = validate_polynomial(q)
    length = max(len(p_list), len(q_list))
    result: List[Number] = []
    for i in range(length):
        c1 = p_list[i] if i < len(p_list) else 0
        c2 = q_list[i] if i < len(q_list) else 0
        result.append(c1 + c2)
    return trim_polynomial(result)


def subtract_polynomials(
    p: Sequence[Number], q: Sequence[Number]
) -> List[Number]:
    """
    Subtract two dense polynomials p(x) - q(x).

    Parameters:
    p (Sequence[Number]): First polynomial coefficient list.
    q (Sequence[Number]): Second polynomial coefficient list.

    Returns:
    List[Number]: Difference polynomial coefficient list.
    """
    p_list = validate_polynomial(p)
    q_list = validate_polynomial(q)
    length = max(len(p_list), len(q_list))
    result: List[Number] = []
    for i in range(length):
        c1 = p_list[i] if i < len(p_list) else 0
        c2 = q_list[i] if i < len(q_list) else 0
        result.append(c1 - c2)
    return trim_polynomial(result)


def multiply_polynomials(
    p: Sequence[Number], q: Sequence[Number]
) -> List[Number]:
    """
    Multiply two dense polynomials p(x) * q(x).

    Parameters:
    p (Sequence[Number]): First polynomial coefficient list.
    q (Sequence[Number]): Second polynomial coefficient list.

    Returns:
    List[Number]: Product polynomial coefficient list.
    """
    p_list = trim_polynomial(p)
    q_list = trim_polynomial(q)
    if not p_list or not q_list:
        return []
    if len(p_list) + len(q_list) - 1 > MAX_DEGREE + 1:
        raise ValueError(
            f"Resulting polynomial degree exceeds limit of {MAX_DEGREE}."
        )

    result: List[Number] = [0] * (len(p_list) + len(q_list) - 1)
    for i, c1 in enumerate(p_list):
        if c1 == 0:
            continue
        for j, c2 in enumerate(q_list):
            result[i + j] += c1 * c2
    return trim_polynomial(result)


def power_polynomial(p: Sequence[Number], exponent: int) -> List[Number]:
    """
    Raise a dense polynomial p(x) to a non-negative integer power.

    Parameters:
    p (Sequence[Number]): Polynomial coefficient list.
    exponent (int): Non-negative integer exponent.

    Returns:
    List[Number]: Polynomial p(x)^exponent as a dense coefficient list.
    """
    base = trim_polynomial(p)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer.")
    if exponent < 0:
        raise ValueError("Exponent must be non-negative.")
    if exponent > MAX_DEGREE:
        raise ValueError(f"Exponent exceeds maximum limit of {MAX_DEGREE}.")
    if exponent == 0:
        return [1]
    if not base:
        return []
    if (len(base) - 1) * exponent > MAX_DEGREE:
        raise ValueError(
            f"Resulting polynomial degree exceeds limit of {MAX_DEGREE}."
        )

    result: List[Number] = [1]
    cur = base
    exp = exponent
    while exp > 0:
        if exp % 2 == 1:
            result = multiply_polynomials(result, cur)
        exp //= 2
        if exp > 0:
            cur = multiply_polynomials(cur, cur)
    return result


def format_polynomial(poly: Sequence[Number]) -> str:
    """
    Format a dense polynomial list [c0, c1, c2, ...] as a string.

    Parameters:
    poly (Sequence[Number]): Dense coefficient list.

    Returns:
    str: Human-readable string representation of the polynomial.
    """
    coeffs = validate_polynomial(poly)
    terms: List[str] = []
    for power, coeff in enumerate(coeffs):
        if coeff == 0:
            continue
        if power == 0:
            terms.append(f"{coeff}")
        elif power == 1:
            terms.append(f"{coeff}x")
        else:
            terms.append(f"{coeff}x^{power}")

    return " + ".join(terms) if terms else "0"
