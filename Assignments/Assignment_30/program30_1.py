# Count Lines in a File
# Problem statement  : Write a program which accepts a file name from the user and counts how many lines are present in the file .

# Input : Demo.txt
# Expected Output : Total number of lines in Demo.txt

import os

def CountLines(name):

    if((os.path.exists(name)) == False):
        print("File not exist")
        return

    fobj = open(name, "r")
    count = 0

    for line in fobj:
        count = count + 1

    fobj.close()
    
    return count

def main():
    FileName = input("Enter the file Name : ")

    Ret = CountLines(FileName)

    print("Total count of line is : ",Ret)

if __name__ == "__main__":
    main()