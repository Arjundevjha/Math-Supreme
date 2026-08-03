from Math.Calculus.Integration.test_helper import isclose
from Math.Geometry.Trigonometry.Trig_Functions.sine import sine
from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine
import pytest
from Math.Calculus.Integration.TrigIntegration import integrate_sin, integrate_cos

class TestTrigIntegration:
    # --- Tests for integrate_sin ---
    def test_integrate_sin_basic(self):
        """Test integral of sin(x) from 0 to pi/2 = 1"""
        result = integrate_sin(0, 3.141592653589793 / 2)
        assert isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_sin_half_period(self):
        """Test integral of sin(x) from 0 to pi = 2"""
        result = integrate_sin(0, 3.141592653589793)
        assert isclose(result, 2.0, rel_tol=1e-5)

    def test_integrate_sin_zero(self):
        """Test integral of sin(x) from 0 to 0 = 0"""
        result = integrate_sin(0, 0)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_full_period(self):
        """Test integral of sin(x) from 0 to 2pi = 0"""
        result = integrate_sin(0, 2 * 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_sin_negative_bounds(self):
        """Test integral of sin(x) from -pi to 0 = -2"""
        result = integrate_sin(-3.141592653589793, 0)
        assert isclose(result, -2.0, rel_tol=1e-5)

    def test_integrate_sin_negative_bounds_half_pi(self):
        """Test integral of sin(x) from -pi/2 to 0 = -1"""
        result = integrate_sin(-3.141592653589793 / 2, 0)
        assert isclose(result, -1.0, rel_tol=1e-5)

    def test_integrate_sin_reversed_bounds(self):
        """Test integral of sin(x) from pi to 0 = -2"""
        result = integrate_sin(3.141592653589793, 0)
        assert isclose(result, -2.0, rel_tol=1e-5)

    def test_integrate_sin_fractional_pi(self):
        """Test integral of sin(x) from 0 to pi/3 = 0.5"""
        result = integrate_sin(0, 3.141592653589793 / 3)
        assert isclose(result, 0.5, rel_tol=1e-5)

    def test_integrate_sin_float_bounds(self):
        """Test integral of sin(x) from 0.5 to 1.5"""
        result = integrate_sin(0.5, 1.5)
        expected = -cosine(1.5) + cosine(0.5)
        assert isclose(result, expected, rel_tol=1e-5)

    def test_integrate_sin_same_bounds(self):
        """Integral of sin(x) from a to a should be 0"""
        result = integrate_sin(3.141592653589793, 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-5)

    # --- Tests for integrate_cos ---
    def test_integrate_cos_basic(self):
        """Test integral of cos(x) from 0 to pi/2 = 1"""
        result = integrate_cos(0, 3.141592653589793 / 2)
        assert isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_cos_zero(self):
        """Test integral of cos(x) from 0 to 0 = 0"""
        result = integrate_cos(0, 0)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_full_period(self):
        """Test integral of cos(x) from 0 to 2pi = 0"""
        result = integrate_cos(0, 2 * 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_negative_bounds(self):
        """Test integral of cos(x) from -pi/2 to 0 = 1"""
        result = integrate_cos(-3.141592653589793 / 2, 0)
        assert isclose(result, 1.0, rel_tol=1e-5)

    def test_integrate_cos_negative_bounds_pi(self):
        """Test integral of cos(x) from -pi to 0 = 0"""
        result = integrate_cos(-3.141592653589793, 0)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_half_period(self):
        """Test integral of cos(x) from -pi/2 to pi/2 = 2"""
        result = integrate_cos(-3.141592653589793 / 2, 3.141592653589793 / 2)
        assert isclose(result, 2.0, rel_tol=1e-5)

    def test_integrate_cos_half_period_zero_to_pi(self):
        """Test integral of cos(x) from 0 to pi = 0"""
        result = integrate_cos(0, 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_same_bounds(self):
        """Test integral of cos(x) from a to a = 0"""
        result = integrate_cos(3.141592653589793, 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-9)

    def test_integrate_cos_reversed_bounds(self):
        """Test integral of cos(x) from pi/2 to 0 = -1"""
        result = integrate_cos(3.141592653589793 / 2, 0)
        assert isclose(result, -1.0, rel_tol=1e-5)

    def test_integrate_cos_fractional_bounds(self):
        """Test integral of cos(x) from pi/6 to pi/3 = (sqrt(3)/2 - 1/2)"""
        result = integrate_cos(3.141592653589793 / 6, 3.141592653589793 / 3)
        expected = sine(3.141592653589793 / 3) - sine(3.141592653589793 / 6)
        assert isclose(result, expected, rel_tol=1e-5)

    def test_integrate_cos_multiple_periods(self):
        """Test integral of cos(x) over multiple periods"""
        result = integrate_cos(-2 * 3.141592653589793, 4 * 3.141592653589793)
        assert isclose(result, 0.0, abs_tol=1e-9)
