# Write a program which accepts one number and prints sum of first N natural number

def Summation(Value):
    Sum = 0

    for i in range(1,Value+1):
        Sum = Sum + i

    return Sum

def main():
    No = 0
    Ret = 0

    print("Enter the number : ")
    No = int(input())

    Ret = Summation(No)

    print("Summation of first",No,"natural number is : ",Ret)

if __name__ == "__main__":
    main()