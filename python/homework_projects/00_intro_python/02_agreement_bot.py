# Question:

"""
Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow! 
"""

# Solution:

def main():
    fav_animal = input("What's your favourite animal? ")
    result = f"My favourite animal is {fav_animal}"
    return result

print(main())