import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)
math_dir = os.path.join(root_dir, 'Math')
if math_dir not in sys.path:
    sys.path.insert(0, math_dir)

import pytest
import math
from Math.Applied_Math.Finance.Simple_Intrest import simple_interest

def test_simple_interest_basic():
    # P=1000, R=5, T=2
    # I = 1000*5*2/100 = 100
    # Total = 1100
    assert simple_interest(1000, 5, 2) == 1100

def test_simple_interest_floats():
    # P=1000.50, R=4.5, T=1.5
    # I = 1000.50*4.5*1.5/100 = 67.53375
    # Total = 1068.03375
    res = simple_interest(1000.50, 4.5, 1.5)
    assert math.isclose(res, 1068.03375, rel_tol=1e-9)

def test_simple_interest_zero_time():
    assert simple_interest(1000, 5, 0) == 1000

def test_simple_interest_zero_rate():
    assert simple_interest(1000, 0, 2) == 1000

def test_simple_interest_zero_principal():
    assert simple_interest(0, 5, 2) == 0

def test_simple_interest_negative_principal():
    with pytest.raises(ValueError, match="Principal amount, interest rate, and time must be non-negative."):
        simple_interest(-1000, 5, 2)

def test_simple_interest_negative_rate():
    with pytest.raises(ValueError, match="Principal amount, interest rate, and time must be non-negative."):
        simple_interest(1000, -5, 2)

def test_simple_interest_negative_time():
    with pytest.raises(ValueError, match="Principal amount, interest rate, and time must be non-negative."):
        simple_interest(1000, 5, -2)
