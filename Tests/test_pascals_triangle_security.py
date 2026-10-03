import unittest
from Math.Discrete_Math.Combinatorics.pascals_triangle import (
    generate_pascals_triangle,
    print_pascals_triangle,
)


class TestPascalsTriangleSecurity(unittest.TestCase):
    def test_generate_pascals_triangle_invalid_types(self):
        # Non-integer types should raise TypeError
        with self.assertRaises(TypeError):
            generate_pascals_triangle("10")
        with self.assertRaises(TypeError):
            generate_pascals_triangle(10.5)
        with self.assertRaises(TypeError):
            generate_pascals_triangle(None)

    def test_generate_pascals_triangle_boolean_rejection(self):
        # Booleans inherit from int in Python, but must be rejected
        with self.assertRaises(TypeError):
            generate_pascals_triangle(True)
        with self.assertRaises(TypeError):
            generate_pascals_triangle(False)

    def test_generate_pascals_triangle_negative_input(self):
        # Negative rows should raise ValueError
        with self.assertRaisesRegex(ValueError, "Number of rows cannot be negative."):
            generate_pascals_triangle(-1)
        with self.assertRaises(ValueError):
            generate_pascals_triangle(-100)

    def test_generate_pascals_triangle_upper_bound_limit(self):
        # num_rows > 1000 should raise ValueError to prevent DoS resource exhaustion
        with self.assertRaisesRegex(
            ValueError, "Number of rows exceeds maximum limit of 1000."
        ):
            generate_pascals_triangle(1001)

    def test_generate_pascals_triangle_valid_boundaries(self):
        # Boundary 0 -> empty list
        self.assertEqual(generate_pascals_triangle(0), [])
        # Upper boundary 1000 should generate without error and have 1000 rows
        res = generate_pascals_triangle(1000)
        self.assertEqual(len(res), 1000)

    def test_print_pascals_triangle_empty(self):
        # Empty triangle should handle gracefully
        self.assertIsNone(print_pascals_triangle([]))

    def test_print_pascals_triangle_invalid_types(self):
        # Invalid container or row types should raise TypeError
        with self.assertRaises(TypeError):
            print_pascals_triangle("invalid")
        with self.assertRaises(TypeError):
            print_pascals_triangle([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
