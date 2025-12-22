#Class to input a polynomial

class Polynomial:

    def polynomial(self):
        self.terms = int(input("Enter the number of terms in the polynomial: "))
        self.coefficients = []
        self.powers = []

    def input_terms(self):
        for i in range(self.terms):
            coeff = float(input(f"Enter coefficient for term {i+1}: "))
            power = float(input(f"Enter power for term {i+1}: "))
            self.coefficients.append(coeff)
            self.powers.append(power)

    def main(self):
        self.polynomial()
        self.input_terms()
        print("The polynomial is:")
        for i in range(self.terms):
            if i == 0:
                print(f"{self.coefficients[i]}x^{self.powers[i]}", end="")
            else:
                print(f" + {self.coefficients[i]}x^{self.powers[i]}", end="")
        print()
        
if __name__ == "__main__":
    poly = Polynomial()
    poly.main()