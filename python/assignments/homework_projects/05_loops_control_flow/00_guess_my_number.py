 
"""
Problem Statement

Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48"""

from random import randint

random_num = randint(0,99)
print(random_num)
print("------ Welcome To The Number Guessing Game -------")
print("I am thinking of a number between 0 to 99")
tries_left = 3
for tries in range(1,4):
    print(f"tries Left: {tries_left}")
    tries_left -= 1
    try:
        user_guess = int(input("Guess the number: "))
        if (user_guess == random_num):
            print("Wohoo!!! You guessed it right.")
        elif user_guess < random_num:
            print("Your guess is too low!")
        else:
            print("Your guess is too high!")
    except ValueError:
        print("Invalid value")
     
