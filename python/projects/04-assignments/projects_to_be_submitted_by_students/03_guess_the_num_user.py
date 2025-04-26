from random import randint

def comp_guess():
  low = 1
  high = 10
  feedback = ""
  while feedback != 'c':
    guess = randint(low,high)
    feedback = input(f"Is {guess} is too high Press(H), too low Press(L), Correct Press(C)")
    if feedback == "h":
      high = guess - 1
    elif feedback == "l":
      low = guess + 1
  print("You guessed it right")
comp_guess()