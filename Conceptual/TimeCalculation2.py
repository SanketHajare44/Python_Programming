# It is used to display how much time is requied to execution (Execution time)

import time

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    
    return Fact


def main():

    value = int(input("Enter Number : "))
    
    start_time = time.time()

    Ret = Factorial(value)

    end_time = time.time()

    print("Factorial is : ",Ret)

    print("Total execution time is : ",end_time - start_time)


if __name__ == "__main__":
    main()
