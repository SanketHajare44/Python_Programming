'''
    write a program which accept N numbers from user and store it into List.
    Accept another number from user and return frequency of that number from list.
    Input : Number of Elements : 6
    Input Elements : 13 5 45 7 4 45
    Enter the number that you want frequency : 45
    Output : 2
'''

def Frequency(Arr,Value):
    Count = 0
    for i in Arr:
        if(i == Value):
            Count += 1

    return Count

def main():
    No1 = 0
    No2 = 0
    Ret = 0
    Data = list()

    print("Enter the number of Element : ")
    No1 = int(input())

    for _ in range(No1):
        print("Enter the element : ")
        Result = int(input())
        Data.append(Result)
    
    print("Enter the number that you want frequency")
    No2 = int(input())
    
    Ret = Frequency(Data,No2)

    print("Frquency is : ",Ret)

if __name__ == "__main__":
    main()