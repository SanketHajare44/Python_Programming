'''
    Write a program which accept N number from user and store it into List.
    Return addition of all prime numbers from that List. Main python file accepts N numbers from user
    and pass each number to Chkprime() function is part of our user defined module named as MarvellousNum. 
    Name of the function from main python file should be ListPrime().

    Input : Number of Elements : 11
    Input Elements : 13 5 45 7 4 56 10 34 2 5 8
    Output : 32
'''
import Marvellousnum

def ListPrime(Arr):
    Sum = 0
    Ans = False
    for i in Arr:
        Ans = Marvellousnum.Chkprime(i)
        if(Ans == True):
            Sum = Sum + i
    
    return Sum


def main():
    No = 0
    Ret = 0
    Data = list()

    print("Enter the number of Element : ")
    No = int(input())

    for _ in range(No):
        print("Enter the element : ")
        Result = int(input())
        Data.append(Result)

    Ret = ListPrime(Data)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()