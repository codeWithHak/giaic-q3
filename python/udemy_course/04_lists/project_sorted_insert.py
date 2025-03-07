def SortedInsert(items, x):
    
    new_items = []
    new_items.append(x)
    new_items += items
    new_items.sort()

    return new_items

print(SortedInsert([4,1,2,3],5))