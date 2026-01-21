# write a program which accepts one marks and displays grade.

def Display(Value):
    if(Value < 50):
        print("Fail")
    elif(Value >= 50 and Value < 60):
        print("Second class")
    elif(Value >= 60 and Value < 75):
        print("First class")
    elif(Value >= 75):
        print("Distinction")  

def main():
    No = 0

    print("Enter the number : ")
    No = int(input())

    Display(No)

if __name__ == "__main__":
    main()
    
