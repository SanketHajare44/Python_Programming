def main():
    Size = 0
    Value = 0
    Data = list()

    print("Enter the number of elements : ")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

if __name__ == "__main__":
    main()