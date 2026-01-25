'''
    write a program which accept N numbers from user and store it into List.
    Return addition of all elements from that list
    Input : Number of Elements : 6
    Input Elements : 13 5 45 7 4 56
    Output : 130
'''

def Addition(Arr):
    Sum = 0
    for i in Arr:
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
    
    Ret = Addition(Data)

    print("Sum is : ",Ret)

if __name__ == "__main__":
    main()