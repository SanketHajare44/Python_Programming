''' Write a program which accept one number ad display below pattern.
    Input : 5
    Output : 
            * * * * * 
            * * * * 
            * * * 
            * * 
            *       
'''

def Display(Value):
    for i in range(Value,0, -1):
        for i in range(i):
            print("*", end = " ")
        print()


def main():
    No = 0
    print("Enter the number : ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()