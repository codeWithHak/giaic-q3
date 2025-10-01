# def merge_dictionaries(a,b):
    
#     # create a temporary copy of both original dicts
#     temp_dict_a = a.copy()
#     temp_dict_b = b.copy()
    
#     # update one dict with second dict so it has all the values
#     temp_dict_a.update(temp_dict_b)
#     print("temp_dict_a.update(temp_dict_a):",temp_dict_a)
#     print("temp_dict_a.update(temp_dict_b):",temp_dict_b)
#     # get keys for both dicts
#     b_keys = temp_dict_b.keys()
#     a_keys = temp_dict_a.keys()
    
#     # travers the dict to see if value duplicates
#     for index,key in enumerate(a_keys):
        
#         # check for duplicate key
#         if key in b_keys:
            
#             # convert the value of that key into a list and add both vlaues in that list
#             print("index:",index,"temp_dict_a:",temp_dict_a)
#             temp_dict_a[key] = [temp_dict_a[key],b[key]]
            
    
#     # result
#     print(temp_dict_a)
    
    
    
# main program    
# a={
#     'john':20,
#     'david':10,
#     'goliath':30
# }

# b={
#     'marsh':20,
#     'shawn':10,
#     'goliath':50
# }    
    
# merge_dictionaries(a,b)


# -------------------- instructors way ---------------------------

def merge_dictionaries(a,b):
    
    # initialize result
    result = {}

    # traverse dict a
    for key in a:
        
        # check if key is in b
        if key in b:
            result[key] = [a[key], b[key]]

        # else assign directly
        else:
            result[key] = a[key]
            
    # traverse dict b
    for key in b:
        
        # if not already present in result assign vlaue
        if key not in result:
            result[key] = b[key]
    
    # result
    return result

# main program
a={
    'john':20,
    'david':10,
    'goliath':30
}

b={
    'marsh':20,
    'shawn':10,
    'goliath':50
}

result = merge_dictionaries(a,b)
print(result)   

def prioritze_a(a,b):

    # initialize result as a copy of b
    result = b.copy()

    # make a copy of a 
    temp_a = a.copy()
    
    # update b (result)
    result.update(temp_a)
    
    # final result
    print(result)

# main program    
prioritze_a(a,b) 

def prioritze_b(a,b):
    
    result = a.copy()
    
    temp_b = b.copy()
    
    result.update(temp_b)
    
    print(result)
    
prioritze_b(a,b)