import sys as s
s.path.append("../..")
from Numerical_Methods.Pi_Algorithms.Machin_algo import MachinAlgorithm
from Geometry.Trigonometry.Trig_Functions.cosine import Cosine 

def CosineRuleLength(radians): 
    sec = 1/Cosine(radians)

    return sec 
def CosineRuleAngle():
   print()

def Menu(): 
  while choice not in ['1','2']:
    print('1: Cosine for Length') 
    print('2: Cosine for Angle\n')
    choice = input('Please input choice: ')
    choice.strip()
    if choice not in ['1','2']:
      raise TypeError('Invalid Choice. Please input your choice again.\n')
  return int(choice)

if __name__ == "__main__":
    choice = Menu() 
    if choice == 1:
      for idx in (2):
       degree = int(input("Please input angle  in degrees: "))
       CosineRuleLength()  
    elif choice == 2:
      CosineRuleAngle()
    precision = 10
    degree = int(input("Please input angle in degrees: "))
    radians = degree/180 * float(MachinAlgorithm.calculate_pi(precision))
    sec = (radians)
    print(f'The value of cosec is {sec:.2f}')
