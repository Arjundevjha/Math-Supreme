#Class that checks if a solution of x is a factor of a polynomial using the Factor Theorem
from polynomial import Polynomial

class FactorTheorem:
    def check_factor(self):
        poly = Polynomial()
        poly.polynomial()
        poly.input_terms()
        
        x = float(input("Enter the value of x to check if it is a factor: "))
        
        # Calculate the polynomial value at x
        result = sum(coeff * (x ** power) for coeff, power in zip(poly.coefficients, poly.powers))
        
        if result == 0:
            print(f"x = {x} is a factor of the polynomial.")
        else:
            print(f"x = {x} is not a factor of the polynomial.")
    
if __name__ == "__main__":
    factor_theorem = FactorTheorem()
    factor_theorem.check_factor()
    print()