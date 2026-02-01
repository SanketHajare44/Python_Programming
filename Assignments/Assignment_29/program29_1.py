# Write a program which acccepts a file name from the user and checks whether that file exist in the current directory or not

# Input : Demo.txt
# Expected output : Display whether Demo.txt exist or not 

import os

def CheckFile(fname):
    if(os.path.exists(fname)):
        return True
    else:
        return False

def main():
    FileName = input("Enter the file name : ")
    bRet = CheckFile(FileName)

    if(bRet == True):
        print("File is exist")
    else:
        print("File is not exist")

if __name__ == "__main__":
    main()