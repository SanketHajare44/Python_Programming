''' Design Automation script whih accepts two directory names. Copy all files from first directory
into second directory. Second directory should br created aat run time.

Usage : DirectoryCopy.py "Demo" "Temp"

Demo is name of directory which is existing and contains files in it . We have to create new directory
as Temp and copy all files from Demo to Temp'''

import os
import sys
import time
import schedule

def CopyFile(SrcFile,DestFile):
    sobj = open(SrcFile,"rb")
    dobj = open(DestFile,"wb")

    Buffer = sobj.read(1024)

    while(len(Buffer) > 0):
        dobj.write(Buffer)
        Buffer = sobj.read(1024)
    
    dobj.close()
    sobj.close()


def CopyDirectory(DirName1,DirName2):

    Border = "-"*46

    TimeStamp = time.ctime()

    LogFileName = "DirectoryScanedReport %s.log"%(TimeStamp)

    LogFileName = LogFileName.replace(" ", "_")
    LogFileName = LogFileName.replace(":", "_")

    os.makedirs("Logs", exist_ok=True)

    LogFileName = os.path.join("Logs", LogFileName)

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("-----------Automation Script Report-----------\n")
    fobj.write("This is Directory Copy Automation script\n")
    fobj.write(Border+"\n")

    Ret = os.path.exists(DirName1)
    if(Ret == False):
        fobj.write("There is no such directory\n")
        fobj.close()
        return

    Ret = os.path.isdir(DirName1) 
    if(Ret == False):
        fobj.write("It is not a directory\n")
        fobj.close()
        return

    FileCount = 0

    for FolderName, SubFolderName, FileName in os.walk(DirName1):

        relpath = os.path.relpath(FolderName, DirName1)
        DestFolder = os.path.join(DirName2, relpath)

        os.makedirs(DestFolder, exist_ok=True)

        for filename in FileName:
            FileCount = FileCount + 1
            srcfile = os.path.join(FolderName, filename)
            destfile = os.path.join(DestFolder, filename)

            try:
                CopyFile(srcfile, destfile)
                fobj.write(f"Copied : {srcfile} -> {destfile}\n")
            except Exception as e:
                fobj.write(f"ERROR copying {srcfile} : {e}\n")

    fobj.write(Border+"\n")
    fobj.write("Total file Count : "+str(FileCount)+"\n")
    fobj.write("This log file is created at : "+TimeStamp+"\n")
    fobj.write(Border+"\n")

    fobj.write("------- Thank you for using our script -------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():

    Border = "-"*40
    print(Border)
    print("-------Sanket Hajare Automation---------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or (sys.argv[1] == '--H')):
            print("This application is used to perform : make the copy of directory")
            print("This is automation script")

        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--U')):
            print("Use the give script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : FileName.py")
            print("Argument2 : old Directory Path")
            print("Argument3 : new Directory Path")
        
        else:
            print("Use the given flags as")
            print("--u : Used to display the use")
            print("--h : Used to display the help")

    elif(len(sys.argv) == 3):

        schedule.every(10).seconds.do(CopyDirectory,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)
    else:
        print("Invalid number of Command line arguments")
        print("Use the given flags as")
        print("--u : Used to display the use")
        print("--h : Used to display the help")
    
    print(Border)
    print("-----Thank you for using our script-----")
    print(Border)

if __name__ == "__main__":
    main()