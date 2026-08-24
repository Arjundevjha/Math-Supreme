# William Shanks' formula for calculating Pi
from decimal import Decimal, getcontext

from Math.Geometry.Trigonometry.Arc_Functions.arctan import calculate_arctan


def calculate_arctan_series_shanks(x: int, precision: int) -> Decimal:
    """
    Calculate arctan(1/x) using Taylor series expansion for Shanks' formula.

    Parameters:
    x (int): The value for arctan(1/x).
    precision (int): The number of decimal places for precision.

    Returns:
    Decimal: The value of arctan(1/x).
    """
    return calculate_arctan(x, precision=precision)



def calculate_pi_shanks(precision: int = 50) -> Decimal:
    """
    Calculate Pi using William Shanks' formula (multi-term arctan formula).
    
    Formula: π/4 = 1587×arctan(1/2852) + 295×arctan(1/4193) + 593×arctan(1/4246) 
                   + 359×arctan(1/39307) + 481×arctan(1/55603) + 625×arctan(1/211050) 
                   - 708×arctan(1/390112)

    Parameters:
    precision (int): The number of decimal places for the result (default: 50).

    Returns:
    Decimal: The value of Pi to the specified precision.
    """
    # Set precision for Decimal calculations
    getcontext().prec = precision + 10
    
    # Apply William Shanks' formula
    pi_over_4 = (1587 * calculate_arctan_series_shanks(2852, precision) +
                 295 * calculate_arctan_series_shanks(4193, precision) +
                 593 * calculate_arctan_series_shanks(4246, precision) +
                 359 * calculate_arctan_series_shanks(39307, precision) +
                 481 * calculate_arctan_series_shanks(55603, precision) +
                 625 * calculate_arctan_series_shanks(211050, precision) -
                 708 * calculate_arctan_series_shanks(390112, precision))
    
    return pi_over_4 * 4