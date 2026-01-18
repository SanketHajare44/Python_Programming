
def main():

    Ans = 0
    try:
        print("Enter first number : ")
        no1 = int(input())

        print("Enter Second number : ")
        no2 = int(input())

    
        print("Inside try.")
        Ans = no1 / no2

    except:
        print("Inside except")

    finally:
        print("Inside finally")

    print("Division is : ",Ans)

if __name__ == "__main__":
    main()