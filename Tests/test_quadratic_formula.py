import os
import sys
import math
import pytest

# Add root directory to path to allow imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.quadratic_formula import solve_quadratic

class TestSolveQuadratic:
    def test_two_distinct_real_roots(self):
        """Test with an equation that has two distinct real roots: x^2 - 3x + 2 = 0"""
        # Roots should be 2 and 1. The formula returns (-b+sqrt(D))/2a and (-b-sqrt(D))/2a
        # For a=1, b=-3, c=2, D=9-8=1, roots are (3+1)/2=2, (3-1)/2=1
        root1, root2 = solve_quadratic(1, -3, 2)
        assert math.isclose(root1, 2.0, rel_tol=1e-9)
        assert math.isclose(root2, 1.0, rel_tol=1e-9)

    def test_one_real_root(self):
        """Test with an equation that has one repeated real root: x^2 - 4x + 4 = 0"""
        # Roots should be 2 and 2
        root1, root2 = solve_quadratic(1, -4, 4)
        assert math.isclose(root1, 2.0, rel_tol=1e-9)
        assert math.isclose(root2, 2.0, rel_tol=1e-9)

    def test_no_real_roots(self):
        """Test with an equation that has no real roots: x^2 + x + 1 = 0"""
        # Discriminant is negative (1 - 4 = -3)
        root1, root2 = solve_quadratic(1, 1, 1)
        assert root1 is None
        assert root2 is None

    def test_zero_a_coefficient_raises_value_error(self):
        """Test that a=0 raises ValueError"""
        with pytest.raises(ValueError, match="Coefficient 'a' cannot be zero"):
            solve_quadratic(0, 1, 1)

    def test_float_coefficients(self):
        """Test with float coefficients: 0.5x^2 - 1.5x + 1 = 0"""
        # Multiply by 2 -> x^2 - 3x + 2 = 0, roots 2 and 1
        root1, root2 = solve_quadratic(0.5, -1.5, 1.0)
        assert math.isclose(root1, 2.0, rel_tol=1e-9)
        assert math.isclose(root2, 1.0, rel_tol=1e-9)

    def test_zero_b_coefficient(self):
        """Test with b=0: x^2 - 4 = 0"""
        # Roots should be 2 and -2
        root1, root2 = solve_quadratic(1, 0, -4)
        assert math.isclose(root1, 2.0, rel_tol=1e-9)
        assert math.isclose(root2, -2.0, rel_tol=1e-9)

    def test_zero_c_coefficient(self):
        """Test with c=0: x^2 - 3x = 0"""
        # Roots should be 3 and 0
        root1, root2 = solve_quadratic(1, -3, 0)
        assert math.isclose(root1, 3.0, rel_tol=1e-9)
        assert math.isclose(root2, 0.0, abs_tol=1e-9)
