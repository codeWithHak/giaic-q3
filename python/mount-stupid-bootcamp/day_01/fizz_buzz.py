print(f"\n{'-'*20} Welcome to FizzBuzz {'-'*20}\n")

# take starting and ending number form the user
start = int(input("Starting number: "))
end = int(input("Ending number: "))

# take two divissors from user
fizz_divisor = int(input("Fizz Divisor: "))
buzz_divisor = int(input("Buzz Divisor: "))

# loop over numbers till starting and ending numbers (that user gave)
for num in range(start,end+1):
     
    # check if number is divisible by both divisers and its not 1  
    if num %  fizz_divisor == 0 and  num %  buzz_divisor == 0:
        print("FizzBuzz")   
    
    # check if number is divisible by fizz diviser and its not 1  
    elif num % fizz_divisor  == 0:
        print("Fizz")    
    
    # check if number is divisible by buzz diviser and its not 1  
    elif  num % buzz_divisor  == 0:
        print("Buzz")

    # if not divisible by any print that num as it is
    else:
        print(num)

