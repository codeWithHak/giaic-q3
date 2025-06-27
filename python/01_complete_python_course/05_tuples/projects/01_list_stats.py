from math import sqrt

# 1- median
    # len lenge list ki
    # agar len even he to beech se do number lekar unko apas me plus karnege or 2 se divide kardenge
    # agar odd he to beech wala number median he 
def GetListStats(*numbers):
    
    # get Arithmetic mean (mean)
    num_len = len(numbers)
    num_sum = sum(numbers)         
    median = num_sum / num_len
    
    # get Standard Deviation
    new_list = []
    new_list_sum = 0
    new_list_sum_div = 0
    new_list_sum_sqrt = 0
    for value in numbers:
        
        print(f"value:{value}")
        
        print("each_val = (value - median) ** 2")
        each_val = (value - median) ** 2
        print(f"each_val: {each_val}")
        
        new_list.append(each_val)
        print(f"new_list: {new_list}")
        
        new_list_sum = sum(new_list)
        print("new_list_sum:",new_list_sum)
        new_list_sum_div = new_list_sum / num_len
        
        new_list_sum_sqrt = sqrt(new_list_sum_div)
       
        # get median
        middle_value_index = 0
        middle_value = 0
        
        if num_len % 2 != 0:
            sorted_numbers = sorted(numbers)
            middle_value_index = num_len//2
            middle_value = sorted_numbers[middle_value_index]
            print(sorted_numbers[middle_value_index]) 
        else:
            sorted_numbers = sorted(numbers)
            print('else')
            middle_value_index = num_len//2
            middle_value = (sorted_numbers[middle_value_index] + sorted_numbers[middle_value_index - 1]) / 2
            print(middle_value)
            print(middle_value_index)
            print(sorted_numbers[middle_value_index - 1])
    return median,new_list_sum_sqrt,middle_value
    
    
mean,standard_deviation,median = GetListStats(1,2,6,9,6,5,1)
print("Mean:",mean)    
print("Standard Deviation:",standard_deviation)    
print("Median:",median)    
    # isEven = False
    # if num_len > 1 and num_len % 2 == 0:
    #     isEven = True
    
    # if isEven:
             