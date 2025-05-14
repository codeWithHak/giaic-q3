# TODO:
# 1. Create a class called `Fruit`
# 2. Add a class variable `category` and set it to "food"
# 3. Inside the constructor, accept two instance variables: `name` and `color`
# 4. Create two fruit objects and print the category for both.

# Sample Output:
# Apple is a food.
# Banana is a food.

class Fruit:
    category = "food"
    
    def __init__(self,name,color):
        self.name = name
        self.color = color
        
f = Fruit('banana','yellow')
f2 = Fruit('apple','red')
# print(f.category)
# print(f2.category)

# --------------------------------------------------------------------------

# TODO:
# 1. Using the class from Practice 1, change the class variable:
#    Fruit.category = "healthy food"
# 2. Print the `category` again for both fruit objects to verify it changed.

# Sample Output:
# Apple is a healthy food.
# Banana is a healthy food.

Fruit.category = "healthy food"
# print(f.category)
# print(f2.category)
# print(Fruit.category)


# ----------------------------------------------------------------------------

# TODO:
# 1. Now change `category` using one fruit object like this:
#    apple.category = "junk food"
# 2. Print category for `apple` and `banana`
# 3. Then print `Fruit.category`

# Question: What do you observe? Does it match your theory?

# Sample Expected Output:
# apple.category --> junk food  (instance-level override)
# banana.category --> healthy food  (still using class variable)
# Fruit.category --> healthy food
f.category = "junk food"
print(f.category)
print(f2.category)
