# hame tuples milenge aik array me
# un tuples me do vlaues hongi 
# name, age
# hamey minimum age wala tuple sabse pehle lana he
# ab array ke andar multiple tuples hen
# ham kese dkehnge ke us array ke andar jo  tuples hen uki age kiya he 
# age ko extract karsakte hen or aik list me append karsakte hen 
# phir minimum age leli  

# use deque as well

# def getMinIndex(user_input):
    
#     # temporary list to store sorted list of tups
#     sorted_tup = []
    
#     # get each tups values 
#     for i in user_input:
        
#         # print statements to understand the flow
#         print("i",i)
#         print("i[0]:",i[1])

#         # temp age as an example based on it check current age and append list accordingly
#         temp_age = user_input[0][1]
        
#         # age of every element
#         curr_age = i[1]
#         print("age:",sorted_tup)
        
#         # age of element is more than the temp age append at the end 
#         if curr_age > temp_age:
#             sorted_tup.append(i)
            
#         # else insert at the start
#         else:
#             sorted_tup.insert(0, i) 
#         print("sorted_tup:",sorted_tup)
        
        

# getMinIndex([('john',20),("david",30),("saad",10),('ishaq1',1)])


# ------------ instructors way -------------

def GetMinIndex(persons):
    
    # Assume it's the first
    min_index = 0 #1
    
    # Traverse List
    for i in range(1, len(persons)):
    
        if persons[i][1] < persons[min_index][1]:
            min_index = i
        
        # Result
        
    return min_index
    
def SortByAge (persons):
    
    # Initialize Output
    output = []
    
    while len(persons) > 0:
        # print("loop started")
        # Get index of person with minimum age
        index = GetMinIndex(persons) 
        # print("stored index called function")

        # Transfer to output list
        print("min_index:",index)
        print("persons:",persons)
        person = persons.pop(index)
        # print("pop person from persons")
        output.append(person) 
        print("output:",output)   
        # print("append person in persons")
    
    # Copy result into inpput list
    persons.extend(output)

# Main program        
persons = [
    ('john',20),
    ("david",30),
    ("saad",10),
    ('ishaq1',1)
    ]

SortByAge(persons)
print(persons)