def Factorial(x):
    
    # base cae
    if x < 2:
        print('num is One ')
        return x
    
    # recursive call
    else: 
        prev_factorial = Factorial(x - 1)
        print("prev_factorial", prev_factorial)
    
    # result
    return x * prev_factorial
    

print(Factorial(5))