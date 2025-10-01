def main(user_list):
    num_list = []
    while True:
        user_input = input("Give a number ")
        if user_input:
            try:
                num = int(user_input)
                num_list.append(num)
                num_list.sort()
            except ValueError:
                return "Invalid value"
        elif user_input == '': 
            break
    return num_list            
print(main([2,4,51]))