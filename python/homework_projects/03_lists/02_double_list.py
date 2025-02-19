# Question:

"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]
"""

def main(numbers):
    doubled = []
    for num in numbers:
        num = num * 2
        doubled.append(num)
    print(doubled)
main([1,2,3,4])