# def SortedInsert(items, x):
    
#     new_items = []
#     new_items.append(x)
#     new_items += items
#     new_items.sort()

#     return new_items

# print(SortedInsert([4,1,2,3],5))


# instructor code

def main(items,x):
    index = 0
    
    # find position
    while index < len(items) and items[index] < x:
        index +=1
    
    # insert item
    items.insert(index,x)