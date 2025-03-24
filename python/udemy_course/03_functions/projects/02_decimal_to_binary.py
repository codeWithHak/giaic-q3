def decimal_to_binary(value)->str:
    result = ""
    while value > 0:
        result += str(value % 2)
        value = value//2
    return result
print(decimal_to_binary(10))

# 22 // 2 = 11 - 0
# 11 // 2 = 