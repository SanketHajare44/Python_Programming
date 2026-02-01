# Write a program which accepts a file name from the user,open that file , and dsiplay the entire 
# contents on the console

# Input : Demo.txt
# Output : Display contents of Demo.txt on console

import os

def Display(fname):
    if(os.path.exists(fname) == False):
        return
    else:
        fobj = open(fname,"r")
        print("File gets succesfully opened")

        Data = fobj.read()

        print(Data)

        print()


def main():
    FileName = input("Enter the file name : ")

    Display(FileName)

if __name__ == "__main__":
    main()