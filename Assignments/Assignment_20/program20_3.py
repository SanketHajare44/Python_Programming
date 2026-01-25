'''
    Design a Python application that creates two threads named EvenList and OddList.

    * Both threads should accept a list of integers as input.

    * The EvenList thread should:
        Extract all even elements from the list.
        Calculate and display their sum.

    *The OddList thread should:
        Extract all odd elements from the list.
        Calculate and display their sum.

    * Threads should run concurrently.
'''

import threading

def EvenList(Arr):
    Even = []
    Sum = 0

    for no in Arr:
        if no % 2 == 0:
            Even.append(no)
            Sum = Sum + no

    print("Even elements :", Even)
    print("Sum of even elements :", Sum)


def OddList(Arr):
    Odd = []
    Sum = 0

    for no in Arr:
        if no % 2 != 0:
            Odd.append(no)
            Sum = Sum + no

    print("Odd elements :", Odd)
    print("Sum of odd elements :", Sum)


def main():
    Data = []

    print("Enter number of elements : ")
    No = int(input())

    for i in range(No):
        print("Enter element :", i + 1)
        Value = int(input())
        Data.append(Value)

    print("Input List :", Data)

    t1 = threading.Thread(target=EvenList, args=(Data,), name="EvenList")
    t2 = threading.Thread(target=OddList, args=(Data,), name="OddList")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()
