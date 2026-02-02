# Search a word in file
# Problem statement : Write a program which accepts a file name and a word from the user and checks whether
#                     that word is present in the file or not

# Input : Demo.txt marvellous
# Expected Output : Display whether the word marvellous is found in demo.txt or not

import os
import sys

def CheckWord(FileName,string):
    if((os.path.exists(FileName)) == False):
        print("File not found")
        return
    
    fobj = open(FileName, "r")

    for line in fobj:
        if string in line:
            return True
    
    fobj.close()

    return False
def main():
    if(len(sys.argv) != 3):
        print("Inavlid input")
    
    Ret = CheckWord(sys.argv[1],sys.argv[2])

    if(Ret == True):
        print(f"{sys.argv[2]} is found in {sys.argv[1]}")
    else:
        print(f"{sys.argv[2]} is not found in {sys.argv[1]}")

    
if __name__ == "__main__":
    main()