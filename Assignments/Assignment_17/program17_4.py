''' write a program which accept number and returns Addition of factors '''

def Addition(Value):
    Ans = 0
    for i in range(1,Value):
        if(Value % i == 0):
            Ans = Ans + i
            
    return Ans

def main():

    No = 0
    iRet = 0

    print("Enter the number : ")
    No = int(input())

    iRet = Addition(No)

    print("Addition of Factor is  : ",iRet)


if __name__ == "__main__":
        main()