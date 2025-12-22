class PrimeFactorisation:
    def __init__(self, number):
        self.number = number
        self.factors = []

    def factorize(self):
        n = self.number
        factor = 2
        while n > 1:
            while n % factor == 0:
                self.factors.append(factor)
                n //= factor
            factor += 1
        return self.factors

    def get_factors(self):
        if not self.factors:
            self.factorize()
        return self.factors
    
def main():
    number = int(input("Enter a number to factorize: "))
    pf = PrimeFactorisation(number)
    factors = pf.get_factors()
    print(f"Prime factors of {number} are: {factors}")
    
if __name__ == "__main__":
    main()