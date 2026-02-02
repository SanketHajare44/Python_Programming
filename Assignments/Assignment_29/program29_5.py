# Frequency of a string in file
# Problem statement : Write a program which accepts a file name and one string from the user and returns 
#                     the frequency (count of occurence) of that string in the file 
# Input : Demo.txt Marvellous
# Expected output : Count how many times "Marvellous" appears in demo.txt.

import sys

def CheckString(FileName, string):
    fobj = open(FileName, "r")

    Data = fobj.read()

    Data = Data.lower()
    string = string.lower()
    
    Ret = Data.count(string)

    print(Ret)

def main():
    if(len(sys.argv) != 3):
        print("Invalid inpiut")
        return
    
    CheckString(sys.argv[1],sys.argv[2])


if __name__ == "__main__":
    main()