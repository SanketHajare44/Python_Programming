''' Write a program which contains one function that accepts one number from user and returns 
    true if number is divisible by 5 otherwise return false ''' 


def Check(Value):
    if(Value % 5 == 0):
        return True
    else:
        return False

def main():
    No = 0
    Ret = False

    print("Enter the number : ")
    No = int(input())

    Ret = Check(No)
    if(Ret == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()