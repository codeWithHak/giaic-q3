from random import choice
def main():
  user_move = input("Chose One, Rock, Paper, Scissors\n").lower()
  computer_move = choice(['rock','paper','scissors'])
  if computer_move == user_move:
    print(f"{user_move} vs {computer_move}")
    print("It's a draw")
  elif user_move == "rock" and computer_move == "scissors" or user_move == "paper" and computer_move == "rock" or user_move == "scissors" and computer_move == "paper":
    print(f"{user_move} vs {computer_move}")
    print("Yohoo, you won")
  else:
    print(f"{user_move} vs {computer_move}")
    print("You lost")     

main()
