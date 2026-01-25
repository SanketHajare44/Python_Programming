'''
    Write a program which contains filter(), map(), reduce() in it . Python application which
    contains one list of numbers list contains the numbers which aare accepted from user. filter
    should filter out  prime numbers. Map function will multiply each number by 2 . reduce will return Maximum number from that number.
    (You can also use normal function instrad of lambda function)

    Input : List = [5,2,3,4,3,4,1,2,8,10]
    list after filter = [2,44,2,8,10]
    list after map = [4,16,16,4,64,100]
    Output : 204
'''

from functools import reduce

def CheckPrime(Value):
    if Value < 2:
        return False

    for i in range(2, int(Value/2) + 1):
        if (Value % i) == 0:
            return False
    return True

def Increase(No):
    return No * 2

def Maximum(A, B):
    if A > B:
        return A
    else:
        return B

def main():
    No = 0
    Data = list()

    print("Enter the number of elements : ")
    No = int(input())

    for i in range(No):
        print("Enter the number : ")
        Ret = int(input())
        Data.append(Ret)

    print("Input List :", Data)

    fData = list(filter(CheckPrime, Data))
    print("List after filter :", fData)

    mData = list(map(Increase, fData))
    print("List after map :", mData)

    rData = reduce(Maximum, mData)
    print("Output :", rData)

if __name__ == "__main__":
    main()
