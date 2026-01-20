# Write a program which accepts two number and prints addition, substraction, multiplication and division.

def Arithematic(Value1,Value2):
    Add = Value1 + Value2
    Substraction = Value1 - Value2
    Multiplication = Value1 * Value2
    Division = Value1 / Value2

    return Add,Substraction,Multiplication,Division

def main():
    No1 = 0
    No2 = 0

    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    Result1,Result2,Result3,Result4 = Arithematic(No1, No2)

    print("Addition is : ",Result1)
    print("Substraction is : ",Result2)
    print("Multiplication is : ",Result3)
    print("Division is : ",Result4)


if __name__ == "__main__":
    main()