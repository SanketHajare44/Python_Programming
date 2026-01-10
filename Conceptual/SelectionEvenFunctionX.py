
def CheckEven(no):
    if(no % 2 == 0):
        print("It is even.")
    else:
        print("It is odd.")


def main():
    Value = 0

    print("enter number : ")
    Value = int(input())

    CheckEven(Value)

if __name__ == "__main__":
    main()