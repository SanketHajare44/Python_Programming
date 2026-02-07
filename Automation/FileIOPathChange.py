import os

def main():
    FileName = input("Enter the name of file : ")
    
    if(os.path.exists(FileName)):
        Ret = os.path.isabs(FileName)       # abs is blind method it doesnt check  file is present or not 
        
        if(Ret == True):
            print("It is absolute path")
        else:
            print("It is relative path")
            NewPath = os.path.abspath(FileName)         # it converts relative to absolute if givened path is not a absolute path (blind method)
            print("Updated path : ",NewPath)
    else:
        print("There is no such file")

if __name__ == "__main__":
    main()