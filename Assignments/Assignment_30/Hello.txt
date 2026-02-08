# Display File Line by Line

# Problem Statement : Write a program which accepts a file name from the user and display the contents pf thr file line by line on the screen
# Input : Demo.txt
# Expected Output : Display each linr of Demo.txt one by one.

import os
import sys

def Display(FileName):
    if((os.path.exists(FileName)) == False):
        print("Error : File not found")

    fobj = open(FileName,"r")

    for line in fobj:
        print(line, end = " ")
    
    fobj.close()


def main():
    if(len(sys.argv) != 2):
        print("Invalid input")
        return
    
    Display(sys.argv[1])

if __name__ == "__main__":
    main()
