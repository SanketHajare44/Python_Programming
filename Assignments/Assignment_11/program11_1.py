# Write a program which accept one number and checks whether it is prime or not.

def ChkPrimeNumber(Value):
    Ans = True
    for i in range(2,Value-1):
        if((Value % i == 0)):
            Ans = False
            break
    
    return Ans

def main():
    No = 0
    bRet = False

    print("Enter the number : ")
    No = int(input())

    bRet = ChkPrimeNumber(No)

    if(bRet == True):
        print(No,"is a prime number")
    else:
        print(No,"is not a prime number")


if __name__ == "__main__":
    main()