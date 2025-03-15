# Implement a function that removes duplicates from a given list while maintaining the original order.


# ---------------- my solution ------------------------- 
def remove_duplicate(numbers:list[int])-> list[int]:
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)
    return new_list

print(remove_duplicate([0,0,1,1,2,3,4,5]))


# ---------------- AI solution -------------------------
def remove_duplicates(numbers:list[int])->list[int]:
    return list(dict.fromkeys(numbers))

remove_duplicates([0,0,1,2,1,1,3,3,4,5,6,6])