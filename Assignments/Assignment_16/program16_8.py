''' Write a program which accepts one number from user and print that number of "*" on screen ''' 


def Display(Value):
    for _ in range(Value):
        print("*")

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()