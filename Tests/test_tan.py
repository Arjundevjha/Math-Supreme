from Math.Geometry.Trigonometry.Trig_Functions.tan import tangent


def test_tangent_standard_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # 0 radians
    assert abs(tangent(0) - 0.0) < tol
    assert abs(tangent(0.0) - 0.0) < tol

    # pi / 6 radians (tan(pi/6) = 1 / sqrt(3) ≈ 0.5773502691896257)
    assert abs(tangent(pi / 6) - 0.5773502691896257) < tol

    # pi / 4 radians (tan(pi/4) = 1.0)
    assert abs(tangent(pi / 4) - 1.0) < tol

    # pi / 3 radians (tan(pi/3) = sqrt(3) ≈ 1.7320508075688772)
    assert abs(tangent(pi / 3) - 1.7320508075688772) < tol

    # pi radians (tan(pi) = 0.0)
    assert abs(tangent(pi) - 0.0) < tol


def test_tangent_negative_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # -pi / 6
    assert abs(tangent(-pi / 6) - (-0.5773502691896257)) < tol

    # -pi / 4
    assert abs(tangent(-pi / 4) - (-1.0)) < tol

    # -pi
    assert abs(tangent(-pi) - 0.0) < tol


def test_tangent_near_singularities():
    pi = 3.141592653589793

    # At pi / 2 and 3 * pi / 2, cosine is close to 0 (limited by float precision of pi),
    # so tangent yields a very large magnitude result.
    val_pi_over_2 = tangent(pi / 2)
    assert abs(val_pi_over_2) > 1e15

    val_3pi_over_2 = tangent(3 * pi / 2)
    assert abs(val_3pi_over_2) > 1e15
