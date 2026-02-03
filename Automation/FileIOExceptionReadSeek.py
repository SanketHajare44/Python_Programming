
def main():
    fobj = None
    try:
        fobj = open("Hello.txt","r")     # opened for 'Read' (fobj is handle)
        print("File gets succesfully opened")

        print("Current offset is : ",fobj.tell())  # 0 # offset checked

        fobj.seek(7)    # offset changed to 7 second parameter is default '0'

        print("Current offset is : ",fobj.tell())   # 7 offset checked

        Data = fobj.read(10)          # read the first from Hello.txt
        print("Data from file is : ",Data)

        print("Current offset is : ",fobj.tell())   # 17 # offset checked

        fobj.close()                # file is closed using 'close()' method

    except FileNotFoundError:           # 'specific'  exception handled
        print("Unable to open file as there is no such file")
    finally:       
        print("End of application")     # always execute


if __name__ == "__main__":        # Also called as dunder key word
    main()