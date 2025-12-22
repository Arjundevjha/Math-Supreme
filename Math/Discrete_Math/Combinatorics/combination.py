# class of Combination formula: for nCr where n and r are non-negative integers,

class Combination:
    """
    Class to calculate combinations (nCr) using the formula:
    nCr = n! / (r! * (n - r)!)
    where n is the total number of items, and r is the number of items to choose.
    """

    @staticmethod
    def factorial(n):
        """Calculate factorial of n."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def nCr(n, r):
        """Calculate combinations (nCr)."""
        if r < 0 or r > n:
            raise ValueError("Invalid values for n and r.")
        return Combination.factorial(n) // (Combination.factorial(r) * Combination.factorial(n - r))
    
if __name__ == "__main__":
    # Example usage
    n = int(input("Enter the value of n (total items): "))
    r = int(input("Enter the value of r (items to choose): "))
    try:
        result = Combination.nCr(n, r)
        print(f"The number of combinations ({n} choose {r}) is: {result}")
    except ValueError as e:
        print(e)