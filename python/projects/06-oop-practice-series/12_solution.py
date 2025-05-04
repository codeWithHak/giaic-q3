# 12. Static Methods

# Assignment:

# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        f = c * 9 / 5 + 32
        return f"F {f}"
    
obj1 = TemperatureConverter()

print(obj1.celsius_to_fahrenheit(23))