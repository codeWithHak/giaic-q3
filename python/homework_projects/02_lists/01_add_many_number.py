# Question:
 
"""
Write a function that takes a list of numbers and returns the sum of those numbers.

"""

# The hard way without bult in sum method
def add_many_number(numbers):
    initial_number = 0
    for num in numbers:
        initial_number += num
    return initial_number
print(add_many_number([1,2,3,4]))

# Use built in sum method of python
def main(x):
    print(sum(x))
main([1,2,3])