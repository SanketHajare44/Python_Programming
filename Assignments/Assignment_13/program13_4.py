# write a program which accepts one number and prints binary equivalent.

def BinaryNumber(Value):
    binary = ""

    while(Value > 0):
        binary = str(Value % 2) + binary
        Value = int(Value / 2)
    
    return binary
    

def main():
    No = 0
    sRet = ""

    print("Enter the number : ")
    No = int(input())

    sRet = BinaryNumber(No)  

    print("Binary Equivalent is : ",sRet)

if __name__ == "__main__":
    main()
    
