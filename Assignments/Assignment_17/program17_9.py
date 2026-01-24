'''
    Write a program which accept number from user and return number of digits in that number.
    Input : 12345
    Output : 5

'''

def Count(Value):
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

    Ret = Count(No)
    print("Total number of digit is : ",Ret)

if __name__ == "__main__":
    main()