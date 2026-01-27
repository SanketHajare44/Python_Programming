import sys

def main():
    Border = "-"*40
    print(Border)
    print("------- Marvellous Automation ----------")
    print(Border)

    if(len(sys.argv) == 2):
        if((sys.argv[1] == '--h') or (sys.argv[1] == '--H')):
            print("This application is used to perform--___")
            print("This is automation script")

        elif((sys.argv[1] == '--u') or (sys.argv[1] == '--U')):
            print("Use the give script as")
            print("ScriptName.py Argument1 Argument2")
            print("Argument1 : _______")
            print("Argument2 : _______")
        
        else:
            print("Use the give flags as")
            print("--u : Used to display the use")
            print("--h : Used to display the help")
    else:
        print("Invalid number of Command line arguments")
        print("Use the given flags as")
        print("--u : Used to display the use")
        print("--h : Used to display the help")
    
    print(Border)
    print("-------Thank you for using our script---")
    print("----------Marvellous Infosystem---------")
    print(Border)

if __name__ == "__main__":
    main()