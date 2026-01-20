# Write a program which contains one function ChkGreater() that accesp two numbers and prints the grater number.

def ChkGreater(value1,value2):
    if(value1>value2):
        return value1
    else:
        return value2


def main():
    No1 = 0
    No2 = 0

    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())
    
    iRet = ChkGreater(No1,No2)

    print("Greater number is : ",iRet)

if __name__ == "__main__":
    main()