# Write a program which accepts one number and prints multiplication table of that number.

def MultiTable(Value):
    for i in range(1,11):
        print(i*Value)

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    MultiTable(No)

if __name__ == "__main__":
    main()