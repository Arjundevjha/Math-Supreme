# Calculate the median of a list of numbers
from typing import List, Union


def median(data: List[Union[int, float]]) -> float:
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    float: The median of the provided numbers.
    """
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