"""
Problem Statement
Fill out the function get_first_element(lst) which takes in a list lst as a parameter
and prints the first element in the list.
The list is guaranteed to be non-empty.
"""


def main():
    
    # initialize an empty list we will append user input in it.
    user_list = []
    
    # this loop will stop when user input will be an empty string ""
    while True:
        try:
            
            # if user givrs empty input this will print the list's first element andbreak the lopp
            user_input = input("give an element: ")
            if user_input == "":
                print(user_list[0])
                break
            
            # this will add the input in the list
            else:
                num = int(user_input)
                user_list.append(num)
                
        # checking for inavlid values e.g: str.        
        except ValueError:
            print(user_input,"is not a number.")   
            print("Provide a valid number!")   

main()