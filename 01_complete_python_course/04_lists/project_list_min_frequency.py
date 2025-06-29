# aik input lena he list me or aik int me
# ab dekhna he ke list me jo elements hen unki frequency kitni he matlab aik element kitni baar repeat horaha he
# ab agar elemnt doosrey arguement yani x ke jitna ya usse ziyada baar repeat horaha ho to usko list new list me add kardena he
# or agar x se kam time repat horaha ho to usko nikaal dena he or yaad rahey list me repeating numbers na ayen


def GetItemsWithMinFrequency (my_list:list[int], x:int)-> list[int]:
    new_list:list[int] = []
    for num in my_list:
        count = my_list.count(num)
        print(f"Num: {num} --- Count:{count}", )
        if count >= x and num not in new_list:
            print(f"X: {x}")
            print(f"new_list before: {new_list}")
            new_list.append(num)
            print(f"new_list after: {new_list}")
    return new_list



my_list = [1,2,3,3,3,4,4,4]
print(GetItemsWithMinFrequency(my_list,3))