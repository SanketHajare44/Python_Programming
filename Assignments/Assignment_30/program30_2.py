# Count Words in a file

# Problem statement : Write  a program which accepts a file name from the user and count the total number
#                     of words in that file 
# Input : Demo.txt
# Expected Output :  total number of words in Demo.txt

def CountWords(name):
    fobj = open(name,"r")

    Data = fobj.read()

    Ans = Data.split()      # split will split the lines into words

    fobj.close()

    return len(Ans)

def main():
    print("Enter the file name : ")
    FileName = input()

    Ret = CountWords(FileName)
    
    print("Total count of Words is : ",Ret)


if __name__ == "__main__":
    main()