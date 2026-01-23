'''Write a lambda function using filter() which accepts list of 
   numbers and returns a list of numbers divisible by both 3 and 5.'''

Division = lambda No : True if((No % 3 == 0) and (No % 5 == 0)) else False

def filterX(Task,Elements):
    Result = list()
    Ans = False
    for i in Elements:
        Ans = Task(i)
        if(Ans == True):
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

    Ret = filterX(Division,Arr)
    print("Divisible by 3 and 5 list of element is :", Ret)


if __name__ == "__main__":
    main()