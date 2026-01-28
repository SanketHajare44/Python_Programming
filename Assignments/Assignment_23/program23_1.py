#  Write a python program to implement a class named BookStore with the following specification
#     * The class chould contains two instance variable
#         - Name (book name)
#         - Author (book author)
#     * The class should contain one class variable.
#         - NoOfBooks(initialize it to 0)
#     * Define a constructor(__init__) that accept Name and Author and initialize instance variable.
#     * Inside the constructor increment the class variable NoOfBooks by 1 Whenever a new object is created.
#     * implement an instance method
#         - Display() - should Display book details in the format
#           <BookName> by <Author>. No of books: <NoOfBooks>

class BookStore:
    NoOfBooks = 0

    def __init__(self,A,B):
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
        self.Name = A
        self.Author = B
    
    def Display(self):
        print(f"{self.Name} by {self.Author} No of books: {BookStore.NoOfBooks}")

def main():
    print("Enter the name of Book : ")
    value1 = str(input())

    print("Enter the Author : ")
    value2 = str(input())

    obj1 = BookStore(value1,value2)

    obj1.Display()

    print("Enter the name of Book : ")
    value1 = str(input())

    print("Enter the Author : ")
    value2 = str(input())

    obj2 = BookStore(value1,value2)

    obj2.Display()

if __name__ == "__main__":
    main()
