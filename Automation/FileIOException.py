
def main():
    try:
        open("Demo.txt")        # if read write mode is not specified then it take defualt 'read' mode
        print("File gets succesfully opened")
    except FileNotFoundError:           # specific  exception handled
        print("Unable to open file as there is no such file")
    finally:
        print("End of application")     # always execute

if __name__ == "__main__":        # Also called as dunder key word
    main()