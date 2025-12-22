import sys as s
s.path.append("../..")
from Numerical_Methods.Constants.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.Trig_Functions.sine import Sine 
import numpy as np 

def ArcSin(sin): 
    for degree in np.arange(0,90,0.1):
        precision = 10
        degree = float(input("Please input angle in degrees: "))
        radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
   
        if sin - Sine(radians) < 0.01:
            return degree

if __name__ == "__main__":
    sin = int(input("Please input value of sin: "))
    degree = ArcSin(sin)
    print(f'The degree in degrees is {degree:.2f}')
    precision = 10
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    print(f'The degree in degrees is {radians:.2f}')