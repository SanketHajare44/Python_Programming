'''
    Write a program which contains filter(), map(), reduce() in it . Python application which
    contains one list of numbers list contains the numbers which aare accepted from user. filter
    should filter out  all such numbers which greater that or equale to 90. Map function will increase
    each number by 10 . reduce will return product of all that numbers

    Input : List = [4,34,36,76,68,24,89,23,86,90,45,70]
    list after filter = [76 , 89,86, 90, 70]
    list after map = [86 , 99,96, 100, 80]
    Output : 6538752000
'''

from functools import reduce

Check = lambda No : No >= 70

Increase = lambda No : No + 10

Multiplication = lambda No1, No2: No1 * No2 

def main():
    No = 0
    Data = list()

    print("Enter the number element : ")
    No = int(input())
    for i in range(No):
        print("Enter the number : ")
        Ret = int(input())
        Data.append(Ret)
    
    fData = list(filter(Check,Data))
    print("output of filter : ",fData)

    mData = list(map(Increase,fData))
    print("output of map : ",mData)

    rData = reduce(Multiplication,mData)
    print(rData)

if __name__ == "__main__":
    main()