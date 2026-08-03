from Math.Calculus.Differentiation.second_derivatives import second_derivative

def test_second_derivative_quadratic():
    # 3x^2 + 2x + 1 -> y'' = 6
    coeffs = [3, 2, 1]
    powers = [2, 1, 0]
    assert second_derivative(coeffs, powers) == [(6, 0)]

def test_second_derivative_cubic():
    # 4x^3 - 2x^2 + x - 5 -> y'' = 24x - 4
    coeffs = [4, -2, 1, -5]
    powers = [3, 2, 1, 0]
    assert second_derivative(coeffs, powers) == [(24, 1), (-4, 0)]

def test_second_derivative_constant():
    # y = 5 -> y'' = 0 (represented as empty list)
    coeffs = [5]
    powers = [0]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_linear():
    # y = 3x -> y'' = 0 (represented as empty list)
    coeffs = [3]
    powers = [1]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_empty():
    assert second_derivative([], []) == []

def test_second_derivative_floats():
    # 2.5x^4 -> y'' = 30.0x^2
    coeffs = [2.5]
    powers = [4.0]
    assert second_derivative(coeffs, powers) == [(30.0, 2.0)]

def test_second_derivative_negative_powers():
    # Based on the current implementation, powers <= 0 are ignored
    # d/dx(3x^-2) -> empty list since power is not > 0
    coeffs = [3]
    powers = [-2]
    assert second_derivative(coeffs, powers) == []

    # Another test case for negative powers
    coeffs = [3, 2]
    powers = [-2, -1]
    assert second_derivative(coeffs, powers) == []

def test_second_derivative_negative_coeffs():
    # -3x^4 -> y'' = -36x^2
    coeffs = [-3]
    powers = [4]
    assert second_derivative(coeffs, powers) == [(-36, 2)]

def test_second_derivative_fractional_powers():
    # x^2.5 -> y'' = 3.75x^0.5
    coeffs = [1]
    powers = [2.5]
    assert second_derivative(coeffs, powers) == [(3.75, 0.5)]

def test_second_derivative_zero_coeffs():
    # 0x^3 -> y'' = 0x^1
    coeffs = [0]
    powers = [3]
    assert second_derivative(coeffs, powers) == [(0, 1)]

    # 0x^3 + 0x^2 -> y'' = 0x
    coeffs = [0, 0]
    powers = [3, 2]
    assert second_derivative(coeffs, powers) == [(0, 1), (0, 0)]

def test_second_derivative_mixed():
    # 3x^3 + 2x^2 + 5x - 4x^-2 -> y'' = 18x + 4
    coeffs = [3, 2, 5, -4]
    powers = [3, 2, 1, -2]
    assert second_derivative(coeffs, powers) == [(18, 1), (4, 0)]

def test_second_derivative_unordered_powers():
    # x + 4x^3 - 2x^2 - 5 -> y'' = 24x - 4
    coeffs = [1, 4, -2, -5]
    powers = [1, 3, 2, 0]
    assert second_derivative(coeffs, powers) == [(24, 1), (-4, 0)]

def test_second_derivative_mismatched_lengths():
    # zip() behavior handles mismatched lengths by stopping at the shortest
    coeffs = [4, -2]
    powers = [3]
    assert second_derivative(coeffs, powers) == [(24, 1)]

    assert second_derivative([1, 2], [3]) == [(6, 1)]

def test_second_derivative_large_numbers():
    # 1000x^1000 -> y'' = 1000 * 1000 * 999 x^998 = 999000000x^998
    coeffs = [1000]
    powers = [1000]
    assert second_derivative(coeffs, powers) == [(999000000, 998)]

def test_second_derivative_fractional_powers_skipped():
    # Power becomes <= 0 after first derivative
    assert second_derivative([4], [0.5]) == []

def test_second_derivative_mixed_skipped():
    # Mix of valid and skipped powers
    assert second_derivative([3, 2, 1], [3, 0.5, -1]) == [(18, 1)]

def test_second_derivative_mixed_terms():
    # 2x^3 + 5x^0 + 4x^-1 -> y'' = 12x
    coeffs = [2, 5, 4]
    powers = [3, 0, -1]
    assert second_derivative(coeffs, powers) == [(12, 1)]

def test_second_derivative_with_negative_coeff_and_positive_power():
    # -2x^2 -> -4x -> -4
    coeffs = [-2]
    powers = [2]
    assert second_derivative(coeffs, powers) == [(-4, 0)]

def test_second_derivative_with_large_powers():
    # 3x^100 -> 300x^99 -> 29700x^98
    coeffs = [3]
    powers = [100]
    assert second_derivative(coeffs, powers) == [(29700, 98)]

def test_second_derivative_with_power_one():
    # 5x^1 -> 5 -> 0
    coeffs = [5]
    powers = [1]
    assert second_derivative(coeffs, powers) == []
