# Calculate the mode (most frequent value) of a list of numbers
from typing import List, Union


def mode(data: List[Union[int, float]]) -> Union[int, float, List[Union[int, float]]]:
    """
    Calculate the mode of a list of numbers.

    Parameters:
    data (List[Union[int, float]]): A list of numerical values (integers or floats).

    Returns:
    Union[int, float, List[Union[int, float]]]: The mode of the provided numbers. 
    If there are multiple modes, a list of modes is returned.
    """
    if not data:
        return 0.0
    
    # Count frequency of each number
    frequency = {}
    for number in data:
        frequency[number] = frequency.get(number, 0) + 1

    # Find the maximum frequency and all numbers with that frequency
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    if len(modes) == 1:
        return modes[0]
    else:
        return modes