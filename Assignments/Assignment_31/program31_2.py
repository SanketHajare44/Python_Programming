'''Design automation script which accept directory name and two filw extension from user.
    Rename all files with first file extension  with the second file extension.
        Usage : DirectoryRename.py "Demo" ".txt" ".jpg"
    Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
    After Executionhis script each .txt  file gets renamed as doc '''

import sys
import os
import time
import schedule

def  DirectoryScanner(DirName,Extension1,Extension2):
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
    RenameCount = 0

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            FileCount = FileCount + 1
            if(fname.endswith(Extension1) == True):
                
                OldName = os.path.join(FolderName, fname)

                name, ext = os.path.splitext(fname)
                
                NewName = os.path.join(FolderName, name+Extension2)

                if(os.path.exists(NewName) == True):
                    fobj.write("SKIPPED (already exists): " + OldName + "\n")
                    continue

                os.rename(OldName,NewName)
                RenameCount = RenameCount + 1
                fobj.write(str(RenameCount)+"."+fname+"->"+NewName+"\n")
    
    fobj.write(Border+"\n")
    fobj.write("Total file scanned : "+str(FileCount)+"\n")
    fobj.write("Total file renamed : "+str(RenameCount)+"\n")
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
            print("This application is used to perform : Change File Extension")
            print("This is automation script")

        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--U')):
            print("Use the give script as")
            print("ScriptName.py Argument1 Argument2 Argument3")
            print("Argument1 : FileName.py")
            print("Argument2 : Directory Path")
            print("Argument3 : old Extension")
            print("Argument4 : New Extension")
        
        else:
            print("Use the given flags as")
            print("--u : Used to display the use")
            print("--h : Used to display the help")

    elif(len(sys.argv) == 4):
        schedule.every(10).seconds.do(DirectoryScanner,sys.argv[1],sys.argv[2],sys.argv[3])

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