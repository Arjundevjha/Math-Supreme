import pytest
import math
import sys
import os

# Add the parent directory of Math so Math can be found, and Math itself so Geometry can be found
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, base_dir)
sys.path.insert(0, os.path.join(base_dir, 'Math'))

from Math.Calculus.Integration.TrigIntegration import integrate_sin, integrate_cos

class TestTrigIntegration:
    def test_integrate_sin_basic(self):
        """Test integral of sin(x) from 0 to pi = 2"""
        result = integrate_sin(0, math.pi)
        assert math.isclose(result, 2.0, rel_tol=1e-5)

    def test_integrate_sin_zero(self):
        """Test integral of sin(x) from 0 to 0 = 0"""
        result = integrate_sin(0, 0)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_full_period(self):
        """Test integral of sin(x) from 0 to 2pi = 0"""
        result = integrate_sin(0, 2 * math.pi)
        assert math.isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_negative_bounds(self):
        """Test integral of sin(x) from -pi to 0 = -2"""
        result = integrate_sin(-math.pi, 0)
        assert math.isclose(result, -2.0, rel_tol=1e-5)

    def test_integrate_cos_basic(self):
        """Test integral of cos(x) from 0 to pi/2 = 1"""
        result = integrate_cos(0, math.pi / 2)
        assert math.isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_cos_zero(self):
        """Test integral of cos(x) from 0 to 0 = 0"""
        result = integrate_cos(0, 0)
        assert math.isclose(result, 0.0, abs_tol=1e-9)
