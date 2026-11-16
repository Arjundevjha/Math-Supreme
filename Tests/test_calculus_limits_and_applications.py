import pytest

from Math.Calculus.Applications_of_Derivatives.curve_sketching import (
    classify_critical_point,
    critical_points,
    tangent_line,
)
from Math.Calculus.Applications_of_Derivatives.optimization_problems import (
    find_extrema_on_interval,
    newton_raphson_root,
)
from Math.Calculus.Applications_of_Derivatives.related_rates import (
    circle_area_rate,
    cone_volume_rate,
    ladder_sliding_rate,
    sphere_volume_rate,
)
from Math.Calculus.Limits.evaluate_limit_rational import (
    evaluate_limit_rational,
)
from Math.Calculus.Limits.limit_infinity_cases import limit_at_infinity
from Math.utils.math_utils import PI


class TestLimits:
    def test_evaluate_limit_rational_finite_and_lhopital(self):
        # (x^2 - 1) / (x - 1) as x -> 1 == 2
        assert evaluate_limit_rational([-1, 0, 1], [-1, 1], 1) == pytest.approx(
            2.0
        )
        # (x^2 + 2x + 1) / (x + 3) as x -> 1 == 4 / 4 == 1
        assert evaluate_limit_rational([1, 2, 1], [3, 1], 1) == pytest.approx(
            1.0
        )

    def test_evaluate_limit_asymptotes(self):
        # 1 / x^2 as x -> 0 == +inf
        assert evaluate_limit_rational([1], [0, 0, 1], 0) == float("inf")
        # 1 / x as x -> 0 -> opposite-sign asymptote -> ValueError
        with pytest.raises(ValueError):
            evaluate_limit_rational([1], [0, 1], 0)

    def test_limit_at_infinity(self):
        # (2x^2 + 1) / (4x^2 - 3) -> 0.5
        assert limit_at_infinity([1, 0, 2], [-3, 0, 4]) == pytest.approx(0.5)
        # deg(P) < deg(Q) -> 0
        assert limit_at_infinity([1, 2], [1, 0, 3]) == 0.0
        # x^3 / x -> +inf as x -> -inf (even deg diff = 2)
        assert limit_at_infinity([0, 0, 0, 1], [0, 1], positive=False) == float(
            "inf"
        )
        # x^3 / 1 -> -inf as x -> -inf (odd deg diff = 3)
        assert limit_at_infinity([0, 0, 0, 1], [1], positive=False) == float(
            "-inf"
        )


class TestApplicationsOfDerivatives:
    def test_curve_sketching(self):
        # P(x) = x^2 - 4x + 3 = [3, -4, 1]
        # Tangent at x=3: P(3)=0, P'(3)=2 -> y = 2x - 6
        slope, intercept = tangent_line([3, -4, 1], 3)
        assert slope == pytest.approx(2.0)
        assert intercept == pytest.approx(-6.0)

        cps = critical_points([3, -4, 1])
        assert cps == [pytest.approx(2.0)]
        assert classify_critical_point([3, -4, 1], 2.0) == "local_minimum"

        # Cubic: x^3 - 3x = [0, -3, 0, 1] -> critical points at -1, 1
        cps_cubic = critical_points([0, -3, 0, 1], -5, 5)
        assert len(cps_cubic) == 2
        assert classify_critical_point([0, -3, 0, 1], -1) == "local_maximum"
        assert classify_critical_point([0, -3, 0, 1], 1) == "local_minimum"

    def test_optimization_and_newton(self):
        # P(x) = x^2 - 4x + 3 on [0, 3] -> min at x=2 (-1), max at x=0 (3)
        ext = find_extrema_on_interval([3, -4, 1], 0, 3)
        assert ext["min_x"] == pytest.approx(2.0)
        assert ext["min_val"] == pytest.approx(-1.0)
        assert ext["max_x"] == pytest.approx(0.0)
        assert ext["max_val"] == pytest.approx(3.0)

        # Root of x^2 - 2 = [-2, 0, 1] near 1.5 -> sqrt(2)
        root = newton_raphson_root([-2, 0, 1], 1.5)
        assert root == pytest.approx(2**0.5, rel=1e-8)

    def test_related_rates(self):
        assert circle_area_rate(5, 2) == pytest.approx(20.0 * PI)
        assert sphere_volume_rate(3, 1) == pytest.approx(36.0 * PI)
        # 5m ladder, base=3m, dx/dt=4 -> y=4m, dy/dt = -(3/4)*4 = -3
        assert ladder_sliding_rate(5, 3, 4) == pytest.approx(-3.0)
        assert cone_volume_rate(3, 4, 1, 2) == pytest.approx(
            (PI / 3.0) * (24.0 + 18.0)
        )
