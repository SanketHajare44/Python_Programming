# Write a lambda function which accepts two number and returns minimum number

Minimum = lambda Value1,Value2 : Value1 if Value1<Value2 else Value2

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    Ret = minimum(No1,No2)

    print("Minimum number is : ",Ret)


if __name__ == "__main__":
    main()