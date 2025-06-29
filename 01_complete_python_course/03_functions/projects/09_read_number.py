def main():
    
    # count atempts
    turns = 0
    
    # give 3 tries to user
    while turns < 3:
        user_input = input("give an integer: ")
        type_user_input = type(user_input)
        print(type_user_input)
        
        # check type of user's input is int
        if type_user_input == int:
            print("same type")
        else:
            print("wrong guess try again")
            turns += 1
    
    # if user failed raise valude error
    else:
        raise ValueError("Three Invalid Attempts")
    
main()