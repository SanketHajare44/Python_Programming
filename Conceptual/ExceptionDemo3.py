
def main():

    Ans = 0
    
    try:

        print("Enter first number : ")
        no1 = int(input())

        print("Enter Second number : ")
        no2 = int(input())

    
        print("Inside try.")
        Ans = no1 / no2

    except ZeroDivisionError as zobj:
        print("Inside except : ",zobj)

    except ValueError as vobj:
        print("Inside except : ",vobj)

    except Exception as eobj:               # Generic except block
        print("Inside except : ",eobj)

    finally:
        print("Inside finally ")

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()