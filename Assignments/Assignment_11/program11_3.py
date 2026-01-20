# Write a program which accepts one number and prints sum of digits

def SumOfDigits(Value):
    Sum = 0
    Digit = 0

    while(Value != 0):
        Digit = Value % 10
        Sum = Sum + Digit
        Value = int(Value / 10)

    return Sum

def main():
    No = 0
    iRet = 0

    print("Enter the number : ")
    No = int(input())

    iRet = SumOfDigits(No)

    print("Sum of digits is : ",iRet)

if __name__ == "__main__":
    main()