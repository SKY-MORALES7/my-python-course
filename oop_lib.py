class Library:
    def __init__(self):
        self.books = {
            "Python" : "Guido Von Rossom",
            "Java" : "James Gosling",
            "C++" : "Bjarne S"
        }

        self.borrowed_books = {}

    def show_books(self):
        print("\n ______Available Books______")
        if not self.books:
            print("No Books Available")
        for book, author in self.books.items():
            print(f"{book} by {author}")

    def borrow_books(self, book):
        if book in self.books:
            self.borrowed_books[book] = self.books[book]
            del self.books[book]
            print(f" {book} borrowed successfully")

        else:
            print("Book not available")

    def return_books(self, book):
        if book in self.borrowed_books:
            self.books[book] = self.borrowed_books[book]
            del  self.borrowed_books[book]
            print(f"{book} returned  successfully")

        else:
            print("This book was not  borrowed")

library = Library()
while True:
    print("\n _____AVAILABLE BOOKS_______")
    print(" 1.Show Books\n 2.Borrow Books\n 3.Return Books\n 4. exit")

    choice = input("Enter choice: ")
    if choice == "1":
        library.show_books()

    elif choice == "2":
        book = input("Ënter book name: ")
        library.borrow_books(book)
    
    elif choice == "3":
        book = input("Ënter book name to return: ")
        library.return_books(book)

    elif choice == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid")

