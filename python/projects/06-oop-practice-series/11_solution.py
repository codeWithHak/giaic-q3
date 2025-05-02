# 11. Class Methods

# Assignment:

# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:

    # calss attribute
    total_books = 0
    
    # an instance method that calls class method (better but optional)
    # def __init__(self):
    #     Book.increment_book_count()
    
    # class method to increasse book count
    @classmethod
    def increment_book_count(cls):
        cls.total_books = cls.total_books + 1
        

# 0 books
print(Book.total_books)

# 1 book
book1 = Book()
Book.increment_book_count()

# 2 books
book2 = Book()
Book.increment_book_count()

# total 2 books
print(Book.total_books)
