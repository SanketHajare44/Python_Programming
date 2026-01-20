# Write a program which accepts one number and prints factorial of that number.

def Factorial(Value):
    Fct = 1

    for i in range(1,Value+1):
        Fct = Fct * i

    return Fct

def main():
    No = 0
    Ret = 0

    print("Enter the number : ")
    No = int(input())

    Ret = Factorial(No)

    print("Factorial of number is : ",Ret)

if __name__ == "__main__":
    main()