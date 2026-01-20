# Write a program which accepts one number and prints all even numbrs till that number.

def EvenNum(Value):
    for i in range(1,Value+1):
        if(i % 2 == 0):
            print(i)

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    EvenNum(No)

if __name__ == "__main__":
    main()