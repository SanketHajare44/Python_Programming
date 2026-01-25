'''
    Design a Python application that creates two threads named Prime and NonPrime.

    * Both threads should accept a list of integers.

    * The Prime thread should display all prime numbers from the list.

    * The NonPrime thread should display all non-prime numbers from the list.

'''

import threading

def CheckPrime(No):
    if No < 2:
        return False

    for i in range(2, int(No/2) + 1):
        if No % i == 0:
            return False

    return True


def PrimeThread(Arr):
    print("Inside Prime Thread")
    print("Prime numbers are : ", end="")

    for no in Arr:
        if (CheckPrime(no) == True):
            print(no, end=" ")
    print()


def NonPrimeThread(Arr):
    print("Inside NonPrime Thread")
    print("Non-prime numbers are : ", end="")

    for no in Arr:
        if (CheckPrime(no) == False):
            print(no, end=" ")
    print()


def main():
    Data = []
    No = 0
    Ans = 0

    print("Enter number of elements : ")
    No = int(input())

    for i in range(No):
        print("Enter element :",)
        Ans = int(input())
        Data.append(Ans)
        

    print("Input List :", Data)

    t1 = threading.Thread(target=PrimeThread, args=(Data,), name="Prime")
    t2 = threading.Thread(target=NonPrimeThread, args=(Data,), name="NonPrime")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
