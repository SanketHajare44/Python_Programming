import os

def main():
    FileName = input("Enter the name of file : ")
    
    if(os.path.exists(FileName)):
        fobj = open(FileName, "b")

        print(fobj.redable())   # returns the True if file is redable

        print(fobj.writable())  # returns the True if file is writable

        print(fobj.seekable())  # returns the True if file is allow to change offset
        
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()