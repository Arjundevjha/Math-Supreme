# Calculate the mode (most frequent value) of a list of numbers
from collections import Counter
from typing import List, Sequence, Union


def mode(data: Sequence[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    data (Sequence[Union[int, float]]): A list or tuple of numerical values (integers or floats).

    Returns:
    Union[int, float, List[Union[int, float]]]: The mode of the provided numbers. 
    If there are multiple modes, a list of modes is returned.
    """
    # Security: Validate input sequence type and element types
    if not isinstance(data, (list, tuple)):
        raise TypeError("Data must be a list or tuple of numbers.")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in data must be integers or floats.")

    if not data:
        return 0.0

    # Count frequency of each number
    frequency = Counter(data)

    # Find the maximum frequency and all numbers with that frequency
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes
