# Compare two files (Command line)

#Problem statement : Write a program which accepts two file names through command line arguments and compares
#                    the contents of both files

#   * If both file contains the same contents display success
#   * Otherwise display failure

import sys
import os
import hashlib

def CheckSum(name):
    fobj = open(name,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def CheckFile(FileName1, FileName2):

    if(((os.path.exists(FileName1)) == False)):
        print(f"{FileName1} is not exists")
        return
    
    if(((os.path.exists(FileName2)) == False)):
        print(f"{FileName2} is not exists")
        return

    Ret1 = CheckSum(FileName1)
    Ret2 = CheckSum(FileName2)

    if(Ret1 == Ret2):
        return True
    else:
        return False

def main():
    if(len(sys.argv) != 3):
        print("Error : Inavlid input")
        return

    Ans = CheckFile(sys.argv[1],sys.argv[2])

    if(Ans == True):
        print("Success")
    else:
        print("Failure")

if __name__ == "__main__":
    main()