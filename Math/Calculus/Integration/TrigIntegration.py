   
def TrigoIntergration(countT,func, coeff, funclist, coeffA):
    ranges = range(0,100)
    ranges = [str(i) for i in ranges]
    
    while countT not in ranges: 
        countT = input('Please input the no of trigo terms in the equation: ')
        print('')
    
    for idx in range(1,countT +1):
        while func not in ['0','1','2'] : 
            print('Sin = 0, Cos = 1, Sec^2 = 2')
            func = input(f'Please enter the function for the {idx} term: ')
            print('')
        
        if func == 0:
            funclist.append('-Cos')
        elif func == 1: 
            funclist.append('Sin')
        elif func == 2:
            funclist.append('Tan')
        
        while coeff not in ranges : 
            coeff = input(f'Please enter the coefficent for the {idx} term: ')
            print('')
                
        while coeffA not in ranges : 
            coeffA = input(f'Please enter the coefficent of the variable in the {idx} term: ')
            print('')        
        
        coefflist.append[coeff/coeffA]
        table = pd.DataFrame({'Function': funclist , 'Coeff':coefflist})
        print(table)
        

if __name__ == "__Main__":
    coefflist = []
    powerlist = []
    coeff = 'a'
    coeffA = 'a'
    countT = 'a'
    func = 0 
    funclist = []
    TrigoIntergration(countT, func, coeff, funclist, coeffA)
    print('')
