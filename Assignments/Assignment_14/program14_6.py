# Write a lambda function which accepts one number and returns true if number is odd otherwise return false

ChkOdd = lambda Value : True if (Value % 2 == 1) else False

def main():
    No = 0
    Ret = False

    print("Enter the Number : ")
    No = int(input())

    Ret = ChkOdd(No)

    if(Ret == True):
        print(No,"Is a odd number")
    else:
        print(No,"Is not a odd number")


if __name__ == "__main__":
    main()