import sys
sys.path.append('../..')
from Algebra.Polynomials.polynomial import Polynomial
from simple_diffrentiation_function import SimpleDifferentiation

class ProductRuleDifferentiation(SimpleDifferentiation):
    def __init__(self):
        super().__init__()
        self.poly2 = Polynomial()
        self.poly2.polynomial()
        self.poly2.input_terms()

    def differentiate(self):
        print("Using Product Rule:")
        poly1 = self.format_polynomial(self.poly)
        poly2 = self.format_polynomial(self.poly2)
        
        print(f"f(x) = {poly1} * {poly2}")

        # Derivative using product rule: (u*v)' = u'v + uv'
        u_prime = self.compute_derivative(self.poly)
        v_prime = self.compute_derivative(self.poly2)

        print(f"f'(x) = ({u_prime}) * ({poly2}) + ({poly1}) * ({v_prime})")
        
    def format_polynomial(self, poly):
        terms = []
        for i in range(poly.terms):
            coeff = poly.coefficients[i]
            power = poly.powers[i]
            term = f"{coeff}x^{int(power)}"
            terms.append(term)
        return " + ".join(terms)
    
    def compute_derivative(self, poly):
        derivative_terms = []
        for i in range(poly.terms):
            if poly.powers[i] == 0:
                continue
            coeff = poly.coefficients[i] * poly.powers[i]
            power = poly.powers[i] - 1
            derivative_terms.append(f"{coeff}x^{int(power)}")
        return " + ".join(derivative_terms)
    
    
if __name__ == "__main__":
    product_rule = ProductRuleDifferentiation()
    product_rule.differentiate()