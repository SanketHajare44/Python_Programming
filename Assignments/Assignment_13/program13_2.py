# write a program which accepts radius of circle and prints area of cricle

def AreaOfCircle(Value):
    Ans = 0

    Ans = 3.14*Value*Value

    return Ans

def main():
    No = 0
    iRet = 0

    print("Enter the radius of circle : ")
    No = int(input())

    iRet = AreaOfCircle(No)

    print("Area of circle is : ",iRet)

if __name__ == "__main__":
    main()
    
