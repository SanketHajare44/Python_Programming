    # Write a program to implement a class named Arithmetic with the following characteristics:
    #     * The class should contain two instance variable : Value1 and Value2
    #     * Define a constructor (__init__) that initialize all instance variable to 0
    #     * Implement the following instance methods
    #         - Accept() : accepts values for Value1 and Value2 from the user
    #         - Addition() : returns the addition of Value1 and Value2
    #         - Substraction() : returns the substraction of Value1 and Value2
    #         - Multiplication() : returns the Multiplication of Value1 and Value2
    #         - Division() : returns the Division of Value1 and Value2 (Handle division by zero properly)
    #     *Create multiple objects of the arithmetic class and invoke all thr instance methods

class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        print("\nEnter the first number : ")
        self.Value1 = int(input())

        print("Enter the second number : ")
        self.Value2 = int(input())

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans
    
    def Substraction(self):
        Ans = self.Value1 - self.Value2
        return Ans

    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        Ans = 0
        try:
            Ans = self.Value1 / self.Value2
        except ZeroDivisionError as eobj:
            print("Error : Division by zero is not allowed")

        return Ans

def main():
    Ret = 0

    obj1 = Arithmetic()

    obj1.Accept()
    Ret = obj1.Addition()
    print("Addition is : ",Ret)

    Ret = obj1.Substraction()
    print("Substraction is : ",Ret)

    Ret = obj1.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj1.Division()
    print("Division is : ",Ret)


    obj2 = Arithmetic()

    obj2.Accept()
    Ret = obj2.Addition()
    print("Addition is : ",Ret)

    Ret = obj2.Substraction()
    print("Substraction is : ",Ret)

    Ret = obj2.Multiplication()
    print("Multiplication is : ",Ret)

    Ret = obj2.Division()
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()