#calculating the value of pi using William Shanks' formula
from decimal import getcontext
import sys
sys.path.append('../..')  # Adjust the path to import from the correct directory
from Geometry.Trigonometry.arctan import ArctanCalculator 
# William Shanks' formula for calculating pi: pi/4 = 1587 * arctan(1/2852) + 295 * arctan(1/4193) 
#                                                   + 593 * arctan(1/4246) + 359 * arctan(39307) 
#                                                   + 481 * arctan(1/55603) + 625 * arctan(1/211050) 
#                                                   - 728 * arctan(1/390112)

class WilliamShanksAlgorithm:

    @staticmethod
    def calculate_pi(precision):
        getcontext().prec = precision + 2  # Set precision for Decimal calculations
        arctan_calculator = ArctanCalculator(precision)

    # William Shanks' formula: pi/4 = 1587 * arctan(1/2852) + 295 * arctan(1/4193) 
    # + 593 * arctan(1/4246) + 359 * arctan(39307) + 481 * arctan(1/55603) 
    # + 625 * arctan(1/211050) - 728 * arctan(1/390112)
    
        pi_over_4 = (1587 * arctan_calculator.calculate_arctan(2852) +
                    295 * arctan_calculator.calculate_arctan(4193) +
                    593 * arctan_calculator.calculate_arctan(4246) +
                    359 * arctan_calculator.calculate_arctan(39307) +
                    481 * arctan_calculator.calculate_arctan(55603) +
                    625 * arctan_calculator.calculate_arctan(211050) -
                    728 * arctan_calculator.calculate_arctan(390112))
        
        return pi_over_4 * 4
if __name__ == "__main__":
    precision = int(input("Enter the number of decimal places for pi: "))
    pi_value = WilliamShanksAlgorithm.calculate_pi(precision)
    print(f"Calculated value of pi to {precision} decimal places: {pi_value}")