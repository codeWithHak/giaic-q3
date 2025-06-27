# remplicate the behaviour of min(), this fumction should return the minimum value.

# my wa;)
def getMin(list:list[int])->int:
    # I sorted the list first so that smallest element came on first index. 
    list.sort()
    
    # And then I returned the first index, which is the smallest element
    return list[0]

my_list=[1,2,3]
print(getMin(my_list))


# instructors way

def getMinVal (list:list[int]) -> int:
    if len(list) == 0:
        raise ValueError("List is empty")
    
    # store a temprary result, imagining that the first element is the lowest, we will change result below.
    result = list[0]

    # traverse the whole list and find a nymber less than result, if found then set result equl to it
    for i in list:

        # if an element is less than i than set that element as result
        if i<result:
            result = i

    # return result       
    return result        

print(getMinVal(my_list))