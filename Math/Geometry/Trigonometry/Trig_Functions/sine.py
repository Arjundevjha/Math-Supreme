import sys as s
s.path.append("../..")
from Numerical_Methods.Factorial.factorial import factorial
from Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import MachinAlgorithm

def Sine(radians): 
    sine = 0
    sign = 0
        
    for idx in range(1,100,2):
        if sign % 2 == 0:   
            sine += radians**idx/factorial(idx)
        else:
            sine -= radians**idx/factorial(idx)
        sign += 1 
    
    return sine 

if __name__ == "__main__":
    precision = 10
    degree = float(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    sine = Sine(radians)
    print(f'The value of sine is {sine:.2f}')
