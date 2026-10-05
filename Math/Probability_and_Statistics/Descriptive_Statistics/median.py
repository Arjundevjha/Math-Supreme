# Calculate the median of a list of numbers
from typing import List, Sequence, Union


def median(data: Sequence[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (Sequence[Union[int, float]]): A list or tuple of numerical values (integers or floats).

    Returns:
    float: The median of the provided numbers.
    """
    # Security: Validate input sequence type and element types
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple of numbers.")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in data):
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
