
def main():
    fobj = None
    try:
        fobj = open("Hello.txt","w")     # opened for write (fobj is handle)
        print("File gets succesfully opened")

        fobj.write("Jay Ganesh Marvellous...")     # write method is used

        fobj.close()                # file is closed using close() method

    except FileNotFoundError:           # specific  exception handled
        print("Unable to open file as there is no such file")
    finally:       
        print("End of application")     # always execute


if __name__ == "__main__":        # Also called as dunder key word
    main()