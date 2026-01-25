def Chkprime(Value):
    Flag = True
    for i in range(2,int(Value/2)+1):
        if(Value % i == 0):
            Flag = False
            break
    return Flag