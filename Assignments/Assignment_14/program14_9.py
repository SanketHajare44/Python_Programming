# write a lambda function which accepts two number and return Multiplication of two number

Multiplication = lambda Value1,Value2 : Value1 * Value2

def main():
    No1 = 0
    No2 = 0
    Ret = 0

    print("Enter the first Number : ")
    No1 = int(input())

    print("Enter the second Number : ")
    No2 = int(input())

    Ret = Multiplication(No1,No2)

    print("Multiplication is : ",Ret)
        

if __name__ == "__main__":
    main()