# iterative function

# def walk(steps):
#     for step in range(1, steps + 1):
#         print("Youe take step #",step)
        
# walk(100)

# recursive function

def walk(steps):
    print("entering walk steps", steps)
    if steps < 1:
        print('basecase hit', steps)
        return
    walk(steps - 1)
    print("You took step:",steps)

walk(5)