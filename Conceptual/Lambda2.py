# functional

# def CheckEven(no):
#     return (no % 2 == 0)

CheckEven = lambda no : ((no % 2) == 0)


def main():
    Value = 0
    Ret = False

    print("Enter number : ")
    Value = int(input())

    Ret = CheckEven(Value)
    
    if(Ret == True):
        print("It is Even")
    else:
        print("It is odd")


if __name__ == "__main__":
    main()