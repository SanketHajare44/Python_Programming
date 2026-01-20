# # Write a program which accepts one number and prints that many numbers in reverse.

def Arithematic(Value):
    for i in range(Value, 0, -1):
        print(i)
    

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    Arithematic(No)
    

if __name__ == "__main__":
    main()