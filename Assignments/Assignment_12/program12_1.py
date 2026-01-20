# Write a program which accepts one character and checks whether it is vowel or consonant.

def ChkVowel(Value):
    if(Value == "a" or Value == "e" or Value == "i" or Value == "o" or Value == "u" or
       Value == "A" or Value == "E" or Value == "I" or Value == "O" or Value == "U"):
       return True
    else:
        return False

def main():
    No = ""
    bRet = False

    print("Enter the Character : ")
    No = input()

    bRet = ChkVowel(No)

    if(bRet == True):
        print("It is vowel")
    else:
        print("It is Consonant")

if __name__ == "__main__":
    main()