# Chudnovsky algorithm.
from decimal import Decimal, getcontext

class ChudnovskyAlgorithm:

    def calculate_pi_chudnovsky(precision):
        getcontext().prec = precision + 2  # Set precision for Decimal calculations
        C = 426880 * Decimal(10005).sqrt()
        K = Decimal(6)
        M = Decimal(1)
        L = Decimal(13591409)
        X = Decimal(1)
        S = L

        for n in range(1, precision):
            M *= (K**3 - 16*K) / (n**3)
            L += 545140134
            X *= -262537412640768000
            S += M * L / X
            K += 12

        pi = C / S
        return str(pi)[:precision + 2]  # Return pi as a string with the desired precision
if __name__ == "__main__":
    precision = int(input("Enter the number of decimal places for pi: "))
    pi_value = ChudnovskyAlgorithm.calculate_pi_chudnovsky(precision)
    print(f"Calculated value of pi to {precision} decimal places: {pi_value}")
