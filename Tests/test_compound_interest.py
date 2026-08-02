import unittest
import sys
import os
import math


from Math.Applied_Math.Finance.Compund_intrest import compound_interest

class TestCompoundInterest(unittest.TestCase):
    def test_regular_compound_intervals(self):
        # Annually
        self.assertTrue(math.isclose(compound_interest(1000, 5, 10, 1), 1628.894626777442))

        # Semi-annually
        self.assertTrue(math.isclose(compound_interest(1000, 5, 10, 2), 1638.616440288897))

        # Quarterly
        self.assertTrue(math.isclose(compound_interest(1000, 5, 10, 4), 1643.6194634289874))

        # Monthly
        self.assertTrue(math.isclose(compound_interest(1000, 5, 10, 12), 1647.00949769028))

        # Daily
        self.assertTrue(math.isclose(compound_interest(1000, 5, 10, 365), 1648.6648137652346))

    def test_zero_time_or_rate(self):
        # 0 time
        self.assertTrue(math.isclose(compound_interest(1000, 5, 0, 1), 1000.0))

        # 0 interest rate
        self.assertTrue(math.isclose(compound_interest(1000, 0, 10, 1), 1000.0))

        # 0 principal
        self.assertTrue(math.isclose(compound_interest(0, 5, 10, 1), 0.0))

    def test_value_errors(self):
        # Negative principal
        with self.assertRaises(ValueError):
            compound_interest(-1000, 5, 10, 1)

        # Negative interest rate
        with self.assertRaises(ValueError):
            compound_interest(1000, -5, 10, 1)

        # Negative time
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, -10, 1)

if __name__ == '__main__':
    unittest.main()
