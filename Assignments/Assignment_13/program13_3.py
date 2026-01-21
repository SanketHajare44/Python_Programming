# write a program which accepts one number and checks whether it is perfect number or not.

def PerfectNumber(Value):
    Ans = 0
    for i in range(1,int(Value/2)+1):
        if(Value % i == 0):
            Ans = Ans + i

    if(Ans == Value):
        return True
    else:
        return False


def main():
    No = 0
    bRet = 0

    print("Enter the number : ")
    No = int(input())

    bRet = PerfectNumber(No)  

    if(bRet == True):
        print("It is perfect number")
    else:
        print("It is not perfect number")

if __name__ == "__main__":
    main()
    
