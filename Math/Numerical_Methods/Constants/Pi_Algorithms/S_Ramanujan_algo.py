import decimal

class S_Ramanujan_algo:

    def calculate_pi_ramanujan(num_decimal_places, num_terms):
        """
        Calculates the value of pi using S. Ramanujan's formula.

        The formula is:
        1/pi = (2*sqrt(2)/9801) * sum_{k=0 to infinity} ( (4k)! * (1103 + 26390k) ) / ( (k!)^4 * 396^(4k) )

        Args:
            num_decimal_places (int): The desired number of decimal places for pi.
            num_terms (int): The number of terms to use in the series summation.

        Returns:
            decimal.Decimal: The calculated value of pi.
        """

        if num_decimal_places < 0:
            raise ValueError("Number of decimal places cannot be negative.")
        if num_terms < 1:
            raise ValueError("Number of terms must be at least 1.")

        # Set the precision for decimal calculations
        # We need extra precision for intermediate calculations to avoid rounding errors
        decimal.getcontext().prec = num_decimal_places + 10

        total_sum = decimal.Decimal(0)
        constant = (decimal.Decimal(2) * decimal.Decimal(2).sqrt()) / decimal.Decimal(9801)

        for k in range(num_terms):
            numerator_factorial = decimal.Decimal(S_Ramanujan_algo.factorial(4 * k))
            numerator_expression = decimal.Decimal(1103 + 26390 * k)
            numerator = numerator_factorial * numerator_expression

            denominator_factorial = (decimal.Decimal(S_Ramanujan_algo.factorial(k)))**4
            denominator_power = decimal.Decimal(396)**(4 * k)
            denominator = denominator_factorial * denominator_power

            term = numerator / denominator
            total_sum += term

        # Calculate 1/pi
        one_over_pi = constant * total_sum

        # Calculate pi
        pi_value = decimal.Decimal(1) / one_over_pi

        return pi_value

    def factorial(n):
        """
        Calculates the factorial of a non-negative integer.
        """
        if n == 0:
            return 1
        else:
            res = 1
            for i in range(1, n + 1):
                res *= i
            return res

if __name__ == "__main__":
    try:
        decimal_places = int(input("Enter the desired number of decimal places for pi: "))
        num_terms = int(input("Enter the number of terms to use in the series: "))

        pi_calculated = S_Ramanujan_algo.calculate_pi_ramanujan(decimal_places, num_terms)
        print(f"\nCalculated value of pi with {decimal_places} decimal places using {num_terms} terms:")
        print(pi_calculated)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")