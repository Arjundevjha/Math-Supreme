"""Calculate European option prices using the Black-Scholes model."""
from typing import Tuple, Union

from Math.Numerical_Methods.Functions.nth_root.nth_root import nth_root

_LN2 = 0.6931471805599453
_SQRT2 = float(nth_root(2, 2))


def _exp(x: float) -> float:
    """
    Compute e^x without using the standard math module.

    Parameters:
    x (float): Exponent value.

    Returns:
    float: Approximate value of e^x.
    """
    if x < -709.0:
        return 0.0
    if x > 709.0:
        raise OverflowError("Exponent exceeds float range.")

    # Range reduction: x = k * ln(2) + r where |r| <= ln(2) / 2
    k = int(round(x / _LN2))
    r = x - k * _LN2

    # Taylor series for e^r
    term = 1.0
    total = 1.0
    for n in range(1, 30):
        term *= r / n
        total += term
        if abs(term) <= 1e-16 * abs(total):
            break

    return total * (2.0**k)


def _ln(x: float) -> float:
    """
    Compute natural logarithm ln(x) for x > 0 without the math module.

    Parameters:
    x (float): Positive real number.

    Returns:
    float: Natural logarithm of x.
    """
    if x <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    if x == 1.0:
        return 0.0

    # Reduce x to m * 2^k with m in [0.5, 1.5]
    k = 0
    m = float(x)
    while m > 1.5:
        m *= 0.5
        k += 1
    while m < 0.5:
        m *= 2.0
        k -= 1

    # Use artanh series: ln(m) = 2 * sum_{n=0..inf} y^(2n+1) / (2n+1)
    y = (m - 1.0) / (m + 1.0)
    y2 = y * y
    term = y
    total = 0.0
    for n in range(1, 100, 2):
        total += term / n
        term *= y2
        if abs(term) <= 1e-16:
            break

    return 2.0 * total + k * _LN2


def _erf(z: float) -> float:
    """
    Approximate the Gauss error function erf(z) using A&S 7.1.26.

    Parameters:
    z (float): Real input value.

    Returns:
    float: Approximate value of erf(z).
    """
    sign = 1.0 if z >= 0 else -1.0
    az = abs(z)
    p = 0.3275911
    a1 = 0.254829592
    a2 = -0.284496736
    a3 = 1.421413741
    a4 = -1.453152027
    a5 = 1.061405429

    t = 1.0 / (1.0 + p * az)
    poly = ((((a5 * t + a4) * t + a3) * t + a2) * t + a1) * t
    return sign * (1.0 - poly * _exp(-az * az))


def _norm_cdf(x: float) -> float:
    """
    Compute the standard normal cumulative distribution function N(x).

    Parameters:
    x (float): Z-score value.

    Returns:
    float: Probability P(Z <= x) for standard normal Z.
    """
    return 0.5 * (1.0 + _erf(x / _SQRT2))


def _validate_bs_inputs(
    spot_price: Union[int, float],
    strike_price: Union[int, float],
    time_to_maturity: Union[int, float],
    risk_free_rate: Union[int, float],
    volatility: Union[int, float],
) -> Tuple[float, float, float, float, float]:
    """
    Validate Black-Scholes input parameters.

    Parameters:
    spot_price (Union[int, float]): Current underlying asset price (S).
    strike_price (Union[int, float]): Option strike price (K).
    time_to_maturity (Union[int, float]): Time to expiration in years (T).
    risk_free_rate (Union[int, float]): Annual risk-free rate (decimal, r).
    volatility (Union[int, float]): Annualized volatility (decimal, sigma).

    Returns:
    Tuple[float, float, float, float, float]: Validated (S, K, T, r, sigma).
    """
    for name, val in [
        ("spot_price", spot_price),
        ("strike_price", strike_price),
        ("time_to_maturity", time_to_maturity),
        ("risk_free_rate", risk_free_rate),
        ("volatility", volatility),
    ]:
        if isinstance(val, bool) or not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be a numeric int or float.")
        if not -float("inf") < val < float("inf"):
            raise ValueError(f"{name} must be a finite number.")

    s_val = float(spot_price)
    k_val = float(strike_price)
    t_val = float(time_to_maturity)
    r_val = float(risk_free_rate)
    sigma_val = float(volatility)
    if s_val <= 0 or k_val <= 0:
        raise ValueError("spot_price and strike_price must be positive.")
    if t_val < 0:
        raise ValueError("time_to_maturity must be non-negative.")
    if sigma_val <= 0:
        raise ValueError("volatility must be positive.")
    if (
        s_val > 1e12
        or k_val > 1e12
        or t_val > 1000
        or abs(r_val) > 100
        or sigma_val > 100
    ):
        raise ValueError("Parameter values exceed maximum allowed limits.")

    return s_val, k_val, t_val, r_val, sigma_val


