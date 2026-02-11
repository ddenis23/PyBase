class Book:
    def __init__(self, name, page_count, author):
        self.name = name
        self.page_count = page_count
        self.author = author

    def __str__(self):
        return f"'{self.name}' de {self.author} ({self.page_count} pagini)"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def get_all_books(self):
        return self.books

    def get_books_from_author(self, author):
        return [book for book in self.books if book.author == author]

    def get_short_books(self):
        return [book for book in self.books if book.page_count < 100]

    def clear_library(self):
        self.books.clear()


library = Library()

book1 = Book("Ion", 250, "Liviu Rebreanu")
book2 = Book("Un veac de singuratate", 490, "Gabriel Garcia Marquez")
book3 = Book("Dragostea in vremea holerei", 480, "Gabriel Garcia Marquez")
book4 = Book("Crima si Pedeapsa", 784, "F. M. Dostoievski")
book5 = Book("IT", 1090, "Stephen King")
book6 = Book("Micul Prinț", 90, "Antoine de Saint-Exupéry")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)
library.add_book(book6)

print("Toate cărțile:")
for book in library.get_all_books():
    print(book)

print("\nCărți de Gabriel Garcia Marquez:")
for book in library.get_books_from_author("Gabriel Garcia Marquez"):
    print(book)
print("\nCărți sub 100 de pagini:")
for book in library.get_short_books():
    print(book)

library.clear_library()
# print("\nLibrăria după ștergere:", library.get_all_books())
