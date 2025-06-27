def main() -> list[int]:
    my_list:list[int] = []    
    while True:
        user_input:str =input("Give a number to add in a list - Submit empty input when done. ")
        if user_input == '':
            break
        else:
            int_input:int = int(user_input)
            my_list.append(int_input)
    return my_list

print(main())