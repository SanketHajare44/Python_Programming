''' write a program which accept number and check whether the that number is prime or not '''

def Addition(Value):
    Flag = False
    for i in range(2,Value):
        if(Value % i == 0):
            Flag = False
            break
        else:
            Flag = True
            
    return Flag

def main():

    No = 0
    iRet = False

    print("Enter the number : ")
    No = int(input())

    iRet = Addition(No)

    if(iRet == True):
        print("It is prime number")
    else:
        print("It is not a prime number")


if __name__ == "__main__":
        main()