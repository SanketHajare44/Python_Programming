# write a program which accepts one number and prints reverse of that number.

def ReverseNumber(Value):
    Ans = 0

    while(Value != 0):
        Digit = int(Value % 10)
        Ans = (Ans*10) + Digit
        Value = int(Value / 10)
    
    return Ans

def main():
    Ret = 0
    No = 0

    print("Enter the number : ")
    No = int(input())
    
    Ret = ReverseNumber(No)

    print("Reverse number is : ",Ret)

if __name__ == "__main__":
    main()