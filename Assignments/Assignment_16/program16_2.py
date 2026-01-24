''' Write a program which contains one function named as ChkNum(). which accept one parameter as number.
    If number is even then it should display "Even number" otherwise display "odd number" 
    otherwise disply "odd number " on console '''

def ChkNum(value):
    if(value % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    No = 0
    print("Enter the number : ")
    No = int(input())

    ChkNum(No)

if __name__ == "__main__":
    main()