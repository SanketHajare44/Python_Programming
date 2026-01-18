
def main():

    Ans = 0
    
    print("Enter first number : ")
    no1 = int(input())

    print("Enter Second number : ")
    no2 = int(input())

    try:
        print("Inside try.")
        Ans = no1 / no2

    except:
        print("Inside except")


    print("Division is : ",Ans)

if __name__ == "__main__":
    main()