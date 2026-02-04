''' Desing automation script which accepts directory name and file extensions from user. 
    Display all files with that extensions.
        Usage : DirectoryFileSearch "Demo"".txt"
        Demo is the name of directory and .txt is the extension that we want to search
'''

import sys
import os
import time
import schedule

def  DirectoryScanner(DirName,Extension):
    Border = "-"*46

    TimeStamp = time.ctime()

    LogFileName = "DirectoryScanedReport %s.log"%(TimeStamp)

    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("-----------Automation Script Report-----------\n")
    fobj.write("This is Directory Scanner Automation script\n")
    fobj.write(Border+"\n")

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
    TextFile = 0

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            FileCount = FileCount + 1
            if(fname.endswith(Extension) == True):
                TextFile = TextFile + 1
                fobj.write(str(TextFile)+"."+fname+"\n")
    
    fobj.write(Border+"\n")
    fobj.write("Total file scanned : "+str(FileCount)+"\n")
    fobj.write("Total Text file found : "+str(TextFile)+"\n")
    fobj.write("This log file is created at : "+TimeStamp+"\n")
    fobj.write(Border+"\n")

def main():
    if(len(sys.argv) != 3):
        print("Error : Invalid input")
        return
    
    schedule.every(10).seconds.do(DirectoryScanner,sys.argv[1],sys.argv[2])

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()