from typing import Union
def Compound_Interest(principal_amount: Union[int, float], interest_rate: Union[int, float], time:  Union[int, float], compound_frequency: Union[int,float]) -> float:
        compound_interest = principal_amount * (1 + (interest_rate / 100) / compound_frequency) ** (compound_frequency * time)
        print(f"The compound interest is: ${compound_interest:.2f}")

if __name__ == "__main__":
    CompoundInterestCalculator.main()
