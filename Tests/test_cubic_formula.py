import os
import sys
import pytest
import cmath

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.cubic_formula import cubic_formula

def test_cubic_formula_real_roots():
    # Equation: x^3 - 6x^2 + 11x - 6 = 0
    # Roots: 1, 2, 3
    roots = cubic_formula(1, -6, 11, -6)
    expected_roots = [1, 2, 3]

    # Check that all expected roots are found (allowing for floating point inaccuracy and complex representation)
    for expected in expected_roots:
        assert any(cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9) for root in roots)

def test_cubic_formula_complex_roots():
    # Equation: x^3 - 1 = 0
    # Roots: 1, -1/2 + sqrt(3)i/2, -1/2 - sqrt(3)i/2
    roots = cubic_formula(1, 0, 0, -1)

    expected_roots = [
        1,
        complex(-0.5, cmath.sqrt(3).real / 2),
        complex(-0.5, -cmath.sqrt(3).real / 2)
    ]

    for expected in expected_roots:
        assert any(cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9) for root in roots)

def test_cubic_formula_zero_roots():
    # Equation: x^3 = 0
    # Roots: 0, 0, 0
    roots = cubic_formula(1, 0, 0, 0)
    for root in roots:
        assert cmath.isclose(0, root, rel_tol=1e-9, abs_tol=1e-9)

def test_cubic_formula_value_error():
    # a = 0 should raise ValueError
    with pytest.raises(ValueError, match="Coefficient 'a' cannot be zero for a cubic equation."):
        cubic_formula(0, 1, 1, 1)

if __name__ == '__main__':
    pytest.main([__file__])
