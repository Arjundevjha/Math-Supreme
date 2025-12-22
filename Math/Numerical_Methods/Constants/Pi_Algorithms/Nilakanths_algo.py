#Calculating pi using Nilakantha's algorithm to a specified number of decimal places and terms
class NilakanthaAlgorithm:

    def calculate_pi_nilakantha(terms):
        """Calculate pi using Nilakantha's algorithm with a specified number of terms."""
        pi = 3.0
        sign = 1  # Start with positive sign for the first term

        for i in range(2, 2 * terms + 1, 2):
            term = sign * (4.0 / (i * (i + 1) * (i + 2)))
            pi += term
            sign *= -1  # Alternate the sign for the next term

        return pi

    def main():
        """Main function to execute the Nilakantha's algorithm for calculating pi."""
        try:
            terms = int(input("Enter the number of terms to calculate pi: "))
            if terms <= 0:
                raise ValueError("Number of terms must be a positive integer.")

            pi_value = NilakanthaAlgorithm.calculate_pi_nilakantha(terms)
            print(f"Calculated value of pi using {terms} terms: {pi_value}")
        except ValueError as e:
            print(f"Invalid input: {e}")
if __name__ == "__main__":
    NilakanthaAlgorithm.main()