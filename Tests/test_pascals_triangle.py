import sys
import os
import pytest

# Add both the project root and Math/ directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
math_dir = os.path.join(parent_dir, 'Math')

if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

from Math.Discrete_Math.Combinatorics.pascals_triangle import print_pascals_triangle, generate_pascals_triangle

class TestPascalsTriangle:
    def test_print_pascals_triangle_normal(self, capsys):
        """Test printing a normal Pascal's triangle."""
        triangle = [[1], [1, 1], [1, 2, 1]]
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        expected_output = "  1  \n 1 1 \n1 2 1\n"
        assert captured.out == expected_output

    def test_print_pascals_triangle_empty(self, capsys):
        """Test printing an empty Pascal's triangle."""
        triangle = []
        print_pascals_triangle(triangle)
        captured = capsys.readouterr()

        assert captured.out == ""

    def test_generate_pascals_triangle_valid(self):
        """Test generating a valid Pascal's triangle."""
        assert generate_pascals_triangle(0) == []
        assert generate_pascals_triangle(1) == [[1]]
        assert generate_pascals_triangle(2) == [[1], [1, 1]]
        assert generate_pascals_triangle(3) == [[1], [1, 1], [1, 2, 1]]
        assert generate_pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_generate_pascals_triangle_invalid(self):
        """Test generating an invalid Pascal's triangle."""
        with pytest.raises(ValueError, match="Number of rows cannot be negative."):
            generate_pascals_triangle(-1)
        with pytest.raises(ValueError, match="Number of rows cannot be negative."):
            generate_pascals_triangle(-5)
        with pytest.raises(ValueError, match="Number of rows cannot exceed 1000"):
            generate_pascals_triangle(1001)
        with pytest.raises(ValueError, match="Number of rows cannot exceed 1000"):
            generate_pascals_triangle(2000)
