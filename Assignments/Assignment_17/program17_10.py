'''
    Write a program which accept number from user and return Addition of digits in that number.
    Input : 5187934
    Output : 37

'''

def Count(Value):
    Sum = 0
    Digit = 0
    while(Value != 0):
        Digit = int(Value % 10)
        Sum = Sum + Digit
        Value = int(Value / 10)

    return Sum

def main():
    No = 0
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Count(No)
    print("Total number of digit is : ",Ret)

if __name__ == "__main__":
    main()