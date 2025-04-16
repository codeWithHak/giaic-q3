def main():
    turns = 0
    while turns < 3:
        user_input = input("give an integer: ")
        type_user_input = type(user_input)
        print(type_user_input)
        if type_user_input == int:
            print("same type")
        else:
            print("wrong guess try again")
            turns += 1
    else:
        raise ValueError("Three Invalid Attempts")
    
main()