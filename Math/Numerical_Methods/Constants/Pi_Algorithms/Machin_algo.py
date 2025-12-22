#calculating the value of pi using Machin's formula
from decimal import getcontext
import sys
sys.path.append('../../..')  # Adjust the path to import from the correct directory
# Import ArctanCalculator class from the arctan module
from Geometry.Trigonometry.Arc_Functions.arctan import ArctanCalculator
# Machin's formula for calculating pi: pi/4 = 4 * arctan(1/5) - arctan(1/239)
class MachinAlgorithm:

    def calculate_pi(precision):
        getcontext().prec = precision + 2  # Set precision for Decimal calculations
        arctan_calculator = ArctanCalculator(precision)

        # Machin's formula: pi/4 = 4 * arctan(1/5) - arctan(1/239)
        pi_over_4 = (4 * arctan_calculator.calculate_arctan(5) -
                    arctan_calculator.calculate_arctan(239))
        return pi_over_4 * 4

if __name__ == "__main__":
    precision = int(input("Enter the number of decimal places for pi: "))
    pi_value = MachinAlgorithm.calculate_pi(precision)
    print(f"Calculated value of pi to {precision} decimal places: {pi_value}")
