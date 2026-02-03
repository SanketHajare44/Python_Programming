import os
import sys
import time

def DirectoryScanner(DirName = "Marvellous"):
    border = "-"*50

    timestamp = time.ctime()

    fobj = open("Marvellous.log","w")

    fobj.write(border+"\n")
    fobj.write("This is a log file created by marvellous Automation\n")
    fobj.write("This is Directory  Cleaner Script\n")
    fobj.write(border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not a directory")
        return
    
    FileCount = 0
    EmptyFileCount = 0

    for FolderName, SubFolder, FileName in os.walk(DirName):
        
        for fname in FileName:
            FileCount = FileCount + 1
        
            fname = os.path.join(FolderName,fname) # previous error here handled
            
            if(os.path.getsize(fname) == 0):        # empty file check
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    fobj.write(border+"\n")
    fobj.write("Total file scanned : "+str(FileCount)+"\n")
    fobj.write("Total Empty file found : "+str(EmptyFileCount)+"\n")
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(border+"\n")


def main():
    border = "-"*50
    print(border)
    print("----------Marvellous Directory Automation---------")
    print(border)
    
    if(len(sys.argv) != 2):
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    DirectoryScanner(sys.argv[1])

    print(border)
    print("----------Marvellous Directory Automation---------")
    print(border)

if __name__ == "__main__":
    main()