from typing import Union

def Compound_Interest(principal_amount: Union[int, float], interest_rate: Union[int, float], time:  Union[int, float], compound_frequency: Union[int,float]) -> Union[int, float]:

        if principal_amount < 0 or interest_rate < 0 or time < 0:
            raise ValueError("Principal amount, interest rate, and time must be non-negative.")
        
        compound_interest = principal_amount * (1 + (interest_rate / 100) / compound_frequency) ** (compound_frequency * time)

        return compound_interest
