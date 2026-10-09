# Finding an equation of a line given two points

from typing import Union


def linear_eqn(
    x1: Union[int, float],
    y1: Union[int, float],
    x2: Union[int, float],
    y2: Union[int, float],
) -> str:
    """
    Calculate the equation of a line given two points (x1, y1) and (x2, y2).

    Parameters:
    x1, y1: Coordinates of the first point.
    x2, y2: Coordinates of the second point.

    Returns:
    str: The equation of the line in the form "y = mx + b".
    """
    # Security: Validate parameter types and magnitude limits to prevent DoS via OverflowError
    for coord in (x1, y1, x2, y2):
        if isinstance(coord, bool) or not isinstance(coord, (int, float)):
            raise TypeError("Coordinates must be numeric values (int or float).")
        if abs(coord) > 1e300:
            raise ValueError(
                "Coordinates exceed maximum allowed magnitude limit of 1e300."
            )

    if x1 == x2:
        raise ValueError("The x-coordinates cannot be the same (vertical line).")

    # Calculate slope (m)
    m = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept (b)
    b = y1 - m * x1

    return f"y = {m}x + {b}"
