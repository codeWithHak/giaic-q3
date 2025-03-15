# Level 1: Strengthening Fundamentals

# ✅ Topics: Lists, Tuples, Dictionaries, Sets, Loops, Conditional Statements


# Q-1 Write a Python function that takes a list of numbers and returns a new list with only the even numbers.


# ---------- my solution -----------------
def iseven (list:list[int]) -> list[int] :
   
    # initializing an empty list will append even numbers in it later 
    even_list = []

    # this loop checks for even nnumbers in the list
    for num in list:
        if num > 1 and num % 2 == 0:
            even_list.append(num)

    # sorting list        
    even_list.sort()  
    return even_list     
my_list = [0,10,2,33,4,1,9]
print(iseven(my_list))


# ------------------ AI suggested solution -----------------

def filter_even_numbers(numbers:list[int])->list[int]:

    # used list comprehension instead of loop
    return sorted([num for num in numbers if num % 2 == 0])

print(filter_even_numbers([1,2,3,4,5,6,7,8,9]))