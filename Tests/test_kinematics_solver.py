import pytest

from Math.Applied_Math.Physics.kinematics_solver import (
    displacement,
    displacement_avg_velocity,
    final_velocity,
    final_velocity_squared,
    solve_kinematics,
)


class TestKinematicsBasicFormulas:
    def test_final_velocity(self):
        assert final_velocity(10, 2, 5) == 20.0
        assert final_velocity(0, -9.8, 2) == pytest.approx(-19.6)

    def test_displacement(self):
        assert displacement(0, 9.8, 2) == pytest.approx(19.6)
        assert displacement(5, 2, 3) == pytest.approx(24.0)

    def test_displacement_avg_velocity(self):
        assert displacement_avg_velocity(10, 20, 5) == pytest.approx(75.0)

    def test_final_velocity_squared(self):
        assert final_velocity_squared(3, 2, 4) == pytest.approx(25.0)


class TestSolveKinematicsAllCases:
    # Reference state: u = 4, a = 2, t = 3 -> v = 10, s = 21
    def _assert_reference(self, result):
        assert result["displacement"] == pytest.approx(21.0, rel=1e-9)
        assert result["initial_velocity"] == pytest.approx(4.0, rel=1e-9)
        assert result["final_velocity"] == pytest.approx(10.0, rel=1e-9)
        assert result["acceleration"] == pytest.approx(2.0, rel=1e-9)
        assert result["time"] == pytest.approx(3.0, rel=1e-9)

    def test_case_u_a_t(self):
        self._assert_reference(
            solve_kinematics(initial_velocity=4, acceleration=2, time=3)
        )

    def test_case_v_a_t(self):
        self._assert_reference(
            solve_kinematics(final_velocity_val=10, acceleration=2, time=3)
        )

    def test_case_u_v_t(self):
        self._assert_reference(
            solve_kinematics(
                initial_velocity=4, final_velocity_val=10, time=3
            )
        )

    def test_case_u_v_a(self):
        self._assert_reference(
            solve_kinematics(
                initial_velocity=4, final_velocity_val=10, acceleration=2
            )
        )

    def test_case_s_u_t(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21, initial_velocity=4, time=3
            )
        )

    def test_case_s_v_t(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21, final_velocity_val=10, time=3
            )
        )

    def test_case_s_u_v(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21,
                initial_velocity=4,
                final_velocity_val=10,
            )
        )

    def test_case_s_u_a(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21, initial_velocity=4, acceleration=2
            )
        )

    def test_case_s_v_a(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21, final_velocity_val=10, acceleration=2
            )
        )

    def test_case_s_a_t(self):
        self._assert_reference(
            solve_kinematics(
                displacement_val=21, acceleration=2, time=3
            )
        )

    def test_zero_acceleration_cases(self):
        res = solve_kinematics(
            displacement_val=50, initial_velocity=10, acceleration=0
        )
        assert res["time"] == pytest.approx(5.0)
        assert res["final_velocity"] == pytest.approx(10.0)


class TestKinematicsValidation:
    def test_invalid_types(self):
        with pytest.raises(TypeError):
            final_velocity("10", 2, 5)
        with pytest.raises(TypeError):
            displacement(True, 2, 5)
        with pytest.raises(TypeError):
            solve_kinematics(
                initial_velocity=4, acceleration=False, time=3
            )

    def test_invalid_values(self):
        with pytest.raises(ValueError):
            final_velocity(10, 2, -1)
        with pytest.raises(ValueError):
            displacement(float("nan"), 2, 1)
        with pytest.raises(ValueError):
            solve_kinematics(initial_velocity=4, acceleration=2)
        with pytest.raises(ValueError):
            solve_kinematics(
                displacement_val=21,
                initial_velocity=4,
                final_velocity_val=10,
                acceleration=2,
            )
        with pytest.raises(ValueError):
            solve_kinematics(
                displacement_val=10, initial_velocity=0, acceleration=-5
            )
        with pytest.raises(ValueError):
            solve_kinematics(
                initial_velocity=10, final_velocity_val=5, acceleration=2
            )
