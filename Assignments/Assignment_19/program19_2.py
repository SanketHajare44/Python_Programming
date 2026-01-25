'''
    Write a program which contains one lambda function which accepts one parameter and
    return power of two.
    Input : 4 3  Output : 12    
    Input : 6 3   Output : 18    
'''

Square = lambda No1,No2 : No1 * No2

def main():
    No1 = 0
    No2 = 0
    Ret = 0
    print("Enter the number : ")
    No1 = int(input())

    print("Enter the number : ")
    No2 = int(input())
    
    Ret =  Square(No1,No2)
    print("multiplication is : ",Ret)

if __name__ == "__main__":
    main()