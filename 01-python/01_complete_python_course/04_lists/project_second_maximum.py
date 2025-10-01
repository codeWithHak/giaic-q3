# algorith:

# ham sabse pehle maximum value lenge or isko remove kardenge
# ab dobara maximum value lenge or usko return kardenge
# kiu ke jo sabse bari value thi wo hamne pehle hi remove kardi
# to ab jo value max hogi wo second highest vlaue hogi

def second_maximum(my_list):
    max = my_list[0]
    for num in my_list:
        if num > max:
            max = num
    my_list.remove(max)
    second_max = my_list[0]
    for num in my_list:
        if num > second_max:
            second_max = num
    return second_max 
print(second_maximum([11,1,2,3,10]))