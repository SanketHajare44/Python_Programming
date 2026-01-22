# Write a lambda function which accepts one number and returns Square of that number.

Square = lambda Value : Value*Value

def main():
    No = 0
    Ret = 0
    print("Enter the Number : ")
    No = int(input())

    Ret = Square(No)
    print("Square is : ",Ret)

if __name__ == "__main__":
    main()