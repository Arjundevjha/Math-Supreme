# Simple interest calculator

class SimpleInterestCalculator:

    def main():
        principal_amount = float(input("Enter your principal amount ($): "))
        interest_rate = float(input("Enter the interest rate (%): "))
        time = float(input("Enter the time applied: "))
        if principal_amount < 0 or interest_rate < 0 or time < 0:
            raise ValueError("Principal amount, interest rate, and time must be non-negative.")
        # Calculate simple interest
        interest = (principal_amount * interest_rate * time) / 100
        # Calculate total amount after interest
        total_amount = principal_amount + interest
        print(f"The simple interest is: ${interest:.2f}")
        print(f"Total amount after {time} at {interest_rate}% simple interest is ${total_amount} ")

if __name__ == "__main__":
    SimpleInterestCalculator.main()