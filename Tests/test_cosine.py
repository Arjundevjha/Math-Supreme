from Math.Geometry.Trigonometry.Trig_Functions.cosine import cosine


def test_cosine_standard_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # 0 (int input)
    assert abs(cosine(0) - 1.0) < tol

    # pi / 6
    assert abs(cosine(pi / 6) - 0.8660254037844386) < tol

    # pi / 4
    assert abs(cosine(pi / 4) - 0.7071067811865476) < tol

    # pi / 3
    assert abs(cosine(pi / 3) - 0.5) < tol

    # pi / 2
    assert abs(cosine(pi / 2) - 0.0) < tol

    # pi
    assert abs(cosine(pi) - (-1.0)) < tol

    # 3pi / 2
    assert abs(cosine(3 * pi / 2) - 0.0) < tol

    # 2pi
    assert abs(cosine(2 * pi) - 1.0) < tol


def test_cosine_negative_angles():
    pi = 3.141592653589793
    tol = 1e-9

    # -pi / 6
    assert abs(cosine(-pi / 6) - 0.8660254037844386) < tol

    # -pi / 2
    assert abs(cosine(-pi / 2) - 0.0) < tol

    # -pi
    assert abs(cosine(-pi) - (-1.0)) < tol


def test_cosine_large_angles():
    pi = 3.141592653589793
    tol = 1e-5

    # 3pi
    assert abs(cosine(3 * pi) - (-1.0)) < tol

    # 4pi
    assert abs(cosine(4 * pi) - 1.0) < tol
