# Write a program which accepts one numbr and prints square of that number.

def Square(Value1):
    return Value1 * Value1

def main():
    No = 0
    iRet = 0

    print("Enter number : ")
    No = int(input())

    iRet = Square(No)

    print("Square of the number is : ",iRet)

if __name__ == "__main__":
    main()