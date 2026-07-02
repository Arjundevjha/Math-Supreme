import sys
import os

# Ensure modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Math.Calculus.Integration.NumIntegration import format_polynomial_integration

def test_format_polynomial_integration_multiple_terms():
    result = format_polynomial_integration([2.0, 3.5, 1.0], [2.0, 1.0, 0.0])
    terms = [term.strip() for term in result.split('+')]
    assert "2.0x^2" in terms
    assert "3.5x" in terms
    assert "1.0" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_zero():
    result = format_polynomial_integration([5.0], [0.0])
    terms = [term.strip() for term in result.split('+')]
    assert "5.0" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_one():
    result = format_polynomial_integration([2.5], [1.0])
    terms = [term.strip() for term in result.split('+')]
    assert "2.5x" in terms
    assert "C" in terms

def test_format_polynomial_integration_single_term_power_gt_one():
    result = format_polynomial_integration([4.0], [3.0])
    terms = [term.strip() for term in result.split('+')]
    assert "4.0x^3" in terms
    assert "C" in terms

def test_format_polynomial_integration_empty():
    result = format_polynomial_integration([], [])
    assert result.strip() == "+ C" or result.strip() == "C"
