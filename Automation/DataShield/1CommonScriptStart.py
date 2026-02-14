
import psutil
import sys
import os
import time
import schedule

def fun(DirName):
    pass

def main():

    Border = "-"*50
    print(Border)
    print("-----------Marvellous Data Shield System-----------")
    print(Border)

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to to : ")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive ofthe backup perodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automationc script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval : The time in minutes for perodic scheduling")
            print("SourceDirectory : Name of directory to backed up")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --u or --h to get more details")
    
    # python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print("Time Interval : ",sys.argv[1])
        print("Directory name : ",sys.argv[2])

        print("Data Shield system started succesfully")
        print("Time interval in minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")

        # Apply the schedular
        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])

        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    else:
        print("Invalid number of command line argument")
        print("Unable to proceed as there is no such option")
        print("Please use --u or --h to get more details")


    print(Border)
    print("------------Thank you for using script------------")
    print(Border)

if __name__ == "__main__":
    main()