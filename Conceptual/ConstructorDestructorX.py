import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")
    
    def __del__(self):
        print("Inside Destructor")

# Allocate memory
obj1 = Demo()
obj2 = Demo()


# Use the memory

# Deallocate memory
del obj1
del obj2

gc.collect()

print("End os application")