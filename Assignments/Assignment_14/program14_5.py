# Write a lambda function which accepts one number and returns true if number is even otherwise return false

ChkEven = lambda Value : True if (Value % 2 == 0) else False

def main():
    No = 0
    Ret = False

    print("Enter the Number : ")
    No = int(input())

    Ret = ChkEven(No)

    if(Ret == True):
        print(No,"Is a Even number")
    else:
        print(No,"Is not a Even number")


if __name__ == "__main__":
    main()