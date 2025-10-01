def sum(*values):
    result = 0
    for num in values:
        result += num
    return result
print(sum(10,20,30))


def sum_negate(negate, *values):
    
    # initialize result
    result = 0
    
    # traverse arguements
    for num in values:
        result += num
    
    # negate values
    if negate:
        result = -result
        
    return result
    
    
print(sum_negate(False,10,20,30)) # OUTPUT 60

print(sum_negate(False,10,20,30)) # output -60