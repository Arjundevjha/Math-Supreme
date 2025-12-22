# General term of the binomial expansion of (a + b)^n is given by:
# T_n+1 = nCr * a^(n-r) * b^r
import sys
sys.path.append("../..")
 
from Discrete_Math.Combinatorics.combination import Combination

class BinomialTheorem:
    """
    Class to calculate the general term in the binomial expansion of (a + b)^n.
    The general term T_(r+1) is given by:
    T_(r+1) = nCr * a^(n-r) * b^r
    where n is the exponent, r is the term index, and nCr is the combination formula.
    """

    @staticmethod
    def general_term(n, r, a, b):
        """Calculate the general term in the binomial expansion."""
        if r < 0 or r > n:
            raise ValueError("Invalid values for n and r.")
        nCr = Combination.nCr(n, r)
        return nCr * (a ** (n - r)) * (b ** r)
    
if __name__ == "__main__":
    # Example usage
    n = int(input("Enter the exponent n for (a + b)^n: "))
    r = int(input("Enter the term index r (0-based): "))
    a = float(input("Enter the value of a: "))
    b = float(input("Enter the value of b: "))
    
    try:
        term = BinomialTheorem.general_term(n, r, a, b)
        print(f"The general term T_{r+1} in the expansion of (a + b)^{n} is: {term}")
    except ValueError as e:
        print(e)

 