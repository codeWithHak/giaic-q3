"""
Problem Statement
Write a program which continuously asks the user to enter values which are added one by one into a list.
When the user presses enter without typing anything, print the list.

Here's a sample run (user input is in blue):

Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']

"""


def main():
    user_list = []
    while True:
        try:
            user_input = input("Provide a number: ")

            if user_input == "":
               print(user_list)
               break
            
            else:
                num = int(user_input)
                user_list.append(num)
                
        except ValueError:
            print(user_input, "is not a valid input.")
            print("Please provide a valid number!")
            
main()
