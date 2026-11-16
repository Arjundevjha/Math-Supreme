import pytest

from Math.Applied_Math.Physics.harmonic_oscillator import (
    angular_frequency,
    period_pendulum,
    period_spring,
    shm_acceleration,
    shm_displacement,
    shm_total_energy,
    shm_velocity,
)
from Math.Applied_Math.Physics.kepler_laws import (
    areal_velocity,
    orbital_period,
    semi_major_axis_from_period,
    vis_viva_speed,
)
from Math.Applied_Math.Physics.newton_laws_force import (
    acceleration_from_force,
    force,
    friction_force,
    gravitational_force,
    normal_force_incline,
    weight,
)
from Math.Applied_Math.Physics.projectile_motion import (
    horizontal_range,
    max_height,
    projectile_position,
    time_of_flight,
)
from Math.Applied_Math.Physics.work_energy_power import (
    elastic_potential_energy,
    kinetic_energy,
    potential_energy,
    power_from_force_velocity,
    power_from_work,
    work_done,
)
from Math.utils.math_utils import PI


class TestNewtonLawsForce:
    def test_force_and_acceleration(self):
        assert force(10, 2.5) == 25.0
        assert acceleration_from_force(25.0, 10) == 2.5

    def test_weight_normal_and_friction(self):
        assert weight(10, 9.8) == pytest.approx(98.0)
        assert normal_force_incline(10, 60, 10.0) == pytest.approx(
            50.0, rel=1e-6
        )
        assert friction_force(0.3, 100) == pytest.approx(30.0)

    def test_gravitational_force(self):
        # F = G * 1 * 1 / 1^2 = G
        assert gravitational_force(1, 1, 1, g_const=6.67430e-11) == pytest.approx(
            6.67430e-11
        )

    def test_validation(self):
        with pytest.raises(TypeError):
            force(True, 5)
        with pytest.raises(ValueError):
            force(-1, 5)
        with pytest.raises(ValueError):
            acceleration_from_force(10, 0)
        with pytest.raises(ValueError):
            normal_force_incline(10, 95)
        with pytest.raises(ValueError):
            gravitational_force(10, 10, 0)


class TestWorkEnergyPower:
    def test_work_and_energies(self):
        assert work_done(10, 5, 0) == pytest.approx(50.0, rel=1e-6)
        assert work_done(10, 5, 60) == pytest.approx(25.0, rel=1e-6)
        assert kinetic_energy(4, 3) == 18.0
        assert potential_energy(2, 5, 10) == 100.0
        assert elastic_potential_energy(200, 0.5) == 25.0

    def test_power(self):
        assert power_from_work(500, 10) == 50.0
        assert power_from_force_velocity(10, 5, 0) == pytest.approx(
            50.0, rel=1e-6
        )

    def test_validation(self):
        with pytest.raises(ValueError):
            kinetic_energy(-2, 5)
        with pytest.raises(ValueError):
            power_from_work(100, 0)
        with pytest.raises(TypeError):
            potential_energy("2", 5)


class TestHarmonicOscillator:
    def test_frequencies_and_periods(self):
        assert angular_frequency(100, 4) == pytest.approx(5.0, rel=1e-9)
        assert period_spring(4, 100) == pytest.approx(
            2.0 * PI / 5.0, rel=1e-9
        )
        assert period_pendulum(9.80665, 9.80665) == pytest.approx(
            2.0 * PI, rel=1e-9
        )

    def test_shm_kinematics_and_energy(self):
        assert shm_displacement(2.0, 3.0, 0.0) == pytest.approx(2.0, rel=1e-6)
        assert shm_velocity(2.0, 3.0, 0.0) == pytest.approx(0.0, abs=1e-9)
        assert shm_acceleration(2.0, 3.0, 0.0) == pytest.approx(
            -18.0, rel=1e-6
        )
        assert shm_total_energy(100, 0.2) == pytest.approx(2.0)

    def test_validation(self):
        with pytest.raises(ValueError):
            angular_frequency(0, 1)
        with pytest.raises(ValueError):
            period_pendulum(-1)
        with pytest.raises(ValueError):
            shm_displacement(-1, 2, 0)


class TestProjectileMotion:
    def test_ground_launch(self):
        # v0 = 20 m/s, angle = 30 deg, g = 10 m/s^2 -> vy = 10 -> T = 2s, H = 5m
        assert time_of_flight(20, 30, gravity=10.0) == pytest.approx(
            2.0, rel=1e-5
        )
        assert max_height(20, 30, gravity=10.0) == pytest.approx(5.0, rel=1e-5)
        assert horizontal_range(20, 30, gravity=10.0) == pytest.approx(
            20 * (3**0.5), rel=1e-5
        )

    def test_elevated_launch_and_position(self):
        t = time_of_flight(0, 0, gravity=10.0, initial_height=20.0)
        assert t == pytest.approx(2.0, rel=1e-6)
        x, y = projectile_position(10, 0, 1.0, gravity=10.0, initial_height=20.0)
        assert x == pytest.approx(10.0, rel=1e-6)
        assert y == pytest.approx(15.0, rel=1e-6)

    def test_validation(self):
        with pytest.raises(ValueError):
            time_of_flight(10, 95)
        with pytest.raises(ValueError):
            projectile_position(10, 45, -1)


class TestKeplerLaws:
    def test_kepler_third_law_roundtrip(self):
        # Earth-Sun approximate: a = 1.496e11 m, M = 1.989e30 kg -> T ~ 1 year
        a = 1.496e11
        m_sun = 1.989e30
        t = orbital_period(a, m_sun)
        assert t == pytest.approx(3.1558e7, rel=1e-2)
        assert semi_major_axis_from_period(t, m_sun) == pytest.approx(
            a, rel=1e-6
        )

    def test_vis_viva_and_areal_velocity(self):
        # Circular orbit r = a -> v = sqrt(GM / a)
        v = vis_viva_speed(1.0e7, 1.0e7, 5.972e24)
        assert v == pytest.approx(6313.48, rel=1e-3)
        assert areal_velocity(100, 10) == 5.0

    def test_validation(self):
        with pytest.raises(ValueError):
            vis_viva_speed(3.0, 1.0, 1.0)
        with pytest.raises(ValueError):
            orbital_period(0, 1.0)
        with pytest.raises(TypeError):
            areal_velocity(True, 1.0)
