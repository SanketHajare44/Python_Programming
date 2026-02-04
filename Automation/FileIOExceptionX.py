
def main():
    try:
        open("Demo.txt","r")
        print("File gets succesfully opened")
    except FileNotFoundError:           # specific  exception handled
        print("Unable to open file as there is no such file")
    finally:
        print("End of application")     # always execute

if __name__ == "__main__":        # Also called as dunder key word
    main()