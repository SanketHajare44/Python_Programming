''' Write a program which display first 10 even numbers on screen ''' 


def Display(Value):
    for i in range(1,Value+1):
        print(i * 2)

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()