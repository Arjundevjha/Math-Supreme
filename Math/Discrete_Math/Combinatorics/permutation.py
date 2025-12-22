class Permutation:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    def factorial(self, num):
        if num == 0:
            return 1
        else:
            return num * self.factorial(num-1)

    def calculate(self):
        return self.factorial(self.n) / self.factorial(self.n - self.r)

if __name__ == "__main__":
    n = int(input("Enter the total number of items (n): "))
    r = int(input("Enter the number of items to arrange (r): "))
    
    if n < r:
        print("Note: n should be greater than or equal to r for permutations to be valid.")
        exit()

    permutation_calculator = Permutation(n, r)
    
    result = permutation_calculator.calculate()
    
    print(f"The number of permutations of {n} items taken {r} at a time is: {result}")