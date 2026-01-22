# Write a lambda function which accepts one number and returns true if number is divisible by 5 otherwise return false

ChkDivision = lambda Value : True if (Value % 5 == 0) else False

def main():
    No = 0
    Ret = False

    print("Enter the Number : ")
    No = int(input())

    Ret = ChkDivision(No)

    if(Ret == True):
        print(No,"is a divisible by 5")
    else:
        print(No,"is not a divisible by 5")


if __name__ == "__main__":
    main()