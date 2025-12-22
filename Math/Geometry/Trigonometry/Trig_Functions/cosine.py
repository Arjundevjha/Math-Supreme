import sys as s
s.path.append("../..")
from Numerical_Methods.Factorial.factorial import factorial
from Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import MachinAlgorithm

def Cosine(radians):
    cos = 1
    sign = 1
    
    for idx in range(2,100,2):
        if sign % 2 == 0:
            cos += radians**idx/factorial(idx)
        else:
            cos -= radians**idx/factorial(idx)
        sign += 1 
    
    return cos 

if __name__ == "__main__":
    precision = 10
    degree = float(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    cos = Cosine(radians)
    print(f'The value of cosine is {cos:.2f}')
