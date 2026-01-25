'''
    Design a Python application that creates three threads named Small, Capital, and

    * All threads should accept a string as input.

    * The Small thread should count and display the number of lowercase characters.

    * The Capital thread should count and display the number of uppercase characters.

    * The Digits thread should count and display the number of numeric digits.

    * Each thread must also display:
        Thread ID
        Thread Name
'''
import threading

def CountSmall(Str):
    count = 0
    for ch in Str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            count += 1

    print("Small Thread")
    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Count :", count)


def CountCapital(Str):
    count = 0
    for ch in Str:
        if ord(ch) >= 65 and ord(ch) <= 90:
            count += 1

    print("\nCapital Thread")
    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Count :", count)


def CountDigits(Str):
    count = 0
    for ch in Str:
        if ord(ch) >= 48 and ord(ch) <= 57:
            count += 1

    print("\nDigits Thread")
    print("Thread ID   :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits Count :", count)


def main():
    print("Enter string : ")
    Data = input()

    t1 = threading.Thread(target=CountSmall, args=(Data,), name="Small")
    t2 = threading.Thread(target=CountCapital, args=(Data,), name="Capital")
    t3 = threading.Thread(target=CountDigits, args=(Data,), name="Digits")

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\nExit from main")


if __name__ == "__main__":
    main()
