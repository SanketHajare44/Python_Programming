''' Write a program which accept one number from user and returns its factorial '''

def Factorial(Value):
    Ans = 1
    for i in range(1, Value + 1):
        Ans = Ans * i
    
    return Ans

def main():
    No = 0
    Ret = 0
    print("Enter the number : ")
    No = int(input())

    Ret = Factorial(No)

    print("Factrial is : ",Ret)

if __name__ == "__main__":
    main()