# Quartic formula solver for equations of the form ax⁴ + bx³ + cx² + dx + e = 0
from typing import Tuple, Union


def quartic_formula(
    a: Union[float, int],
    b: Union[float, int],
    c: Union[float, int],
    d: Union[float, int],
    e: Union[float, int],
) -> Tuple[complex, complex, complex, complex]:
    """
    Solve quartic equations of the form ax⁴ + bx³ + cx² + dx + e = 0
    using Landesman's closed-form quartic formula.

    Parameters:
    a (Union[float, int]): Coefficient of x⁴.
    b (Union[float, int]): Coefficient of x³.
    c (Union[float, int]): Coefficient of x².
    d (Union[float, int]): Coefficient of x.
    e (Union[float, int]): Constant term.

    Returns:
    Tuple[complex, complex, complex, complex]: The four roots of the quartic.

    Examples:
    >>> quartic_formula(1, -10, 35, -50, 24)
    ((1+0j), (2+0j), (3+0j), (4+0j))
    """
    if a == 0:
        raise ValueError(
            "Coefficient 'a' cannot be zero for a quartic equation."
        )

    ca = complex(a)
    cb = complex(b)
    cc = complex(c)
    cd = complex(d)
    ce = complex(e)

    # Step 1: Base & Invariant Terms
    p1 = cc**2 - 3.0 * cb * cd + 12.0 * ca * ce
    p2 = (
        2.0 * (cc**3)
        - 9.0 * cb * cc * cd
        - 72.0 * ca * cc * ce
        + 27.0 * ca * (cd**2)
        + 27.0 * (cb**2) * ce
    )

    # Step 2: Core Cube-Root Term (U)
    inner = p2**2 - 4.0 * (p1**3)
    base_U = (p2 + inner**0.5) ** (1.0 / 3.0)

    # Pre-calculate constant 2^(1/3) and primitive cube root of unity omega
    cube_root_2 = 2.0 ** (1.0 / 3.0)
    omega = complex(-0.5, 0.8660254037844386)

    shift = -cb / (4.0 * ca)

    best_roots = None
    best_error = float("inf")

    # Evaluate all 3 cube root branches of U to find the optimal branch
    for k in range(3):
        U = base_U * (omega**k)

        # Partial terms for R and Q
        term_U = U / (3.0 * cube_root_2 * ca)
        term_p1 = (
            (cube_root_2 * p1) / (3.0 * ca * U) if abs(U) > 1e-15 else 0.0
        )

        # Step 3: Resolvent Radical (R)
        R_inner = (
            (cb**2) / (4.0 * (ca**2))
            - (2.0 * cc) / (3.0 * ca)
            + term_U
            + term_p1
        )
        R = R_inner**0.5

        # Step 4: Core Polynomial Shift & Cross-Term (V) and Base Expression (Q)
        if abs(R) > 1e-15:
            v_num = (
                -((cb**3) / (ca**3))
                + (4.0 * cb * cc) / (ca**2)
                - (8.0 * cd) / ca
            )
            V = v_num / (4.0 * R)
        else:
            V = 0.0

        Q = (
            (cb**2) / (2.0 * (ca**2))
            - (4.0 * cc) / (3.0 * ca)
            - term_U
            - term_p1
        )

        # Step 5: Compact Quartic Roots
        half_R = 0.5 * R
        sqrt_Q_minus_V = (Q - V) ** 0.5
        sqrt_Q_plus_V = (Q + V) ** 0.5

        x1 = shift - half_R - 0.5 * sqrt_Q_minus_V
        x2 = shift - half_R + 0.5 * sqrt_Q_minus_V
        x3 = shift + half_R - 0.5 * sqrt_Q_plus_V
        x4 = shift + half_R + 0.5 * sqrt_Q_plus_V

        roots = (x1, x2, x3, x4)

        # Calculate residual error by evaluating polynomial at roots
        err = sum(
            abs(ca * (r**4) + cb * (r**3) + cc * (r**2) + cd * r + ce)
            for r in roots
        )

        if err < best_error:
            best_error = err
            best_roots = roots

    return best_roots



