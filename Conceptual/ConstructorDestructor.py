import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")
    
    def __del__(self):
        print("Inside Destructor")

# Allocate memory
obj = Demo()

# Use the memory

# Deallocate memory
del obj

gc.collect()

print("End os application")