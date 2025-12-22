import sys as s
s.path.append("../..")
from Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.Trig_Functions.sine import Sine 
from Geometry.Trigonometry.Trig_Functions.cosine import Cosine 

def Tan(radians): 
    tan = Sine(radians)/Cosine(radians)

    return tan 


if __name__ == "__main__":
    precision = 10
    degree = float(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    tan = Tan(radians)
    print(f'The value of tan is {tan:.2f}')
