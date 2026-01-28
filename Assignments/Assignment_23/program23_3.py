# Write a python to implemet a class named Numbers with the following specification:
#     * The class should contains one instance variable
#         - value
#     * Define a constructor (__init__) that accepts a number from the user and initialize value
#     * implement the following instance methods
#         - ChkPrime() - return True if the number is prime otherwise return False
#         - ChkPerfect() - return True if the number is perfect otherwise returns False
#         - Factors() - display all factors of the number
#         - SumFactors() - return the sum of all factors
#             (you may use this method as a helper in ChkPerfect() if required)
#     * Creat multiple objects and all methods

class Numbers:
    def __init__(self,A):
        self.Value = A

    def ChkPrime(self):
        flag = True

        if self.Value <= 1:
            return False

        for i in range(2,int(self.Value / 2) + 1):
            if (int(self.Value % i) == 0):
                flag = False
                break
        return flag
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,int(self.Value / 2) + 1):
            if (int(self.Value % i) == 0):
                Sum = Sum + i
        
        if(Sum == self.Value):
            return True
        else:
            return False

    def Factors(self):
        for i in range(1,self.Value + 1):
            if (int(self.Value % i) == 0):
                print(i, end = " ")
        
        print()
    
    def SumFactors(self):
        
        Sum = 0
        for i in range(2,int(self.Value / 2) + 1):
            if (int(self.Value % i) == 0):
                Sum = Sum + i
        
        return Sum

def main():

    obj1 = Numbers(20)

    Ret = obj1.ChkPrime()
    if(Ret == False):
        print("It is not a prime number")
    else:
        print("It is a prime number")


    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print("It is perfect number")
    else:
        print("It is not a perfect number")

    obj1.Factors()

    Ret = obj1.SumFactors()
    print("Sum of factors is : ",Ret)

if __name__ == "__main__":
    main()
        
