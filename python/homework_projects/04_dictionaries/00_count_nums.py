"""
Problem Statement
This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

An example run of the program looks like this (user input is in blue):

Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3
Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.
"""

    
def get_user_numbers():
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        else:
            num = int(user_input)
            user_numbers.append(num)
    return user_numbers

def count_numbers(num_lst):
    
    num_dict = {}
    for i in num_lst:
        if i in num_dict:
            num_dict[i] += 1
        else:
            num_dict[i] = 1
    return num_dict

def print_count(num_dict):
    for i in num_dict:
        print(f"{i} appeard {num_dict[i]} times")

def main():
    user_numbers = get_user_numbers()
    count_nums = count_numbers(user_numbers)
    print_count(count_nums10)
    
main()