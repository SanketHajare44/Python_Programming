
def EmployeeInfo(Name, Age, Salary, City="Pune"):   # Default argument
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salary : ",Salary)
    print("City : ",City)

def main():
    # Default
    EmployeeInfo("Rahul", 26, 2000.50)     # Correct

if __name__ == "__main__":
    main()