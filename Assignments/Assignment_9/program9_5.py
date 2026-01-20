# Write a program which accepts one number and checks whether it is divisible by 3 and 5

def Division(Value):
    if((Value % 3 == 0) and (Value % 5 == 0)):
        return True
    
def main():
    No = 0
    bRet = False

    print("Enter the number : ")
    No = int(input())

    bRet = Division(No)

    if(bRet == True):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")

if __name__ == "__main__":
    main()