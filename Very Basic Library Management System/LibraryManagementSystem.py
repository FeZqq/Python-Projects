import os

def clear():

    if os.name == 'nt':
        # For windows
        _ = os.system('cls')
         
    elif os.name == 'mac':
        # For MAC
        _ = os.system('clear')
                                     
    elif os.name == 'posix':
        # For Linux
        _ = os.system('clear')
                                                            
    else:
        # For Others                           
        _ = os.system('clear')

class Library():
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path,"a+")

    def __del__(self):
        self.file.close()
    
    def list_books(self):
        self.file.seek(0) # it takes you to the top of the page
        lines = self.file.read().splitlines()
        i = 1
        print("===================================================================================================")
        for line in lines:
            book_info = line.split(",")
            print(i,"-","|Book Name: {}|".format(book_info[0]),"|Author: {}|".format(book_info[1]),"|Release Date: {}|".format(book_info[2]),"|Pages: {}|".format(book_info[3]))
            i = i + 1
        print("===================================================================================================")

    def add_book(self):
        name = input("Enter the book title: ")
        author = input("Enter the author: ")
        release = input("Enter the release year: ")
        pages = input("Enter the number of pages: ")
        self.file.write(name + "," + author + "," + release + "," + pages + "\n")
        print("Book Added Sucsessfully!!")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")

        self.file.seek(0) 
        lines = self.file.read().splitlines()
        updated_books = []

        for line in lines:
                updated_books.append(line)

        self.file.seek(0)
        

        for book in updated_books:
            if title_to_remove.lower() == book.split(",")[0].lower():
                updated_books.remove(book)   
                self.file.truncate() # it deletes all items in books.txt
                for book in updated_books:
                    self.file.write(book + "\n")
                print("Book '{}' removed successfully!".format(title_to_remove))
                break
            else:
                continue
    def find_book(self):
        found = None
        self.file.seek(0)
        find = input("Enter the book name: ")
        books = self.file.read().splitlines()
        for book in books:
            if find.lower() == book.split(",")[0].lower():
                found = True
                clear()
                print("===================================================================================================")
                print("|Book Name: {}|".format(book.split(",")[0]),"|Author: {}|".format(book.split(",")[1]),"|Release Date: {}|".format(book.split(",")[2]),"|Pages: {}|".format(book.split(",")[3]))
                print("===================================================================================================")
            else:
                continue
        if found == True:
            None
        else:
            print("Not Found any book named '{}'".format(find))   
# The Object Named "lib"
lib = Library()

# The Menu
while True:
    print("*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Find Book")
    print("5) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        clear()
        lib.list_books()
        input("***Press enter to continue***")
        clear()

    elif choice == "2":
        clear()
        lib.add_book()
        input("***Press enter to continue***")
        clear()

    elif choice == "3":
        clear()
        lib.remove_book()
        input("***Press enter to continue***")
        clear()

    elif choice == "4":
        clear()
        lib.find_book()
        input("***Press enter to continue***")
        clear()
    elif choice == "5":
        break
    else:
        clear()
        print("Invalid choice. Please enter a number between 1 and 4.")
        input("Press enter to continue")
        clear()
