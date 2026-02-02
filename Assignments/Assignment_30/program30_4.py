# Copy file contents into another file

# Problem Statement : Write a program which accepts two file names from the user
#   * First file is an existing file
#   * Second file is a new file
# Copy all contents from the first file into the second file

# input : ABC.txt Demo.txt
# Expected Output : contents of ABC.txt Demo.txt copied into Demo.txt

import os
import sys

def CpyFile(FileName1,FileName2):
    if((os.path.exists(FileName1)) == False):
        print("File not Found")
        return
    
    fobj1 = open(FileName1, "r")

    fobj2 = open(FileName2,"w")

    for line in fobj1:
        fobj2.write(line)

    fobj1.close()
    fobj2.close()

def main():
    if(len(sys.argv) != 3):
        print("Invalid input")

    CpyFile(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()