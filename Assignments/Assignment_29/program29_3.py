# Copy file content into new file (Command line)
# Problem Statement : Write a program which accepts an existing file name hrough command line arguments,
#                     create a new file named Demo.txt and copies all contents from the given file into Demo.txt
# Input : ABC.txt
# Output : create Demo.txt and copy contents of ABC.txt into  demo.txt

import os
import sys

def CpyFile(name):
    if(os.path.exists(name) == False):
        print("file is not s exists")
        return

    fobjsec = open(name,"r")

    fobjdest = open("Demo.txt","w")
    
    data = fobjsec.read()

    fobjdest.write(data)

    print("Copied the file succesfully")

    fobjsec.close()
    fobjdest.close()

def main():
    if(len(sys.argv) != 2):
        print("Invalid  input")
        return

    CpyFile(sys.argv[1])

if __name__ == "__main__":
    main()