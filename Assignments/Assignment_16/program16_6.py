''' Write a program which accepts number from user and check whether that number is positive or negative or Zero '''
def Check(Value):
    if(Value > 0):
        print("Positive number")
    elif(Value < 0):
        print("Negative number")
    else:
        print("Zero")

def main():
    No = 0
    print("Enter the number : ")
    No = int(input())

    Check(No)


if __name__ == "__main__":
    main()