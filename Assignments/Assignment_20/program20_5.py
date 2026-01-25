'''
   Design a Python application that creates two threads named Thread1 and Thread2.

    * Thread1 should display numbers from 1 to 50.

    * Thread2 should display numbers from 50 to 1 in reverse order.

    * Ensure that:
        Thread2 starts execution only after Thread1 has completed.

    * Use appropriate thread synchronization   
'''
import threading

def Display1():
    print("Inside Thread 1")
    for i in range(1, 51):
        print(i, end=" ")
    print("\nThread1 completed...\n")

def Display2():
    print("Inside Thread 2")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print("\nThread2 completed...\n")

def main():
    t1 = threading.Thread(target=Display1, name="Thread1")
    t2 = threading.Thread(target=Display2, name="Thread2")

    t1.start()
    t1.join()  

    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()