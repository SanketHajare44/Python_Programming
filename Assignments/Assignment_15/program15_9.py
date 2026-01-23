'''Write a lambda function using reduce() which accepts list of 
   numbers and returns product of all elements'''

Multiplication = lambda No1, No2 : No1 * No2

def reduceX(Task,Elements):
    Result = 1
    for i in Elements:
        Result = Task(Result,i)
    
    return Result

def main():
    Arr = list()
    Ret = 0
    print("Enter the number of elements")
    value = int(input())

    for i in range(value):
        Data = int(input("Enter the element : "))
        Arr.append(Data)

    print("Original list : ",Arr)

    Ret = reduceX(Multiplication,Arr)
    print("Product of all element is  :", Ret)


if __name__ == "__main__":
    main()