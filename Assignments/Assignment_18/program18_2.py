'''
    write a program which accept N numbers from user and store it into List.
    Return Maximum number from that list
    Input : Number of Elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 56
'''

def Maximum(Arr):
    Max = Arr[0]
    for i in Arr:
        if(Max < i):
            Max = i
        
    
    return Max

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
    
    Ret = Maximum(Data)

    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()