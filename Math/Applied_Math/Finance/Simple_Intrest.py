#Returns total amount after simple interest
from typing import Union

def Simple_Interest(principal_amount: Union[int, float], interest_rate: Union[int, float], time: Union[int, float]) -> Union[int, float]:

        if principal_amount < 0 or interest_rate < 0 or time < 0:
            raise ValueError("Principal amount, interest rate, and time must be non-negative.")

        # Calculate simple interest
        interest = (principal_amount * interest_rate * time) / 100

        # Calculate total amount after interest
        total_amount = principal_amount + interest
        return total_amount

