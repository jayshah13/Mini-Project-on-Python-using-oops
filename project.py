class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def checkout(self):
        if self.is_available:
            self.is_available = False
            print("Book checked out successfully.")
        else:
            print("Sorry, the book is already checked out.")

    def checkin(self):
        if not self.is_available:
            self.is_available = True
            print("Book checked in successfully.")
        else:
            print("The book is already available.")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_available_books(self):
        available_books = [book.title for book in self.books if book.is_available]
        if available_books:
            print("Available Books:")
            for book in available_books:
                print(book)
        else:
            print("No books are currently available.")

    def display_checked_out_books(self):
        checked_out_books = [book.title for book in self.books if not book.is_available]
        if checked_out_books:
            print("Checked Out Books:")
            for book in checked_out_books:
                print(book)
        else:
            print("No books are currently checked out.")


def main():
    library = Library()

    book1 = Book("Book 1", "Author 1")
    book2 = Book("Book 2", "Author 2")
    book3 = Book("Book 3", "Author 3")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    while True:
        print("\nMenu:")
        print("1. Display Available Books")
        print("2. Display Checked Out Books")
        print("3. Checkout a Book")
        print("4. Checkin a Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            library.display_available_books()
        elif choice == "2":
            library.display_checked_out_books()
        elif choice == "3":
            title = input("Enter the title of the book you want to checkout: ")
            for book in library.books:
                if book.title == title:
                    book.checkout()
                    break
            else:
                print("Book not found.")
        elif choice == "4":
            title = input("Enter the title of the book you want to checkin: ")
            for book in library.books:
                if book.title == title:
                    book.checkin()
                    break
            else:
                print("Book not found.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
