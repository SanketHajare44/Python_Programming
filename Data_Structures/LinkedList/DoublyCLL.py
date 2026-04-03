###################################################################
#   Doubly Circular Linked List
###################################################################

class node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None

class DoublyCLL:

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

        if(self.first == None or self.last == None):
            self.first = newn
            self.last = newn
        
        else:
            newn.next = self.first
            self.first.prev = newn
            self.first = newn

        self.last.next = self.first
        self.first.prev = self.last
        
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

        if(self.first == None or self.last == None):
            self.first = newn
            self.last = newn
        
        else:
            self.last.next = newn
            newn.prev = self.last
            self.last = newn
        
        self.last.next = self.first
        self.first.prev = self.last

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
        if(pos < 1 or pos > self.iCount + 1):
            print("\nInvalid Position")
            return

        if(pos == 1):
            InsertFirst(no)
        
        elif(pos == self.iCount + 1):
            InsertLast(no)
        
        else:
            newn = node(no)

            temp = self.first

            for i in range(1,pos-1):
                temp = temp.next

            newn.next = temp.next
            temp.next.prev = newn

            temp.next = newn
            newn.prev = temp

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
            self.first = None
            self.last = None
        
        else:
            self.first = self.first.next
            self.last.next = self.first
            self.first.prev = self.last
        
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
            self.first = None
            self.last = None
        
        else:
            self.first.prev = self.last.prev
            self.last.prev.next = self.first

            self.last = self.last.prev
        
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
            print("\nInvalid position")
            return
        
        if(pos == 1):
            self.DeleteFirst()
        
        elif(pos == self.iCount):
            self.DeleteLast()
        
        else:
            temp = self.first

            for i in range(1,pos):
                temp = temp.next
            
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

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
        temp = self.first
        
        print("<-",end="")
        for i in range(self.iCount):

            print("| ",temp.data," |->",end=" ")
            temp = temp.next
        
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
    dobj = DoublyCLL()

    dobj.InsertFirst(11)
    dobj.InsertFirst(21)
    dobj.InsertFirst(51)
    dobj.InsertFirst(101)
    dobj.InsertFirst(121)

    print("\nElements of Linked List are : ")
    dobj.Display()

    print("Total number of node is : ",dobj.Count())

###################################################################

    dobj.InsertLast(151)
    dobj.InsertLast(201)
    
    print("\nElements of Linked List are : ")
    dobj.Display()
  
    print("Total number of node is : ",dobj.Count())

#################################################################

    dobj.InsertAtPos(200,6)

    print("\nElements of Linked List are : ")
    dobj.Display()
  
    print("Total number of node is : ",dobj.Count())

#################################################################

    dobj.DeleteFirst()

    print("\nElements of Linked List are : ")
    dobj.Display()
  
    print("Total number of node is : ",dobj.Count())

#################################################################

    dobj.DeleteLast()

    print("\nElements of Linked List are : ")
    dobj.Display()
  
    print("Total number of node is : ",dobj.Count())

#################################################################

    dobj.DeleteAtPos(6)

    print("\nElements of Linked List are : ")
    dobj.Display()
  
    print("Total number of node is : ",dobj.Count())

if __name__=="__main__":
    main()