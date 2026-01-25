'''
    Design a python application that creates two seprates threads named Even and Odd.
    
    * The Even thread should diaplay the first 10 even numbers.
    * The odd thread should display the first 10 odd numbers.
    * both threads should execute independenlty using the threading module.
    * Ensure proper thread creation and execution
'''
import threading

def DisplayEven():
    print("Even Thread started...")
    for i in range(1, 11):
        print(i * 2)

def DisplayOdd():
    print("Odd Thread started...")
    for i in range(10):
        print((i * 2) + 1)

def main():
    Even = threading.Thread(target=DisplayEven)
    Odd = threading.Thread(target=DisplayOdd)

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

    print("Both threads execution completed")

if __name__ == "__main__":
    main()
