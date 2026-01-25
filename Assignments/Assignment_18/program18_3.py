'''
    write a program which accept N numbers from user and store it into List.
    Return Minimum number from that list
    Input : Number of Elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 4
'''

def Minimum(Arr):
    Min = Arr[0]
    for i in Arr:
        if(Min > i):
            Min = i

    return Min

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
    
    Ret = Minimum(Data)

    print("Minimum is : ",Ret)

if __name__ == "__main__":
    main()