def main(user_list,x):
    index = 0
    while index < len(user_list):
        if (user_list[index] == x):
            user_list.pop(index)
        else:
            index+=1
    return user_list    

print(main([1,2,2,2,3,4,],2))
