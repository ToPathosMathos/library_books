class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f'"{self.title}" by {self.author}'

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self.books.append(book)

    def find_books_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def get_all_books(self):
        return self.books