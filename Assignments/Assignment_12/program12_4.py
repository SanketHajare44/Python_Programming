# Write a program which accepts two number and prints addition, substraction, multiplication and division.

def Arithematic(Value):
    for i in range(1, Value+1):
        print(i)
    

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    Arithematic(No)
    

if __name__ == "__main__":
    main()