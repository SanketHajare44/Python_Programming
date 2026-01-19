import threading

iCnt = 0

def Update():
    global iCnt

    for _ in range(200000):
        iCnt = iCnt + 1

def  main():
    Update()
    Update()

    global iCnt

    print("Value of iCnt is : ",iCnt)

if __name__ == "__main__":
    main()