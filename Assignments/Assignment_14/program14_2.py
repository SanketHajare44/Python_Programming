# Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda Value : Value*Value*Value

def main():
    No = 0
    Ret = 0
    print("Enter the Number : ")
    No = int(input())

    Ret = Cube(No)
    print("Cube is : ",Ret)

if __name__ == "__main__":
    main()