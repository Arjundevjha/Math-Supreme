# Class for Simple Differentiation of a Polynomial with Two or More Terms
import sys
sys.path.append('../..')
from Algebra.Polynomials.polynomial import Polynomial

class SimpleDifferentiation:
    def __init__(self):
        self.poly = Polynomial()
        self.poly.polynomial()
        self.poly.input_terms()

    def differentiate(self):
        print("The derivative is:")
        for i in range(self.poly.terms):
            if self.poly.powers[i] == 0:
                continue
            coeff, power = self.poly.coefficients[i] * self.poly.powers[i], self.poly.powers[i] - 1
            if i == 0:
                print(f"{coeff}x^{power}", end="")
            else:
                print(f" + {coeff}x^{power}", end="")
        print()

if __name__ == "__main__":
    differentiation = SimpleDifferentiation()
    differentiation.differentiate()