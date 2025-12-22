import sys as s
s.path.append("../..")
from Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.Trig_Functions.sine import Sine 

def Cosec(radians): 
    cosec = 1/Sine(radians)

    return cosec 


if __name__ == "__main__":
    precision = 10
    degree = float(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    cosec = Cosec(radians)
    print(f'The value of cosec is {cosec:.2f}')
