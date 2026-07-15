import os
import sys
import pytest
import cmath

# Add root directory to path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Math.Algebra.Polynomials.cubic_formula import cubic_formula

def verify_roots(expected_roots, actual_roots):
    """
    Helper function to verify roots, accounting for multiplicity and floating point inaccuracies.
    Ensures that each expected root has exactly one corresponding actual root.
    """
    roots_list = list(actual_roots)
    for expected in expected_roots:
        matched = False
        for i, root in enumerate(roots_list):
            if cmath.isclose(expected, root, rel_tol=1e-9, abs_tol=1e-9):
                roots_list.pop(i)
                matched = True
                break
        assert matched, f"Expected root {expected} not found. Remaining unmatched actual roots: {roots_list}"
    assert len(roots_list) == 0, f"Unexpected extra roots found: {roots_list}"

def test_cubic_formula_real_roots():
    # Equation: x^3 - 6x^2 + 11x - 6 = 0
    # Roots: 1, 2, 3
    roots = cubic_formula(1, -6, 11, -6)
    expected_roots = [1, 2, 3]

    verify_roots(expected_roots, roots)

def test_cubic_formula_complex_roots():
    # Equation: x^3 - 1 = 0
    # Roots: 1, -1/2 + sqrt(3)i/2, -1/2 - sqrt(3)i/2
    roots = cubic_formula(1, 0, 0, -1)

    expected_roots = [
        1,
        complex(-0.5, cmath.sqrt(3).real / 2),
        complex(-0.5, -cmath.sqrt(3).real / 2)
    ]

    verify_roots(expected_roots, roots)

def test_cubic_formula_zero_roots():
    # Equation: x^3 = 0
    # Roots: 0, 0, 0
    roots = cubic_formula(1, 0, 0, 0)
    expected_roots = [0, 0, 0]

    verify_roots(expected_roots, roots)

def test_cubic_formula_value_error():
    # a = 0 should raise ValueError
    with pytest.raises(ValueError, match="Coefficient 'a' cannot be zero for a cubic equation."):
        cubic_formula(0, 1, 1, 1)


def test_cubic_formula_double_root():
    # Equation: x^3 - 3x + 2 = 0
    # Roots: 1, 1, -2
    roots = cubic_formula(1, 0, -3, 2)
    expected_roots = [1, 1, -2]

    verify_roots(expected_roots, roots)

def test_cubic_formula_float_coefficients():
    # Equation: 2.5x^3 - 7.5x^2 + 7.5x - 2.5 = 0
    # Roots: 1, 1, 1
    roots = cubic_formula(2.5, -7.5, 7.5, -2.5)
    expected_roots = [1, 1, 1]

    verify_roots(expected_roots, roots)

if __name__ == '__main__':
    pytest.main([__file__])
