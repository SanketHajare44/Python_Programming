''' Write a program which contains one function named as Add(). which accept two numbers
from user and returns addition of that two numbers '''

def Add(Value1, Value2):
    return Value1 + Value2

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the first number : ")
    No1 = int(input())
    print("Enter the first number : ")
    No2 = int(input())

    Ret = Add(No1,No2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()