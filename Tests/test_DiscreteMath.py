import pytest
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
        assert generate_pascals_triangle(1) == [[1]]
        assert generate_pascals_triangle(3) == [[1], [1, 1], [1, 2, 1]]
        assert generate_pascals_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    def test_generate_pascals_triangle_invalid(self):
        """Test generating an invalid Pascal's triangle."""
        with pytest.raises(ValueError, match="Number of rows must be positive."):
            generate_pascals_triangle(0)

        with pytest.raises(ValueError, match="Number of rows must be positive."):
            generate_pascals_triangle(-1)
