'''
    Design a Python application that creates two threads.

    * Thread 1 should calculate and display the maximum element from an list.

    * Thread 2 should calculate and display the minimum element from the same list.

    * The list should be accepted from the user.

'''

import threading

def DisplayMax(Arr):
    Max = Arr[0]
    for i in Arr:
        if i > Max:
            Max = i
    print("Maximum element is :", Max)

def DisplayMin(Arr):
    Min = Arr[0]
    for i in Arr:
        if i < Min:
            Min = i
    print("Minimum element is :", Min)

def main():
    Data = []

    print("Enter number of elements : ")
    n = int(input())

    for i in range(n):
        print("Enter element :", i + 1)
        Data.append(int(input()))

    print("Input list :", Data)

    t1 = threading.Thread(target=DisplayMax, args=(Data,), name="Thread1")
    t2 = threading.Thread(target=DisplayMin, args=(Data,), name="Thread2")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()
