'''
    Write a program which contains filter(), map(), reduce() in it . Python application which
    contains one list of numbers list contains the numbers which aare accepted from user. filter
    should filter out  all such numbers which are even. Map function will calculate its square . reduce will return addition of all that numbers

    Input : List = [5,2,3,4,3,4,1,2,8,10]
    list after filter = [2,44,2,8,10]
    list after map = [4,16,16,4,64,100]
    Output : 204
'''

from functools import reduce

Check = lambda No : No % 2 == 0

Increase = lambda No : No**2

Multiplication = lambda No1, No2: No1 + No2 

def main():
    No = 0
    Data = list()

    print("Enter the number element : ")
    No = int(input())
    for i in range(No):
        print("Enter the number : ")
        Ret = int(input())
        Data.append(Ret)
    
    print(Data)
    
    fData = list(filter(Check,Data))
    print("output of filter : ",fData)

    mData = list(map(Increase,fData))
    print("output of map : ",mData)

    rData = reduce(Multiplication,mData)
    print(rData)

if __name__ == "__main__":
    main()