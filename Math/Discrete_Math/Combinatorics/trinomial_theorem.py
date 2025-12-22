#trinomial theorem class

class TrinomialTheorem:
    def __init__(self, a, b, c, n):
        self.a = a
        self.b = b
        self.c = c
        self.n = n

    def coefficient(self, i, j):
        if i < 0 or j < 0 or i + j > self.n:
            return 0
        from math import comb
        k = self.n - i - j
        return comb(self.n, i) * comb(self.n - i, j)

    def expand(self):
        result = []
        for i in range(self.n + 1):
            for j in range(self.n - i + 1):
                k = self.n - i - j
                coeff = self.coefficient(i, j)
                term = f"{coeff}*{self.a}^{i}*{self.b}^{j}*{self.c}^{k}"
                result.append(term)
        return " + ".join(result)
    
if __name__ == "__main__":
    a = input("Enter the value of a: ")
    b = input("Enter the value of b: ")
    c = input("Enter the value of c: ")
    n = int(input("Enter the value of n: "))
    
    trinomial = TrinomialTheorem(a, b, c, n)
    expansion = trinomial.expand()
    print(f"The expansion of ({a} + {b} + {c})^{n} is: {expansion}")