# It is used to calculate the check sum of file using md5 algo

import hashlib
import os

def CalculateCheckSum(FileName):
    fobj = open(FileName, "rb")
    
    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    
    fobj.close()

    return hobj.hexdigest()


def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("There is no such  directory")
        return
    
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return

    Duplicate = {}

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):

        for fname in FileName:
            fname = os.path.join(FolderName,fname)         
            CheckSum = CalculateCheckSum(fname)
            
            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]
    
    return Duplicate
    
def DeleteDuplicate(Path = "Marvellous"):
    MyDict = FindDuplicate(Path)

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    count = 0
    cnt = 0

    for value in Result:
        for subvalue in value:
            count = count + 1

            if(count > 1):
                print("Deleted file : ",subvalue)
                os.remove(subvalue)
                cnt = cnt + 1
        
        count = 0

    print("Total deleted file : ",cnt)


def main():

    DeleteDuplicate()

if __name__ == "__main__":
    main()