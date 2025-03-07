# build a calculator which takes input from the user, beside basic functionality include modulus, floor division, Exponentiation


def calculator() -> str:
    operation:str = input("Enter operation to perform: ")
    if operation not in ("+", "-", "*","/","//","**","%"):
        return "Invalid Operation"
    else:
        try:
            num1:float = float(input("Enter the first number: "))
            num2 :float= float(input("Enter the second number: "))
        except ValueError:
            return "Invalid input. Please enter numbers only."
        
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else: return f"Cannot divid {num1} by zero."       
        elif operation == "//":
            if num2 != 0:
                result = num1 // num2
            else: return f"Cannot divide {num1} by zero."    
        elif operation == "**":
            result = num1 ** num2
        elif operation == "%":
            result = num1 % num2        
        else:
            return f"Invalid Operarion"
        return f"Result is: {result}"
    
print(calculator())