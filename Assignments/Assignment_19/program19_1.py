'''
    Write a program which contains one lambda function which accepts one parameter and
    return power of two.
    Input : 4   Output : 16    
    Input : 6   Output : 64    
'''

Square = lambda No : No ** 2

def main():
    No = 0
    Ret = 0
    print("Enter the number : ")
    No = int(input())
    
    Ret =  Square(No)
    print(Ret)

if __name__ == "__main__":
    main()