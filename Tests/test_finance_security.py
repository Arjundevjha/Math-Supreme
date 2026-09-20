import unittest
import pytest
from Math.Applied_Math.Finance.Simple_Intrest import simple_interest
from Math.Applied_Math.Finance.Compund_intrest import compound_interest


class TestFinanceSecurity(unittest.TestCase):
    def test_simple_interest_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            simple_interest("1000", 5, 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, "5", 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, 5, "2")
        with self.assertRaises(TypeError):
            simple_interest(None, 5, 2)

        # Booleans should raise TypeError
        with self.assertRaises(TypeError):
            simple_interest(True, 5, 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, False, 2)
        with self.assertRaises(TypeError):
            simple_interest(1000, 5, True)

    def test_simple_interest_bounds(self):
        # Upper bounds exceed max limit
        with self.assertRaises(ValueError):
            simple_interest(1e13, 5, 2)
        with self.assertRaises(ValueError):
            simple_interest(1000, 10001, 2)
        with self.assertRaises(ValueError):
            simple_interest(1000, 5, 10001)

        # Maximum allowed values should pass
        self.assertEqual(simple_interest(1e12, 10000, 10000), 1e12 + (1e12 * 10000 * 10000) / 100)

    def test_compound_interest_invalid_types(self):
        # Non-numeric types should raise TypeError
        with self.assertRaises(TypeError):
            compound_interest("1000", 5, 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, "5", 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, "2", 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, 2, "12")
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, 2, None)

        # Booleans should raise TypeError
        with self.assertRaises(TypeError):
            compound_interest(True, 5, 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, False, 2, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, True, 12)
        with self.assertRaises(TypeError):
            compound_interest(1000, 5, 2, False)

    def test_compound_interest_bounds(self):
        # Upper bounds exceed max limit
        with self.assertRaises(ValueError):
            compound_interest(1e13, 5, 2, 12)
        with self.assertRaises(ValueError):
            compound_interest(1000, 10001, 2, 12)
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, 10001, 12)
        with self.assertRaises(ValueError):
            compound_interest(1000, 5, 2, 10001)


if __name__ == "__main__":
    unittest.main()
