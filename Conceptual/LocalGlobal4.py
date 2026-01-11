no = 11          # global

def fun():
    global no       #refer global variable
    print("Value of no from fun is : ", no) # 11
    no =  no + 1
    print("Value of no from fun is : ", no) # 12

print("Value of no is :",no)    # 11

fun()

print("Valuue of no is :",no)   # 12
