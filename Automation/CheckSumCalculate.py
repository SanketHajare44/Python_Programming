# It is used to calculate the check sum of file using md5 algo

import hashlib

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()


def main():

    Ret = CalculateCheckSum("Demo.txt")     # it will return hexadecimal value 

    print("CheckSum is : ",Ret)

if __name__ == "__main__":
    main()