# Question:

"""
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.

Read the input and convert it to an integer.

Prompt the user to enter the second number.

Read the input and convert it to an integer.

Calculate the sum of the two numbers.

Print the total sum with an appropriate message.
"""

# Solution:

def main():
    first_num = int(input("First Number: "))
    second_num = int(input("Second Number: "))
    sum = first_num + second_num
    return sum
print(f"Sum: {main()}")