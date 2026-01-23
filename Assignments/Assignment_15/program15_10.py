'''Write a lambda function using filter() which accepts list of 
   numbers and returns the count of even numbers'''

EvenCount = lambda No : True if (No % 2 == 0) else False

def filterX(Task,Elements):
    Result = False
    Count = 0
    for i in Elements:
        Result = Task(i)
        if(Result == True):
            Count += 1
    
    return Count

def main():
    Arr = list()
    Ret = 0
    print("Enter the number of elements")
    value = int(input())

    for i in range(value):
        Data = int(input("Enter the element : "))
        Arr.append(Data)

    print("Original list : ",Arr)

    Ret = filterX(EvenCount,Arr)
    print("Even number of count is  :", Ret)


if __name__ == "__main__":
    main()