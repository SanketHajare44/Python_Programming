'''Write a lambda function using filter() which accepts list of 
   numbers and returns minimum of number of elements'''

addition = lambda No1, No2 : No1 if len(No1) > len(No2) else No2

def filterX(Task,Elements):
    Result = Elements[0]
    for i in Elements:
        Result = Task(Result,i)
    return Result

def main():
    Arr = list()
    Ret = ""
    print("Enter the number of strings")
    value = int(input())

    for i in range(value):
        Data = str(input("Enter the string : "))
        Arr.append(Data)

    print("Original string list : ",Arr)

    Ret = filterX(addition,Arr)
    print("maximum length of string is  :", Ret)


if __name__ == "__main__":
    main()