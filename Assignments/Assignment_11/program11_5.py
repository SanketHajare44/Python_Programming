# Write a program which accepts one number and checks whether it is palimdrome or not

def ChkPalimdrome(Value):
    Number = Value
    Ans = 0
    Digit = 0

    while(Value != 0):
        Digit = int(Value % 10)
        Ans = (Ans * 10) + Digit
        Value = int(Value / 10)

    if(Ans == Number):
        return True
    else:
        False

def main():
    bRet = False
    No = 0

    print("Enter the number : ")
    No = int(input())

    bRet = ChkPalimdrome(No)

    if(bRet == True):
        print("It is palimdrome")
    else:
        print("It is not a palimdrome")


if __name__ == "__main__":
    main()