"""Module for calculating the median of a list or tuple of numbers."""
# pylint: disable=duplicate-code,no-else-return
from typing import List, Union


def median(data: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    float: The median of the provided numbers.
    """
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input data must be a list or tuple.")
    if len(data) > 1000000:
        raise ValueError("Input data length exceeds maximum limit of 1,000,000.")
    for x in data:
        if isinstance(x, bool) or not isinstance(x, (int, float)):
            raise TypeError("All elements in data must be integers or floats.")

    if not data:
        return 0.0

    # Sort the data to find the middle value(s)
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        # If even, return the average of the two middle numbers
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # If odd, return the middle number
        return sorted_data[mid]
