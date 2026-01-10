
def CheckEven(no):
    if(no % 2 == 0):
        print("It is even.")
    else:
        print("It is odd.")


def main():
    CheckEven(21)       # positional
    CheckEven(no = 22)  # keyword



if __name__ == "__main__":
    main()