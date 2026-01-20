# Write a program which accepts one number and prints cube of that number.

def CubeOfNumber(Value):
    Ans = 0
    Ans = Value * Value * Value    # Ans = Value**3
    return Ans

def main():
    No = 0
    iRet = 0

    print("Enter the number : ")
    No = int(input())

    iRet = CubeOfNumber(No)

    print("Cube is : ",iRet)

if __name__ == "__main__":
    main()