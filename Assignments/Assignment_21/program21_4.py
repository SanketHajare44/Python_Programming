'''
    Design a Python application that creates two threads.

    * Thread 1 should compute the sum of elements from a list.

    * Thread 2 should compute the product of elements from the same list.

    * Return the results to the main thread and display them.
'''

import threading

def SumList(Arr):
    Sum = 0
    for no in Arr:
        Sum = Sum + no
    print("Sum of elements :", Sum)

def ProductList(Arr):
    Prod = 1
    for no in Arr:
        Prod = Prod * no
    print("Product of elements :", Prod)

def main():
    Data = []
    Result = {}

    print("Enter number of elements : ")
    n = int(input())

    for i in range(n):
        print("Enter element :", i + 1)
        Data.append(int(input()))

    print("Input List :", Data)

    t1 = threading.Thread(target=SumList, args=(Data,), name="Thread1")
    t2 = threading.Thread(target=ProductList, args=(Data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
