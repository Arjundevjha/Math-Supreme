from polynomial import Polynomial

def check_remainder(self):
        poly = Polynomial()
        polynomial()
        input_terms()

        x = float(input("Enter the value of x to find the remainder: "))

        # Calculate the polynomial value at x
        result = sum(coeff * (x ** power) for coeff, power in zip(poly.coefficients, poly.powers))

        print(f"The remainder of the polynomial divided by (x - {x}) is: {result}")
