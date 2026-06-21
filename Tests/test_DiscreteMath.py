import pytest
from Math.Discrete_Math.Number_Theory.partitions_approximation import partition_approximation
from Math.Discrete_Math.Number_Theory.partitions import partition

def test_partition_approximation_edge_cases():
    """Test edge cases for partition approximation."""
    # Test zero
    assert partition_approximation(0) == 1

    # Test negative numbers
    with pytest.raises(ValueError, match="Number must be a non-negative integer."):
        partition_approximation(-1)

def test_partition_approximation_small_values():
    """Test small values to ensure the formula computes successfully."""
    # We test values to see if they roughly equal actual partitions

    # The approximation formula is quite poor for very small n, but we can verify the output
    # p(1) ≈ 1
    assert partition_approximation(1) == 1

    # p(2) ≈ 2
    assert partition_approximation(2) == 2

    # p(3) = 3, approx is 4
    assert partition_approximation(3) == 4

    # p(4) = 5, approx is 6
    assert partition_approximation(4) == 6

    # p(5) = 7, approx is 8
    assert partition_approximation(5) == 8

def test_partition_approximation_large_values():
    """Test larger values to ensure the formula produces expected output."""
    # p(10) = 42, approx is 48
    assert partition_approximation(10) == 48

    # p(20) = 627, approx is 692
    assert partition_approximation(20) == 692

    # p(50) = 204226, approx is 217590
    assert partition_approximation(50) == 217590

    # p(100) = 190569292, approx is 199280893
    assert partition_approximation(100) == 199280893

def test_partition_approximation_relative_error():
    """Test that the approximation improves relative to the exact partition function."""
    # Compute relative error = |approx - exact| / exact
    n_values = [10, 20, 50, 100]
    errors = []

    for n in n_values:
        approx = partition_approximation(n)
        exact = partition(n)
        relative_error = abs(approx - exact) / exact
        errors.append(relative_error)

    # Relative error should generally decrease as n gets larger
    # Let's ensure the error at n=100 is less than error at n=10
    assert errors[-1] < errors[0]

    # And at n=100, the relative error should be < 5%
    assert errors[-1] < 0.05
