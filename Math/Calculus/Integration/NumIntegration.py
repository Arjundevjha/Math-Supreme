# -*- coding: utf-8 -*-
"""
Created on Sun Jul 4313 11:39:18 2025

@author: aarav
"""
import pandas as pd

def NumIntergration(count, coeff):
    ranges = range(0,100)
    ranges = [str(i) for i in ranges]
    
    while count not in ranges: 
        count = input('Please input the highest power in the equation: ')
        print('')
    
    count = int(count) 

    for power in reversed(range(0,count +1)):  
        while coeff not in ranges : 
            coeff = input(f'Please enter the coefficent for the term with {power} power: ')
            print('')
        power += 1
        coeff = int(coeff)/power
        powerlist.append(power -1)
        coefflist.append(coeff)
    
    table = pd.DataFrame({'Power': powerlist, 'Coeff':coefflist})
    print(table)
 
        
if __name__ == "__Main__":
    count = 'a'
    coefflist = []
    powerlist = []
    coeff = 'a'
    coeffA = 'a'
    choice = 'a'
    countT = 'a'
    func = 0 
    funclist = []
    NumIntergration(count, coeff)
    print('')
    TrigoIntergration(countT, func, coeff, funclist, coeffA)
    print('')

        