from datetime import datetime

class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print(f"\nThe available books are: \n")

        for book in self.books:
            print(f" * {book}")
 
    def borrowBook(self,bookName):
        now = datetime.now()
        time = now.strftime("%d/%m/%Y %H:%M:%S")

        if bookName in self.books:
            print(f'''You have been issued the book. Enjoy reading your book and return it on time.
            Current Date and Time is: {time}.
            ''')
            self.books.remove(bookName)
            return True

        else:
            print("Sorry! Either the book is not available or it is borrowed by some other user.Please wait until it is available")
            return False

    def returnBook(self,bookName,days):
        self.books.append(bookName)

        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

    def addBook(self,bookName):
        self.books.append(bookName)

        print("Thanks for adding this book! Have a great day ahead!")


class Students:

    def requestBook(self):
        self.book = input("Please Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Please Enter the name of the book you want to return: ")
        return self.book

    def addBook(self):
        self.book = input("Please Enter the name of the book you want to add: ")
        return self.book

    def fine(self,days):
        self.days = days

        if days > 30:
            self.fine = "10Rs\."
            print (f"Your Fine is {self.fine} as you have not returned book on time.")
        else:
            return
        
        

if __name__ == "__main__":

    listOfBooks = ["The Night Circus", "Rich Dad Poor Dad", "Atomic Habits", "The Power of Habit", "The Jungle Book", "Becoming Bulletproof", "The 48 Laws of Power", "The Power of Positive Thinking", "Business Adventures", "A Gentleman in Moscow"]

    Quid_e_Azam_Library = Library(listOfBooks)
    student = Students()

    while (True):
    
        welcomeMessage = '''\n~~~~ Welcome to the Quaid-e-Azam Library ~~~~
        Please select an option:
        1: To display available books.
        2: To request a book.
        3: To return a book.
        4: To add a book.
        5: To exit.  \n'''

        print(welcomeMessage)
        option = int(input("Enter your option: "))

        if option == 1:
            Quid_e_Azam_Library.displayAvailableBooks()

        elif option ==2:
            Quid_e_Azam_Library.borrowBook(student.requestBook())

        elif option ==3:
            daysNo = int (input("Enter no of days you have borrowed book for: "))
            Quid_e_Azam_Library.returnBook(student.returnBook(),daysNo)
            student.fine(daysNo)

        elif option ==4:
            Quid_e_Azam_Library.addBook(student.addBook())

        elif option ==5:
            print("ThankYou! For using this library...")
            exit()

        else:
            print('Invalid option.')