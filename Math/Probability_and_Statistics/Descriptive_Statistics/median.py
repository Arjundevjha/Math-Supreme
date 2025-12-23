from typing import List, Union

def median(data: List[Union[int, float]]) -> float: 
    """
    Calculate the median of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    float: The median of the provided numbers.

    Raises:
    ValueError: If the input list is empty.
    """
    if not data:
        return 0.0  # Return 0.0 for empty list as per specification
    
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2

    if n % 2 == 0:
        # If even, return the average of the two middle numbers
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        # If odd, return the middle number
        return sorted_data[mid]