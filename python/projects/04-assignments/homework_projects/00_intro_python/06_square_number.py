# Question:
"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0

"""

# Answer:

def main():
    user_input = float(input("Type a number to see its square: "))
    print(f"{user_input} squared is {user_input ** 2}")
main()