''' write a function which accepts one number and display below pattern 
    *   *   *   *   *
    *   *   *   *   *
    *   *   *   *   *
    *   *   *   *   *
    *   *   *   *   *   '''

def display(Value):
    for i in range(Value):
        for j in range(Value):
            print("*", end = " ")
        print()


def main():

    No = 0

    print("Enter the number : ")
    No = int(input())

    display(No)


if __name__ == "__main__":
        main()