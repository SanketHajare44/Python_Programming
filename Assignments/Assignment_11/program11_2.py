# write a program which accepts one number and prints count of digits inn that number.

def CountDigits(Value):
    iCount = 0
    
    while(Value != 0):
        Value = int(Value / 10)
        iCount += 1
    
    return iCount

def main():
    No = 0
    Ret = 0

    print("Enter the number : ")
    No = int(input())

    Ret = CountDigits(No)

    print("Total number of digits is : ",Ret)

if __name__ == "__main__":
    main()