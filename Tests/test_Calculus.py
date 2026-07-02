import pytest
import math
import sys
import os

# Add Math as root to path for the internal modules of Math to resolve
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Math')))

from Math.Calculus.Integration.TrigIntegration import integrate_cos, integrate_sin

def test_integrate_cos_basic():
    # Integral of cos(x) from 0 to pi/2 should be sin(pi/2) - sin(0) = 1 - 0 = 1
    result = integrate_cos(0, math.pi / 2)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_cos_full_period():
    # Integral of cos(x) from 0 to 2*pi should be 0
    result = integrate_cos(0, 2 * math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_cos_negative_bounds():
    # Integral of cos(x) from -pi/2 to 0 should be sin(0) - sin(-pi/2) = 0 - (-1) = 1
    result = integrate_cos(-math.pi / 2, 0)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_cos_same_bounds():
    # Integral of cos(x) from a to a should be 0
    result = integrate_cos(math.pi, math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_sin_basic():
    # Integral of sin(x) from 0 to pi/2 should be -cos(pi/2) - (-cos(0)) = 0 + 1 = 1
    result = integrate_sin(0, math.pi / 2)
    assert math.isclose(result, 1.0, rel_tol=1e-5)

def test_integrate_sin_full_period():
    # Integral of sin(x) from 0 to 2*pi should be 0
    result = integrate_sin(0, 2 * math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)

def test_integrate_sin_negative_bounds():
    # Integral of sin(x) from -pi/2 to 0 should be -cos(0) - (-cos(-pi/2)) = -1 - 0 = -1
    result = integrate_sin(-math.pi / 2, 0)
    assert math.isclose(result, -1.0, rel_tol=1e-5)

def test_integrate_sin_same_bounds():
    # Integral of sin(x) from a to a should be 0
    result = integrate_sin(math.pi, math.pi)
    assert math.isclose(result, 0.0, abs_tol=1e-5)
