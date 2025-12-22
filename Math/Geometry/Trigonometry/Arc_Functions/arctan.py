#class to calculate the arctangent of (1/x) in radians with a specified precision
from decimal import Decimal, getcontext
class ArctanCalculator:
    def __init__(self, precision):
        getcontext().prec = precision + 2  # Set precision for Decimal calculations
        self.precision = precision

    def calculate_arctan(self, x, number_of_terms=None):
        if x == 0:
            return Decimal(0)
        elif x < 0:
            return -self.calculate_arctan(-x, number_of_terms)

        arctan_value = Decimal(0)
        term = Decimal(1) / Decimal(x)  # First term of the series
        n = 0

        if number_of_terms is not None:
            while n < number_of_terms:
                arctan_value += term / (2 * n + 1)
                n += 1
                term *= -Decimal(1) / (x * x)
        else:
            while abs(term) > Decimal(10) ** (-self.precision):
                arctan_value += term / (2 * n + 1)
                n += 1
                term *= -Decimal(1) / (x * x)

        return arctan_value
    
if __name__ == "__main__":
    precision = int(input("Enter the number of decimal places for arctan(1/x): "))
    number_of_terms = int(input("Enter the number of terms to calculate: "))
    if precision < 0 or number_of_terms <= 0:
        print("Precision must be a non-negative integer and number of terms must be a positive integer.")
        exit(1)
    getcontext().prec = precision + 2  # Set precision for Decimal calculations
    x = Decimal(input("Enter the value of x: "))
    calculator = ArctanCalculator(precision)
    arctan_value = calculator.calculate_arctan(x, number_of_terms)
    print(f"Calculated value of arctan(1/{x}) to {precision} decimal places using {number_of_terms} terms: {arctan_value}")
