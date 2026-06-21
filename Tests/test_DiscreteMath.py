import pytest
from Math.Discrete_Math.Combinatorics.pascals_triangle import generate_pascals_triangle

def test_generate_pascals_triangle():
    # Edge case: non-positive number of rows
    assert generate_pascals_triangle(0) == []

    with pytest.raises(ValueError, match="Number of rows cannot be negative."):
        generate_pascals_triangle(-5)

    # Base cases
    assert generate_pascals_triangle(1) == [[1]]
    assert generate_pascals_triangle(2) == [[1], [1, 1]]

    # Typical case
    assert generate_pascals_triangle(5) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
