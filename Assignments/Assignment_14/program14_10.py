# Write a lambda function which accepts three number and returns maximum number

Maximum = lambda Value1,Value2,Value3 : Value1 if (Value1 > Value2 and Value1 > Value3) else (Value2 if Value2 > Value3 else Value3)

def main():
    No1 = 0
    No2 = 0
    No3 = 0
    Ret = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    print("Enter the third Number : ")
    No3 = int(input())

    Ret = Maximum(No1,No2,No3)

    print("Maximum number is : ",Ret)


if __name__ == "__main__":
    main()