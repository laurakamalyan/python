import os
import subprocess

class Book:
    def __init__(self, author, title):
        self.__author = author
        self.__title = title

    @property
    def author(self):
        return self.__author

    @property
    def title(self):
        return self.__title


class Library():
    def __init__(self):
        self.books = list()

    def add_book(self, author, title):
        self.books.append(Book(author, title))

    def show_books(self):
        for book in self.books:
            print(f"Author: {book.author}, book: {book.title}")

    def show_author_books_list(self):
        author = input("Input author: ")
        x = False
        for book in self.books:
            if book.author == author:
                x = True
                print(book.title)

        if not x:
            print("We don't have a book by this author.")

    def open_book_file(self):
        book = input("Input book name: ")

        # change the input to match the file name
        book = book.lower().replace(" ", "_") + ".pdf"

        if os.path.exists(book):
            subprocess.Popen(book, shell=True)
        else:
            print("No such book.")


library = Library()
library.add_book("Agatha Christie", "The Murder of Roger Ackroyd")
library.add_book("Daniel Keyes", "Flowers for Algernon")
library.add_book("Agatha Christie", "Murder on the Orient Express")
library.add_book("Alberto Moravia", "Contempt")

library.show_author_books_list()
library.open_book_file()
