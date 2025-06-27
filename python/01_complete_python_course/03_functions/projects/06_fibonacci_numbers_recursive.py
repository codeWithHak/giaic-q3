# use recursive function to print fibonacci numbers
# e.g 0 1 1 2 3 5 8 13 21 34

def Fibonacci(n):
    print("again")
    #base case
    if n <= 1:
        print('return n') # yahan aya
        return n # yahan phir
    
    # get previous values
    print(n,": one_back = Fibonacci(n-1)") # 3 2
    one_back = Fibonacci(n-1) # 2 1
    print("one_back:",one_back) # yahan phir phir
    
    print(n,": two_back = Fibonacci(n-2)") # 1 
    two_back = Fibonacci(n-2) # yahan phir phir phir 1  
    print("two_back:",two_back) # yahan phir phir phir phir
    
    # return sum
    print("one_back + two_back:",one_back + two_back)
    
    return one_back + two_back # yahan phir phir phir phir phir or khatam

print(Fibonacci(3))  
    