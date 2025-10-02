Number = int | float

def add(a:Number, b:Number):
    if isinstance(a, (int,float)) and isinstance(b, (int, float)):
        return a+b
    
    raise TypeError("Input is not a vlaid number")