def black_scholes_call(
    spot_price: Union[int, float],
    strike_price: Union[int, float],
    time_to_maturity: Union[int, float],
    risk_free_rate: Union[int, float],
    volatility: Union[int, float],
) -> float:
    """
    Calculate the European call option price using the Black-Scholes model.

    Parameters:
    spot_price (Union[int, float]): Current underlying asset price (S).
    strike_price (Union[int, float]): Option strike price (K).
    time_to_maturity (Union[int, float]): Time to expiration in years (T).
    risk_free_rate (Union[int, float]): Annual risk-free rate (decimal, r).
    volatility (Union[int, float]): Annualized volatility (decimal, sigma).

    Returns:
    float: Theoretical European call option price.

    Examples:
    >>> round(black_scholes_call(100, 100, 1, 0.05, 0.2), 2)
    10.45
    """
    s_val, k_val, t_val, r_val, sigma_val = _validate_bs_inputs(
        spot_price, strike_price, time_to_maturity, risk_free_rate, volatility
    )

    if t_val == 0:
        return max(0.0, s_val - k_val)

    sqrt_t = float(nth_root(t_val, 2))
    vol_sqrt_t = sigma_val * sqrt_t
    d1 = (
        _ln(s_val / k_val)
        + (r_val + 0.5 * sigma_val * sigma_val) * t_val
    ) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    discount = _exp(-r_val * t_val)
    return s_val * _norm_cdf(d1) - k_val * discount * _norm_cdf(d2)


def black_scholes_put(
    spot_price: Union[int, float],
    strike_price: Union[int, float],
    time_to_maturity: Union[int, float],
    risk_free_rate: Union[int, float],
    volatility: Union[int, float],
) -> float:
    """
    Calculate the European put option price using the Black-Scholes model.

    Parameters:
    spot_price (Union[int, float]): Current underlying asset price (S).
    strike_price (Union[int, float]): Option strike price (K).
    time_to_maturity (Union[int, float]): Time to expiration in years (T).
    risk_free_rate (Union[int, float]): Annual risk-free rate (decimal, r).
    volatility (Union[int, float]): Annualized volatility (decimal, sigma).

    Returns:
    float: Theoretical European put option price.

    Examples:
    >>> round(black_scholes_put(100, 100, 1, 0.05, 0.2), 2)
    5.57
    """
    s_val, k_val, t_val, r_val, sigma_val = _validate_bs_inputs(
        spot_price, strike_price, time_to_maturity, risk_free_rate, volatility
    )

    if t_val == 0:
        return max(0.0, k_val - s_val)

    sqrt_t = float(nth_root(t_val, 2))
    vol_sqrt_t = sigma_val * sqrt_t
    d1 = (
        _ln(s_val / k_val)
        + (r_val + 0.5 * sigma_val * sigma_val) * t_val
    ) / vol_sqrt_t
    d2 = d1 - vol_sqrt_t

    discount = _exp(-r_val * t_val)
    return k_val * discount * _norm_cdf(-d2) - s_val * _norm_cdf(-d1)


def black_scholes_price(  # pylint: disable=too-many-arguments,too-many-positional-arguments
    spot_price: Union[int, float],
    strike_price: Union[int, float],
    time_to_maturity: Union[int, float],
    risk_free_rate: Union[int, float],
    volatility: Union[int, float],
    option_type: str = "call",
) -> float:
    """
    Calculate a European call or put option price via Black-Scholes.

    Parameters:
    spot_price (Union[int, float]): Current underlying asset price (S).
    strike_price (Union[int, float]): Option strike price (K).
    time_to_maturity (Union[int, float]): Time to expiration in years (T).
    risk_free_rate (Union[int, float]): Annual risk-free rate (decimal, r).
    volatility (Union[int, float]): Annualized volatility (decimal, sigma).
    option_type (str): Either "call" or "put" (case-insensitive).

    Returns:
    float: Theoretical European option price.
    """
    if not isinstance(option_type, str):
        raise TypeError("option_type must be a string ('call' or 'put').")

    kind = option_type.strip().lower()
    if kind == "call":
        return black_scholes_call(
            spot_price,
            strike_price,
            time_to_maturity,
            risk_free_rate,
            volatility,
        )
    if kind == "put":
        return black_scholes_put(
            spot_price,
            strike_price,
            time_to_maturity,
            risk_free_rate,
            volatility,
        )
    raise ValueError("option_type must be either 'call' or 'put'.")
