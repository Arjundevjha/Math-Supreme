class CompoundInterestCalculator:

    def main():
        principal_amount = float(input("Enter the principal amount($): "))
        interest_rate = float(input("Enter the interest rate(%): "))
        time = int(input("Enter the time applied: "))
        compound_frequency = int(input("Enter the number of times interest is compounded per year: "))
        compound_interest = principal_amount * (1 + (interest_rate / 100) / compound_frequency) ** (compound_frequency * time)
        print(f"The compound interest is: ${compound_interest:.2f}")

if __name__ == "__main__":
    CompoundInterestCalculator.main()