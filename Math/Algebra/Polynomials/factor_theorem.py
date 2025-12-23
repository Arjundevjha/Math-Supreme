#Function that checks if a solution of x is a factor of a polynomial using the Factor Theorem
from polynomial import polynomial
from typing import Union

def check_factor(x: Union[int, float]) -> bool:
        poly = polynomial()
        polynomial()
        input_terms()
        
        
        # Calculate the polynomial value at x
        result = sum(coeff * (x ** power) for coeff, power in zip(poly.coefficients, poly.powers))
        
        if result == 0:
            return True
        else:
            return False
    