import sys
sys.path.append('../..')
from Algebra.Polynomials.polynomial import Polynomial

from simple_diffrentiation_function import SimpleDifferentiation

# Class for Differentiation using Chain Rule (ax+b)^n
# Inherits from SimpleDifferentiation to use Polynomial class
class ChainRuleDifferentiation:
    def __init__(self):
        self.inner_poly = Polynomial()
        self.inner_poly.polynomial()
        self.inner_poly.input_terms()
        self.exponent = int(input("Enter the power to which the polynomial is raised (n in [g(x)]^n): "))

    def format_polynomial(self):
        terms = []
        for i in range(self.inner_poly.terms):
            coeff = self.inner_poly.coefficients[i]
            power = self.inner_poly.powers[i]
            term = f"{coeff}x^{int(power)}"
            terms.append(term)
        return " + ".join(terms)

    def differentiate(self):
        print("\nUsing Chain Rule:")
        g_x = self.format_polynomial()
        print(f"f(x) = ({g_x})^{self.exponent}")

        # Compute derivative of the inner polynomial
        derivative_terms = []
        for i in range(self.inner_poly.terms):
            if self.inner_poly.powers[i] == 0:
                continue
            coeff = self.inner_poly.coefficients[i] * self.inner_poly.powers[i]
            power = self.inner_poly.powers[i] - 1
            derivative_terms.append(f"{coeff}x^{int(power)}")

        g_prime = " + ".join(derivative_terms)

        # Final output
        print(f"f'(x) = {self.exponent}({g_x})^{self.exponent - 1} * ({g_prime})")

if __name__ == "__main__":
    crd = ChainRuleDifferentiation()
    crd.differentiate()