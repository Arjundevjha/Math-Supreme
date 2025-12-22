#binomial theorem class

class BinomialTheorem:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def coefficient(self, r):
        if r < 0 or r > self.n:
            return 0
        from math import comb
        return comb(self.n, r)

    def expand(self):
        result = []
        for r in range(self.n + 1):
            coeff = self.coefficient(r)
            term = f"{coeff}*{self.a}^{self.n - r}*{self.b}^{r}"
            result.append(term)
        return " + ".join(result)
    
if __name__ == "__main__":
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")
    n = int(input("Enter the value of n: "))
    
    binomial = BinomialTheorem(a, b, n)
    expansion = binomial.expand()
    print(f"The expansion of ({a} + {b})^{n} is: {expansion}")