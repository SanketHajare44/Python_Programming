''' Write a program which accept name from user and display length of its name.''' 

def Display(Value):
    Count = 0

    for ch in Value:
        Count += 1
    
    return Count

def main():
    No = ""

    print("Enter the string : ")
    No = str(input())

    Ret = Display(No)

    print("Length of string is : ",Ret)

if __name__ == "__main__":
    main()