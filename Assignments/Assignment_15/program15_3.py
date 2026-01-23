# # Write a lambda function using filter() which accepts list of numbers and returns a list of odd numbers

OddNumbers = lambda No : (No % 2 == 1)

def filterX(Task,Elements):
    Result = list()
    for i in Elements:
        Ret = Task(i)

        if(Ret == True):
            Result.append(i)
    
    return Result

def main():
    Arr = list()
    Ret = list()
    print("Enter the number of elements")
    value = int(input())

    for i in range(value):
        Data = int(input("Enter the element : "))
        Arr.append(Data)

    print("Original list : ",Arr)

    Ret = list(filterX(OddNumbers,Arr))
    print("Odd elements :", Ret)


if __name__ == "__main__":
    main()