###################################################################
#   Singly Circular Linked List
###################################################################

class node:
    def __init__(self,Value):
        self.data = Value

        self.next = None

class SinglyCLL:

    ###################################################################
    #
    #   Function Name : __init__
    #   Input         : Nothing
    #   Output        : Nothing
    #   Description   : It is constructor used to create instance variable
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def __init__(self):
        self.first = None
        self.last = None
        self.iCount = 0
        
    ###################################################################
    #
    #   Function Name : InsertFirst
    #   Input         : Data of node
    #   Output        : Nothing
    #   Description   : Used to insert node at first position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def InsertFirst(self,no):

        newn = node(no)
        
        if self.first == None and self.last == None:
            self.first = newn
            self.last = newn

            self.last.next = self.first
        else:
            newn.next = self.first
            self.first = newn

            self.last.next = self.first

        self.iCount = self.iCount + 1        

    ###################################################################
    #
    #   Function Name : InsertLast
    #   Input         : Data of node
    #   Output        : Nothing
    #   Description   : Used to insert node at last position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def InsertLast(self,no):
        
        newn = node(no)

        if(self.first == None and self.last == None):
            self.first = newn
            self.last = newn

            self.last.next = self.first
        else:
            self.last.next = newn
            newn.next = self.first

            self.last = newn
        
        self.iCount = self.iCount + 1

    ###################################################################
    #
    #   Function Name : InsertAtPos
    #   Input         : Data of node, Integer
    #   Output        : Nothing
    #   Description   : Used to insert a node at the given position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################
   
    def InsertAtPos(self,no,pos):
        
        newn = node(no)

        if(pos < 1 or pos > self.iCount+1):
            print("Invalid Position")
            return

        if(pos == 1):
            self.InsertFirst(no)

        elif(pos == self.iCount + 1):
            self.InsertLast(no)

        else:
            temp = self.first

            for i in range(pos-2):
                temp = temp.next

            newn.next = temp.next
            temp.next = newn

            self.iCount = self.iCount + 1

    ###################################################################
    #
    #   Function Name : DeleteFirst
    #   Input         : Nothing
    #   Output        : Nothing
    #   Description   : Used to delete node at first position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################
        
    def DeleteFirst(self):
        
        if(self.first == None and self.last == None):
            return

        if(self.first == self.last):
            
            del self.first
            del self.last

            self.first = None
            self.last = None
        else:
            temp = self.first.next
            
            self.last.next = temp
            
            del self.first

            self.first = temp

        self.iCount = self.iCount - 1

    ###################################################################
    #
    #   Function Name : DeleteLast
    #   Input         : Nothing
    #   Output        : Nothing
    #   Description   : Used to delete node at last position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def DeleteLast(self):

        if(self.first == None and self.last == None):
            return

        if(self.first == self.last):
            
            del self.first
            del self.last

            self.first = None
            self.last = None

        else:
            
            temp = self.first

            while(temp.next.next != self.first):
                temp = temp.next

            del self.last

            temp.next = self.first

        self.iCount = self.iCount - 1

    ###################################################################
    #
    #   Function Name : DeleteAtPos
    #   Input         : Integer
    #   Output        : Nothing
    #   Description   : Used to Delete a node from the given position
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def DeleteAtPos(self,pos):

        if(pos < 1 or pos > self.iCount):
            print("Invalid Position")
            return

        if(self.first == None and self.last == None):
            return

        elif(pos == 1):
            self.DeleteFirst()

        elif(pos == self.iCount):
            self.DeleteLast()
        
        else:
            
            temp = self.first

            for i in range(pos-2):
                temp = temp.next

            temp.next = temp.next.next

            self.iCount = self.iCount - 1

    ###################################################################
    #
    #   Function Name : Display
    #   Input         : Nothing
    #   Output        : Nothing
    #   Description   : Used to display the nodes
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################
       
    def Display(self):

        if(self.first == None):
            return

        temp = self.first

        while(True):
            print("| ",temp.data," |->",end=" ")
            temp = temp.next

            if(temp == self.first):
                break

        print()

    ###################################################################
    #
    #   Function Name : Count
    #   Input         : Nothing
    #   Output        : Integer
    #   Description   : Used to count the nodes
    #   Author        : Sanket Sadashiv Hajare
    #   Date          : 23//03/2026
    #
    ###################################################################

    def Count(self):
        return self.iCount

###################################################################
#
#   Function Name : main
#   Input         : Nothing
#   Output        : Nothing
#   Description   : Used to control all helper module
#   Author        : Sanket Sadashiv Hajare
#   Date          : 23//03/2026
#
###################################################################

def main():
    sobj = SinglyCLL()

    sobj.InsertFirst(11)
    sobj.InsertFirst(21)
    sobj.InsertFirst(51)
    sobj.InsertFirst(101)
    sobj.InsertFirst(121)

    print("\nElements of Linked List are : ")
    sobj.Display()

    print("Total number of node is : ",sobj.Count())

###################################################################

    sobj.InsertLast(151)
    sobj.InsertLast(201)
    
    print("\nElements of Linked List are : ")
    sobj.Display()
  
    print("Total number of node is : ",sobj.Count())

###################################################################

    sobj.InsertAtPos(200,3)

    print("\nElements of Linked List are : ")
    sobj.Display()
  
    print("Total number of node is : ",sobj.Count())

###################################################################

    sobj.DeleteFirst()

    print("\nElements of Linked List are : ")
    sobj.Display()
  
    print("Total number of node is : ",sobj.Count())

###################################################################

    sobj.DeleteLast()

    print("\nElements of Linked List are : ")
    sobj.Display()
  
    print("Total number of node is : ",sobj.Count())

###################################################################

    sobj.DeleteAtPos(3)

    print("\nElements of Linked List are : ")
    sobj.Display()
  
    print("Total number of node is : ",sobj.Count())

if __name__=="__main__":
    main()