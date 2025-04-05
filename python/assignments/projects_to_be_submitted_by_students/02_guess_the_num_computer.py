from random import randint
random_number = randint(1,11)
while True:
  user_guess = int(input("Guess a number between 1 to 10 "))
  if user_guess +1 == random_number or user_guess -1 == random_number:
    print("Too close")
  elif user_guess > random_number:
    print("Too high, try again")
  elif user_guess < random_number:
    print("Too low, try again")
  else:
    print("You won")
    break