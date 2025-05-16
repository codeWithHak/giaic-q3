# print a welcome message
print(f"{'-'*20} Welcome to unit convertor {'-'*20}")

# all conversions of meter
length_values={
    'meter':1,
    'kilometer':1000,
    'centimeter':0.01,
    'millimeter':0.001,
    'micrometer':1e+6,
    'nanometer':1e+9,
    'yard':1.094,
    'foot':3.281,
    'inch':39.37,
    'mile':1609.34
}

print("Available Values")
for index,val in enumerate(length_values):
    print(f"{index+1} - {val}")

try:
    from_index = int(input("Convert From (enter number): ")) - 1
    to_index = int(input("Convert To (enter number): ")) - 1
    val = float(input("Value: "))

except ValueError:
    print("Invalid Value!")
    
units = list(length_values.keys())   
print(units) 
from_unit = units[from_index]
to_unit = units[to_index]
        
# a method to convert unit
def convert_length(val,from_unit,to_unit):
    
    # convert user input to meters first
    meters = val * length_values[from_unit]
    
    # perform conversion from meters to selected to_unit also round the value to only two floating points
    result = round(meters / length_values[to_unit], 2)
    return result


print(convert_length(val,from_unit,to_unit))
