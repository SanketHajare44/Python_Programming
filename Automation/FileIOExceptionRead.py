
def main():
    fobj = None
    try:
        fobj = open("Demo.txt","r")     # opened for Read (fobj is handle)
        print("File gets succesfully opened")

        Data = fobj.read()          # read the data from Hello.txt
        print("Data from file is : ",Data)

        fobj.close()                # file is closed using close() method

    except FileNotFoundError:           # specific  exception handled
        print("Unable to open file as there is no such file")
    finally:       
        print("End of application")     # always execute


if __name__ == "__main__":        # Also called as dunder key word
    main()