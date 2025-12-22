import sys

sys.path.append('../..')
from Algebra.Polynomials.polynomial import Polynomial
from simple_diffrentiation_function import SimpleDifferentiation

class SecondDerivatives(SimpleDifferentiation):
    def __init__(self):
        super().__init__()

    def differentiate(self):
        print("Calculating Second Derivative:")
        first_derivative = self.compute_derivative(self.poly)
        print(f"First Derivative: {first_derivative}")

        # Compute second derivative
        second_derivative = self.compute_derivative_from_string(first_derivative)
        print(f"Second Derivative: {second_derivative}")

    def compute_derivative_from_string(self, derivative_str):
        terms = derivative_str.split(" + ")
        derivative_terms = []
        for term in terms:
            coeff, power = term.split("x^")
            coeff = int(coeff)
            power = int(power)
            if power > 0:
                new_coeff = coeff * power
                new_power = power - 1
                derivative_terms.append(f"{new_coeff}x^{new_power}")
        return " + ".join(derivative_terms)
    
if __name__ == "__main__":
    second_derivative = SecondDerivatives()
    second_derivative.differentiate()