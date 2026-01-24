''' Write a program which accept one number ad display below pattern.
    Input : 5
    Output :
            1 2 3 4 5 6 
            1 2 3 4 5 6 
            1 2 3 4 5 6 
            1 2 3 4 5 6 
            1 2 3 4 5 6 
            1 2 3 4 5 6               
'''

def Display(Value):
    for i in range(1,Value + 1):
        for j in range(1, Value + 1):
            print(j , end = " ")
        print()

def main():
    No = 0
    print("Enter the number : ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()