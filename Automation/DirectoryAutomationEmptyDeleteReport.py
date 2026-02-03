import os
import sys

def DirectoryScanner(DirName = "Marvellous"):
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

            print("File name : ",fname)
            print("File Size : ",os.path.getsize(fname))
            
            if(os.path.getsize(fname) == 0):        # empty file check
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)

    border = "-"*50
    print(border)
    print("-----------------Automation Report----------------")
    print("Total file scanned : ",FileCount)
    print("Total Empty file found : ",EmptyFileCount)
    print(border)



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