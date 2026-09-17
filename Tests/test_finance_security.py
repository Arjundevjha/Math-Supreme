import unittest
import pytest
from Math.Applied_Math.Finance.Simple_Intrest import simple_interest
from Math.Applied_Math.Finance.Compund_intrest import compound_interest


class TestFinanceSecurity(unittest.TestCase):
    def test_simple_interest_invalid_types(self):
        # Invalid parameter types (str, None, bool)
        with self.assertRaises(TypeError):
            simple_interest("1000", 5, 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, None, 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, 5, True)
        with self.assertRaises(TypeError):
            simple_interest(False, 5, 2)

    def test_simple_interest_resource_limit(self):
        # Time upper bound check
        with self.assertRaises(ValueError):
            simple_interest(1000, 5, 100001)

    def test_compound_interest_invalid_types(self):
        # Invalid parameter types (str, None, bool)
        with self.assertRaises(TypeError):
            compound_interest("1000", 5, 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, "5", 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, None, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, 2, "12")
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, True, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, 2, False)

    def test_compound_interest_resource_limit(self):
        # Exceeding frequency or exponent bounds
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, 2, 100001)
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, 100001, 1)
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, 200, 1000)


if __name__ == "__main__":
    unittest.main()
