class Library:
    class Book:
        def __init__(self, title, author, isbn):
            self.title = title
            self.author = author
            self.isbn = isbn
        def get_book_info(self):
            return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    def __init__(self):
        self.books = []
    def add_book(self, title, author, isbn):
        book = Library.Book(title, author, isbn)
        self.books.append(book)
    def display_all_books(self):
        for book in self.books:
            print(book.get_book_info())


    def find_books_by_author(self, author_name):
        found_books = []
        for book in self.books:

            if book.author == author_name:
                found_books.append(book)


        return found_books


library = Library()
library.add_book("The Law", "Moses","578-1-56619-909-4")
library.add_book("The Psalm", "David", "878-1-56619-698-4")
library.add_book("The Gospel", "Jesus Christ our Lord", "778-1-57719-909-4")
library.add_book("I am the way","Jesus Christ our Lord","127-3-10712-376-1")
library.add_book("Truth", "Jesus Christ our Lord","127-3-10712-376-1")
library.display_all_books()

print("\n ========Now get the object!========\n")

print(library.find_books_by_author("Jesus Christ our Lord"))

print("\n ========Now get the books!========\n")

books = library.find_books_by_author("Jesus Christ our Lord")
for books in books:
    print(books.get_book_info())





