# your output should be - Names: [value1, value2, ....]

# my sol
def print_values (prefix, *values):
    return f"{prefix}: {list(values)}"

print(print_values("Name","david","john"))

# instructors sol

def print_val_ins(prefix, *values):
    result = prefix + ": ["
    
    seprator = ""
    
    for val in values:
        result += seprator
        result += val
        
        seprator = ', '
        
    result += "]"
        
    return result

print(print_val_ins("Names", "david", "mesii")) 