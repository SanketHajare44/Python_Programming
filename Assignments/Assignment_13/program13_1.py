# write a program which accepts length and width of rectangle and prints area

def AreaOfRectangle(Value1,Value2):
    Ans = 0

    Ans = Value1*Value2

    return Ans

def main():
    No1 = 0
    No2 = 0
    iRet = 0

    print("Enter the Length of Rectangle : ")
    No1 = int(input())

    print("Enter the Length of Rectangle : ")
    No2 = int(input())

    iRet = AreaOfRectangle(No1,No2)

    print("Area of rectangle is : ",iRet)

if __name__ == "__main__":
    main()
    
