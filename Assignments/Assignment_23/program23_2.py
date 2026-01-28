# Write a python program to implement a class named BankAccount With the following Requirements.
#     * The class should contains two instance variable
#         -Name(Account holder name)
#         -Amount(Account balance)
#     * The class should contains one class variable
#         -ROT(Rate of Interest),initialized to 10.5
#     * Define a constructor (__init__) that accept Name and initial ammount.
#     * Implement the following instance methods.
#         - Display() - display account holder name and current balance
#         - Deposite() - accept an ammount from the user and adds it to balance
#         - withdraw() - accepts an ammount from the user and substract it from balance
#             (Ensure withdrawal is allowed only if sufficient balance exist)
#         - CalculateInterest() -claculates and returns Interest using formula
#           Interest = (Amount * ROI) / 100
#     * Create multiple objects and demonstrate all methods

class BankAccount:
    ROI = 10.5

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B
    
    def Display(self):
        print("Name : ",self.Name)
        print("Amount : ",self.Amount)
    
    def Deposite(self,Value):
        self.Amount = self.Amount + Value
    
    def withdraw(self,Value):
        if(Value > self.Amount):
            print("Insufficient balance")
            return

        self.Amount = self.Amount - Value
        
            
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

def main():
    Ret = 0.0

    obj1 = BankAccount("Sanket",10000)

    obj1.Display()

    obj1.Deposite(500)

    obj1.Display()
        
    obj1.withdraw(500)

    obj1.Display()

    Ret = obj1.CalculateInterest()
    print("Interest is : ",Ret)

    print("------------------------------------------------------")
    
    obj2 = BankAccount("Hajare",20000)

    obj2.Display()

    obj2.Deposite(500)

    obj2.Display()
        
    obj2.withdraw(500)

    obj2.Display()

    Ret = obj2.CalculateInterest()
    print("Interest is : ",Ret)

if __name__ == "__main__":
    main()